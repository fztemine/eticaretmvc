#Yazan: Timur SOMAY

import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
    
      continue

    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
   
    image.flags.writeable = False
    results = hands.process(image)

    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:

        x, y = hand_landmarks.landmark[0].x, hand_landmarks.landmark[0].y
        x1, y1 = hand_landmarks.landmark[4].x, hand_landmarks.landmark[4].y

        font = cv2.FONT_HERSHEY_PLAIN
        
        if y1 > y:
                cv2.putText(image, "COLBAN icin durum OLUMSUZ!...", (10, 50), font, 1.5, (0, 0, 255), 2)
        else:
                cv2.putText(image, "COLBAN icin durum OLUMLU!...", (10, 50), font, 1.5, (0, 255, 0), 2)
        
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()