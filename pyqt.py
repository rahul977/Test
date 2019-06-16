# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from PyQt5 import QtGui #for icon
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        self.title = "PyQt5 Window"
        self.top = 100
        self.left = 100
        self.width = 680
        self.height =500
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.InitWindow()
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)
        self.show()
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())

#push button
import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow,QApplication,QPushButton,QToolTip



class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.title = "pyQt5 push button"
        self.left = 100
        self.top = 100
        self.width = 680
        self.height = 540
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        button = QPushButton("click me",self)
        button.move(200,200)
        button.setToolTip("<h3>This is a click button</h3>")
        self.InitUI()
    def InitUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top,self.left,self.width,self.height)
        self.show()
        
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())


#basics of signaland slots


        