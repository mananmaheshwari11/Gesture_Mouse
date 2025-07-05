import tkinter as tk
import threading
import mouse_controls

gesture_thread = None

def start_gesture():
    global gesture_thread
    if gesture_thread is None or not gesture_thread.is_alive():
        gesture_thread = threading.Thread(target=mouse_controls.start_gesture)
        gesture_thread.start()
        status_label.config(text="🟢 Gesture Control Running")

def stop_gesture():
    mouse_controls.stop_gesture()
    status_label.config(text="🔴 Gesture Control Stopped")
    root.after(1500, root.destroy)  # Delay exit for user clarity

# Initialize the GUI
root = tk.Tk()
root.title("🖐️ Virtual Gesture Mouse")
root.geometry("640x480")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="Gesture Control Interface", font=("Helvetica", 16, "bold"))
title_label.pack(pady=15)

# Status Label
status_label = tk.Label(root, text="🔴 Not Running", font=("Helvetica", 12))
status_label.pack(pady=5)

# Start Button
start_btn = tk.Button(root, text="▶ Start Gesture", command=start_gesture,
                      width=25, bg="#4CAF50", fg="white", font=("Helvetica", 11))
start_btn.pack(pady=10)

# Stop Button
stop_btn = tk.Button(root, text="⛔ Stop & Exit", command=stop_gesture,
                     width=25, bg="#f44336", fg="white", font=("Helvetica", 11))
stop_btn.pack(pady=5)

# Footer note
footer = tk.Label(root, text="Press '$' to stop manually in video feed", font=("Helvetica", 9), fg="gray")
footer.pack(pady=10)

# Launch GUI
root.mainloop()
