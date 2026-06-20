import os
import time

def middletriangle(totallines,timer):
	print("TRIANGLE AT THE CENTER")
	totallines=int(q)
	starcount=1
	space=totallines-1
	for i in range(totallines):
		temp=""
		for k in range(space):
			temp+=" "
		for j in range(starcount):
			temp+="*"
		print(temp)
		time.sleep(timer)
		space-=1
		starcount+=2

def lefttorightstraight(totallines,timer):
	print("STRAIGHT LEFT TO RIGHT")
	stars=1
	for i in range(totallines):
		print("*"*stars)
		time.sleep(timer)
		stars+=3

def righttoleftstraight(totallines,timer):
	print("STRAIGHT RIGHT TO LEFT")
	stars=1
	spaces=1
	for i in range(totallines-1):
		stars+=2
	for i in range(totallines):
		if spaces==1:
			print("*"*stars)
			spaces+=1
		else:
			print(" "*spaces+"*"*stars)
			spaces+=2
		time.sleep(timer)
		stars-=2

def reverselefttorightstraight(totallines,timer):
	print("REVERSE TRIANGLE FROM LEFT TO RIGHT")
	totallines=int(q)
	stars=1
	for i in range(totallines-1):
		stars+=2
	for i in range(totallines):
		print("*"*stars)
		time.sleep(timer)
		stars-=2

def reversetrianglerighttoleft(totallines,timer):
	print("REVERSE TRIANGLE FROM RIGHT TO LEFT")
	totallines=int(q)
	stars=1
	spaces=1
	for i in range(totallines-1):
		stars+=2
	for i in range(totallines):
		if spaces!=1:
			print(" "*spaces + "*"*stars)
			spaces+=2
		else:
			print("*"*stars)
			spaces+=1
		time.sleep(timer)
		stars-=2

def topdowntriangle(totallines,timer):
	print("TRIANGLE FROM TOP TO DOWN")
	totallines=int(q)
	stars=1
	spaces=0
	for i in range(totallines-1):
		stars+=2
	for i in range(totallines):
		print(" "*spaces + "*"*stars)
		time.sleep(timer)
		stars-=2
		spaces+=1

def main():
	pause=input("do you want to have breaks in printing the lines or not(Y/N):")
	if pause=="N" or pause =="n":
		timer=0
	else:
		timer=1
	totallines=int(q)

	middletriangle(totallines,timer)
	print()
	lefttorightstraight(totallines,timer)
	print()
	righttoleftstraight(totallines,timer)
	print()
	reverselefttorightstraight(totallines,timer)
	print()
	reversetrianglerighttoleft(totallines,timer)
	print()
	topdowntriangle(totallines,timer)
	
os.system('cls' if os.name == 'nt' else 'clear')
q=input("enter number of line for which the pattern must be made:")
try:
	q=int(q)
	main()
except:
	print("number na ennanu theriyatha da? mutaal")