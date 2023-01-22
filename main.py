import tkinter as ttk
from tkinter import filedialog
import fuction
from tkinter.ttk import Progressbar
import os
import time

path = os.getcwd()


def get_diretorio():

    global path, barra_progresso, atualizar_progresso

    fuction.del_filetext()
    barra_progresso.config(value=0)
    atualizar_progresso()

    path = str(filedialog.askdirectory(title='selecione'))
    Label02['text'] = path
    Label03['text'] = "Novo diretório selecionado!"


def converter():

    global path, vjpge, barra_progresso, atualizar_progresso
    fuction.del_filetext()
    barra_progresso.config(value=0)
    atualizar_progresso()

    if vjpge.get() == 1:
        time.sleep(2)
        fuction.to_jpeg(path)
        barra_progresso.config(value=30)
        atualizar_progresso()

    if vpng.get() == 1:
        time.sleep(2)
        fuction.to_png(path)
        barra_progresso.config(value=60)
        atualizar_progresso()

    if vgif.get() == 1:
        time.sleep(2)
        fuction.to_gif(path)
        barra_progresso.config(value=90)
        atualizar_progresso()

    barra_progresso.config(value=100)
    atualizar_progresso()


janela = ttk.Tk()


# Frame 01
frame01 = ttk.Frame(janela)
label01 = ttk.Label(frame01, text='SELECIONE O DIRETÓRIO DOS ARQUIVOS',
                    font=("Arial", 20, "bold"), foreground="white")
Label02 = ttk.Label(frame01, text=path,
                    width='50', relief='groove')
Label03 = ttk.Label(frame01, text='')
botao01 = ttk.Button(frame01, text='SELECIONAR',
                     command=get_diretorio)

frame01.grid(column=0, row=0, sticky='n', pady=5)
label01.grid(column=0, row=1, sticky='w', pady=5)
Label02.grid(column=0, row=2, pady=5, sticky='w')
Label03.grid(column=0, row=3, sticky='w', pady=5)
botao01.grid(column=3, row=2, pady=5)

# Frame 02

frame02 = ttk.Frame(janela)
barra_rolagem = ttk.Scrollbar(frame02)
texto_log1 = ttk.Text(frame02, borderwidth='1', width=80,
                      height=10, relief="groove", yscrollcommand=barra_rolagem.set)
barra_rolagem.config(command=texto_log1.yview)


barra_progresso = Progressbar(
    frame02, mode='determinate', length=550, value=0)

Label04 = ttk.Label(
    frame02, text='Selecione para que formato você deseja converter')


def atualizar_progresso():
    with open("conversion_log.txt", "r") as f:
        texto_log1.delete(1.0, ttk.END)
        texto_log1.insert(ttk.END, f.read())
        janela.update()


frame02.grid(column=0, row=2, pady=5)
texto_log1.grid(column=0, row=0, sticky='w')
barra_rolagem.grid(column=1, row=0, sticky='ns')
barra_progresso.grid(column=0, row=2)
Label04.grid(column=0, row=3, sticky='w', padx=5, pady=5)

# Frame 03
frame03 = ttk.Frame(janela)


vjpge = ttk.IntVar()
checkbutton_jpge = ttk.Checkbutton(
    frame03, text='Jpge', variable=vjpge, onvalue=True, offvalue=False)

vpng = ttk.IntVar()
checkbutton_png = ttk.Checkbutton(
    frame03, text='Png', variable=vpng, onvalue=True, offvalue=False)

vgif = ttk.IntVar()
checkbutton_gif = ttk.Checkbutton(
    frame03, text='Gif', variable=vgif, onvalue=True, offvalue=False)


botao02 = ttk.Button(
    frame03, text='CONVERTER IMAGENS', command=converter)


frame03.grid(column=0, row=3, sticky='w')
frame03.grid_columnconfigure(0, weight=1)
frame03.grid_columnconfigure(1, weight=1)
frame03.grid_columnconfigure(2, weight=1)

checkbutton_jpge.grid(column=0, row=1, padx=5, pady=5,
                      sticky='w')
checkbutton_png.grid(column=1, row=1, padx=5, pady=5,
                     sticky='ew')
checkbutton_gif.grid(column=2, row=1, padx=5, pady=5,
                     sticky='e')
botao02.grid(column=3, row=2, sticky='ew')


janela.mainloop()
fuction.del_filetext()
