import pandas as pd
import numpy as np

data = {
    'Height': np.random.randint(150, 200, 100),  
    'Weight': np.random.randint(50, 100, 100),  
    'Age': np.random.randint(18, 50, 100),        
    'Gender': np.random.choice(['Male', 'Female'], 100) 
}

df = pd.DataFrame(data)

df['Gender'] = df['Gender'].map({'Male': 0, 'Female': 1})

X = df[['Height', 'Weight', 'Age']]
y = df['Gender']
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')
new_data = np.array([[175, 70, 25]])  
prediction = model.predict(new_data)

gender = 'Male' if prediction[0] == 0 else 'Female'
print(f'Predicted Gender: {gender}')
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
