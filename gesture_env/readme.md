# 🖐️ Gesture Mouse using MediaPipe

Gesture Mouse is a computer vision-based Python tool that allows users to control their mouse using hand gestures. Built with MediaPipe and OpenCV, this system captures real-time hand movements via webcam and translates them into cursor actions, enabling a hands-free interface experience.

---

## 🚀 Approach

The core idea is to detect and track hand landmarks using MediaPipe’s Hand Tracking module. Specific finger positions and gestures are recognized through geometric analysis and mapped to mouse operations like movement, click, drag, etc. For example:
- Moving the index finger moves the cursor
- Pinching fingers triggers click or drag events

OpenCV is used for camera feed processing and visualization, while `pyautogui` or `pynput` simulate actual mouse events.

---

## 💡 Benefits

- **Touchless control**: Hygienic and futuristic interface
- **Accessibility**: Useful for people with limited mobility
- **Engagement**: Great for interactive systems and kiosks
- **Learning**: Helps understand computer vision, gesture tracking, and input mapping

---

## 🧰 Tech Stack

- **Python 3.10** (required for MediaPipe)
- **MediaPipe** – Real-time hand tracking
- **OpenCV** – Image processing and camera handling
- **PyAutoGUI / pynput** – Simulating mouse actions
- **NumPy** – Coordinate processing

---

## ⚙️ Installation

### Prerequisites:
- Python 3.10  
- pip (Python package manager)

### Steps:
```bash
# Clone the repositorym
git clone https://github.com/mananmaheshwari11/Gesture_Mouse.git
cd gesture_env

# Create virtual environment (optional)
python -m venv gesture_env
source gesture_env/bin/activate  # or Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the app
python main.py

