import gui #importing gui.py file 
from time import strftime 

def main():
    gui_obj = gui.Gui()

    def update_time():
        current_time=strftime("%I:%M:%S %p")
        gui_obj.time_label.config(text=current_time)
        gui_obj.root.after(1000, update_time)

    update_time()
    gui_obj.root.mainloop()
    
if __name__=="__main__":
    main()