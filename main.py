import cv2
import mediapipe as mp
import time
from gesture_detector import GestureDetector
from game_logic import determine_winner, counter_move
from pattern_ai import PatternAI

detector = GestureDetector()
ai_brain = PatternAI()

user_score = 0
ai_score = 0
last_result = ""
last_gesture = ""
last_ai_move = ""

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Camera not working")
    exit()

# Control states
wait_for_ready = True
countdown_phrases = ["Rock", "Paper", "Scissors", "Shoot!"]
count_index = 0
last_count_time = time.time()
round_end_time = 0

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        continue

    frame = cv2.flip(frame, 1)
    gesture, landmarks = detector.detect(frame)

    if landmarks:
        detector.drawing.draw_landmarks(frame, landmarks, mp.solutions.hands.HAND_CONNECTIONS)

    current_time = time.time()

    if wait_for_ready:
        # Wait for thumbs up
        cv2.putText(frame, " Show Thumbs Up to Start", (50, 250),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
        if gesture == "thumbs_up":
            wait_for_ready = False
            count_index = 0
            last_count_time = current_time
    else:
        # Show countdown
        if count_index < len(countdown_phrases):
            if current_time - last_count_time > 1.2:
                last_count_time = current_time
                count_index += 1

            if count_index > 0:
                phrase = countdown_phrases[count_index - 1]
                cv2.putText(frame, phrase, (200, 200),
                            cv2.FONT_HERSHEY_SIMPLEX, 2.5, (0, 255, 255), 5)
        elif count_index == len(countdown_phrases):
            # Capture move after shoot
            if gesture and gesture != "unknown":
                predicted = ai_brain.predict()
                ai_move = counter_move(predicted)
                ai_brain.update(gesture)
                result = determine_winner(gesture, ai_move)

                if result == "You Win!":
                    user_score += 1
                elif result == "AI Wins!":
                    ai_score += 1

                last_result = result
                last_gesture = gesture
                last_ai_move = ai_move

                round_end_time = current_time
                count_index += 1  # prevent reprocessing
        else:
            # Wait 2.5s after round before next
            if current_time - round_end_time > 2.5:
                wait_for_ready = True

    # Overlay status
    cv2.rectangle(frame, (0, 0), (640, 60), (30, 30, 30), -1)
    cv2.putText(frame, f"Score - You: {user_score}  AI: {ai_score}",
                (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 0), 2)

    if last_result:
        cv2.putText(frame, f"{last_result}", (10, 440), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 200), 2)
        cv2.putText(frame, f"You: {last_gesture} | AI: {last_ai_move}",
                    (10, 480), cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 255, 100), 2)

    cv2.imshow("🤖 Rock-Paper-Scissors Smart AI", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
