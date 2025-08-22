import cv2
import mediapipe as mp

class GestureDetector:
    def __init__(self):
        self.hands = mp.solutions.hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5)
        self.drawing = mp.solutions.drawing_utils

    def detect(self, image):
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = self.hands.process(image_rgb)

        if results.multi_hand_landmarks:
            landmarks = results.multi_hand_landmarks[0]
            finger_states = self.get_finger_states(landmarks)
            gesture = self.classify(finger_states)
            return gesture, landmarks
        return None, None

    def get_finger_states(self, hand_landmarks):
        tips = [4, 8, 12, 16, 20]
        pips = [3, 6, 10, 14, 18]

        fingers = []
        for tip, pip in zip(tips, pips):
            fingers.append(hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y)
        return fingers

    def classify(self, fingers):
        if fingers == [False, False, False, False, False]:
            return "rock"
        elif fingers == [False, True, True, False, False]:
            return "scissors"
        elif fingers == [True, True, True, True, True]:
            return "paper"
        elif fingers[0] and fingers[1] == False and fingers[2] == False:
            return "thumbs_up"
        else:
            return "unknown"
