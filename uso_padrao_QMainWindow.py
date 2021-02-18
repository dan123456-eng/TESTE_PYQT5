import sys
#interface grafica para APP_ID_NOME_QUANTIDADE 
from PyQt5.QtWidgets import (QWidget, QListWidget, QListView, QHBoxLayout, QVBoxLayout,
                             QApplication, QProgressBar, QAction, QToolBar, QTextEdit, QDockWidget, QMenuBar, QMainWindow, QLabel, QPushButton, QLineEdit, QGroupBox, QFormLayout)

from PyQt5.QtGui import QIcon, QPixmap #mostra imagens
from PyQt5.QtCore import *
#from PyQt5.QtGui import *

class aplicativo(QWidget):
      def __init__(self, parent=None):
          """Esse é o init dessa classe aplicativo"""
          super(aplicativo, self).__init__(parent)
          
          """QUADRO DA JANELA"""
          self.setWindowTitle("NOTAS FISCAIS")
          self.setGeometry(200, 200, 200, 200)
          self.setWindowIcon(QIcon("notas.jfif"))
          
          """GROUPBOX"""
          self.layout = QFormLayout()
          self.layout.addRow(QLabel("Name:"), QLineEdit())
          self.layout.addRow(QLabel("numero:"), QLineEdit())
          self.layout.addRow(QLabel("quantidade:"), QLineEdit())
          
          """LISTA DE ITENS"""
          self.lista = QListWidget()
          self.lista.setGeometry(50, 50, 50, 50)
          self.layout.addRow(QLabel("LISTA DE ITENS:"), self.lista)

          #buttons
          self.adiciona = QPushButton("adiciona")
          self.exclui = QPushButton("ecluir")
          self.atualiza = QPushButton("atualizar")
          self.motra = QPushButton("mostrar")
          self.limpar =QPushButton("limpar")
          
          self.layout.addRow(QLabel("ADD:"), self.adiciona)
          self.layout.addRow(QLabel("DELETE:"), self.exclui)
          self.layout.addRow(QLabel("UPDARE:"), self.atualiza)
          self.layout.addRow(QLabel("VIEW:"), self.motra)
          self.layout.addRow(QLabel("CLIER:"), self.limpar)
          #Final buttons
          
          self.setLayout(self.layout)
"""
#ABRE A JANELA 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = aplicativo()
    janela.show()
    sys.exit(app.exec_())"""


class menudemo(QMainWindow): # Para criar um menu para um programa PyQt5, precisamos usar uma Janela QMain.
   def __init__(self, parent = None):
      super(menudemo, self).__init__(parent)

      self.setWindowTitle("NOTAS FISCAIS")
      self.setGeometry(700, 600, 550, 500)
      self.setWindowIcon(QIcon("notas.jfif"))
		
      self.layout = QHBoxLayout()
      bar = self.menuBar()
      file = bar.addMenu("File")
      file.addAction("New")
		
      save = QAction("Save",self)
      save.setShortcut("Ctrl+S")
      file.addAction(save)
		
      edit = file.addMenu("Edit")
      edit.addAction("copy")
      edit.addAction("paste")
		
      quit = QAction("Quit",self) 
      file.addAction(quit)
      file.triggered[QAction].connect(self.processtrigger)

      self.setLayout(self.layout)
      
      #toolbar
      toolbar = QToolBar("My main toolbar")
      self.addToolBar(toolbar)
      # final toolbar

      # StatusBar
      self.statusBar().showMessage('Minha messagem na statusBar!!!')
      # Final StatusBar
      
      #QListWidget
      self.listWidget = QListWidget()
      self.listWidget.addItem("item1")
      self.listWidget.addItem("item2")
      self.setCentralWidget(self.listWidget)

      """
      # QProgressBar
      self.progress = QProgressBar(self)
      self.progress.setGeometry(0, 0, 300, 25)
      self.progress.setMaximum(100)
      # final QProgressBar"""
      
      #USANDO QDockWidget
      self.items = QDockWidget("GERENCIADOR DE DADOS", self)
      #self.setCentralWidget(self.hlayout)
      self.items.setWidget(aplicativo()) # adiciona a class aplicativo(QWidget):
      self.items.setFloating(False)
      #self.setCentralWidget(QTextEdit())
      self.addDockWidget(Qt.RightDockWidgetArea, self.items)
      
   def processtrigger(self,q):
      print(q.text()+" is triggered")

def main():
   app = QApplication(sys.argv)
   ex = menudemo()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()
   
