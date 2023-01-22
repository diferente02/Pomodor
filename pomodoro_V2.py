from time import sleep
from pyautogui import confirm, alert
import datetime

tempo_de_estudo = 0
alert('press ok to init')
print('=' * 48)
print(' ' * 16, 'pomodoro')
print('=' * 48)

print()  # just espace
print(''' pomodoro Tecnique
    25 minutes focus
    5 minutes resting''')
print()  # just space

while True:
    # count form 0 to 25
    print('=' * 18)
    print(' ' * 6, 'focus')
    print('=' * 18)
    for c in range(0, 25):
        print(c)
        sleep(60)
    tempo_de_estudo += 25

    # button that notify the time over
    des = confirm(text='the time over, press ok to continue', title='Pomodoro tecnique',
                  buttons=['ok', 'cancel'])

    if des == 'cancel':
        hora, minutos = divmod(datetime.timedelta(minutes=tempo_de_estudo).total_seconds(), 3600)
        minutos, segundos = divmod(minutos, 60)
        if hora == 0:
            alert(f' congratulations, you worked for {minutos:.0f} minutes')
        else:
            alert(f" congratulations, you worked {hora:.0f} o'clock and {minutos:.0f} minutes")
        break
    else:
        if tempo_de_estudo % 10 == 0:
            #contagem de 0 a 30
            alert("you are work a lot, rest a little")
            print('=' * 24)
            print(' ' * 8, 'rest')
            print('=' * 24)
            for x in range(0, 30):
                print(x)
                sleep(60)
        else:
            # contagem de 0 a 5
            print('=' * 24)
            print(' ' * 8, 'rest')
            print('=' * 24)
            for x in range(0, 5):
                print(x)
                sleep(60)
            des = confirm(text='the time over press ok to continue', title='Pomodoro Tecnique',
                          buttons=['ok', 'cancel'])

            if des == 'cancel':
                hora, minutos = divmod(datetime.timedelta(minutes=tempo_de_estudo).total_seconds(), 3600)
                minutos, segundos = divmod(minutos, 60)
                if hora == 0:
                    alert(f' parabens, você estudou por {minutos:.0f} minutos')
                else:
                    alert(f' parabens, você estudou por{hora:.0f} hora(s) e {minutos:.0f} minutos')
                break
