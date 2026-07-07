#main_file:

#import section:
import datetime
import winsound
from gui import Alarm

def input_time():
    set_timer= f"{alarm_obj.hour.get()}:{alarm_obj.mins.get()}:{alarm_obj.sec.get()}"
    wake_up(set_timer)

def wake_up(set_timer):
    current= datetime.datetime.now()
    now= current.strftime("%H:%M:%S")
    date= current.strftime("%y/%m/%d")
    print(f"the current date is: {date}")
    print(f"{now}")
    if now == set_timer: #Time to wake up!
        print(f"Time to wake up!")
        print(f"Its {set_timer}")
        winsound.PlaySound('alarm.wav', winsound.SND_FILENAME) #playing 'alarm.wav'

    alarm_obj.alarm.after(1000, lambda: wake_up(set_timer))

alarm_obj= Alarm(input_time) #creating the object

alarm_obj.time_clock()

alarm_obj.run()