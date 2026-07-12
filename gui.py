#gui_file:

#import section:
from tkinter import *
import tkinter.font as font
import time

class Alarm():
    def __init__(self, command_function):
        self.time_now= time.strftime("%H:%M:%S")

        self.alarm= Tk()
        self.alarm.title("Alarm clock")
        self.alarm.config(bg="yellow")
        self.alarm.resizable(False, False)
        self.alarm.geometry("450x300")

        self.screen_width= self.alarm.winfo_screenwidth()
        self.screen_hight= self.alarm.winfo_screenheight()

        self.x= (self.screen_width // 2) - (450 // 2)
        self.y= (self.screen_hight // 2) - (300 // 2)

        self.alarm.geometry(f"450x300+{self.x}+{self.y}")

        self.my_font= font.Font(family="Open Sans Light")

        self.clock= Label(self.alarm, text=self.time_now, font=("Arial", 60, "bold"),
                    bg="black", foreground="white")
        self.clock.grid(row=1, column=0, columnspan=2, sticky="we")

        self.user_time= Label(self.alarm, text="Enter the time in 24 hours format:",
                    font=("Arial", 13, "bold"), bg="yellow", foreground="black",)
        self.user_time.grid(row=2)

        self.hr= Label(self.alarm, font=(self.my_font, 16, "bold"),
                    text= "hour:", bg="black", foreground="white")
        self.hr.grid(row=3, column=0, sticky="w")

        self.mi= Label(self.alarm, font=(self.my_font, 16, "bold"),
                    text= "min:", bg="black", foreground="white")
        self.mi.grid(row=4, column=0, sticky="w")

        self.se= Label(self.alarm, font=(self.my_font, 16, "bold"),
                    text= "sec:", bg="black", foreground="white")
        self.se.grid(row=5, column=0, sticky="w")

        self.hour= StringVar(value="00")
        self.mins= StringVar(value="00")
        self.sec= StringVar(value="00")

        self.hour_time= Entry(textvariable=self.hour, width=10, bg="white",
                    foreground="black", bd=2, font=("Arial", 12))
        self.hour_time.grid(row=3, column=0, sticky="")

        self.min_time= Entry(textvariable=self.mins, width=10, bg="white",
                    foreground="black", bd=2, font=("Arial", 12))
        self.min_time.grid(row=4, column=0, sticky="")

        self.sec_time= Entry(textvariable=self.sec, width=10, bg="white",
                    foreground="black", bd=2, font=("Arial", 12))
        self.sec_time.grid(row=5, column=0, sticky="")

        self.submit=Button(text="Set the alarm", bg="yellow", fg="black",
        activebackground="cyan", activeforeground="black",
        width=25, height=10,
        command= command_function)

        self.submit.grid(row=3, column=1, rowspan=3, sticky="e")

    def time_clock(self):
        time_now= time.strftime("%H:%M:%S")
        self.clock.config(text=time_now)
        self.alarm.after(1000, lambda: self.time_clock())

    def run(self):
        self.alarm.mainloop()