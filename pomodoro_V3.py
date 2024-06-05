from time import sleep
from pyautogui import confirm, alert
import datetime

tempo_de_estudo = 0
alert('pressione ok para começar')
print('=' * 48)
print(' ' * 16, 'pomodoro')
print('=' * 48)

print()  # só pra dar uns espaços
print(''' Técnica pomodoro
    25 minutos focado
    5 minutos descansando''')
print()  # só pra dar uns espaços

while True:
    # contagem de 0 a 25 minutos
    print('=' * 18)
    print(' ' * 6, 'foco')
    print('=' * 18)
    for c in range(0, 25):
        print(c)
        sleep(60)
    tempo_de_estudo += 1

    # botão que aparece na tela notificando que o tempo de trabalho acabou
    des = confirm(text='sessão finalizada aperte ok para continuar', title='Técnica pomodoro',
                  buttons=['ok', 'cancelar'])

    if des == 'cancelar':
        hora, minutos = divmod(datetime.timedelta(minutes=tempo_de_estudo).total_seconds(), 3600)
        minutos, segundos = divmod(minutos, 60)
        if hora == 0:
            alert(f' parabens, você estudou por {minutos:.0f} minutos')
        else:
            alert(f' parabens, você estudou por{hora:.0f} hora(s) e {minutos:.0f} minutos')
        break
    else:
        if tempo_de_estudo % 4 == 0:
            # contagem de 0 a 30
            des = confirm(
                text="você está estudando muito e como um prêmio você recebeu um descanço de meia hora,aproveite",
                title='descanso premium', buttons=['descansar', 'continuar trabalhando', 'sair'])

            # se a pessoa desejar parar de estudar/trabalhar
            if des == 'sair':
                hora, minutos = divmod(datetime.timedelta(minutes=tempo_de_estudo).total_seconds(), 3600)
                minutos, segundos = divmod(minutos, 60)
                if hora == 0:
                    alert(f' parabens, você estudou por {minutos:.0f} minutos')
                else:
                    alert(f' parabens, você estudou por{hora:.0f} hora(s) e {minutos:.0f} minutos')
                break

            # se a pessoa desejar continuar trabalhando sem a pausa premium
            elif des == 'continuar trabalhando':
                alert('pelo menos descanse 5 minutos')
                print('=' * 24)
                print(' ' * 8, 'descanso')
                print('=' * 24)
                for x in range(0, 5):
                    print(x)
                    sleep(60)
                des = confirm(text='sessão finalizada aperte ok para continuar', title='Técnica pomodoro',
                              buttons=['ok', 'cancelar'])

            # se a pessoa desejar o descanso premium
            else:
                print('=' * 24)
                print(' ' * 8, 'descanso premium')
                print('=' * 24)
                for x in range(0, 30):
                    print(x)
                    sleep(60)
                des = confirm(text='sessão finalizada aperte ok para continuar', title='Técnica pomodoro',
                              buttons=['ok', 'cancelar'])

                if des == 'cancelar':
                    hora, minutos = divmod(datetime.timedelta(minutes=tempo_de_estudo).total_seconds(), 3600)
                    minutos, segundos = divmod(minutos, 60)
                    if hora == 0:
                        alert(f' parabens, você estudou por {minutos:.0f} minutos')
                    else:
                        alert(f' parabens, você estudou por{hora:.0f} hora(s) e {minutos:.0f} minutos')
                    break


        else:
            # contagem de 0 a 5
            print('=' * 24)
            print(' ' * 8, 'descanso')
            print('=' * 24)
            for x in range(0, 5):
                print(x)
                sleep(60)
            des = confirm(text='sessão finalizada aperte ok para continuar', title='Técnica pomodoro',
                          buttons=['ok', 'cancelar'])

            if des == 'cancelar':
                hora, minutos = divmod(datetime.timedelta(minutes=tempo_de_estudo).total_seconds(), 3600)
                minutos, segundos = divmod(minutos, 60)
                if hora == 0:
                    alert(f' parabens, você estudou por {minutos:.0f} minutos')
                else:
                    alert(f' parabens, você estudou por{hora:.0f} hora(s) e {minutos:.0f} minutos')
                break
