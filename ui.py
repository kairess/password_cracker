import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui
import random

class App(QMainWindow):
  def __init__(self):
    super().__init__()
    self.title = '컴투존피씨방에서 만원에 구입한 싸구려 보안 프로그램'
    self.left = 0
    self.top = 0
    self.width = 1920
    self.height = 1080
    self.initUI()
 
  def initUI(self):
    self.setWindowTitle(self.title)
    self.setGeometry(self.left, self.top, self.width, self.height)
 
    self.label = QLabel('님컴퓨터이제못함ㅋ\n비밀번호입력하셈 -엄마', self)
    self.label.setFont(QFont("Arial", 20))
    self.label.resize(280, 200)
    self.label.move(640, 160)

    # Create textbox
    self.textbox = QLineEdit(self)
    self.textbox.setEchoMode(QLineEdit.Password)
    self.textbox.setFont(QFont("Arial", 20))
    # self.textbox.setAlignment(QtCore.Qt.AlignCenter)
    self.textbox.move(580, 300)
    self.textbox.resize(280, 40)
 
    # Create a button in the window
    self.button = QPushButton('확인', self)
    self.button.move(670, 360)
 
    # connect button to function on_click
    self.button.clicked.connect(self.on_click)
    self.textbox.returnPressed.connect(self.on_click)
    self.show()
 
  @pyqtSlot()
  def on_click(self):
    textboxValue = self.textbox.text()
    if len(textboxValue) < 2 or len(textboxValue) > 10:
      QMessageBox.question(self, '엄마로부터의 메시지', '비밀번호는 최소 2자리, 최대 10자리입니다', QMessageBox.Ok, QMessageBox.Ok)
    else:
      rand = random.randint(0, 100)
      QMessageBox.question(self, '', '비밀번호 일치 점수: %s' % (rand), QMessageBox.Ok, QMessageBox.Ok)
    self.textbox.setText('')

if __name__ == '__main__':
  app = QApplication(sys.argv)
  ex = App()
  sys.exit(app.exec_())