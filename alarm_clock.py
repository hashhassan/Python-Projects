import tkinter as tk
from tkinter import messagebox
import datetime
import time
import winsound  # For Windows users to play sound. On Linux/macOS, you might use 'playsound' library or similar.


def set_alarm():
    """Sets the alarm based on user input."""
    alarm_hour = int(hour_entry.get())
    alarm_minute = int(minute_entry.get())

    messagebox.showinfo("Alarm Set", f"Alarm set for {alarm_hour:02d}:{alarm_minute:02d}")

    while True:
        now = datetime.datetime.now()
        current_hour = now.hour
        current_minute = now.minute

        if current_hour == alarm_hour and current_minute == alarm_minute:
            messagebox.showinfo("Alarm!", "Time to wake up!")
            winsound.Beep(1000, 2000)  # Play a beep sound (Frequency, Duration in ms)
            break
        time.sleep(1)  # Check every second


# --- GUI Setup ---
app = tk.Tk()
app.title("Simple Alarm Clock")

# Labels and Entries for Hour and Minute
hour_label = tk.Label(app, text="Hour (0-23):")
hour_label.pack(pady=5)
hour_entry = tk.Entry(app)
hour_entry.pack(pady=5)

minute_label = tk.Label(app, text="Minute (0-59):")
minute_label.pack(pady=5)
minute_entry = tk.Entry(app)
minute_entry.pack(pady=5)

# Set Alarm Button
set_button = tk.Button(app, text="Set Alarm", command=set_alarm)
set_button.pack(pady=20)

app.mainloop()