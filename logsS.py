from PyQt5 import QtWidgets, uic
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QStatusBar, QFileDialog, QDialog, QMessageBox
from PyQt5.QtCore import QDateTime, QTimer

def logs_special(result_sum_ascii):
	i = 0
	log = ''
	while i < len(result_sum_ascii):
		if result_sum_ascii[i] == 0:
			datetime = QDateTime.currentDateTime()
			log = log + str(datetime.toString('dd.MM.yyyy, hh:mm:ss.zzz ')) + 'special symbol No0 - NOP\n'
			
		if result_sum_ascii[i] == 1:
			datetime = QDateTime.currentDateTime()
			log = log + str(datetime.toString('dd.MM.yyyy, hh:mm:ss.zzz ')) + 'special symbol No1 - SOP\n'
			
		if result_sum_ascii[i] == 2:
			datetime = QDateTime.currentDateTime()
			log = log + str(datetime.toString('dd.MM.yyyy, hh:mm:ss.zzz ')) + 'special symbol No2 - STX\n'
			
		if result_sum_ascii[i] == 3:
			datetime = QDateTime.currentDateTime()
			log = log + str(datetime.toString('dd.MM.yyyy, hh:mm:ss.zzz ')) + 'special symbol No3 - ETX\n'
			
		if result_sum_ascii[i] == 4:
			datetime = QDateTime.currentDateTime()
			log = log + str(datetime.toString('dd.MM.yyyy, hh:mm:ss.zzz ')) + 'special symbol No4 - EOT\n'
			
		if result_sum_ascii[i] == 5:
			datetime = QDateTime.currentDateTime()
			log = log + str(datetime.toString('dd.MM.yyyy, hh:mm:ss.zzz ')) + 'special symbol No5 - ENQ\n'
			
		if result_sum_ascii[i] == 6:
			datetime = QDateTime.currentDateTime()
			log = log + str(datetime.toString('dd.MM.yyyy, hh:mm:ss.zzz ')) + 'special symbol No6 - ACK\n'
			
		if result_sum_ascii[i] == 7:
			datetime = QDateTime.currentDateTime()
			log = log + str(datetime.toString('dd.MM.yyyy, hh:mm:ss.zzz ')) + 'special symbol No7 - BEL\n'
			
		if result_sum_ascii[i] == 8:
			datetime = QDateTime.currentDateTime()
			log = log + str(datetime.toString('dd.MM.yyyy, hh:mm:ss.zzz ')) + 'special symbol No8 - BS\n'
			
		if result_sum_ascii[i] == 9:
			datetime = QDateTime.currentDateTime()
			log = log + str(datetime.toString('dd.MM.yyyy, hh:mm:ss.zzz ')) + 'special symbol No9 - TABULATION\n'
			
		if result_sum_ascii[i] == 10:
			datetime = QDateTime.currentDateTime()
			log = log + str(datetime.toString('dd.MM.yyyy, hh:mm:ss.zzz ')) + 'special symbol No10 - LF\n'
			
		if result_sum_ascii[i] == 11:
			datetime = QDateTime.currentDateTime()
			log = log + str(datetime.toString('dd.MM.yyyy, hh:mm:ss.zzz ')) + 'special symbol No11 - VT\n'
			
		if result_sum_ascii[i] == 12:
			datetime = QDateTime.currentDateTime()
			log = log + str(datetime.toString('dd.MM.yyyy, hh:mm:ss.zzz ')) + 'special symbol No12 - FF\n'
			
		if result_sum_ascii[i] == 13:
			datetime = QDateTime.currentDateTime()
			log = log + str(datetime.toString('dd.MM.yyyy, hh:mm:ss.zzz ')) + 'special symbol No13 - CR\n'
		
		if result_sum_ascii[i] == 14:
			datetime = QDateTime.currentDateTime()
			log = log + str(datetime.toString('dd.MM.yyyy, hh:mm:ss.zzz ')) + 'special symbol No14 - SO\n'
		
		if result_sum_ascii[i] == 15:
			datetime = QDateTime.currentDateTime()
			log = log + str(datetime.toString('dd.MM.yyyy, hh:mm:ss.zzz ')) + 'special symbol No15 - SI\n'
		
		if result_sum_ascii[i] == 16:
			datetime = QDateTime.currentDateTime()
			log = log + str(datetime.toString('dd.MM.yyyy, hh:mm:ss.zzz ')) + 'special symbol No16 - DLE\n'
		
		if result_sum_ascii[i] == 17:
			datetime = QDateTime.currentDateTime()
			log = log + str(datetime.toString('dd.MM.yyyy, hh:mm:ss.zzz ')) + 'special symbol No17 - DC1\n'
		
		if result_sum_ascii[i] == 18:
			datetime = QDateTime.currentDateTime()
			log = log + str(datetime.toString('dd.MM.yyyy, hh:mm:ss.zzz ')) + 'special symbol No18 - DC2\n'
		
		if result_sum_ascii[i] == 19:
			datetime = QDateTime.currentDateTime()
			log = log + str(datetime.toString('dd.MM.yyyy, hh:mm:ss.zzz ')) + 'special symbol No19 - DC3\n'
		
		if result_sum_ascii[i] == 20:
			datetime = QDateTime.currentDateTime()
			log = log + str(datetime.toString('dd.MM.yyyy, hh:mm:ss.zzz ')) + 'special symbol No20 - DC4\n'
		
		if result_sum_ascii[i] == 21:
			datetime = QDateTime.currentDateTime()
			log = log + str(datetime.toString('dd.MM.yyyy, hh:mm:ss.zzz ')) + 'special symbol No21 - NAK\n'
		
		if result_sum_ascii[i] == 22:
			datetime = QDateTime.currentDateTime()
			log = log + str(datetime.toString('dd.MM.yyyy, hh:mm:ss.zzz ')) + 'special symbol No22 - SYN\n'
		
		if result_sum_ascii[i] == 23:
			datetime = QDateTime.currentDateTime()
			log = log + str(datetime.toString('dd.MM.yyyy, hh:mm:ss.zzz ')) + 'special symbol No23 - ETB\n'
		
		if result_sum_ascii[i] == 24:
			datetime = QDateTime.currentDateTime()
			log = log + str(datetime.toString('dd.MM.yyyy, hh:mm:ss.zzz ')) + 'special symbol No24 - CAN\n'
		
		if result_sum_ascii[i] == 25:
			datetime = QDateTime.currentDateTime()
			log = log + str(datetime.toString('dd.MM.yyyy, hh:mm:ss.zzz ')) + 'special symbol No25 - EM\n'
		
		if result_sum_ascii[i] == 26:
			datetime = QDateTime.currentDateTime()
			log = log + str(datetime.toString('dd.MM.yyyy, hh:mm:ss.zzz ')) + 'special symbol No26 - SUB\n'
		
		if result_sum_ascii[i] == 27:
			datetime = QDateTime.currentDateTime()
			log = log + str(datetime.toString('dd.MM.yyyy, hh:mm:ss.zzz ')) + 'special symbol No27 - ESC\n'
		
		if result_sum_ascii[i] == 28:
			datetime = QDateTime.currentDateTime()
			log = log + str(datetime.toString('dd.MM.yyyy, hh:mm:ss.zzz ')) + 'special symbol No28 - FS\n'
		
		if result_sum_ascii[i] == 29:
			datetime = QDateTime.currentDateTime()
			log = log + str(datetime.toString('dd.MM.yyyy, hh:mm:ss.zzz ')) + 'special symbol No29 - GS\n'
		
		if result_sum_ascii[i] == 30:
			datetime = QDateTime.currentDateTime()
			log = log + str(datetime.toString('dd.MM.yyyy, hh:mm:ss.zzz ')) + 'special symbol No30 - RS\n'
		
		if result_sum_ascii[i] == 31:
			datetime = QDateTime.currentDateTime()
			log = log + str(datetime.toString('dd.MM.yyyy, hh:mm:ss.zzz ')) + 'special symbol No31 - US\n'
		
		if result_sum_ascii[i] == 32:
			datetime = QDateTime.currentDateTime()
			log = log + str(datetime.toString('dd.MM.yyyy, hh:mm:ss.zzz ')) + 'special symbol No32 - SP (space)\n'
		
		if result_sum_ascii[i] == 127:
			datetime = QDateTime.currentDateTime()
			log = log + str(datetime.toString('dd.MM.yyyy, hh:mm:ss.zzz ')) + 'special symbol No127\n'
		
		i +=1
	return log
