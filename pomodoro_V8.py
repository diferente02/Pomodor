from time import time
import time
import pyttsx3
from tkinter import *
from pyautogui import alert
mudo = ()
n = 0

def alertando_o_descanso():
    alert('Tempo de trabalho terminado')
    rest()


def alertando_o_foco():
    alert('tempo de foco terminado')
    countdowntimer()


# https://www.tutorialspoint.com/how-to-create-a-timer-using-tkinter
# Define the function for the timer
def countdowntimer():
    df['text'] = 'FOCO'
    df.place(x='115', y='30')
    times = int(25) * 60 + int(0)
    while times > -1:
        minute, second = (times // 60, times % 60)
        sec.set(second)
        min.set(minute)
        # Update the time
        root.update()
        time.sleep(1)
        if (times == 0):
            sec.set('00')
            min.set('00')
        times -= 1
    alertando_o_descanso()

def rest():
    df['text'] = 'DESCANSO'
    df.place(x='85', y='30')
    times = int(5) * 60 + int(0)
    while times > -1:
        minute, second = (times // 60, times % 60)
        sec.set(second)
        min.set(minute)
        # Update the time
        root.update()
        time.sleep(1)
        if (times == 0):
            sec.set('00')
            min.set('00')
        times -= 1
    alertando_o_foco()


root = Tk()
root.title('Tecnica pomodoro')
root.geometry('300x400+200+50')

# descanso ou foco
df = Label(root, text='FOCO', font="Arial 20")
df.place(x='115', y='30')

# Variable second
sec = StringVar()
Label(root, textvariable=sec, width=2, font="Arial 14").place(x='155', y='130')
sec.set('00')

# just two points (:)
two_point = Label(root, text=':', font='Arial 16').place(x='145', y='130')

# Variable minutes
min = StringVar()
Label(root, textvariable=min, width=2, font="Arial 14").place(x='120', y='130')
min.set('25')

bt = Button(root, width=10, text='foco', font='Arial 12', command=countdowntimer)
bt.place(x='50', y='230')

bt = Button(root, width=10, text='descanso', font='Arial 12', command=rest)
bt.place(x='150', y='230')

s = IntVar()
s.get()

#btsound = Radiobutton(root, text='som', variable=s, value='s', command=lambda:cli(s.get())).place(x='10', y='330')

#btmute = Radiobutton(root, text='mudo', variable=s, value='m', command=lambda:cli(s.get())).place(x='10', y='350')

save = Button(root, width=10, text='save', font='Arial 4',).place(x='10', y='370')

root.mainloop()
