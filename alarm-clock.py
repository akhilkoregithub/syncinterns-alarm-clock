from tkinter import *
import winsound
import datetime

root = Tk()
root.title("Alarm Clock")
root.geometry("270x300")
root.resizable(False, False)

Label(root, text='Enter in 24-hour format', font=("Arial", 14)).place(x=0, y=0)
Label(root, text='Hour', font=("Arial", 11)).place(x=50, y=70)
Label(root, text='Minute', font=("Arial", 11)).place(x=100, y=70)
Label(root, text='Second', font=("Arial", 11)).place(x=160, y=70)

hours = [str(i).zfill(2) for i in range(24)]
minutes = [str(i).zfill(2) for i in range(60)]
seconds = [str(i).zfill(2) for i in range(60)]

hour = StringVar(root)
hour.set(hours[0])
hour_option = OptionMenu(root, hour, *hours)
hour_option.config(bg='lightpink')
hour_option.place(x=40, y=100)

minute = StringVar(root)
minute.set(minutes[0])
minute_option = OptionMenu(root, minute, *minutes)
minute_option.config(bg='lightpink')
minute_option.place(x=100, y=100)

second = StringVar(root)
second.set(seconds[0])
second_option = OptionMenu(root, second, *seconds)
second_option.config(bg='lightpink')
second_option.place(x=160, y=100)

message_label = Label(root, text='', font=("Arial", 11))
message_label.place(x=80, y=200)

def set_alarm():
    alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
    return alarm_time

def check_alarm():
    alarm_time = set_alarm()
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    if current_time == alarm_time:
        message_label.config(text="Wake up Akhil!")
        winsound.PlaySound('C:/Users/kore akhil/Music/mixkit-alert-alarm-1005.wav', winsound.SND_ASYNC)
    root.after(1000, check_alarm)

submit_btn = Button(root, text='Submit', width=7, font=("Arial", 9), bg='lightgreen', command=check_alarm)
submit_btn.place(x=100, y=150)

root.mainloop()
