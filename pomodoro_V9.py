import pyttsx3
from tkinter import *
from pyautogui import confirm, alert

mudo = ()
cont = 0
engine = pyttsx3.init()

try:
    try:
        # tente abrir o arquivo txt
        aquivo = open("./tempodequalidade.txt", 'r')
        linha = aquivo.readlines()  # lê linhas especificas
        if not linha:
            m, s = 0, 0  # zera os minutos e segundos
        else:
            m = int(linha[0])  # lê na linha 0, os minutos
            s = int(linha[1])  # lê na linha 1, os segundos
        aquivo.close()


    except:

        # se não haver um arquivo TXT o programa irá dar erro, se der ele der erro deverá criar um novo arquivo txt
        aquivo = open("./tempodequalidade.txt", 'w')  # criando o arquivo TXT
        m, s = 0, 0  # zera os minutos e segundos
        aquivo.close()


    # ========================== funções ==========================================

    def salvandotxt(mi=0, se=0):
        arquivo = open("./tempodequalidade.txt", 'w')
        arquivo.write(str(mi))  # escreve no arquivo txt
        arquivo.write('\n')  # da uma quebra de linha
        arquivo.write(str(se))
        arquivo.close()



    def alertando_o_descanso():  # função que inicia o tempo de descanso
        global m, s  # definindoa as variaves m e s como globais
        estado = ligadooumudo.get()  # pegando o estado da variavel ligado ou mudo
        if estado == 'l':
            engine.say(f'os {m} minutos e {s} segundos já se passaram, descanse um pouco')  # aviso sonoro que acabou
            engine.runAndWait()
        alert(title='Descanso',
              text='tempo de foco terminado, descanse um pouco')  # janela de alerta, avisado que o tmepo de descanso terminou, só avisa mesmo


        rest()  # chama a função que inicia os 5 minutos de descanso


    def alertando_o_foco():  # função que volta pro tempo de trabalho
        estado = ligadooumudo.get()  # pegando o estado da variavel ligado ou mudo
        if estado == 'l':
            engine.say(f'O tempo de descanso acabou')  # aviso falado que o tempo de descanso acabou
            engine.runAndWait()
        alert(title='Descanso',
              text='tempo de descanso terminado')  # janela de alerta, avisado que o tmepo de descanso terminou, só avisa mesmo

        countdowntimer()  # chama a função que inicia a contagem do tempo de trabalho


    def btmin_click():  # botão de "mais" dos minutos
        global m  # coloca mimutos como variavel global
        m += 1  # quando o botão é pressionado m é acrescido de 1
        if m > 59:  m = 0  # zera a contagem quando o valor da variavel supera 59
        min.set(m)  # altera na janela o valor dos minutos, variavel m
        salvandotxt(m, s)  # chama a função que salva no arquivo txt o novo valor dos segundo e minutos


    def btmin2_click():  # botão de "menos" dos minutos
        global m  # coloca n como variavel global
        m -= 1  # subtrai 1 da variavel m
        if m < 0: m = 0  # zera a variavel se o valor da variavel for menor que 0
        min.set(m)  # diminui o número dos minutos
        salvandotxt(m, s)  # chama a função que salva no arquivo txt o novo valor dos segundo e minutos


    def btsec_click():  # botão de mais dos minutos
        global s  # coloca s como variavel global
        s += 1  # quando pressionado soma 1 ao valor da variavel s
        if s > 59: s = 0  # zera a contagem quando o valor da variavel supera 59
        sec.set(s)  # aumenta o número dos segundos
        salvandotxt(m, s)  # chama a função que salva no arquivo txt o novo valor dos segundo e minutos


    def btsec2_click():  # botão de menos dos segundos
        global s  # coloca s como variavel global
        s -= 1  # subtrai 1 do valor da variavel s quando o botão é pressionado
        if 0 > s: s = 0  # zera a variavel se o valor da variavel for menor que 0
        sec.set(s)  # diminui o número dos segundos
        salvandotxt(m, s)  # chama a função que salva no arquivo txt o novo valor dos segundo e minutos


    def parar():
        global cont
        cont += 1


    def countdowntimer():  # o temporizador
        # https://www.tutorialspoint.com/how-to-create-a-timer-using-tkinter
        # Define the function for the timer
        global cont
        global s, m, aquivo, linha
        cont += 1
        btp.place(x='100', y='270')  # aparece o botão pausar
        df['text'] = 'FOCO'  # muda o texto do Label de "descanso" para "foco"
        df.place(x='115', y='30')  # define a posição do Label "foco"
        bt['text'] = 'reiniciar'  # muda o text odo botão bt de iniciar para reiniciar
        bt.place(x='100', y='230') # volta a mostrar o botão iniciar

        # enquanto o temporizador estiver ligado não mostra os botoes de mais e menos dos minutos e segundos
        btmin.place_forget()
        btmin2.place_forget()
        btsec.place_forget()
        btsec2.place_forget()

        times = int(m) * 60 + int(s)

        m_inicial = m
        s_inicial = s
        while times > -1:
            minute, second = (times // 60, times % 60)
            sec.set(second)
            min.set(minute)
            # Update the time
            root.after(1000, root.update())  # depois de 1 segundo (1000 ms) atualiza a pagina

            # verfica se o usuário decidiu pausar a contagem
            if cont % 2 == 0:  # essa condição encerra o loop, caso o usuario deseja continuar, um novo loop se inicia a partir dos minutos e segundo pausados
                bt['text'] = 'Continuar'  # muda o texto do botão de "iniciar" para "continuar"
                m, s = minute, second
                break

            # se o loop não for interrompido( se o usuario não apertar o botão de pause)
            else:
                # m e s volta a ser o que ta salvo no arquivo txt
                aquivo = open("./tempodequalidade.txt", 'r')
                m = int(linha[0])  # lê na linha 0, os minutos
                s = int(linha[1])  # lê na linha 1, os segundos
                aquivo.close()

            times -= 1
        if cont % 2 == 1:  # se a contagem estiver acontecendo
            bt['text'] = 'Iniciar'  # muda o texto do botão de "continuar" para "iniciar"
            alertando_o_descanso()

        # voltando a mostrar os botões de mais e de menos
        btmin.place(x='125', y='95')
        btmin2.place(x='125', y='160')
        btsec.place(x='155', y='95')
        btsec2.place(x='155', y='160')


    def rest():  # função descanso
        global m, s
        df['text'] = 'DESCANSO'  # muda o texto do label de "foco" para "descanso"
        df.place(x='85', y='30')
        btp.place_forget()  # desaparecer com o botão pausar
        bt.place_forget()  # desaparece com o botão iniciar

        # enquanto o temporizador estiver ligado não mostra os botoes de mais e menos dos minutos e segundos
        btmin.place_forget()
        btmin2.place_forget()
        btsec.place_forget()
        btsec2.place_forget()

        # essa parte eu ainda não entendi
        times = int(0) * 60 + int(10)
        while times > -1:
            minute, second = (times // 60, times % 60)
            sec.set(second)
            min.set(minute)
            # Update the time
            root.after(1000, root.update())  # depois de 1 segundo (1000 ms) atualiza a pagina

            if times == 0:  # quando a contagem terminar fica com "00" ao invés de "0"
                sec.set('00')
                min.set('00')
            times -= 1
        alertando_o_foco()


    root = Tk()
    root.title('Tecnica pomodoro')
    root.geometry('300x400+200+50')

    # ======================== descanso ou foco ==================================
    df = Label(root, text='FOCO', font="Arial 20")
    df.place(x='115', y='30')

    # =============================== Variable second =============================
    sec = StringVar()
    Label(root, textvariable=sec, width=2, font="Arial 14").place(x='155', y='130')
    sec.set(s)

    # ===================== just two points (:) ===================================
    Label(root, text=':', font='Arial 16').place(x='145', y='130')

    # ======================== Variable minutes ====================================
    min = StringVar()
    Label(root, textvariable=min, width=2, font="Arial 14").place(x='120', y='130')
    min.set(m)

    # ========================= botões =============================================
    bt = Button(root, width=10, text='Iniciar', font='Arial 12', command=countdowntimer)
    bt.place(x='100', y='230')

    btp = Button(root, width=10, text='Pausar', font='Arial 12', command=parar)

    btmin = Button(root, width=1, text='+', font='Arial 12', command=btmin_click)
    btmin.place(x='125', y='95')

    btmin2 = Button(root, width=1, text='-', font='Arial 12', command=btmin2_click)
    btmin2.place(x='125', y='160')

    btsec = Button(root, width=1, text='+', font='Arial 12', command=btsec_click)
    btsec.place(x='155', y='95')

    btsec2 = Button(root, width=1, text='-', font='Arial 12', command=btsec2_click)
    btsec2.place(x='155', y='160')

    ligadooumudo = StringVar()  # variavel necessária pro radiobutton

    bt_somdesligado = Radiobutton(root, text='Alerta Sonoro desligado', font='Arial 10', value='d', variable=ligadooumudo)
    bt_somdesligado.place(x='10', y='370')

    bt_somligado = Radiobutton(root, text='Alerta Sonoro ligado', font='Arial 10', value="l", variable=ligadooumudo)
    bt_somligado.place(x='10', y='350')

    root.mainloop()

except:  # caso de algum erro o arquivo executavél vai mostrar uma janela de alerta informando que deu erro.
    alert(title="erro", text='ocorreu algum erro')
