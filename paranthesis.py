#!/usr/bin/env python3

import sys
import exploit_patterns
import pyfiglet
import clipboard as clip
from restricted_input import r_input
from exploit_patterns import create,offset

def intro():
	banner = pyfiglet.figlet_format("Paranthesis", font = "slant")
	print(banner)
	print("Developed By AthisOffsec\n")

def pattern_create():
	create = int(input("Enter the length of pattern you needed : "))
	pattern = exploit_patterns.create(create)
	print("\n")
	print(pattern)
	print("\n")
	copy = input("Do You Want to Copy the pattern in your clipboard Y/N: ")
	if copy == 'Y' or 'y' :
		clip.copy(pattern)
	elif copy == 'N' or 'n':
		print("\n")
		print("Sure !")
	else:
		print("Please only answer the question with the Specified Letters")

def pattern_offset():
	offset = input("Enter the address or string you want to find: ")
	r = exploit_patterns.offset(offset)
	print("The offset is : ",r)

PATTERN = {
	1: pattern_create,
	2: pattern_offset
}

def Menu():
	while True:
		Option = 1
		print("\n")
		print("1: Pattern Create")
		print("2: Pattern Offset")
		print("3: Exit")
		print("\n")
		Option = int(input("$ "))
		print("\n")
		if (Option < 3) and (Option >= 1):
			PATTERN[Option]()
		elif Option == 3:
			print("See You Buddy\n")
			sys.exit()
		else:
			print("Please Select an Proper Option")

if __name__ == "__main__":
	try:
		intro()
		Menu()
	except KeyboardInterrupt:
		print("Thanks For Your Time Buddy :)")
