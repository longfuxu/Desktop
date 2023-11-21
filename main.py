
import tkinter as tk
import json
import datetime
from tkinter import messagebox, simpledialog, Entry, Checkbutton
    
# Styling constants
BG_COLOR = "#282c34"
FG_COLOR = "#abb2bf"
BTN_BG = "#61afef"
BTN_FG = "#282c34"
FONT_NAME = "Courier New"
TIMER_FONT = (FONT_NAME, 48, "bold")
LABEL_FONT = (FONT_NAME, 14)
BTN_FONT = (FONT_NAME, 14, "bold")

class PomodoroTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("Pomodoro Timer")
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
        self.settings_button.grid(row=2, column=0, columnspan=2, pady=(10, 0), ipadx=10)

        # To-Do List Frame
        self.todo_frame = tk.Frame(self.master, bg=BG_COLOR)
        self.todo_frame.grid(row=3, column=0, columnspan=2, pady=(10, 0), sticky="ew")

        # To-Do List Label
        self.todo_label = tk.Label(self.todo_frame, text="To-Do List", font=LABEL_FONT, bg=BG_COLOR, fg=FG_COLOR)
        self.todo_label.grid(row=0, column=0, pady=(0, 10), sticky="w")

        # To-Do Entry
        self.todo_entry = Entry(self.todo_frame, font=LABEL_FONT, bg=FG_COLOR, fg=BG_COLOR)
        self.todo_entry.grid(row=1, column=0, padx=(0, 10), sticky="ew")

        # Add Task Button
        self.add_task_button = tk.Button(self.todo_frame, text="Add Task", command=self.add_task, font=LABEL_FONT, bg=BTN_BG, fg=BTN_FG)
        self.add_task_button.grid(row=1, column=1, padx=(10, 0), sticky="ew")

        # To-Do List Tasks Frame
        self.tasks_frame = tk.Frame(self.todo_frame, bg=BG_COLOR)
        self.tasks_frame.grid(row=2, column=0, columnspan=2, pady=(10, 0), sticky="ew")

        # Initialize the list to store tasks
        self.tasks = []

        self.POMODORO_TIME = 1500  # 25 minutes in seconds
        self.BREAK_TIME = 300      # 5 minutes in seconds
        self.time_remaining = self.POMODORO_TIME
        self.timer_running = False
        self.load_state()
        
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
            self.timer_running = False
            self.start_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.DISABLED)
            messagebox.showinfo("Pomodoro Timer", "Time's up!")
            # Reset the timer to Pomodoro time
            self.time_remaining = self.POMODORO_TIME
            self.update_timer_label()

    # Method to add a new task
    def add_task(self):
        task_text = self.todo_entry.get()
        if task_text:
            # Create a variable to store the state of the checkbox
            task_state = tk.BooleanVar()
            # Create a checkbox for the new task
            task = tk.Checkbutton(self.tasks_frame, text=task_text, variable=task_state, font=LABEL_FONT, bg=BG_COLOR, fg=FG_COLOR, selectcolor=BG_COLOR)
            task.pack(anchor="w")
            # Add the task and its state to the list
            self.tasks.append((task, task_state))
            # Clear the entry field
            self.todo_entry.delete(0, tk.END)
    
    def save_state(self):
        data = {
            'pomodoro_time': self.POMODORO_TIME,
            'break_time': self.BREAK_TIME,
            'todos': [
                {'task': task[0].cget("text"), 'completed': task[1].get()}
                for task in self.tasks
            ],
            'timestamp': datetime.datetime.now().isoformat()
        }
        with open('pomodoro_data.json', 'w') as f:
            json.dump(data, f, indent=4)

    def display_past_records(self):
        try:
            with open('pomodoro_data.json', 'r') as f:
                data = json.load(f)
                print("Past Pomodoro Records:")
                for todo in data['todos']:
                    status = "Completed" if todo['completed'] else "Not Completed"
                    print(f"- {todo['task']} - {status}")
                print(f"Last session was on {data['timestamp']}")
        except FileNotFoundError:
            print("No past records found.")

    def load_state(self):
        try:
            with open('pomodoro_data.json', 'r') as f:
                data = json.load(f)
                self.POMODORO_TIME = data['pomodoro_time']
                self.BREAK_TIME = data['break_time']
                for todo in data['todos']:
                    self.load_task(todo['task'], todo['completed'])
        except FileNotFoundError:
            pass  # It's okay if the file doesn't exist yet

    def load_task(self, task_text, completed=False):
        if task_text:
            task_state = tk.BooleanVar(value=completed)
            task = tk.Checkbutton(self.tasks_frame, text=task_text, variable=task_state, font=LABEL_FONT, bg=BG_COLOR, fg=FG_COLOR, selectcolor=BG_COLOR)
            task.pack(anchor="w")
            if completed:
                task.select()
            self.tasks.append((task, task_state))
    

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroTimer(root)
    app.display_past_records()  # Display past records when the application starts
    root.mainloop()
