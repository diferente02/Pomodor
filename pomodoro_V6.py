from time import sleep
from pyautogui import confirm, alert
import datetime
import pyttsx3
from tkinter import *

tempo_de_estudo = 0
pomodoro = 0

jl = Tk()
jl.title('Técnica pomodoro')
jl.geometry('500x700')

df = Label(jl, text='foco', )
df.place(x='200', y='80')

jl.mainloop()

# iniciando a notificação em fala
engine = pyttsx3.init()


# botão cancelar pressionado
def cancelou():
    hora, minutos = divmod(datetime.timedelta(minutes=tempo_de_estudo).total_seconds(), 3600)
    minutos, segundos = divmod(minutos, 60)
    if hora == 0:
        engine.say(f' parabens, você estudou por {minutos:.0f} minutos')
        engine.runAndWait()
        alert(f' parabens, você estudou por {minutos:.0f} minutos')

    else:
        engine.say(f' parabens, você estudou por{hora:.0f} hora(s) e {minutos:.0f} minutos')
        engine.runAndWait()
        alert(f' parabens, você estudou por{hora:.0f} hora(s) e {minutos:.0f} minutos')


# descanso normal
def descanso():
    # contagem de 0 a 5
    print('=' * 24)
    print(' ' * 8, 'descanso')
    print('=' * 24)
    for x in range(0, 5):
        print(x)
        sleep(60)
    engine.say('o descanso acabou')
    engine.runAndWait()
    des = confirm(text='O descanso acabou, aperte ok para voltar a trabalhar', title='Técnica pomodoro',
                  buttons=['ok', 'cancelar'])

# começo
alert('pressione ok para começar')
print('=' * 48)
print(' ' * 16, 'pomodoro')
print('=' * 48)
engine.say('vamos começar')
engine.runAndWait()

print()  # só pra dar uns espaços
#print(' Técnica pomodoro'
#   25 minutos focado
#   5 minutos descansando)
print()  # só pra dar uns espaços

while True:
    # contagem de 0 a 25 minutos
    print('=' * 18)
    print(' ' * 6, 'foco')
    print('=' * 18)
    for c in range(0, 25):
        print(c)
        sleep(60)

    tempo_de_estudo += 25
    pomodoro += 1

    # fala baby
    engine.say('tempo de trabalho terminado')
    engine.runAndWait()

    # botão que aparece na tela notificando que o tempo de trabalho acabou
    des = confirm(text='sessão finalizada aperte ok para descansar', title='Pausa pro café',
                  buttons=['ok', 'cancelar'])

    # caso a pessoa deseje parar de estudar
    if des == 'cancelar':
        cancelou()
        break

    # caso o usuario deseje continuar estudando
    else:
        # se já tiver passado 4 pomodoros
        if pomodoro % 4 == 0:
            # contagem de 0 a 30
            engine.say('"você está estudando muito e como um prêmio você recebeu um descanço de meia hora,aproveite"')
            engine.runAndWait()
            des = confirm(
                text="você está estudando muito e como um prêmio você recebeu um descanço de meia hora,aproveite",
                title='descanso premium', buttons=['descansar', 'continuar trabalhando', 'cancelar'])

            # se a pessoa desejar parar de estudar/trabalhar
            if des == 'cancelar':
                cancelou()
                break

            # se a pessoa desejar continuar trabalhando sem a pausa premium
            elif des == 'continuar trabalhando':
                descanso()

            # se a pessoa desejar o descanso premium
            else:
                print('=' * 48)
                print(' ' * 8, 'descanso premium')
                print('=' * 48)
                for x in range(0, 30):
                    print(x)
                    sleep(60)
                engine.say('descanso terminado')
                engine.runAndWait()
                des = confirm(text=' o descanso acabou, aperte ok para voltar a trabalhar', title='Descanso',
                              buttons=['ok', 'cancelar'])

                if des == 'cancelar':
                    cancelou()
                    break
        # se não tiver passado 4 pomodoros, ou seja descanso comum
        else:
            descanso()

            if des == 'cancelar':
                cancelou()
                break

print('by Victor Eduardo')
