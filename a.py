
import tkinter as tk
from tkinter import messagebox, simpledialog

class PomodoroTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("Pomodoro Timer")
        
        self.timer_label = tk.Label(self.master, text="25:00", font=("Arial", 24))
        # Improved UI layout with additional settings
        self.timer_label.grid(row=0, column=0, columnspan=2, pady=20)
        
        self.start_button = tk.Button(self.master, text="Start", command=self.start_timer)
        self.start_button.grid(row=1, column=0, padx=5, pady=10)
        
        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_timer, state=tk.DISABLED)
        self.stop_button.grid(row=1, column=1, padx=5, pady=10)
        
        self.settings_button = tk.Button(self.master, text="Settings", command=self.set_timer)
        self.settings_button.grid(row=2, column=0, columnspan=2, pady=10)
        
        # Configuration constants
        self.POMODORO_TIME = 1500  # 25 minutes in seconds
        self.BREAK_TIME = 300      # 5 minutes in seconds
        self.time_remaining = self.POMODORO_TIME
        self.timer_running = False
        
    # New method to set the timer duration
    def set_timer(self):
        try:
            new_time = simpledialog.askinteger("Settings", "Enter Pomodoro time in minutes:", minvalue=1, maxvalue=60)
            if new_time is not None:
                self.POMODORO_TIME = new_time * 60
                self.time_remaining = self.POMODORO_TIME
                self.update_timer_label()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    
    # Method to update the timer label
    def update_timer_label(self):
        minutes = self.time_remaining // 60
        seconds = self.time_remaining % 60
        time_str = f"{minutes:02d}:{seconds:02d}"
        self.timer_label.config(text=time_str)
    
    def start_timer(self):
        try:
            if not self.timer_running:
                self.timer_running = True
                self.start_button.config(state=tk.DISABLED)
                self.stop_button.config(state=tk.NORMAL)
                self.countdown()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    
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
            try:
                self.timer_running = False
                self.start_button.config(state=tk.NORMAL)
                self.stop_button.config(state=tk.DISABLED)
                messagebox.showinfo("Pomodoro Timer", "Time's up!")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")
    
if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.mainloop()
