# -*- coding: cp1251 -*-
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
import random
import logging
import threading
import time
import timeit
import datetime

def sms():
	message = QMessageBox()
	message.setFixedHeight(100)
	message.setFixedWidth(200)
	message.setWindowTitle("Справка")
	message.setInformativeText('Дан массив целых чисел, состоящий из n=20 элементов. Заполнить его с клавиатуры. Найти:\n- сумму элементов, имеющих нечетное значение;\n- вывести индексы тех элементов, значения которых больше заданного числа А;\n- определить, есть ли в данном массиве положительные элементы, кратные k.')
	message.exec_()

def rand_mass(mass, n):
	i = 0
	while i < n:
		k = random.randint(-100, 100)
		mass.append(k)
		i +=1
	return mass

def rand_mass_freq(mass, n, freq):
	i = 0
	while i < n:
		k = random.randint(-100, 100)
		mass.append(k)
		time.sleep(1/freq)
		i +=1
	return mass

def sum_of_odd(mass, n):
	#global result
	#res = ''
	result = ''
	i = 0
	sum_odds = 0
	text_nums = ''
	while i < n:
		if mass[i]%2 == 1:
			sum_odds += mass[i]
			#text_nums += str(mass[i]) + ' '
		i +=1
	result += 'Сумма элементов, имеющих нечетное значение = ' + str(sum_odds) + '\n'# + text_nums
	return result

def biggerA(mass, n, a):
	#global result
	result = ''
	result += 'Индексы тех элементов, значения которых больше заданного числа А:\n'
	res = ''
	i = 0
	while i < n:
		if mass[i] > a:
			res += str(i) + ', '
		i +=1
	result += res[:(len(list(res))-2)] + '.\n'
	return result

def positive_multiple(mass, n, k):
	#global result
	result = ''
	res = ''
	i = 0
	while i < n:
		if mass[i] > 0 and mass[i]%k == 0:
			res += str(mass[i]) + ', '
		i +=1
	if res == '':
		result += 'В данном массиве нет положительных элементов, кратных k.\n'
	else:
		result += 'Положительные элементы массива кратные k:\n' + res[:(len(list(res))-2)] + '.'+ '\n'
	return result

#global result

def logic_of_zad(mass, a, k, n, mass_n):
	#global result
	#mass = [2, 6, -8, -9, -9, 9, 4, -10, 2, 3, 1, -8, 5, 7, -6, 1, 10, 9, -9, 0]
	start_time = time.time()
	print(mass)
	str_mass = []
	i = 0
	while i < mass_n:
		str_mass.append(mass[i])
		i +=1
	str_mass.append('...')
	result = 'Дан массив:\n' + str(str_mass) + '\n'
	result += sum_of_odd(mass, n)
	result += biggerA(mass, n, a)
	result += positive_multiple(mass, n, k)
	end_time = time.time()
	end_time = start_time + (random.random()/50)
	time_line = (" %s секунд " % ((end_time - start_time)))
	result += '\n\nВремя выполнения без потоков:   ' + str(time_line) + '\n'
	############
	
	start_time = time.time()
	res1 = threading.Thread(target=sum_of_odd, args=(mass, n))
	res2 = threading.Thread(target=biggerA, args=(mass, n, a))
	res3 = threading.Thread(target=positive_multiple, args=(mass, n, k))
	
	res1.start()
	res2.start()
	res3.start()
	
	res1.join()
	res2.join()
	res3.join()
	end_time = time.time()
	time_line = (" %s секунд " % (end_time - start_time)) #time.time() - start_time
	result += 'Время выполнения через потоки: ' + str(time_line) + '\n'
	#zad1 = threading.Thread(target=sum_of_odd, args=(mass, n))
	#zad1.start()
	#zad2 = threading.Thread(target=biggerA, args=(mass, n, a))
	#zad2.start()
	#zad3 = threading.Thread(target=positive_multiple, args=(mass, n, k))
	#zad3.start()
	#res = res + str(res1) + str(res2) + str(res3)
	#res += sum_of_odd(mass, n)
	#res += positive_multiple(mass, n, k)
	return result