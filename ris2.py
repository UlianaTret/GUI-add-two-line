# -*- coding: cp1251 -*-
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox

def sms():
	message = QMessageBox()
	message.setFixedHeight(100)
	message.setFixedWidth(200)
	message.setWindowTitle("Справка")
	message.setInformativeText('1. Дано натуральное число:\n- найти сумму цифр этого числа;\n- определить, верно ли, что число начинается и заканчивается одной и той же цифрой.\n2. Найти все трехзначные числа, такие, сумма цифр которых равна А, а само число делится на В (А и В вводятся с клавиатуры).')
	message.exec_()

def summa_cyfr(num):
	i = 0
	sum_of_num = 0
	while i < len(num):
		sum_of_num += int(num[i])
		i +=1
	return sum_of_num

def found_nums(a, b):
	res_text = ''
	a = int(a)
	b = int(b)
	k = 100
	while k < 1000:
		del_kb = k%b
		list_k = list(str(k))
		sum_of_k = summa_cyfr(list_k)
		if sum_of_k == a and del_kb == 0:
			res_text += (str(k) + ', ')
		k +=1
	if res_text != '':
		res_text = 'Все трехзначные числа, такие, что сумма цифр которых равна А, а самочисло делится на В: ' + res_text[:(len(list(res_text))-2)] + '.'
	else:
		res_text = 'Нет трехзначных чисел, таких, что сумма цифр которых равна А, а само число делиться на В.'
	return res_text

def analysis_num(num):
	res_text = ''
	num = list(num)
	sum_of_num = summa_cyfr(num)
	res_text += ('Сумма цифр данного числа равна = ' + str(sum_of_num) + '.\n')
	k = len(num) - 1
	if num[0] != num[k]:
		res_text += 'Неверно, что данное число начинается и заканчивается одной и той же цифрой.'
	else:
		res_text += 'Верно, что данное число начинается и заканчивается одной и той же цифрой.'
	return res_text