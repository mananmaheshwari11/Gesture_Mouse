import math

def get_distance(p1, p2, frame_width, frame_height):
    x1, y1 = int(p1.x * frame_width), int(p1.y * frame_height)
    x2, y2 = int(p2.x * frame_width), int(p2.y * frame_height)
    return math.hypot(x2 - x1, y2 - y1)

def get_finger_states(hand_landmarks):
    finger_states = []
    finger_tips = [4, 8, 12, 16, 20]
    finger_pips = [2, 6, 10, 14, 18]

    for tip, pip in zip(finger_tips, finger_pips):
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y:
            finger_states.append(1)
        else:
            finger_states.append(0)
    return finger_states
