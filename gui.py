import tkinter as tk #importing tkinter module

class Gui():
    def __init__(self):
        self.root= tk.Tk()
        self.root.title("Alarm_clock")
        self.root.geometry("700x200")
        self.root.resizable(False, False)
        self.root.config(bg="black")
        self.time_label= tk.Label(
            self.root,
            bg="black",
            fg="cyan",
            font=("Currier", 80, "bold")
        )

        self.time_label.pack(anchor="center", pady=30)