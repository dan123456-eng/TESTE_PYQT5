#interface grafica para APP_ID_NOME_QUANTIDADE 
from PyQt5.QtWidgets import (QWidget, QListWidget, QListView, QHBoxLayout, QVBoxLayout,
                             QApplication, QAction, QMenuBar, QMainWindow, QLabel, QPushButton, QLineEdit, QGroupBox, QFormLayout)

import sys

#from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QPixmap #mostra imagens


class aplicativo(QWidget):
      def __init__(self, parent=None):
          """Esse é o init dessa classe aplicativo"""
          super(aplicativo, self).__init__(parent)
          
          """QUADRO DA JANELA"""
          self.setWindowTitle("NOTAS FISCAIS")
          self.setGeometry(700, 400, 350, 300)
          self.setWindowIcon(QIcon("notas.jfif"))

          """buttons"""
          self.adiciona = QPushButton("adiciona")
          self.exclui = QPushButton("ecluir")
          self.atualiza = QPushButton("atualizar")
          self.motra = QPushButton("mostrar")
          self.limpar =QPushButton("limpar")
          
          """GROUPBOX"""
          self.layout = QFormLayout()
          self.layout.addRow(QLabel("Name:"), QLineEdit())
          self.layout.addRow(QLabel("numero:"), QLineEdit())
          self.layout.addRow(QLabel("quantidade:"), QLineEdit())
          
          """LISTA DE ITENS"""
          self.lista = QListWidget()
          self.lista.setGeometry(100, 100, 100, 100)
          self.layout.addRow(QLabel("LISTA DE ITENS:"), self.lista)
          #self.layout.addRow(QLabel("buttons:"), self.adiciona)
          self.setLayout(self.layout)


#ABRE A JANELA 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = aplicativo()
    janela.show()
    sys.exit(app.exec_())
