import cv2
import mediapipe as mp
import requests
import os
from datetime import datetime

# Initialize MediaPipe
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(model_complexity=1, min_detection_confidence=0.7, min_tracking_confidence=0.5)
mp_draw = mp.solutions.drawing_utils

ALERT_API = "http://127.0.0.1:5000/alert"

def detect_gesture(landmarks):
    # Tip of thumb (4) and IP joint (3)
    thumb_tip = landmarks[4]
    thumb_ip = landmarks[3]
    
    # 1. 👎 DANGER (Strict Thumb Down)
    # Tip must be significantly lower than the joint
    if thumb_tip.y > (thumb_ip.y + 0.05):
        return "DANGER"

    # 2. 👍 SUSPICIOUS (Side Thumb / Thumbs Up)
    # Using your original horizontal distance logic
    elif abs(thumb_tip.x - thumb_ip.x) > 0.05:
        return "SUSPICIOUS"

    return "NORMAL"

def start_camera():
    cap = cv2.VideoCapture(0)
    
    print("Camera started. Press 'ESC' to quit.")

    while True:
        success, frame = cap.read()
        if not success:
            break

        # Flip the frame for a mirror effect
        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        gesture = "NORMAL" # Default state

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                landmarks = handLms.landmark
                gesture = detect_gesture(landmarks)

                # Draw the skeleton
                mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

                if gesture != "NORMAL":
                    # --- Alerting Logic ---
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"alerts/{gesture}_{timestamp}.jpg"
                    os.makedirs("alerts", exist_ok=True)
                    cv2.imwrite(filename, frame)

                    # Wrap in try-except so the code doesn't crash if your Flask server is off
                    try:
                        data = {
                            "camera_id": "CAM_01",
                            "gesture": gesture,
                            "image": filename,
                            "time": timestamp
                        }
                        requests.post(ALERT_API, json=data, timeout=0.5)
                    except:
                        pass 

        # Display the current status on the screen
        color = (0, 255, 0) # Green for Normal
        if gesture == "DANGER": color = (0, 0, 255) # Red
        if gesture == "SUSPICIOUS": color = (0, 255, 255) # Yellow

        cv2.putText(frame, f"STATUS: {gesture}", (10, 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

        cv2.imshow("Gesture Detection", frame)

        # Press 'ESC' to exit
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    start_camera()