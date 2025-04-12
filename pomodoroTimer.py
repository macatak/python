'''
Simple Pomodoro timer to help maintain focus
Enter the task to Focus on in the Focus text box (not required)
Update time fields as desired
When it gets to 60 seconds it will start flashing on a predefined interval
Background color and flashing colors and intervals can be set in the 
   PomodoroTimer functions
Developed using the ChatGPT 03-mini-high GPT model
'''

# colors and can be customized in the timer
import tkinter as tk

class PomodoroTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("Pomodoro Timer")
        
        # Background and flash colors setup
        self.backgroundColor = "light blue"
        self.flashColor1 = "dark blue"
        self.flashColor2 = "light blue"
        self.flashInterval = 1  # in seconds
        # Initially, set the main window background to backgroundColor
        self.master.configure(bg=self.backgroundColor)
        # Toggle flag for flashing
        self.flash_on = False
        
        # Default durations in minutes
        self.default_work = 25
        self.default_short_break = 5
        self.default_long_break = 15
        
        # Convert minutes to seconds for timing
        self.work_duration = self.default_work * 60
        self.short_break_duration = self.default_short_break * 60
        self.long_break_duration = self.default_long_break * 60
        
        # Current selected session attributes
        self.current_session = "Work"  # Options: "Work", "Short Break", "Long Break"
        self.session_duration = self.work_duration  # Default session length
        self.time_left = self.session_duration
        
        # Boolean flag to know if the timer is running
        self.running = False
        # After job reference for canceling scheduled calls
        self.job = None
        
        # Create the GUI components
        self.create_session_adjustments()
        self.create_focus_box()        # Focus text box added here
        self.create_display()
        self.create_buttons()

    def create_session_adjustments(self):
        # Frame for entering custom durations for each session type
        frame = tk.Frame(self.master, bg=self.backgroundColor)
        frame.pack(pady=10)

        # Work session input
        tk.Label(frame, text="Work (min):", bg=self.backgroundColor).grid(row=0, column=0, padx=5)
        self.work_var = tk.StringVar(value=str(self.default_work))
        tk.Entry(frame, width=5, textvariable=self.work_var).grid(row=0, column=1, padx=5)
        
        # Short break input
        tk.Label(frame, text="Short Break (min):", bg=self.backgroundColor).grid(row=0, column=2, padx=5)
        self.short_break_var = tk.StringVar(value=str(self.default_short_break))
        tk.Entry(frame, width=5, textvariable=self.short_break_var).grid(row=0, column=3, padx=5)
        
        # Long break input
        tk.Label(frame, text="Long Break (min):", bg=self.backgroundColor).grid(row=0, column=4, padx=5)
        self.long_break_var = tk.StringVar(value=str(self.default_long_break))
        tk.Entry(frame, width=5, textvariable=self.long_break_var).grid(row=0, column=5, padx=5)

    def create_focus_box(self):
        # Frame for the focus text box with matching background
        frame = tk.Frame(self.master, bg=self.backgroundColor)
        frame.pack(pady=10)
        # Focus label with a large font
        tk.Label(frame, text="Focus:", bg=self.backgroundColor, font=("Helvetica", 48)).pack(side="left", padx=5)
        # Entry widget for the focus text, centered
        self.focus_text = tk.Entry(frame, width=20, font=("Helvetica", 48), justify="center")
        self.focus_text.pack(side="left", padx=5)
    
    def create_display(self):
        # Countdown display label with consistent background
        self.timer_label = tk.Label(self.master, text=self.format_time(self.time_left),
                                    font=("Helvetica", 48), bg=self.backgroundColor)
        self.timer_label.pack(pady=20)
        
        # Progress bar using canvas; fixed width of 300 pixels.
        self.canvas_width = 300
        self.canvas_height = 30
        self.canvas = tk.Canvas(self.master, width=self.canvas_width,
                                height=self.canvas_height, bg="white")
        self.canvas.pack(pady=10)
        # Initial empty progress bar
        self.progress_bar = self.canvas.create_rectangle(0, 0, 0,
                                                         self.canvas_height, fill="green")

    def create_buttons(self):
        # Frame for control buttons using the default background
        frame = tk.Frame(self.master, bg=self.backgroundColor)
        frame.pack(pady=10)
        
        # Session selection buttons
        tk.Button(frame, text="Work", command=lambda: self.set_session("Work")).grid(row=0, column=0, padx=5)
        tk.Button(frame, text="Short Break", command=lambda: self.set_session("Short Break")).grid(row=0, column=1, padx=5)
        tk.Button(frame, text="Long Break", command=lambda: self.set_session("Long Break")).grid(row=0, column=2, padx=5)
        
        # Timer control buttons
        tk.Button(frame, text="Start", command=self.start).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(frame, text="Pause", command=self.pause).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(frame, text="Reset", command=self.reset).grid(row=1, column=2, padx=5, pady=5)

    def set_session(self, session_type):
        """Switches session types and resets the timer accordingly."""
        # Cancel any ongoing timer job
        if self.job:
            self.master.after_cancel(self.job)
        
        self.running = False
        self.current_session = session_type
        # Read user adjustments if any
        if session_type == "Work":
            try:
                minutes = int(self.work_var.get())
            except ValueError:
                minutes = self.default_work
            self.session_duration = minutes * 60
        elif session_type == "Short Break":
            try:
                minutes = int(self.short_break_var.get())
            except ValueError:
                minutes = self.default_short_break
            self.session_duration = minutes * 60
        elif session_type == "Long Break":
            try:
                minutes = int(self.long_break_var.get())
            except ValueError:
                minutes = self.default_long_break
            self.session_duration = minutes * 60

        self.time_left = self.session_duration
        # Reset the timer label and progress bar, and also reset background
        self.timer_label.config(text=self.format_time(self.time_left), fg="black")
        self.canvas.coords(self.progress_bar, 0, 0, 0, self.canvas_height)
        self.master.configure(bg=self.backgroundColor)
        self.flash_on = False

    def format_time(self, seconds):
        minutes, sec = divmod(seconds, 60)
        return f"{minutes:02d}:{sec:02d}"
    
    def update_timer(self):
        """Updates the timer every second using .after() and manages background flashing."""
        if self.running and self.time_left > 0:
            self.time_left -= 1
            self.timer_label.config(text=self.format_time(self.time_left))
            
            # Update the progress bar based on elapsed time
            elapsed = self.session_duration - self.time_left
            progress_width = (elapsed / self.session_duration) * self.canvas_width
            self.canvas.coords(self.progress_bar, 0, 0, progress_width, self.canvas_height)
            
            # If remaining time is 1 minute or less, flash the background
            if 0 < self.time_left <= 60:
                # Toggle the flash state each second
                self.flash_on = not self.flash_on
                bg_color = self.flashColor1 if self.flash_on else self.flashColor2
                self.master.configure(bg=bg_color)
            else:
                # Otherwise, ensure the background is set to the default
                self.master.configure(bg=self.backgroundColor)
            
            self.job = self.master.after(1000, self.update_timer)
        elif self.time_left == 0:
            self.running = False
            self.notify_session_end()
    
    def notify_session_end(self):
        """Visual notification when the session ends."""
        self.timer_label.config(text="Time's up!", fg="red")
        # Reset the background to the default color on session end
        self.master.configure(bg=self.backgroundColor)

    def start(self):
        """Starts the timer."""
        if not self.running:
            self.running = True
            self.update_timer()
    
    def pause(self):
        """Pauses the timer by canceling the scheduled job."""
        if self.running:
            self.running = False
            if self.job:
                self.master.after_cancel(self.job)
                self.job = None
            # Reset the background when paused
            self.master.configure(bg=self.backgroundColor)
            self.flash_on = False

    def reset(self):
        """Resets the timer to the original duration for the selected session."""
        self.pause()
        self.time_left = self.session_duration
        self.timer_label.config(text=self.format_time(self.time_left), fg="black")
        self.canvas.coords(self.progress_bar, 0, 0, 0, self.canvas_height)
        self.master.configure(bg=self.backgroundColor)
        self.flash_on = False

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.mainloop()

