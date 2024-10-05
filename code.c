#include <SoftwareSerial.h>


SoftwareSerial gpsSerial(4, 3);  
SoftwareSerial gsmSerial(7, 8);  

String latitude = "";
String longitude = "";


String policeNumber = "+1234567890";  


int buttonPin = 9;
int buttonState = 0;

void setup() {
  
  Serial.begin(9600);
  gpsSerial.begin(9600);
  gsmSerial.begin(9600);

  
  pinMode(buttonPin, INPUT);

  delay(10000); 
}

void loop() {
  buttonState = digitalRead(buttonPin);

  if (buttonState == HIGH) {
    getGPSLocation();
    sendAlert();
  }
  delay(1000);
}

void getGPSLocation() {
  while (gpsSerial.available() > 0) {
    String gpsData = gpsSerial.readStringUntil('\n');
    
    if (gpsData.startsWith("$GPGGA") || gpsData.startsWith("$GPRMC")) {
      latitude = parseLatitude(gpsData);
      longitude = parseLongitude(gpsData);
    }
  }
}

String parseLatitude(String gpsData) {
  int latIndex = gpsData.indexOf(',') + 1;  
  return gpsData.substring(latIndex, latIndex + 10);  

String parseLongitude(String gpsData) {
  int lonIndex = gpsData.indexOf(',', gpsData.indexOf(',') + 1) + 1;  
  return gpsData.substring(lonIndex, lonIndex + 10);  

void sendAlert() {
  String message = "Emergency! Woman in danger. Location: https://maps.google.com/?q=" + latitude + "," + longitude;

  // Send the SMS
  gsmSerial.println("AT+CMGF=1");  
  delay(1000);
  gsmSerial.println("AT+CMGS=\"" + policeNumber + "\"");  
  delay(1000);
  gsmSerial.println(message);  
  delay(1000);
  gsmSerial.write(26);  
  delay(5000);
  
  Serial.println("Alert sent: " + message);  
}