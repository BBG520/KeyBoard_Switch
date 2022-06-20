# -*- coding:utf-8 -*-
# import sys
# from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
# class MainWindow(QMainWindow):
#     def __init__(self, parent=None):
#         super(MainWindow, self).__init__(parent)
#         self.resize(600, 300)
#         self.setWindowTitle('创建按钮和按钮点击事件的例子')
#         self.button1 = QPushButton('按键1', self)
#         self.button1.clicked.connect(self.clickButton)
#     def clickButton(self):
#         sender = self.sender()
#         print(sender.text() + '被点击')
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     main = MainWindow()
#     main.show()
#     sys.exit(app.exec_())
#--------------------------------------------------------
# 实例：点击按钮按钮数字加1
# 导入相关模块和包
# from PyQt5.Qt import *
# import sys
#
# # 创建一个app对象
# app = QApplication(sys.argv)
# # 创建一个窗口
# window = QWidget()
# # 设置窗口标题
# window.setWindowTitle('按钮功能测试')
# # 设置窗口大小
# window.resize(500, 500)
#
#
# # 创建槽函数
# def add_one():
#     # 接受用户设置 并转为int类型
#     number = int(btn.text())
#     # 每次点击+1
#     number += 1
#     # 把int类型转为字符串类型
#     btn.setText(str(number))
#
#
# # 创建一个按钮控件
# btn = QPushButton(window)
# # 设置按钮内容
# btn.setText('Press')
# # 连接按钮点击事件
# btn.pressed.connect(add_one)
# # 展示窗口
# window.show()
# # 进入事件循环
# sys.exit(app.exec_())
#--------------------------------------------------------
import sys
from PyQt5 import QtWidgets,QtGui
import PyQt5.QtCore
from pynput.keyboard import Key, Controller
import pynput
import time

# keys = pynput.keyboard.Controller()
def Keyboard_Switch():
    keys = pynput.keyboard.Controller()
    with pynput.keyboard.Events() as events:
        for event in events:
            if event.key == pynput.keyboard.Key.esc:
                sys.exit(app.exec_())
                break
            # elif event.key == pynput.keyboard.Events.Press('1'):
            #     print('Test OK')
            #     key.press('A')
            #     time.sleep(1)
            #     key.release('A')
            # Windows key cmd test
            elif event.key == pynput.keyboard.KeyCode.from_char('v'):
                time.sleep(5)
                keys.press(Key.cmd)
                time.sleep(2)
                keys.release(Key.cmd)
            elif event.key == pynput.keyboard.KeyCode.from_char('1'):
                time.sleep(0)  # Adjust the delay time when the key pressed
                keys.press(Key.alt_l)
                time.sleep(0.1)  # Adjust the two key sequence delay time
                keys.press('q')
                keys.release(Key.alt_l)
                keys.release('q')
            elif event.key == pynput.keyboard.KeyCode.from_char('2'):
                time.sleep(0)  # Adjust the delay time when the key pressed
                keys.press(Key.alt_l)
                time.sleep(0.1)  # Adjust the two key sequence delay time
                keys.press('w')
                keys.release(Key.alt_l)
                keys.release('w')
            elif event.key == pynput.keyboard.KeyCode.from_char('3'):
                time.sleep(0)  # Adjust the delay time when the key pressed
                keys.press(Key.alt_l)
                time.sleep(0.1)  # Adjust the two key sequence delay time
                keys.press('a')
                keys.release(Key.alt_l)
                keys.release('a')
            elif event.key == pynput.keyboard.KeyCode.from_char('4'):
                time.sleep(0)  # Adjust the delay time when the key pressed
                keys.press(Key.alt_l)
                time.sleep(0.1)  # Adjust the two key sequence delay time
                keys.press('d')
                keys.release(Key.alt_l)
                keys.release('d')
            elif event.key == pynput.keyboard.KeyCode.from_char('5'):
                time.sleep(0)  # Adjust the delay time when the key pressed
                keys.press(Key.alt_l)
                time.sleep(0.1)  # Adjust the two key sequence delay time
                keys.press(Key.tab)
                keys.release(Key.alt_l)
                keys.release(Key.tab)
            else:
                print('Received event {}'.format(event))
                # with open("KeyBoardLog.txt", 'w', encoding='utf-8') as log:
                #     count = log.write(str(event))
                #     print(str(event)+"-Test")
                #
                time_b = time.localtime(time.time())  # Get the system time
                datatime_b = time.strftime('%Y-%m-%d,%H:%M:%S', time_b)  # Reform the time struction
                # log = open("KeyBoardLog.txt",'w')
                # log.close()
                log = open("KeyBoardLog.txt", 'a', encoding='utf-8')  # Open/New and Write in the file
                # log = open("F:\KeyBoardLog.txt",'a',encoding='utf-8') # Set the file path by user
                time.sleep(0)  # Set the writing delay time
                log.write(str(datatime_b) + '-' + str(event) + '\n')  # File's form`
                log.close()  # File close
        btn.clicked.connect(PyQt5.QtCore.QCoreApplication.instance().quit)

app = QtWidgets.QApplication(sys.argv)
# Create q widget lit basic class
windows = QtWidgets.QWidget()
# Set widget kit size(w,h)
windows.resize(320,220)
# Set widget kit position (x,y)
windows.move(50,50)
"""
qr = windows.frameGeometry()
cp = QtWidgets.QDesktopWidget().availableGeometry().center()
qr.moveCenter(cp)
windows.move(qr.topLeft())
"""
#等同于 w.resize(500,500)和w.move(100,100)两句结合,(x,y,w,h)
#windows.setGeometry(100,100,500,500)
#给widget组件设置标题
windows.setWindowTitle('KeyBoard Switch')
#给widget组件设置图标
#windows.setWindowIcon(QtGui.QIcon('2.png'))
#设置提示语的字体和大小
QtWidgets.QToolTip.setFont(QtGui.QFont('SansSerif', 10))
# Set the widget hint info
windows.setToolTip('Windows info hint')

# Set the name of buttom exit
btn = QtWidgets.QPushButton('Exit',windows)
# Set button position (x,y,w,h)
btn.setGeometry(200,130,70,50)
btn.setToolTip('Pressed to exit')
btn.setStyleSheet("background-color: rgb(164, 185, 255);"
 "border-color: rgb(170, 150, 163);"
 "font: 75 12pt \"Arial Narrow\";"
 "color: rgb(126, 255, 46);")
btn.clicked.connect(PyQt5.QtCore.QCoreApplication.instance().quit)

# Set the start buttom
btn1 = QtWidgets.QPushButton('Start',windows)
btn1.setGeometry(50,130,70,50)
btn1.setToolTip('Pressed to start KeyboardSwitch')
btn1.setStyleSheet("background-color: rgb(164, 185, 255);"
 "border-color: rgb(170, 150, 163);"
 "font: 75 12pt \"Arial Narrow\";"
 "color: rgb(126, 255, 46);")
btn1.clicked.connect(Keyboard_Switch)

# Set the Instruction with Button
Text = QtWidgets.QPushButton('1=ALT+Q'+':::::2=ALT+W'+'\n'+'2=ALT+A:::::3=ALT+D:::::4=CTRL+TAB'+'\n'+'V= Windows',windows)
Text.setGeometry(0,0,320,120)
Text.setToolTip('KeySwitch Info')
Text.setStyleSheet("background-color: rgb(240, 240, 240);"
 "border-color: rgb(170, 150, 163);"
 "font: 75 12pt \"Arial Narrow\";"
 "color: rgb(0, 0, 0);")

# Start the Windows always True
windows.show()
sys.exit(app.exec_())

# How to package with pyinstaller
# CMD Input
# pyinstaller -F -w --icon=photo.ico test.py
# -w Delete the cmd
# --icon add icon; ico must in the same path with programmer
# The Exe file will in dist file