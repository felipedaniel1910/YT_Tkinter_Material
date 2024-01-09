# Esta linha importa todos os símbolos do módulo tkinter. 
# tkinter é um módulo em Python que fornece funcionalidades para criar interfaces gráficas de usuário (GUI).
from tkinter import ttk, Frame, Tk
import requests
import pandas as pd

def PegarCotacao():
    link = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'

    req = requests.get(link).content
    df = pd.read_json(req)
    print(df.loc['bid','USDBRL'])
    return None

def Converter():
    tela1_resultado =  Frame(body_frame, height=300, highlightbackground="red", highlightthickness=2, background="yellow")
    label3 = ttk.Label(tela1_resultado, text="X Reais é equivalente a: xxxx Doláres", background="#d3d3d3", font="georgia 20 bold")
    label3.grid(row=2, column=0, padx=20, pady=20)
    tela1_resultado.pack(fill="x")
    tela1_resultado.propagate(False)
    return None

def Tela1():
    label1 = ttk.Label(header_frame, text="Conversor de Moedas", background="#d3d3d3", font="georgia 20 bold")
    label1.pack(pady=20)
    tela1_body =  Frame(body_frame, height=300, highlightbackground="red", highlightthickness=2, background="yellow")
    label2 = ttk.Label(tela1_body, text="Valor em Real:", background="#d3d3d3", font="georgia 20 bold")
    label2.grid(row=0, column=0, padx=20, pady=20)
    ttk.Entry(tela1_body, width=10, font="georgia 20 bold").grid(row=0, column=1, padx=20)
    ttk.Label(tela1_body, text="Converter para:", background="#d3d3d3", font="georgia 20 bold").grid(row=1, column=0, padx=20)
    style = ttk.Style()
    style.configure("TRadiobutton", foreground="black", background="#d3d3d3", padding=20, font="georgia 20 bold") # fonte: https://ultrapythonic.com/ttk-radiobutton/
    ttk.Radiobutton(tela1_body, text="Dólar", value=1).grid(row=1, column=1 )
    ttk.Radiobutton(tela1_body, text="Euro", value=2).grid(row=1, column=2 )
    ttk.Radiobutton(tela1_body, text="Bitcoin", value=3).grid(row=1, column=3)
    #style.theme_use("clam")
    style.configure("TButton", font=("georgia", 20, "bold"), foreground="blue", background="yellow")
    ttk.Button(footer_frame, text="Converter", command= lambda: Converter()).pack(pady=20)
    tela1_body.pack(fill="x")
    tela1_body.propagate(False)
    return None

root = Tk()
root.geometry("800x500")

# Defina uma largura para a borda do Frame
general_frame = Frame(root, highlightbackground="blue", highlightthickness=2)
header_frame = Frame(general_frame, height=100, highlightbackground="blue", highlightthickness=2, background="blue")
body_frame =  Frame(general_frame, height=300, highlightbackground="red", highlightthickness=2, background="red")
footer_frame =  Frame(general_frame, height=100, highlightbackground="green", highlightthickness=2, background="green")

general_frame.pack(fill="both", expand=True)
header_frame.pack(fill="x")
header_frame.propagate(False)
body_frame.pack(fill="x")
body_frame.propagate(False)
footer_frame.pack(fill="x")
footer_frame.propagate(False)

Tela1()
root.mainloop()


"""

# pegar cotação de moedas
# link = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'
link = 'https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL'

import requests
import pandas as pd

req = requests.get(link).content
df = pd.read_json(req)
print(df.loc['bid','USDBRL'])

"""



