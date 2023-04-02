#!/bin/python3

import sys
import getopt
import string

def r(lines):
	for line in lines:
		l = line[::-1]
		print(l)
		
def w(lines):
	for line in lines:
		l = line.split()[::-1]
		print(' '.join(l))
		
def R(lines):
	for line in lines:
		l = line.split()
		new_line = []
		for word in l:
			w = word[::-1]
			new_line.append(w)
		print(' '.join(new_line))

def u(lines):
	for line in lines:
		print(line.upper())

def U(lines):
	for line in lines:
		l = line.split()
		new_line = []
		for word in l:
			 w = word.capitalize()
			 new_line.append(w)
		print(' '.join(new_line))

def H(lines):
	for line in lines:
		l = line.split()
		new_line = []
		for word in l:
			length = len(word)
			w = ''
			if (length%2) == 0:
				length = length/2
			else:
				length = (len(word)+1)/2
				
			for i in range(len(word)):
				if i < length:
					w += word[i].upper()
				else:
					w += word[i]
			new_line.append(w)
			
		print(' '.join(new_line))


def l(lines):
	for line in lines:
		print(line.lower())

def a(lines):
	for line in lines:
		l = line.split()
		l.sort(key=str.casefold)
		print(' '.join(l))

def d(lines, a):
	for line in lines:
		for ch in a:
			l = line.replace(ch, '')
		print(l)

def c(lines):
	for line in lines:
		print(len(line.split()), 'w, ', len(line), 'c: ', line)


argv = sys.argv[1:]
	
try:
	opts, args = getopt.getopt(argv, "rwRuUHlad:c")
except getopt.getoptError as err:
	print(err)
	opts = []
	
f = open("/home/yana/sjp/lab8/tekst.txt", "r")
lines = f.readlines()

for opt, arg in opts:
			
	if opt in ['-r']:
		r(lines) 
				
	elif opt in ['-w']:
		w(lines)
				
	elif opt in ['-R']:
		R(lines)
			
	elif opt in ['-u']:
		u(lines)
				
	elif opt in ['-U']:
		U(lines)
			
	elif opt in ['-H']:
		H(lines)
			
	elif opt in ['-l']:
		l(lines)
				
	elif opt in ['-a']:
		a(lines)
				
	elif opt in ['-d']:
		a = arg
		d(lines, a)
				
	elif opt in ['-c']:
		c(lines)
