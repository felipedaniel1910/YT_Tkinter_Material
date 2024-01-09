###########################################
##### Aula 01 - Introdução ao Tkinter #####
###########################################

"""
Nome do Projeto: Aula 01 - Introdução ao Tkinter
Autor: Felipe Daniel Ferreira de Almeida
Data de Criação: Janeiro de 2024
Objetivo: Ensinar conceitos iniciais sobre Tkinter.
Versões: Python (3.9.2)
"""
#########################
#### Install Tkinter ####
#########################

# No CMD, digitar: pip install tk

##########################
#### Testando Tkinter ####
##########################

"""
import tkinter as tk
tk._test()
print(tkinter.Tcl().eval('info patchlevel'))
"""

# Esta linha importa todos os símbolos do módulo tkinter. 
# tkinter é um módulo em Python que fornece funcionalidades para criar interfaces gráficas de usuário (GUI).
from tkinter import *
# Themed Tk (Ttk) é uma família mais recente de widgets Tk 
# que fornecem uma aparência muito melhor em diferentes plataformas 
# do que muitos dos widgets Tk clássicos. O Ttk é distribuído como parte do Tk, começando com o Tk versão 8.5.
from tkinter import ttk 
# Cria uma instância da classe Tk(), que representa a janela principal da GUI. 
# root é geralmente usado como um nome comum para a instância principal da janela.
root = Tk()
# Esta linha cria um botão (Button) com o texto "Hello World" e o coloca na janela principal (root). 
# O widget ttk.Button é utilizado para criar botões usando o tema aprimorado do ttk. 
# O método pack() organiza os widgets em blocos antes de inseri-los na janela. 
# Se não houver argumentos passados para o método pack(), o widget é colocado no bloco padrão da janela.
ttk.Button(root, text="Hello World").pack()
#  Inicia o loop principal da aplicação. Isso mantém a janela aberta, permitindo a interação do usuário. 
# O programa continua executando até que a janela seja fechada pelo usuário.
root.mainloop()

################
#### Janela ####
################

#################
#### Widgets ####
#################

# Widget é um elemento da interface gráfica do usuário (GUI) que exibe/ilustra informações 
# ou fornece uma maneira para o usuário interagir com o sistema operacional. 
# No Tkinter, Widgets são objetos; instâncias de classes que representam botões, quadros e assim por diante.

#################
#### Eventos ####
#################

#################
#### Layouts ####
#################

#############################
#### Classes ou funções? ####
#############################

# Complexidade do Projeto: Para aplicativos pequenos e simples, 
# funções podem ser mais diretas. No entanto, à medida que a complexidade 
# do projeto aumenta, a utilização de classes pode proporcionar uma estrutura mais sólida.






