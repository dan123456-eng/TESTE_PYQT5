#CALCULADORA SIMPLES

#do PYQT5
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout,QApplication, QMainWindow, QLabel, QPushButton, QLineEdit
import sys


class aplicativo(QWidget):
      def __init__(self, parent=None):
          """Esse é o init dessa classe aplicativo"""
          super(aplicativo, self).__init__(parent)
          
          
          #QUADRO DA JANELA
          self.setWindowTitle("CALCULADORA SIMPLES")
          self.setGeometry(700, 400, 350, 300)

          #LAYOUT
          #HORIZONTAL
          self.hor = QHBoxLayout()
          self.setLayout(self.hor)
          #VERTICAL
          self.vor = QVBoxLayout()
          self.vor.addLayout(self.hor)
          self.setLayout(self.vor)

          #BOTÕES
          #transforma em maiuscula
          self.modifica_txt = QPushButton("modifica_txt")
          self.modifica_txt.setGeometry(100, 100, 100, 100) #cria a geometria do  botão
          self.hor.addWidget(self.modifica_txt) # adicionei self.b no layout

          # transforma em minuscula
          self.modifica_m = QPushButton("modifica_minuscula")
          self.modifica_txt.setGeometry(100, 100, 100, 100) #cria a geometria do  botão
          self.hor.addWidget(self.modifica_m) # adicionei self.b no layout
        
        
          self.limpar = QPushButton("limpar")
          self.limpar.setGeometry(100, 100, 100, 100) #cria a geometria do  botão
          self.hor.addWidget(self.limpar) # adicionei self.limpar no layout

          #ENTRADAS DE DADOS
          self.entradax = QLineEdit()
          self.hor.addWidget(self.entradax) #adiciona self.entradax no layout
          
          #SAIDA DE DADOS
          self.saida_result = QLabel("RESULTADO")
          self.saida_result.move(150,500)
          self.hor.addWidget(self.saida_result)
          
          '''sinais conecta nas funçoes(slots)'''
          self.modifica_txt.clicked.connect(self.analisa_txt)
          self.modifica_m.clicked.connect(self.analisa_minu)
          #limpa a operacao:
          self.limpar.clicked.connect(self.limpa)
          
      def analisa_txt(self):
          """txt maiusculo"""
          #print(self.entradax.text()) #mostra o valor digitado em self.entradax.
          r = self.entradax.text()
          txt = r.upper() # usando upper para mudar o tamanho do texto.
          #txt = r.lower() #transforma em minusculas
          self.saida_result.setText(txt)# usa saida_result para setar o resultado.
          
      def analisa_minu(self):
          """ txt minusculo"""
          #print(self.entradax.text()) #mostra o valor digitado em self.entradax.
          r = self.entradax.text()
          txt = r.lower() #transforma em minusculas
          self.saida_result.setText(txt)# usa saida_result para setar o resultado.
             
      def limpa(self):
          """limpa os imputs e output"""
          self.entradax.clear()
          self.saida_result.clear()
          
            
#ABRE A JANELA DA CALCULADORA
if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = aplicativo()
    janela.show()
    sys.exit(app.exec_())
