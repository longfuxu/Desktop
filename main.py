
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
        
    # Updated method to set the timer durations
    def set_timer(self):
        try:
            new_pomodoro_time = simpledialog.askinteger("Settings", "Enter Pomodoro time in minutes:", minvalue=1, maxvalue=60)
            new_break_time = simpledialog.askinteger("Settings", "Enter break time in minutes:", minvalue=1, maxvalue=60)
            if new_pomodoro_time is not None and new_break_time is not None:
                self.POMODORO_TIME = new_pomodoro_time * 60
                self.BREAK_TIME = new_break_time * 60
                self.time_remaining = self.POMODORO_TIME  # Reset to Pomodoro time by default
                self.update_timer_label()
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    
    # Updated method to update the timer label based on the current mode
    def update_timer_label(self, mode="pomodoro"):
        if mode == "pomodoro":
            minutes, seconds = divmod(self.POMODORO_TIME, 60)
        else:  # mode == "break"
            minutes, seconds = divmod(self.BREAK_TIME, 60)
        self.timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
    
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
        # Styling constants
        BG_COLOR = "#282c34"
        FG_COLOR = "#abb2bf"
        BTN_BG = "#61afef"
        BTN_FG = "#282c34"
        FONT_NAME = "Courier New"
        TIMER_FONT = (FONT_NAME, 48, "bold")
        LABEL_FONT = (FONT_NAME, 14)
        BTN_FONT = (FONT_NAME, 14, "bold")

        # Main window styling
        self.master.configure(bg=BG_COLOR)

        # Timer label with modern font and larger size
        self.timer_label = tk.Label(self.master, text="25:00", font=TIMER_FONT, bg=BG_COLOR, fg=FG_COLOR)
        self.timer_label.grid(row=0, column=0, columnspan=2, pady=(20, 10))

        # Start button with vibrant color
        self.start_button = tk.Button(self.master, text="Start", command=self.start_timer, font=BTN_FONT, bg=BTN_BG, fg=BTN_FG)
        self.start_button.grid(row=1, column=0, padx=5, pady=10, ipadx=20)

        # Stop button with vibrant color
        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_timer, state=tk.DISABLED, font=BTN_FONT, bg=BTN_BG, fg=BTN_FG)
        self.stop_button.grid(row=1, column=1, padx=5, pady=10, ipadx=20)

        # Settings button with a modern look
        self.settings_button = tk.Button(self.master, text="Settings", command=self.set_timer, font=LABEL_FONT, bg=BTN_BG, fg=BTN_FG)
        self.settings_button.grid(row=2, column=0, columnspan=2, pady=(10, 20), ipadx=10)
