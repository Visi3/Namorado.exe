import tkinter
from tkinter import messagebox

root = tkinter.Tk()
root.withdraw()

count = 0

msg_box = messagebox.showwarning('TOMOU CABEÇUDO','VOCÊ FOI HACKEADO')
if msg_box == 'ok':
    msg_box = messagebox.showwarning('A SOLUÇÃO','PARA SER DESHACKEADO PRECISA RESPONDER UMA PERGUNTA...')
if msg_box == 'ok':
    msg_box = messagebox.askquestion('','QUER PASSAR O RESTO DA VIDA COMIGO???')

while msg_box == 'no':
    count += 1
    msg_box = messagebox.askquestion('','QUER PASSAR O RESTO DA VIDA COMIGO???')
    if count == 5:
        msg_box = messagebox.showerror('TO INDO AI', 'SE VAI APANHAR PIA!')
        break
if msg_box == 'yes':
    msg_box = messagebox.showinfo('BOA ESCOLHA', 'AMO VOCÊ, GATÃO DE UMA VIDA!')

