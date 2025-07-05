import cv2
import mediapipe as mp
import pyautogui
import time

from gesture_utils import get_finger_states, get_distance
from labels_util import get_label
running = True

def stop_gesture():
    global running
    running = False

def get_sense(finger_states, handlms, frame_w, frame_h):
    screen_w, screen_h = pyautogui.size()

    if finger_states == [1, 1, 0, 0, 0]:
        index_tip = handlms.landmark[8]
        screen_x = int(index_tip.x * screen_w)
        screen_y = int(index_tip.y * screen_h)
        return ["MOVE", screen_x, screen_y]
    elif finger_states == [1, 1, 0, 0, 1]:
        return ["LEFT"]
    elif finger_states == [1, 0, 0, 0, 1]:
        return ["RIGHT"]
    elif finger_states == [1, 1, 1, 0, 0]:
        return ["SCROLL"]
    elif finger_states == [1, 1, 1, 0, 1]:
        return ["SCROLL_DOWN"]
    elif finger_states == [1, 1, 1, 1, 0]:
        return ["ALT_TAB"]
    return None

def start_gesture():
    global running
    running = True
    mp_hands = mp.solutions.hands
    mp_draw = mp.solutions.drawing_utils
    hands = mp_hands.Hands(max_num_hands=1)

    cap = cv2.VideoCapture(0)

    prev_x, prev_y = 0, 0
    smoothing = 0.5
    click_time = 0
    alt_tab_timer = 0
    alt_tab_active = False
    scroll_time = 0

    while running:
        success, frame = cap.read()
        if not success:
            continue
        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb)

        gesture = None

        if result.multi_hand_landmarks:
            for handLms in result.multi_hand_landmarks:
                mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

                finger_states = get_finger_states(handLms)
                gesture = get_sense(finger_states, handLms, frame.shape[1], frame.shape[0])

                if gesture:
                    if gesture[0] == "MOVE":
                        target_x, target_y = gesture[1], gesture[2]
                        curr_x = prev_x + (target_x - prev_x) * smoothing
                        curr_y = prev_y + (target_y - prev_y) * smoothing
                        pyautogui.moveTo(curr_x, curr_y)
                        prev_x, prev_y = curr_x, curr_y

                    elif gesture[0] == "LEFT":
                        if time.time() - click_time > 0.7:
                            pyautogui.click()
                            click_time = time.time()

                    elif gesture[0] == "RIGHT":
                        if time.time() - click_time > 0.7:
                            pyautogui.rightClick()
                            click_time = time.time()

                    elif gesture[0] == "SCROLL":
                        if time.time() - scroll_time > 0.05:
                            pyautogui.scroll(10)
                            scroll_time = time.time()

                    elif gesture[0] == "SCROLL_DOWN":
                        if time.time() - scroll_time > 0.05:
                            pyautogui.scroll(-10)
                            scroll_time = time.time()

                    elif gesture[0] == "ALT_TAB":
                        if not alt_tab_active:
                            alt_tab_active = True
                            alt_tab_timer = time.time()
                            pyautogui.keyDown('alt')
                            pyautogui.press('tab')
                        elif time.time() - alt_tab_timer > 0.7:
                            pyautogui.press('tab')
                            alt_tab_timer = time.time()

        if gesture is None or gesture[0] != "ALT_TAB":
            if alt_tab_active:
                pyautogui.keyUp('alt')
                alt_tab_active = False
        # Display label
        if gesture:
            label_text, label_color = get_label(gesture[0])
            cv2.putText(frame, label_text, (10, 40), cv2.FONT_HERSHEY_SIMPLEX,
                        1.1, label_color, 3)

        cv2.imshow("Hand Tracking", frame)
        if cv2.waitKey(1) & 0xFF == ord('$'):
            break

    cap.release()
    cv2.destroyAllWindows()
