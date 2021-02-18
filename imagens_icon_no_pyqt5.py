#interface grafica para APP_ID_NOME_QUANTIDADE 
from PyQt5.QtWidgets import (QWidget, QListWidget, QListView, QHBoxLayout, QVBoxLayout,
                             QApplication, QMainWindow, QLabel, QPushButton, QLineEdit, QGroupBox, QFormLayout)
import sys

#from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon, QPixmap #mostra imagens


class aplicativo(QWidget):
      def __init__(self, parent=None):
          """Esse é o init dessa classe aplicativo"""
          super(aplicativo, self).__init__(parent)
          
          #QUADRO DA JANELA
          self.setWindowTitle("APP - LISTA SIMPLES NO SQLITE SIMPLES")
          self.setGeometry(700, 400, 350, 300)
          self.setWindowIcon(QIcon("cifra.jfif"))  
          
          self.l1 = QLabel()
          self.l1.setPixmap(QPixmap("cifra.jfif"))
          
          vbox = QVBoxLayout()
          vbox.addWidget(self.l1)
          self.setLayout(vbox)


#ABRE A JANELA 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = aplicativo()
    janela.show()
    sys.exit(app.exec_())
