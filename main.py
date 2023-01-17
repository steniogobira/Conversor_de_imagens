import tkinter as ttk
from tkinter import filedialog
import os

pasta = ''


def get_diretorio():
    global pasta
    pasta = str(filedialog.askdirectory(title='selecione'))
    Label02['text'] = pasta
    Label03['text'] = "Diretório selecionado!"


def converter():
    global pasta


janela = ttk.Tk()
janela.title('Conversor de Imagens')


frame01 = ttk.Frame(janela)
label01 = ttk.Label(
    frame01, text='SELECIONE UM DIRETÓRIO', font=('helvetica', 15))
Label02 = ttk.Label(frame01, text='INFORMAÇÕES APARECERAM AQUI', width='30',
                    relief='groove')
Label03 = ttk.Label(frame01, text='STATUS')
botao01 = ttk.Button(frame01, text='SELECIONAR',
                     command=get_diretorio)


frame02 = ttk.Frame(janela)
checkbutton = ttk.Checkbutton(janela,)
botao02 = ttk.Button(
    frame02, text='CONVERTER IMAGENS', command=converter)


frame03 = ttk.Frame(janela, borderwidth='1', width='25',
                    height='10', relief="groove")
Label04 = ttk.Label(frame03, text='A', borderwidth='1', width='25',
                    height='10', relief="groove")


botao01.grid(column=3, row=2, padx='5', sticky='w')
botao02.grid(column=0, row=0)


frame01.grid(column=0, row=0)
frame02.grid(column=0, row=1, pady='5')
frame03.grid(column=2, row=0, pady='5', sticky='s')


label01.grid(column=0, row=0, sticky='w')
Label02.grid(column=0, row=2)
Label03.grid(column=0, row=3, sticky='w')
Label04.grid(column=0, row=0, sticky='s')


janela.mainloop()
