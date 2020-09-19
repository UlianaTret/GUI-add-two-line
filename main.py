# -*- coding: cp1251 -*-
from PyQt5 import QtWidgets, uic
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QStatusBar, QFileDialog, QDialog, QMessageBox
from PyQt5.QtCore import QDateTime, QTimer
import logsS

def iam():
	message = QMessageBox()
	message.setFixedHeight(100)
	message.setFixedWidth(200)
	message.setWindowTitle("Об авторе")
	message.setText("Третьякова Юлиана, группа 3745")
	message.setInformativeText('почта: user747483@mail.ru\nтелефон: +7 900 654 6559')
	message.exec_()

def unicod(name, fam):
	i = 0
	name  = list(name)
	fam = list(fam)
	while i < len(name):
		name[i] = ord(name[i])
		i +=1
	i = 0
	while i < len(fam):
		fam[i] = ord(fam[i])
		i +=1
	return name, fam

def getting_tail(mass, n):
	i = 0
	k = len(list(mass)) - n
	mass = mass[k:]
	tail = '' 
	while i < len(list(mass)):
		tail = tail + str(chr(mass[i]))
		i +=1
	return tail

def add00(mass, n):
	i = 0
	while i < n:
		mass.append(0)
		i +=1
	return mass

def work_ris1(name, fam, tail_str, result_sum, result_sum_ascii):
	if len(name) != len(fam):
		n = abs(len(name) - len(fam))
		if len(name) < len(fam):
			tail_str = getting_tail(fam, n)
			name = add00(name, n)
		else:
			tail_str = getting_tail(name, n)
			fam = add00(fam, n)
	else:
		tail_str = ''
	i = 0
	result_sum_ascii = []
	while i < len(name):
		cakesumm = int(name[i])^int(fam[i])
		result_sum_ascii.append(cakesumm)
		cakesumm = chr(cakesumm)
		result_sum = result_sum + cakesumm
		i +=1
	return name, fam, tail_str, result_sum, result_sum_ascii

def push_transform():
	tail_str = ''
	result_sum = ''
	result_sum_ascii = []
	name = win_ris1.lineEdit_name.text()
	fam = win_ris1.lineEdit_fam.text()
	checkk = logs(name, fam)
	if checkk == 0: # have errors
		win_ris1.lineEdit_name.setText('')
		win_ris1.lineEdit_fam.setText('')
		#tail_str = ''
		#result_sum = ''
		win_ris1.name_asciicode.setText('')
		win_ris1.fam_asciicode.setText('')
		win_ris1.tail_line.setText('')
		win_ris1.line_result_ascii.setText('')
		win_ris1.line_result.setText('')
		return
	else:
		datetime = QDateTime.currentDateTime()
		log = win.textEdit.toPlainText() + str(datetime.toString('dd.MM.yyyy, hh:mm:ss.zzz ')) + 'All data entered correctly\n'
		win.textEdit.setText(log)
		name, fam = unicod(name, fam)
		name, fam, tail_str, result_sum, result_sum_ascii = work_ris1(name, fam, tail_str, result_sum, result_sum_ascii)
		message = symbol_special(result_sum_ascii)
		win_ris1.name_asciicode.setText(str(name))
		win_ris1.fam_asciicode.setText(str(fam))
		win_ris1.tail_line.setText(str(tail_str))
		win_ris1.line_result_ascii.setText(str(result_sum_ascii))
		win_ris1.line_result.setText(str(result_sum))
		datetime = QDateTime.currentDateTime()
		log = win.textEdit.toPlainText() + str(datetime.toString('dd.MM.yyyy, hh:mm:ss.zzz ')) + 'Transform is end\n'
		win.textEdit.setText(log)
	

def rislr1():
	win_ris1.lineEdit_name.setText('')
	win_ris1.lineEdit_fam.setText('')
	win_ris1.name_asciicode.setText('')
	win_ris1.fam_asciicode.setText('')
	win_ris1.tail_line.setText('')
	win_ris1.line_result_ascii.setText('')
	win_ris1.line_result.setText('')
	win_ris1.show()
	win_ris1.btn_transform.clicked.connect(push_transform)
	
appris1 = QtWidgets.QApplication([])
win_ris1 = uic.loadUi("ris_lr1.ui")
app = QtWidgets.QApplication([])
win = uic.loadUi("mydesign.ui")
win.avtor.triggered.connect(iam)

def worlds127(name, fam):
	checkk = True
	name = list(name)
	fam = list(fam)
	name, fam = unicod(name, fam)
	i = 0
	while i < len(name):
		if name[i]> 192 or (name[i]>65 and name[i]<90) or (name[i]>97 and name[i]<122) or name[i] ==32:
			print('')
			#print (name[i], "ok")#checkk = false #it ok
		else:
			checkk = False #not ok
			#print (name[i], "not")
		i +=1
	#print('end name')
	i = 0
	while i < len(fam):
		if fam[i]> 192 or (fam[i]>65 and fam[i]<90) or (fam[i]>97 and fam[i]<122) or fam[i] == 32:
			print('')
			#print (fam[i], "ok")#checkk = false #it ok
		else:
			checkk = False #not ok
			#print (fam[i], "not")
		i +=1
	#print('end')
	return checkk

############## WRITE LOGS ##############
def logs(name, fam):
    if len(name) == 0 or len(fam) == 0:  # Data not found
        datetime = QDateTime.currentDateTime()
        log = win.textEdit.toPlainText() + str(datetime.toString('dd.MM.yyyy, hh:mm:ss.zzz ')) + 'User do not write name or familia\n'
        win.textEdit.setText(log)
        return 0
    all_ok = worlds127(name, fam)
    if all_ok != True:
    #if name.isalpha() != True or fam.isalpha() != True:  # Data not right
    #if name.isspace() != True or fam.isspace() != True:  # Data not right #isspace
        datetime = QDateTime.currentDateTime()
        log = win.textEdit.toPlainText() + str(datetime.toString('dd.MM.yyyy, hh:mm:ss.zzz ')) + 'There are not only words in name or familia\n'
        win.textEdit.setText(log)
        return 0
    return 1

def symbol_special(result_sum_ascii):
	mess = logsS.logs_special(result_sum_ascii)
	log = win.textEdit.toPlainText() + mess
	win.textEdit.setText(log)
	return mess

############## STATUS BAR ##############
datetime = QDateTime.currentDateTime()
 
#show status bar
statusbar = QStatusBar()
win.statusbar.setGeometry(300, 300, 250, 150)
win.statusbar.setWindowTitle('Statusbar')
win.statusbar.show()
win.statusbar.showMessage(datetime.toString('dd.MM.yyyy, hh:mm:ss.zzz'))
 
#timer on status bar
def time():
    datetime = QDateTime.currentDateTime()
    win.statusbar.showMessage(datetime.toString('dd.MM.yyyy, hh:mm:ss.zzz'))
    timer.start()
 
#timer out
timer = QTimer()
timer.setInterval(10)
timer.start()
timer.timeout.connect(time)
 
#open file for save logs
def openLog():
    try:
        fname = QFileDialog.getOpenFileName(filter='*.txt')[0]
        f = open(fname, 'r', encoding="utf8")
        data = f.read()
        win.textEdit.setText(data)
    except:
        return
win.openFile.triggered.connect(openLog)
 
#write logs in file
def saveLog():
    try:
        fileName, _ = QFileDialog.getSaveFileName(filter='*.txt')
        writeFile = open(fileName, 'w', encoding='utf8')
        writeFile.write(win.textEdit.toPlainText())
        writeFile.close()
    except:
        return
win.saveFile.triggered.connect(saveLog)
 
#creat new log.txt
def createFile():
    win.textEdit.clear()
win.newFile.triggered.connect(createFile)

win.show()

win.ris1.triggered.connect(rislr1)

sys.exit(app.exec())