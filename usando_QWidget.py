# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 16:54:37 2020

@author: LG
"""
# UM OLA MUNDO ESPECIAL

from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QPushButton
import sys

apl = QApplication([])

janela = QMainWindow()
janela.setGeometry(30,30,500,500)
janela.setWindowTitle("OLA MUNDO")

label = QLabel(janela)
label.setGeometry(100,100,300,300)
label.setText("msg")

botao = QPushButton(janela)
botao.move(10,10)
botao.setText("info")

def mostra():
    label.setText("fala ai pessoal!")
botao.clicked.connect(mostra)
    
janela.show()
apl.exec_()