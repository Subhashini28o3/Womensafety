mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

def classify_hand_gesture(landmarks):
    
    
    thumb_tip = landmarks[4]
    index_tip = landmarks[8]
    
    if index_tip.y < thumb_tip.y: 
        return " Gesture Detected"
    else:
        return "in danger"

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break
    
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    image = cv2.flip(image, 1)
    
    results = hands.process(image)
    
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            gesture = classify_hand_gesture(hand_landmarks.landmark)
            
            cv2.putText(image, gesture, (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
    
    cv2.imshow('Distress and Violence Hand Sign Detection', image)
    
    if cv2.waitKey(5) & 0xFF == 27: 
        break

cap.release()
cv2.destroyAllWindows()
cv2.waitKey(5) & 0xFF == ord('q')

import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="google.protobuf.symbol_database")

import cv2
import mediapipe as mp
from twilio.rest import Client
import os

account_sid = os.getenv('ACd46d6cbc3af71d28451b347fc6785f3c')
auth_token = os.getenv('92cb624c85f22256235c32838923e892')
twilio_phone_number = '(925) 309-8119' 

def send_alert_sms(recipient_phone_number, message):
    try:
        client = Client(account_sid, auth_token)
        client.messages.create(
            body=message,
            from_=twilio_phone_number,
            to=recipient_phone_number
        )
        print("need help")
    except Exception as e:
        print(f"Error sending message: {e}")