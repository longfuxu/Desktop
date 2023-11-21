
import time
import tkinter as tk
from tkinter import messagebox

class PomodoroTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("Pomodoro Timer")
        
        self.timer_label = tk.Label(self.master, text="25:00", font=("Arial", 24))
        self.timer_label.pack(pady=20)
        
        self.start_button = tk.Button(self.master, text="Start", command=self.start_timer)
        self.start_button.pack(pady=10)
        
        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.pack(pady=10)
        
        self.time_remaining = 1500  # 25 minutes in seconds
        self.timer_running = False
        
    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.start_button.config(state=tk.DISABLED)
            self.stop_button.config(state=tk.NORMAL)
            self.countdown()
    
    def stop_timer(self):
        if self.timer_running:
            self.timer_running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
    
    def countdown(self):
        if self.timer_running and self.time_remaining > 0:
            minutes = self.time_remaining // 60
            seconds = self.time_remaining % 60
            time_str = f"{minutes:02d}:{seconds:02d}"
            self.timer_label.config(text=time_str)
            self.time_remaining -= 1
            self.master.after(1000, self.countdown)
        elif self.time_remaining == 0:
            self.timer_running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            messagebox.showinfo("Pomodoro Timer", "Time's up!")
    
if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.mainloop()
