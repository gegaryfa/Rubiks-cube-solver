#!/usr/bin/env python
"""
Rubiks Cube Solver

Enter the Cube colours in the correct orientation:

Colour in Front | Colour on Top

1. Yellow | Blue

2. White | Green

3. Blue | White

4. Red | White

5. Green | White

6. Orange | White

For extra info, contact me at: garyfallou.george@gmail.com
"""



from Tkinter import *
import time
import sys


yellow_face = ['y', 'y', 'y',
			   'y', 'y', 'y',
			   'y', 'y', 'y']

white_face = ['w', 'w', 'w',
			  'w', 'w', 'w',
			  'w', 'w', 'w']

blue_face = ['b', 'b', 'b',
			 'b', 'b', 'b',
			 'b', 'b', 'b']

red_face = ['r', 'r', 'r',
			'r', 'r', 'r',
			'r', 'r', 'r']

green_face = ['g', 'g', 'g',
			  'g', 'g', 'g',
			  'g', 'g', 'g']

orange_face = ['o', 'o', 'o',
			   'o', 'o', 'o',
			   'o', 'o', 'o']


raw_cube_string = ""

def generate_raw_cube():
	raw_cube_string = ""
	for color in yellow_face:
		raw_cube_string = raw_cube_string + color
		#catenate 'raw_cube_string' with yellow_face[0], [1], on and on.....

	for color in white_face:
		raw_cube_string = raw_cube_string + color
		#catenate 'raw_cube_string' with yellow_face[0], [1], on and on.....
	
	for color in red_face:
		raw_cube_string = raw_cube_string + color
		#catenate 'raw_cube_string' with yellow_face[0], [1], on and on.....
	
	for color in blue_face:
		raw_cube_string = raw_cube_string + color
		#catenate 'raw_cube_string' with yellow_face[0], [1], on and on.....

	for color in green_face:
		raw_cube_string = raw_cube_string + color
		#catenate 'raw_cube_string' with yellow_face[0], [1], on and on.....

	for color in orange_face:
		raw_cube_string = raw_cube_string + color
		#catenate 'raw_cube_string' with yellow_face[0], [1], on and on.....
	return raw_cube_string

def send_raw_cube():
	# send the raw_cube_string<
	print "color sent: ", raw_cube_string


###### Gui functions ########
def enter_yellow_face():
	top,mid,btm=[0,0,0],[0,0,0],[0,0,0]
	bord = [top,mid,btm]
	counter = [0, 0, 0,
			   0, 0, 0,
			   0, 0, 0]

	def change_color(x, b=bord):
		# seems like x is the square number out of the 9 squares
		#global counter
		r=x/3
		c=x%3
		if b[r][c] == 0:
			b[r][c]= 5
			bb[x].ss.configure(bg='white', activebackground='white')
			counter[x] = 0
			yellow_face[x] = 'w'

		elif counter[x] == 0:
			bb[x].ss.configure(bg='blue', activebackground='blue')
			counter[x] = 1
			yellow_face[x] = 'b'

		elif counter[x] == 1:
			bb[x].ss.configure(bg='red', activebackground='red')
			counter[x] = 2
			yellow_face[x] = 'r'

			### keep following the cycle of white-yellow-red...
		elif counter[x] == 2:
			bb[x].ss.configure(bg='green', activebackground='green')
			counter[x] = 3
			yellow_face[x] = 'g'

		elif counter[x] == 3:
			bb[x].ss.configure(bg='orange', activebackground='orange')
			counter[x] = 4
			yellow_face[x] = 'o'

		elif counter[x] == 4:
			bb[x].ss.configure(bg='yellow', activebackground='yellow')
			counter[x] = 5
			yellow_face[x] = 'y'

		elif counter[x] == 5:
			bb[x].ss.configure(bg='white', activebackground='white')
			counter[x] = 0
			yellow_face[x] = 'w'

	root = Tk()
	root.title('Enter Yellow Face | Blue on Top')

	class Knop():
		"""This is the docstring of the class"""

		def __init__(self, i, master=None):
			self.nummer = i
			self.row = i/3
			self.col = i%3
			def human_move():
				change_color(self.nummer)
			self.ss = Button(root, command=human_move, bg='yellow', activebackground='yellow', width=10, height=5)
			self.ss.grid(row=self.row, column=self.col) 
			
			next_face = Button(root, text="Next Face",  command=root.destroy)
			next_face.grid(row=4, column=1)  

	bb = range(9)
	for i in range(9):
		bb[i]= Knop(i, master=root)

	mainloop()

def enter_white_face():
	top,mid,btm=[0,0,0],[0,0,0],[0,0,0]
	bord = [top,mid,btm]
	counter = [0, 0, 0,
			   0, 0, 0,
			   0, 0, 0]

	def change_color(x, b=bord):
		# seems like x is the square number out of the 9 squares
		r=x/3
		c=x%3
		if b[r][c] == 0:
			b[r][c]= 5
			bb[x].ss.configure(bg='blue', activebackground='blue')
			counter[x] = 0
			white_face[x] = 'b'

		elif counter[x] == 0:
			bb[x].ss.configure(bg='red', activebackground='red')
			counter[x] = 1
			white_face[x] = 'r'

		elif counter[x] == 1:
			bb[x].ss.configure(bg='green', activebackground='green')
			counter[x] = 2
			white_face[x] = 'g'

			### keep following the cycle of white-yellow-red...
		elif counter[x] == 2:
			bb[x].ss.configure(bg='orange', activebackground='orange')
			counter[x] = 3
			white_face[x] = 'o'

		elif counter[x] == 3:
			bb[x].ss.configure(bg='yellow', activebackground='yellow')
			counter[x] = 4
			white_face[x] = 'y'

		elif counter[x] == 4:
			bb[x].ss.configure(bg='white', activebackground='white')
			counter[x] = 5
			white_face[x] = 'w'

		elif counter[x] == 5:
			bb[x].ss.configure(bg='blue', activebackground='blue')
			counter[x] = 0
			white_face[x] = 'b'

	root = Tk()
	root.title('Enter White Face | Green on Top')

	class Knop():
		"""This is the docstring of the class"""

		def __init__(self, i, master=None):
			self.nummer = i
			self.row = i/3
			self.col = i%3
			def human_move():
				change_color(self.nummer)
			self.ss = Button(root, command=human_move, bg='white', activebackground='white', width=10, height=5)
			self.ss.grid(row=self.row, column=self.col) 
			
			next_face = Button(root, text="Next Face",  command=root.destroy)
			next_face.grid(row=4, column=1)

	bb = range(9)
	for i in range(9):
		bb[i]= Knop(i, master=root)

	mainloop()

def enter_blue_face():
	top,mid,btm=[0,0,0],[0,0,0],[0,0,0]
	bord = [top,mid,btm]

	counter = [0, 0, 0,
			   0, 0, 0,
			   0, 0, 0]

	def change_color(x, b=bord):
		# seems like x is the square number out of the 9 squares
		r=x/3
		c=x%3
		if b[r][c] == 0:
			b[r][c]= 5
			bb[x].ss.configure(bg='red', activebackground='red')
			counter[x] = 0
			blue_face[x] = 'r'

		elif counter[x] == 0:
			bb[x].ss.configure(bg='green', activebackground='green')
			counter[x] = 1
			blue_face[x] = 'g'

		elif counter[x] == 1:
			bb[x].ss.configure(bg='orange', activebackground='orange')
			counter[x] = 2
			blue_face[x] = 'o'

			### keep following the cycle of white-yellow-red...
		elif counter[x] == 2:
			bb[x].ss.configure(bg='yellow', activebackground='yellow')
			counter[x] = 3
			blue_face[x] = 'y'

		elif counter[x] == 3:
			bb[x].ss.configure(bg='white', activebackground='white')
			counter[x] = 4
			blue_face[x] = 'w'

		elif counter[x] == 4:
			bb[x].ss.configure(bg='blue', activebackground='blue')
			counter[x] = 5
			blue_face[x] = 'b'

		elif counter[x] == 5:
			bb[x].ss.configure(bg='red', activebackground='red')
			counter[x] = 0
			blue_face[x] = 'r'

	root = Tk()
	root.title('Enter Blue Face | White on Top')

	class Knop():
		"""This is the docstring of the class"""

		def __init__(self, i, master=None):
			self.nummer = i
			self.row = i/3
			self.col = i%3
			def human_move():
				change_color(self.nummer)
			self.ss = Button(root, command=human_move, bg='blue', activebackground='blue', width=10, height=5)
			self.ss.grid(row=self.row, column=self.col) 
			
			next_face = Button(root, text="Next Face",  command=root.destroy)
			next_face.grid(row=4, column=1) 

	bb = range(9)
	for i in range(9):
		bb[i]= Knop(i, master=root)

	mainloop()

def enter_red_face():
	top,mid,btm=[0,0,0],[0,0,0],[0,0,0]
	bord = [top,mid,btm]

	counter = [0, 0, 0,
			   0, 0, 0,
			   0, 0, 0]

	def change_color(x, b=bord):
		# seems like x is the square number out of the 9 squares
		r=x/3
		c=x%3
		if b[r][c] == 0:
			b[r][c]= 5
			bb[x].ss.configure(bg='green', activebackground='green')
			counter[x] = 0
			red_face[x] = 'g'

		elif counter[x] == 0:
			bb[x].ss.configure(bg='orange', activebackground='orange')
			counter[x] = 1
			red_face[x] = 'o'

		elif counter[x] == 1:
			bb[x].ss.configure(bg='yellow', activebackground='yellow')
			counter[x] = 2
			red_face[x] = 'y'

			### keep following the cycle of white-yellow-red...
		elif counter[x] == 2:
			bb[x].ss.configure(bg='white', activebackground='white')
			counter[x] = 3
			red_face[x] = 'w'

		elif counter[x] == 3:
			bb[x].ss.configure(bg='blue', activebackground='blue')
			counter[x] = 4
			red_face[x] = 'b'

		elif counter[x] == 4:
			bb[x].ss.configure(bg='red', activebackground='red')
			counter[x] = 5
			red_face[x] = 'r'

		elif counter[x] == 5:
			bb[x].ss.configure(bg='green', activebackground='green')
			counter[x] = 0
			red_face[x] = 'g'

	root = Tk()
	root.title('Enter Red Face | White on Top')

	class Knop():
		"""This is the docstring of the class"""

		def __init__(self, i, master=None):
			self.nummer = i
			self.row = i/3
			self.col = i%3
			def human_move():
				change_color(self.nummer)
			self.ss = Button(root, command=human_move, bg='red', activebackground='red', width=10, height=5)
			self.ss.grid(row=self.row, column=self.col) 
			
			next_face = Button(root, text="Next Face",  command=root.destroy)
			next_face.grid(row=4, column=1) 

	bb = range(9)
	for i in range(9):
		bb[i]= Knop(i, master=root)

	mainloop()

def enter_green_face():
	top,mid,btm=[0,0,0],[0,0,0],[0,0,0]
	bord = [top,mid,btm]

	counter = [0, 0, 0,
			   0, 0, 0,
			   0, 0, 0]

	def change_color(x, b=bord):
		# seems like x is the square number out of the 9 squares
		r=x/3
		c=x%3
		if b[r][c] == 0:
			b[r][c]= 5
			bb[x].ss.configure(bg='orange', activebackground='orange')
			counter[x] = 0
			green_face[x] = 'o'

		elif counter[x] == 0:
			bb[x].ss.configure(bg='yellow', activebackground='yellow')
			counter[x] = 1
			green_face[x] = 'y'

		elif counter[x] == 1:
			bb[x].ss.configure(bg='white', activebackground='white')
			counter[x] = 2
			green_face[x] = 'w'

			### keep following the cycle of white-yellow-red...
		elif counter[x] == 2:
			bb[x].ss.configure(bg='blue', activebackground='blue')
			counter[x] = 3
			green_face[x] = 'b'

		elif counter[x] == 3:
			bb[x].ss.configure(bg='red', activebackground='red')
			counter[x] = 4
			green_face[x] = 'r'

		elif counter[x] == 4:
			bb[x].ss.configure(bg='green', activebackground='green')
			counter[x] = 5
			green_face[x] = 'g'

		elif counter[x] == 5:
			bb[x].ss.configure(bg='orange', activebackground='orange')
			counter[x] = 0
			green_face[x] = 'o'

	root = Tk()
	root.title('Enter Green Face | White on Top')

	class Knop():
		"""This is the docstring of the class"""

		def __init__(self, i, master=None):
			self.nummer = i
			self.row = i/3
			self.col = i%3
			def human_move():
				change_color(self.nummer)
			self.ss = Button(root, command=human_move, bg='green', activebackground='green', width=10, height=5)
			self.ss.grid(row=self.row, column=self.col) 
			
			next_face = Button(root, text="Next Face",  command=root.destroy)
			next_face.grid(row=4, column=1)

	bb = range(9)
	for i in range(9):
		bb[i]= Knop(i, master=root)

	mainloop()

def enter_orange_face():
	top,mid,btm=[0,0,0],[0,0,0],[0,0,0]
	bord = [top,mid,btm]

	counter = [0, 0, 0,
			   0, 0, 0,
			   0, 0, 0]

	def change_color(x, b=bord):
		# seems like x is the square number out of the 9 squares
		r=x/3
		c=x%3
		if b[r][c] == 0:
			b[r][c]= 5
			bb[x].ss.configure(bg='yellow', activebackground='yellow')
			counter[x] = 0
			orange_face[x] = 'y'

		elif counter[x] == 0:
			bb[x].ss.configure(bg='white', activebackground='white')
			counter[x] = 1
			orange_face[x] = 'w'

		elif counter[x] == 1:
			bb[x].ss.configure(bg='blue', activebackground='blue')
			counter[x] = 2
			orange_face[x] = 'b'

			### keep following the cycle of white-yellow-red...
		elif counter[x] == 2:
			bb[x].ss.configure(bg='red', activebackground='red')
			counter[x] = 3
			orange_face[x] = 'r'

		elif counter[x] == 3:
			bb[x].ss.configure(bg='green', activebackground='green')
			counter[x] = 4
			orange_face[x] = 'g'

		elif counter[x] == 4:
			bb[x].ss.configure(bg='orange', activebackground='orange')
			counter[x] = 5
			orange_face[x] = 'o'

		elif counter[x] == 5:
			bb[x].ss.configure(bg='yellow', activebackground='yellow')
			counter[x] = 0
			orange_face[x] = 'y'

	root = Tk()
	root.title('Enter Orange Face | White on Top')

	class Knop():
		"""This is the docstring of the class"""

		def __init__(self, i, master=None):
			self.nummer = i
			self.row = i/3
			self.col = i%3
			def human_move():
				change_color(self.nummer)
			self.ss = Button(root, command=human_move, bg='orange', activebackground='orange', width=10, height=5)
			self.ss.grid(row=self.row, column=self.col) 
			
			next_face = Button(root, text="Send Cube!",  command=root.destroy)
			next_face.grid(row=4, column=1) 

	bb = range(9)
	for i in range(9):
		bb[i]= Knop(i, master=root)

	mainloop()

def print_face(current_face):
	print current_face[0], current_face[1], current_face[2]
	print current_face[3], current_face[4], current_face[5]
	print current_face[6], current_face[7], current_face[8]

def print_cube():
	print "Yellow Face: "
	print_face(yellow_face)

	print "White Face: "
	print_face(white_face)

	print "Blue Face: "
	print_face(blue_face)

	print "Red Face: "
	print_face(red_face)

	print "Green Face: "
	print_face(green_face)

	print "Orange Face: "
	print_face(orange_face)

# Add more checks
def legal_cube_check():
	if yellow_face[4] != 'y' or white_face[4] != 'w' or blue_face[4] != 'b' or red_face[4] != 'r' or green_face[4] != 'g' or orange_face[4] != 'o': 
		print "Incorrect center pieces, Try Again"
		sys.exit()


	# elif [check if there are 9 of each color]

def enter_cube():
	enter_yellow_face()
	enter_white_face()
	enter_blue_face()
	enter_red_face()
	enter_green_face()
	enter_orange_face()





###########/ Cube Move Notation #############/
# They print, simulate and call the physical functions

def left():

	print "L(Y|B), "
	global solution_moves 
	solution_moves.append("L")
	

	# Cube simulation
	r_yellow_face = [0]*10
	r_blue_face   = [0]*10
	r_white_face  = [0]*10
	r_green_face  = [0]*10
	r_red_face    = [0]*10

	for i in range(0, 9):
		r_yellow_face[i] = yellow_face[i]
	
	for i in range(0, 9):
		r_blue_face[i] = blue_face[i]
	
	for i in range(0, 9):
		r_white_face[i] = white_face[i]
	
	for i in range(0, 9):
		r_green_face[i] = green_face[i]
	

	yellow_face[0] = r_blue_face[0]
	yellow_face[3] = r_blue_face[3]
	yellow_face[6] = r_blue_face[6]

	blue_face[0] = r_white_face[0]
	blue_face[3] = r_white_face[3]
	blue_face[6] = r_white_face[6]

	white_face[0] = r_green_face[8]
	white_face[3] = r_green_face[5]
	white_face[6] = r_green_face[2]

	green_face[8] = r_yellow_face[0]
	green_face[5] = r_yellow_face[3]
	green_face[2] = r_yellow_face[6]

	for i in range(0, 9):
		r_red_face[i] = red_face[i]
	

	red_face[0] = r_red_face[6]
	red_face[1] = r_red_face[3]
	red_face[2] = r_red_face[0]
	red_face[3] = r_red_face[7]
	red_face[4] = r_red_face[4]
	red_face[5] = r_red_face[1]
	red_face[6] = r_red_face[8]
	red_face[7] = r_red_face[5]
	red_face[8] = r_red_face[2]

def left_inverted():
	print "L'(Y|B), "
	global solution_moves
	solution_moves.append("Li")
	

	# Cube simulation
	r_yellow_face = [0]*10
	r_blue_face   = [0]*10
	r_white_face  = [0]*10
	r_green_face  = [0]*10
	r_red_face    = [0]*10
	for i in range(0, 9):
		r_yellow_face[i] = yellow_face[i]
	
	for i in range(0, 9):
		r_blue_face[i] = blue_face[i]
	
	for i in range(0, 9):
		r_white_face[i] = white_face[i]
	
	for i in range(0, 9):
		r_green_face[i] = green_face[i]
	

	yellow_face[0] = r_green_face[8]
	yellow_face[3] = r_green_face[5]
	yellow_face[6] = r_green_face[2]

	blue_face[0] = r_yellow_face[0]
	blue_face[3] = r_yellow_face[3]
	blue_face[6] = r_yellow_face[6]

	white_face[0] = r_blue_face[0]
	white_face[3] = r_blue_face[3]
	white_face[6] = r_blue_face[6]

	green_face[8] = r_white_face[0]
	green_face[5] = r_white_face[3]
	green_face[2] = r_white_face[6]

	for i in range(0, 9):
		r_red_face[i] = red_face[i]
	

	red_face[0] = r_red_face[2]
	red_face[1] = r_red_face[5]
	red_face[2] = r_red_face[8]
	red_face[3] = r_red_face[1]
	red_face[4] = r_red_face[4]
	red_face[5] = r_red_face[7]
	red_face[6] = r_red_face[0]
	red_face[7] = r_red_face[3]
	red_face[8] = r_red_face[6]

def right():
	print "R(Y|B), "
	global solution_moves
	solution_moves.append("R")
	
	# Cube simulation
	r_yellow_face = [0]*10
	r_blue_face   = [0]*10
	r_white_face  = [0]*10
	r_green_face  = [0]*10
	r_orange_face = [0]*10

	for i in range(0, 9):
		r_yellow_face[i] = yellow_face[i]
	
	for i in range(0, 9):
		r_blue_face[i] = blue_face[i]
	
	for i in range(0, 9):
		r_white_face[i] = white_face[i]
	
	for i in range(0, 9):
		r_green_face[i] = green_face[i]
	

	yellow_face[2] = r_green_face[6]
	yellow_face[5] = r_green_face[3]
	yellow_face[8] = r_green_face[0]

	blue_face[2] = r_yellow_face[2]
	blue_face[5] = r_yellow_face[5]
	blue_face[8] = r_yellow_face[8]

	white_face[2] = r_blue_face[2]
	white_face[5] = r_blue_face[5]
	white_face[8] = r_blue_face[8]

	green_face[6] = r_white_face[2]
	green_face[3] = r_white_face[5]
	green_face[0] = r_white_face[8]

	for i in range(0, 9):
		r_orange_face[i] = orange_face[i]
	

	orange_face[0] = r_orange_face[6]
	orange_face[1] = r_orange_face[3]
	orange_face[2] = r_orange_face[0]
	orange_face[3] = r_orange_face[7]
	orange_face[4] = r_orange_face[4]
	orange_face[5] = r_orange_face[1]
	orange_face[6] = r_orange_face[8]
	orange_face[7] = r_orange_face[5]
	orange_face[8] = r_orange_face[2]

def right_inverted():
	print "R'(Y|B), "
	global solution_moves
	solution_moves.append("Ri")

	# Cube simulation
	r_yellow_face = [0]*10
	r_blue_face   = [0]*10
	r_white_face  = [0]*10
	r_green_face  = [0]*10
	r_orange_face = [0]*10

	for i in range(0, 9):
		r_yellow_face[i] = yellow_face[i]
	
	for i in range(0, 9):
		r_blue_face[i] = blue_face[i]
	
	for i in range(0, 9):
		r_white_face[i] = white_face[i]
	
	for i in range(0, 9):
		r_green_face[i] = green_face[i]
	

	yellow_face[2] = r_blue_face[2]
	yellow_face[5] = r_blue_face[5]
	yellow_face[8] = r_blue_face[8]

	blue_face[2] = r_white_face[2]
	blue_face[5] = r_white_face[5]
	blue_face[8] = r_white_face[8]

	white_face[2] = r_green_face[6]
	white_face[5] = r_green_face[3]
	white_face[8] = r_green_face[0]

	green_face[6] = r_yellow_face[2]
	green_face[3] = r_yellow_face[5]
	green_face[0] = r_yellow_face[8]

	for i in range(0, 9):
		r_orange_face[i] = orange_face[i]
	

	orange_face[0] = r_orange_face[2]
	orange_face[1] = r_orange_face[5]
	orange_face[2] = r_orange_face[8]
	orange_face[3] = r_orange_face[1]
	orange_face[4] = r_orange_face[4]
	orange_face[5] = r_orange_face[7]
	orange_face[6] = r_orange_face[0]
	orange_face[7] = r_orange_face[3]
	orange_face[8] = r_orange_face[6]

def down():
	print "D(Y|B), "
	global solution_moves
	solution_moves.append("D")


	# Cube simulation
	r_yellow_face = [0]*10
	r_white_face  = [0]*10
	r_orange_face = [0]*10
	r_red_face    = [0]*10
	r_green_face  = [0]*10

	for i in range(0, 9):
		r_yellow_face[i] = yellow_face[i]
	
	for i in range(0, 9):
		r_orange_face[i] = orange_face[i]
	
	for i in range(0, 9):
		r_white_face[i] = white_face[i]
	
	for i in range(0, 9):
		r_red_face[i] = red_face[i]
	

	orange_face[8] = r_yellow_face[6]
	orange_face[5] = r_yellow_face[7]
	orange_face[2] = r_yellow_face[8]

	yellow_face[6] = r_red_face[0]
	yellow_face[7] = r_red_face[3]
	yellow_face[8] = r_red_face[6]

	red_face[0] = r_white_face[2]
	red_face[3] = r_white_face[1]
	red_face[6] = r_white_face[0]

	white_face[0] = r_orange_face[2]
	white_face[1] = r_orange_face[5]
	white_face[2] = r_orange_face[8]

	for i in range(0, 9):
		r_green_face[i] = green_face[i]
	
	# reassign colours on face
	green_face[0] = r_green_face[6]
	green_face[1] = r_green_face[3]
	green_face[2] = r_green_face[0]
	green_face[3] = r_green_face[7]
	green_face[4] = r_green_face[4]
	green_face[5] = r_green_face[1]
	green_face[6] = r_green_face[8]
	green_face[7] = r_green_face[5]
	green_face[8] = r_green_face[2]

def down_inverted():

	print "D'(Y|B), "
	global solution_moves
	solution_moves.append("Di")

	# Cube simulation
	r_yellow_face = [0]*10
	r_white_face  = [0]*10
	r_orange_face = [0]*10
	r_red_face    = [0]*10
	r_green_face  = [0]*10

	for i in range(0, 9):
		r_yellow_face[i] = yellow_face[i]
	
	for i in range(0, 9):
		r_orange_face[i] = orange_face[i]
	
	for i in range(0, 9):
		r_white_face[i] = white_face[i]
	
	for i in range(0, 9):
		r_red_face[i] = red_face[i]
	

	yellow_face[6] = r_orange_face[8]
	yellow_face[7] = r_orange_face[5]
	yellow_face[8] = r_orange_face[2]

	red_face[0] = r_yellow_face[6]
	red_face[3] = r_yellow_face[7]
	red_face[6] = r_yellow_face[8]

	white_face[0] = r_red_face[6]
	white_face[1] = r_red_face[3]
	white_face[2] = r_red_face[0]

	orange_face[2] = r_white_face[0]
	orange_face[5] = r_white_face[1]
	orange_face[8] = r_white_face[2]

	for i in range(0, 9):
		r_green_face[i] = green_face[i]
	

	green_face[0] = r_green_face[2]
	green_face[1] = r_green_face[5]
	green_face[2] = r_green_face[8]
	green_face[3] = r_green_face[1]
	green_face[4] = r_green_face[4]
	green_face[5] = r_green_face[7]
	green_face[6] = r_green_face[0]
	green_face[7] = r_green_face[3]
	green_face[8] = r_green_face[6]

def up():
	print "U(Y|B), "
	global solution_moves
	solution_moves.append("U")
	# Cube simulation
	r_yellow_face = [0]*10
	r_white_face  = [0]*10
	r_orange_face = [0]*10
	r_red_face    = [0]*10
	r_blue_face   = [0]*10

	for i in range(0, 9):
		r_yellow_face[i] = yellow_face[i]
	
	for i in range(0, 9):	
		r_orange_face[i] = orange_face[i]
	
	for i in range(0, 9):
		r_white_face[i] = white_face[i]
	
	for i in range(0, 9):
		r_red_face[i] = red_face[i]
	

	yellow_face[0] = r_orange_face[6]
	yellow_face[1] = r_orange_face[3]
	yellow_face[2] = r_orange_face[0]

	red_face[2] = r_yellow_face[0]
	red_face[5] = r_yellow_face[1]
	red_face[8] = r_yellow_face[2]

	white_face[6] = r_red_face[8]
	white_face[7] = r_red_face[5]
	white_face[8] = r_red_face[2]

	orange_face[0] = r_white_face[6]
	orange_face[3] = r_white_face[7]
	orange_face[6] = r_white_face[8]

	for i in range(0, 9):
		r_blue_face[i] = blue_face[i]
	

	blue_face[0] = r_blue_face[6]
	blue_face[1] = r_blue_face[3]
	blue_face[2] = r_blue_face[0]
	blue_face[3] = r_blue_face[7]
	blue_face[4] = r_blue_face[4]
	blue_face[5] = r_blue_face[1]
	blue_face[6] = r_blue_face[8]
	blue_face[7] = r_blue_face[5]
	blue_face[8] = r_blue_face[2]

def up_inverted():

	print "U'(Y|B), "
	global solution_moves
	solution_moves.append("Ui")

	# Cube simulation
	r_yellow_face = [0]*10
	r_white_face  = [0]*10
	r_orange_face = [0]*10
	r_red_face    = [0]*10
	r_blue_face   = [0]*10

	for i in range(0, 9):	
		r_yellow_face[i] = yellow_face[i]
	
	for i in range(0, 9):
		r_orange_face[i] = orange_face[i]
	
	for i in range(0, 9):	
		r_white_face[i] = white_face[i]
	
	for i in range(0, 9):	
		r_red_face[i] = red_face[i]
	

	orange_face[6] = r_yellow_face[0]
	orange_face[3] = r_yellow_face[1]
	orange_face[0] = r_yellow_face[2]

	yellow_face[0] = r_red_face[2]
	yellow_face[1] = r_red_face[5]
	yellow_face[2] = r_red_face[8]

	red_face[2] = r_white_face[8]
	red_face[5] = r_white_face[7]
	red_face[8] = r_white_face[6]

	white_face[8] = r_orange_face[6]
	white_face[7] = r_orange_face[3]
	white_face[6] = r_orange_face[0]

	for i in range(0, 9):
	
		r_blue_face[i] = blue_face[i]
	

	blue_face[0] = r_blue_face[2]
	blue_face[1] = r_blue_face[5]
	blue_face[2] = r_blue_face[8]
	blue_face[3] = r_blue_face[1]
	blue_face[4] = r_blue_face[4]
	blue_face[5] = r_blue_face[7]
	blue_face[6] = r_blue_face[0]
	blue_face[7] = r_blue_face[3]
	blue_face[8] = r_blue_face[6]

def front():
	print "F(Y|B), "	
	global solution_moves
	solution_moves.append("F")

	# Cube simulation
	r_blue_face	  = [0]*10
	r_orange_face = [0]*10
	r_green_face  = [0]*10
	r_red_face    = [0]*10
	r_yellow_face = [0]*10

	for i in range(0, 9):	
		r_blue_face[i] = blue_face[i]
	
	for i in range(0, 9):
		r_orange_face[i] = orange_face[i]
	
	for i in range(0, 9):	
		r_green_face[i] = green_face[i]
	
	for i in range(0, 9):	
		r_red_face[i] = red_face[i]
	

	blue_face[6] = r_red_face[6]
	blue_face[7] = r_red_face[7]
	blue_face[8] = r_red_face[8]

	red_face[6] = r_green_face[6]
	red_face[7] = r_green_face[7]
	red_face[8] = r_green_face[8]

	green_face[6] = r_orange_face[6]
	green_face[7] = r_orange_face[7]
	green_face[8] = r_orange_face[8]

	orange_face[6] = r_blue_face[6]
	orange_face[7] = r_blue_face[7]
	orange_face[8] = r_blue_face[8]


	for i in range(0, 9):
		r_yellow_face[i] = yellow_face[i]
	

	yellow_face[0] = r_yellow_face[6]
	yellow_face[1] = r_yellow_face[3]
	yellow_face[2] = r_yellow_face[0]
	yellow_face[3] = r_yellow_face[7]
	yellow_face[4] = r_yellow_face[4]
	yellow_face[5] = r_yellow_face[1]
	yellow_face[6] = r_yellow_face[8]
	yellow_face[7] = r_yellow_face[5]
	yellow_face[8] = r_yellow_face[2]

def front_inverted():
	print "F' (Y|B), "
	global solution_moves
	solution_moves.append("Fi")


	# Cube simulation
	r_blue_face   = [0]*10
	r_orange_face = [0]*10
	r_green_face  = [0]*10
	r_red_face    = [0]*10
	r_yellow_face = [0]*10

	for i in range(0, 9):
		r_blue_face[i] = blue_face[i]
	
	for i in range(0, 9):
		r_orange_face[i] = orange_face[i]
	
	for i in range(0, 9):
		r_green_face[i] = green_face[i]
	
	for i in range(0, 9):
		r_red_face[i] = red_face[i]
	

	blue_face[6] = r_orange_face[6]
	blue_face[7] = r_orange_face[7]
	blue_face[8] = r_orange_face[8]

	red_face[6] = r_blue_face[6]
	red_face[7] = r_blue_face[7]
	red_face[8] = r_blue_face[8]

	green_face[6] = r_red_face[6]
	green_face[7] = r_red_face[7]
	green_face[8] = r_red_face[8]

	orange_face[6] = r_green_face[6]
	orange_face[7] = r_green_face[7]
	orange_face[8] = r_green_face[8]

	for i in range(0, 9):
		r_yellow_face[i] = yellow_face[i]
	

	yellow_face[0] = r_yellow_face[2]
	yellow_face[1] = r_yellow_face[5]
	yellow_face[2] = r_yellow_face[8]
	yellow_face[3] = r_yellow_face[1]
	yellow_face[4] = r_yellow_face[4]
	yellow_face[5] = r_yellow_face[7]
	yellow_face[6] = r_yellow_face[0]
	yellow_face[7] = r_yellow_face[3]
	yellow_face[8] = r_yellow_face[6]

def back():
	print "B (Y|B), "
	global solution_moves
	solution_moves.append("B")
	print solution_moves

	# Cube simulation
	r_blue_face   = [0]*10
	r_orange_face = [0]*10
	r_green_face  = [0]*10
	r_red_face    = [0]*10
	r_white_face  = [0]*10

	for i in range(0, 9):
		r_blue_face[i] = blue_face[i]
	
	for i in range(0, 9):	
		r_orange_face[i] = orange_face[i]
	
	for i in range(0, 9):	
		r_green_face[i] = green_face[i]
	
	for i in range(0, 9):	
		r_red_face[i] = red_face[i]
	

	blue_face[0] = r_orange_face[0]
	blue_face[1] = r_orange_face[1]
	blue_face[2] = r_orange_face[2]

	red_face[0] = r_blue_face[0]
	red_face[1] = r_blue_face[1]
	red_face[2] = r_blue_face[2]

	green_face[0] = r_red_face[0]
	green_face[1] = r_red_face[1]
	green_face[2] = r_red_face[2]

	orange_face[0] = r_green_face[0]
	orange_face[1] = r_green_face[1]
	orange_face[2] = r_green_face[2]

	for i in range(0, 9):
		r_white_face[i] = white_face[i]
	

	white_face[0] = r_white_face[6]
	white_face[1] = r_white_face[3]
	white_face[2] = r_white_face[0]
	white_face[3] = r_white_face[7]
	white_face[4] = r_white_face[4]
	white_face[5] = r_white_face[1]
	white_face[6] = r_white_face[8]
	white_face[7] = r_white_face[5]
	white_face[8] = r_white_face[2]

def back_inverted():

	print "B'(Y|B), "
	global solution_moves
	solution_moves.append("Bi")

	# Cube simulation
	r_blue_face   = [0]*10
	r_orange_face = [0]*10
	r_green_face  = [0]*10
	r_red_face    = [0]*10
	r_white_face  = [0]*10

	for i in range(0, 9):
		r_blue_face[i] = blue_face[i]
	
	for i in range(0, 9):
		r_orange_face[i] = orange_face[i]
	
	for i in range(0, 9):
		r_green_face[i] = green_face[i]
	
	for i in range(0, 9):
		r_red_face[i] = red_face[i]
	

	blue_face[0] = r_red_face[0]
	blue_face[1] = r_red_face[1]
	blue_face[2] = r_red_face[2]

	red_face[0] = r_green_face[0]
	red_face[1] = r_green_face[1]
	red_face[2] = r_green_face[2]

	green_face[0] = r_orange_face[0]
	green_face[1] = r_orange_face[1]
	green_face[2] = r_orange_face[2]

	orange_face[0] = r_blue_face[0]
	orange_face[1] = r_blue_face[1]
	orange_face[2] = r_blue_face[2]

	for i in range(0, 9):
		r_white_face[i] = white_face[i]
	

	white_face[0] = r_white_face[2]
	white_face[1] = r_white_face[5]
	white_face[2] = r_white_face[8]
	white_face[3] = r_white_face[1]
	white_face[4] = r_white_face[4]
	white_face[5] = r_white_face[7]
	white_face[6] = r_white_face[0]
	white_face[7] = r_white_face[3]
	white_face[8] = r_white_face[6]

def flip_cube(cube_rotation):	# flips the cube on the F or U axis

	r_blue_face =   [0]*10
	r_orange_face = [0]*10
	r_green_face =  [0]*10
	r_red_face =    [0]*10
	r_white_face =  [0]*10
	r_yellow_face = [0]*10

	if cube_rotation == 'F': 

		print "[Cube Flip: CW on F], "
		global solution_moves
		solution_moves.append("Cube Flip: CW on F")

		# cube simulation
		for i in range(0, 9):	
			r_blue_face[i] = blue_face[i]
		
		for i in range(0, 9):	
			r_orange_face[i] = orange_face[i]
		
		for i in range(0, 9):
			r_green_face[i] = green_face[i]
		
		for i in range(0, 9):
			r_red_face[i] = red_face[i]
		

		for i in range(0, 9):
			r_white_face[i] = white_face[i]
		
		for i in range(0, 9):
			r_yellow_face[i] = yellow_face[i]
		

		# assign copies to real faces
		for i in range(0, 9):
			orange_face[i] = r_blue_face[i]
		
		for i in range(0, 9):
			green_face[i] = r_orange_face[i]
		
		for i in range(0, 9):
			red_face[i] = r_green_face[i]
		
		for i in range(0, 9):
			blue_face[i] = r_red_face[i]
		

		white_face[0] = r_white_face[2]
		white_face[1] = r_white_face[5]
		white_face[2] = r_white_face[8]
		white_face[3] = r_white_face[1]
		white_face[4] = r_white_face[4]
		white_face[5] = r_white_face[7]
		white_face[6] = r_white_face[0]
		white_face[7] = r_white_face[3]
		white_face[8] = r_white_face[6]

		yellow_face[0] = r_yellow_face[6]
		yellow_face[1] = r_yellow_face[3]
		yellow_face[2] = r_yellow_face[0]
		yellow_face[3] = r_yellow_face[7]
		yellow_face[4] = r_yellow_face[4]
		yellow_face[5] = r_yellow_face[1]
		yellow_face[6] = r_yellow_face[8]
		yellow_face[7] = r_yellow_face[5]
		yellow_face[8] = r_yellow_face[2]

	elif cube_rotation ==  'f': 					# CCW on F
		print "[Cube Flip: CCW on F], "
		global solution_moves
		solution_moves.append("Cube Flip: CCW on F")

		# assign colors to a copy of the face
		for i in range(0, 9):
			r_blue_face[i] = blue_face[i]
		
		for i in range(0, 9):
			r_orange_face[i] = orange_face[i]
		
		for i in range(0, 9):
			r_green_face[i] = green_face[i]
		
		for i in range(0, 9):
			r_red_face[i] = red_face[i]
		

		for i in range(0, 9):
			r_white_face[i] = white_face[i]
		
		for i in range(0, 9):
			r_yellow_face[i] = yellow_face[i]
		

		# assign copies to real faces
		for i in range(0, 9):
			red_face[i] = r_blue_face[i]
		
		for i in range(0, 9):
			blue_face[i] = r_orange_face[i]
		
		for i in range(0, 9):
			orange_face[i] = r_green_face[i]
		
		for i in range(0, 9):
			green_face[i] = r_red_face[i]
		

		yellow_face[0] = r_yellow_face[2]
		yellow_face[1] = r_yellow_face[5]
		yellow_face[2] = r_yellow_face[8]
		yellow_face[3] = r_yellow_face[1]
		yellow_face[4] = r_yellow_face[4]
		yellow_face[5] = r_yellow_face[7]
		yellow_face[6] = r_yellow_face[0]
		yellow_face[7] = r_yellow_face[3]
		yellow_face[8] = r_yellow_face[6]

		white_face[0] = r_white_face[6]
		white_face[1] = r_white_face[3]
		white_face[2] = r_white_face[0]
		white_face[3] = r_white_face[7]
		white_face[4] = r_white_face[4]
		white_face[5] = r_white_face[1]
		white_face[6] = r_white_face[8]
		white_face[7] = r_white_face[5]
		white_face[8] = r_white_face[2]

	elif cube_rotation == 'U': 				# CW on U
		print "[Cube Flip: CW on U], "
		global solution_moves
		solution_moves.append("Cube Flip: CW on U")

		for i in range(0, 9):
			r_white_face[i] = white_face[i]
		
		for i in range(0, 9):
			r_orange_face[i] = orange_face[i]

		
		for i in range(0, 9):
			r_yellow_face[i] = yellow_face[i]
		
		for i in range(0, 9):
			r_red_face[i] = red_face[i]
		

		for i in range(0, 9):
			r_blue_face[i] = blue_face[i]
		
		for i in range(0, 9):
			r_green_face[i] = green_face[i]
		

		orange_face[0] = r_white_face[8]
		orange_face[1] = r_white_face[7]
		orange_face[2] = r_white_face[6]
		orange_face[3] = r_white_face[5]
		orange_face[4] = r_white_face[4]
		orange_face[5] = r_white_face[3]
		orange_face[6] = r_white_face[2]
		orange_face[7] = r_white_face[1]
		orange_face[8] = r_white_face[0]


		yellow_face[0] = r_orange_face[6]
		yellow_face[1] = r_orange_face[3]
		yellow_face[2] = r_orange_face[0]
		yellow_face[3] = r_orange_face[7]
		yellow_face[4] = r_orange_face[4]
		yellow_face[5] = r_orange_face[1]
		yellow_face[6] = r_orange_face[8]
		yellow_face[7] = r_orange_face[5]
		yellow_face[8] = r_orange_face[2]

		white_face[8] = r_red_face[6]
		white_face[7] = r_red_face[3]
		white_face[6] = r_red_face[0]
		white_face[5] = r_red_face[7]
		white_face[4] = r_red_face[4]
		white_face[3] = r_red_face[1]
		white_face[2] = r_red_face[8]
		white_face[1] = r_red_face[5]
		white_face[0] = r_red_face[2]

		red_face[6] = r_yellow_face[0]
		red_face[3] = r_yellow_face[1]
		red_face[0] = r_yellow_face[2]
		red_face[7] = r_yellow_face[3]
		red_face[4] = r_yellow_face[4]
		red_face[1] = r_yellow_face[5]
		red_face[8] = r_yellow_face[6]
		red_face[5] = r_yellow_face[7]
		red_face[2] = r_yellow_face[8]

		green_face[0] = r_green_face[2]
		green_face[1] = r_green_face[5]
		green_face[2] = r_green_face[8]
		green_face[3] = r_green_face[1]
		green_face[4] = r_green_face[4]
		green_face[5] = r_green_face[7]
		green_face[6] = r_green_face[0]
		green_face[7] = r_green_face[3]
		green_face[8] = r_green_face[6]

		blue_face[0] = r_blue_face[6]
		blue_face[1] = r_blue_face[3]
		blue_face[2] = r_blue_face[0]
		blue_face[3] = r_blue_face[7]
		blue_face[4] = r_blue_face[4]
		blue_face[5] = r_blue_face[1]
		blue_face[6] = r_blue_face[8]
		blue_face[7] = r_blue_face[5]
		blue_face[8] = r_blue_face[2]

	elif cube_rotation ==  'u':
		print "[Cube Flip: CCW on U], "
		global solution_moves
		solution_moves.append("Cube Flip: CCW on U")

		for i in range(0, 9):
			r_white_face[i] = white_face[i]
		
		for i in range(0, 9):
			r_orange_face[i] = orange_face[i]

		
		for i in range(0, 9):
			r_yellow_face[i] = yellow_face[i]
		
		for i in range(0, 9):
			r_red_face[i] = red_face[i]
		

		for i in range(0, 9):
			r_blue_face[i] = blue_face[i]
		
		for i in range(0, 9):
			r_green_face[i] = green_face[i]
		

		red_face[6] = r_white_face[0]
		red_face[3] = r_white_face[1]
		red_face[0] = r_white_face[2]
		red_face[7] = r_white_face[3]
		red_face[4] = r_white_face[4]
		red_face[1] = r_white_face[5]
		red_face[8] = r_white_face[6]
		red_face[5] = r_white_face[7]
		red_face[2] = r_white_face[8]


		white_face[0] = r_orange_face[6]
		white_face[1] = r_orange_face[3]
		white_face[2] = r_orange_face[0]
		white_face[3] = r_orange_face[7]
		white_face[4] = r_orange_face[4]
		white_face[5] = r_orange_face[1]
		white_face[6] = r_orange_face[8]
		white_face[7] = r_orange_face[5]
		white_face[8] = r_orange_face[2]

		yellow_face[0] = r_red_face[6]
		yellow_face[1] = r_red_face[3]
		yellow_face[2] = r_red_face[0]
		yellow_face[3] = r_red_face[7]
		yellow_face[4] = r_red_face[4]
		yellow_face[5] = r_red_face[1]
		yellow_face[6] = r_red_face[8]
		yellow_face[7] = r_red_face[5]
		yellow_face[8] = r_red_face[2]

		orange_face[6] = r_yellow_face[0]
		orange_face[3] = r_yellow_face[1]
		orange_face[0] = r_yellow_face[2]
		orange_face[7] = r_yellow_face[3]
		orange_face[4] = r_yellow_face[4]
		orange_face[1] = r_yellow_face[5]
		orange_face[8] = r_yellow_face[6]
		orange_face[5] = r_yellow_face[7]
		orange_face[2] = r_yellow_face[8]

		blue_face[0] = r_blue_face[2]
		blue_face[1] = r_blue_face[5]
		blue_face[2] = r_blue_face[8]
		blue_face[3] = r_blue_face[1]
		blue_face[4] = r_blue_face[4]
		blue_face[5] = r_blue_face[7]
		blue_face[6] = r_blue_face[0]
		blue_face[7] = r_blue_face[3]
		blue_face[8] = r_blue_face[6]

		green_face[0] = green_face[6]
		green_face[1] = green_face[3]
		green_face[2] = green_face[0]
		green_face[3] = green_face[7]
		green_face[4] = green_face[4]
		green_face[5] = green_face[1]
		green_face[6] = green_face[8]
		green_face[7] = green_face[5]
		green_face[8] = green_face[2]

	else:
		print "INVALID CUBE ROTATION: SEE < def flip_cube() >"
	


##########/ Cube Algorithms #############/
def fix_cross_instance_1():					 # bad pieces up and right

	print"	Fix Cross Instance 1: "

	# cube simulation
	right()
	right()
	back()
	up()
	up()
	back_inverted()
	right()
	right()
	

def fix_cross_instance_2():				 # bad pieces up and down
	print "	Fix Cross Instance 2: "

	# cube simulation
	up()
	up()
	back()
	back()
	down()
	down()
	back()
	back()
	up()
	up()
	

def fix_corners_instance_1(): # top left
	
	print "	Fix Corners Instance 1: "
	
	# cube simulation
	up()
	back()
	up_inverted()



def fix_corners_instance_2(): # top right
	print"	Fix Corners Instance 2: "

	# cube simulation
	up_inverted()
	back_inverted()
	up()




def fix_corners_instance_3():
	print "	Fix Corners Instance 3 (bring yellow piece up): "

	# cube simulation
	left_inverted()
	back()
	left()



def add_edges_instance_1(): # 2 left
	print"	Add Edges Instance 1: "

	# cube simulation
	back_inverted()
	left_inverted()
	back()
	left()
	back()
	up()
	back_inverted()
	up_inverted()




def add_edges_instance_2(): # 2 right
	print "	Add edges Instance 2: "

	# cube simulation	
	back()
	right()
	back_inverted()
	right_inverted()
	back_inverted()
	up_inverted()
	back()
	up()




def add_edges_instance_3():
	print "	Add edges Instance 3: " 

	# cube simulation
	back_inverted()
	up_inverted()
	back()
	up()
	back()
	right()
	back_inverted()
	right_inverted()



def white_cross_on_top():
	print "	White Cross On Top: "
	
	# cube simulation
	right_inverted()
	back_inverted()
	up_inverted()
	back()
	up()
	right()



def finish_white_face_instance_1():
	print "	Finish White Face Instance 1: "
	
	# cube simulation
	right()
	back()
	right_inverted()
	back()
	right()
	back()
	back()
	right_inverted()



def finish_white_face_instance_2():
	print"	Finish White Face Instance 2: "
	
	# cube simulation
	left_inverted()
	back_inverted()
	left()
	back_inverted()
	left_inverted()
	back_inverted()
	back_inverted()
	left()




# insert top layer corners
def green_on_right():
	print "	Green On Right: "

	# cube simulation
	right_inverted()
	up()
	right_inverted()
	down()
	down()
	right()
	up_inverted()
	right_inverted()
	down()
	down()
	right()
	right()


def green_on_left():
	print "	Green On Left: "

	# cube simulation
	left()
	up_inverted()
	left()
	down_inverted()
	down_inverted()
	left_inverted()
	up()
	left()
	down_inverted()
	down_inverted()
	left_inverted()
	left_inverted()

	# insert top layer edges
def cw_rotation(): # can also be used for 4 bad edges
	print "	CW Rotation: ";
	finish_white_face_instance_1()
	flip_cube('f')	# rotate cube: right side = front side
	finish_white_face_instance_2()
	flip_cube('F')  # rotate cube back to original state: left side = front side

def  ccw_rotation():
	print "	CCW Rotation: "
	finish_white_face_instance_2()
	flip_cube('F')	# rotate cube: left side = front side
	finish_white_face_instance_1()
	flip_cube('f')





######################### cube decide algorithms #####################


solve_stage = 1
cube_solved = True

def solve_cube():
	print "Solving Cube: "
	print_cube()
	global solve_stage 
	solve_stage = 1
	while solve_stage != 10:
		print  "STAGE:",solve_stage
		cube_decide()
	

def cube_decide():
	if solve_stage == 1:
		# Cross
		cube_decide_cross()
	elif solve_stage == 2:
		# Whole Cross
		cube_decide_whole_cross()
	elif solve_stage == 3:
		# First layer (corners)
		cube_decide_corners()
	elif solve_stage == 4:
		# Second Layer
		cube_decide_add_edges()
	elif solve_stage == 5:
		# White Cross
		cube_decide_white_cross()
	elif solve_stage == 6:
		# White Top
		cube_decide_white_top()
	elif solve_stage == 7:
		# Orientation of the Last Layer
		cube_decide_oll()
	elif solve_stage == 8:
		# Permute the Last Layer
		cube_decide_pll()	
	elif solve_stage == 9:
		cube_decide_solved()



def cube_decide_cross(): 
	
	print "Cross: " 

	global solve_stage 

	if (yellow_face[1] == 'y' and yellow_face[3] == 'y' and yellow_face[5] == 'y' and yellow_face[7] == 'y' ) :
		solve_stage = 2 
		print "Cross Solved. GOTO", solve_stage  
	# move the pieces from the sides up #######/ #/ should turn this into a function later(blue_face, moves)
	elif(solve_stage == 1):
		# move from blue_face[3]
		if (blue_face[3] == 'y'):
			for x in range(0, 3):		 # rotate cube four times, or until there is an empty space
				if (yellow_face[3] != 'y'):
					left() 
					break  ## end loop since yellow piece has reached the top
				else:
					front() 
		## move from blue_face[5]
		elif (blue_face[5] == 'y'):
			for x in range(0, 3): # rotate cube four times, or until there is an empty space
				if (yellow_face[5] != 'y'):
					right_inverted() 
					break  # end loop since yellow piece has reached the top
				else:
					front() 
		## move from red_face[5]
		elif (red_face[5] == 'y'):
			for x in range(0, 3): # rotate cube four times, or until there is an empty space
				if (yellow_face[1] != 'y'):				
					up_inverted() 
					break  # end loop since yellow piece has reached the top
				else:			
					front() 			
		
		# move from red_face[3]
		elif (red_face[3] == 'y'):		
			for x in range(0, 3): # rotate cube four times, or until there is an empty space			
				if (yellow_face[7] != 'y'):			
					down() 
					break  # end loop since yellow piece has reached the top				
				else:				
					front() 
			
			
		# move from green_face[5]
		elif (green_face[5] == 'y'):		
			for x in range(0, 3): # rotate cube four times, or until there is an empty space			
				if (yellow_face[3] != 'y'):				
					left_inverted() 
					break  # end loop since yellow piece has reached the top				
				else:				
					front() 
		

		# move from green_face[3]
		elif (green_face[3] == 'y'):
			for x in range(0, 3): # rotate cube four times, or until there is an empty space	
				if (yellow_face[5] != 'y'):			
					right() 
					break  # end loop since yellow piece has reached the top			
				else:			
					front() 
				

		# move from orange_face[5]
		elif (orange_face[5] == 'y'):
			for x in range(0, 3): # rotate cube four times, or until there is an empty space		
				if (yellow_face[7] != 'y'):			
					down_inverted() 
					break  # end loop since yellow piece has reached the top			
				else:
					front() 
		
		# move from orange_face[3]
		elif (orange_face[3] == 'y'):
			for x in range(0, 3): # rotate cube four times, or until there is an empty space	
				if (yellow_face[1] != 'y'):		
					up() 
					break  # end loop since yellow piece has reached the top		
				else:	
					front() 
	
		# move from white_face[1]
		elif (white_face[1] == 'y'):
			for x in range(0, 3): # rotate cube four times, or until there is an empty space
				if (yellow_face[7] != 'y'):
					down() 
					down() 
					break  # end loop since yellow piece has reached the top	
				else:
					front() 	
		
		# move from white_face[7]
		elif (white_face[7] == 'y'):
			for x in range(0, 3): # rotate cube four times, or until there is an empty space
				if (yellow_face[1] != 'y'):
					up() 
					up() 
					break  # end loop since yellow piece has reached the top
				else:
					front() 
	
		# move from white_face[3]
		elif (white_face[3] == 'y'):
			for x in range(0, 3): # rotate cube four times, or until there is an empty space
				if (yellow_face[3] != 'y'):
					left() 
					left() 
					break  # end loop since yellow piece has reached the top
				else:
					front() 
		
		# move from white_face[5]
		elif (white_face[5] == 'y'):
			for x in range(0, 3): # rotate cube four times, or until there is an empty space
				if (yellow_face[5] != 'y'):
					right() 
					right() 
					break  # end loop since yellow piece has reached the top
				else:
					front() 
		
		#############/ get the piece from 2- move spots, like blue_face[7]
		## blue_face[1]
		elif (blue_face[1] == 'y'):	
			for x in range(0, 3): # rotate cube four times, or until there is an empty space			
				if (yellow_face[1] != 'y'):				
					up() 
					front() 
					right_inverted() 
					break  # end loop since yellow piece has reached the top				
				else:				
					front() 							
		
		## blue_face[7]
		elif (blue_face[7] == 'y'):		
			if (yellow_face[1] != 'y'):			
				up_inverted() 
				front() 
				right_inverted() 			
			else:			
				up_inverted() 
			
		
		## red_face[1]
		elif (red_face[1] == 'y'):		
			for x in range(0, 3): # rotate cube four times, or until there is an empty space			
				if (yellow_face[3] != 'y'):				
					left() 
					front() 
					up_inverted() 
					break  # end loop since yellow piece has reached the top				
				else:				
					front() 		
		
		# red_face[7]
		elif (red_face[7] == 'y'):	
			if (yellow_face[3] != 'y'):		
				left_inverted() 
				front() 
				up_inverted() 			
			else:		
				left_inverted() 
			
		
		# green_face[1]
		elif (green_face[1] == 'y'):	
			for x in range(0, 3): # rotate cube four times, or until there is an empty space			
				if (yellow_face[7] != 'y'):				
					down() 
					front() 
					left_inverted() 
					break  # end loop since yellow piece has reached the top			
				else:				
					front() 		
		
		# green_face[7]
		elif (green_face[7] == 'y'):	
			if (yellow_face[7] != 'y'):			
				down() 
				front_inverted() 
				right() 		
			else:			
				down() 
					
		# orange_face[1]
		elif (orange_face[1] == 'y'):		
			for x in range(0, 3): # rotate cube four times, or until there is an empty space		
				if (yellow_face[5] != 'y'):				
					right() 
					front() 
					down_inverted() 
					break  # end loop since yellow piece has reached the top				
				else:				
					front() 
				
		
		# green_face[7]
		elif (orange_face[7] == 'y'):		
			if (yellow_face[5] != 'y'):		
				right_inverted() 
				front() 
				down_inverted() 			
			else:
				right_inverted() 


def cube_decide_whole_cross():


	print "Whole Cross: "

	global solve_stage 

	if (solve_stage == 2 and blue_face[7] == 'b' and red_face[7] == 'r' and green_face[7] == 'g' and orange_face[7] == 'o'):
		print "Solved."
		solve_stage = 3
	
	# green and orange are good
	elif (solve_stage == 2 and blue_face[7] != 'b' and red_face[7] != 'r' and green_face[7] == 'g' and orange_face[7] == 'o'):
	
		flip_cube('F')
		fix_cross_instance_1()
		flip_cube('f')
	
	# red and orange are good
	elif (solve_stage == 2 and blue_face[7] != 'b' and red_face[7] == 'r' and green_face[7] != 'g' and orange_face[7] == 'o'):
	
		fix_cross_instance_2()
	
	# red and green are good
	elif (solve_stage == 2 == True and blue_face[7] != 'b' and red_face[7] == 'r' and green_face[7] == 'g' and orange_face[7] != 'o'):
	
		fix_cross_instance_1()
	
	# blue and orange are good
	elif (solve_stage == 2 and blue_face[7] == 'b' and red_face[7] != 'r' and green_face[7] != 'g' and orange_face[7] == 'o'):
	
		flip_cube('F')
		flip_cube('F')
		fix_cross_instance_1()
		flip_cube('f')
		flip_cube('f')
	
	# blue and green are good
	elif (solve_stage == 2 and blue_face[7] == 'b' and red_face[7] != 'r' and green_face[7] == 'g' and orange_face[7] != 'o'):
	
		flip_cube('F')
		fix_cross_instance_2()
		flip_cube('f')
	
	# red and blue are good
	elif (solve_stage == 2 and blue_face[7] == 'b' and red_face[7] == 'r' and green_face[7] != 'g' and orange_face[7] != 'o'):
	
		flip_cube('f')
		fix_cross_instance_1()
		flip_cube('F')
	
	# none match, cross in done but whole cross isn't
	elif (solve_stage == 2):
		front()
	
	else:
		print "Error in whole_cross"
	



def cube_decide_corners(): # needs fixing, maybe yellows at bottom portion

	print "Corners (First Layer): "

	global solve_stage 

	# First layer is done correctly
	if (solve_stage == 3 and yellow_face[0] == 'y' and blue_face[6] == 'b' and yellow_face[2] == 'y' and orange_face[6] == 'o' and green_face[6] == 'g' and yellow_face[6] == 'y' and orange_face[6] == 'o' and yellow_face[8] == 'y' and red_face[6] == 'r'):
		print "Solved."
		solve_stage = 4
	
	elif(solve_stage == 3):
	
		##### if THERE ARE yellow on top
		if (blue_face[0] == 'y' or blue_face[2] == 'y' or red_face[0] == 'y' or red_face[2] == 'y' or green_face[0] == 'y' or green_face[2] == 'y' or orange_face[0] == 'y' or orange_face[2] == 'y' or white_face[0] == 'y' or white_face[2] == 'y' or white_face[6] == 'y' or white_face[8] == 'y'):
		
			##### Do all possible cases for corner (4x3):
			#### 3 cases for the blue/orange sides
			if (blue_face[2] == 'y' and white_face[8] == 'b' and orange_face[0] == 'o'):
			
				fix_corners_instance_2()
			
			elif (blue_face[2] == 'o' and white_face[8] == 'y' and orange_face[0] == 'b'):
				fix_corners_instance_2()
				fix_corners_instance_2()
				back()
				fix_corners_instance_2()
			
			elif (blue_face[2] == 'b' and white_face[8] == 'o' and orange_face[0] == 'y'):
				flip_cube('f')
				fix_corners_instance_1()
				flip_cube('F')
			
			#### 3 cases for the orange/green sides
			elif (orange_face[2] == 'y' and white_face[2] == 'o' and green_face[0] == 'g'):
			
				flip_cube('f')
				fix_corners_instance_2()
				flip_cube('F')
			
			elif (orange_face[2] == 'g' and white_face[2] == 'y' and green_face[0] == 'o'):
				flip_cube('f')
				fix_corners_instance_2()
				fix_corners_instance_2()
				back()
				fix_corners_instance_2()
				flip_cube('F')
			
			elif (orange_face[2] == 'o' and white_face[2] == 'g' and green_face[0] == 'y'):
				flip_cube('F')
				flip_cube('F')
				fix_corners_instance_1()
				flip_cube('f')
				flip_cube('f')
			
			#### 3 cases for the green/red sides
			elif (green_face[2] == 'y' and white_face[0] == 'g' and red_face[0] == 'r'):
				flip_cube('F')
				flip_cube('F')
				fix_corners_instance_2()
				flip_cube('f')
				flip_cube('f')
			
			elif (green_face[2] == 'r' and white_face[0] == 'y' and red_face[0] == 'g'):	
				flip_cube('F')
				flip_cube('F')
				fix_corners_instance_2()
				fix_corners_instance_2()
				back()
				fix_corners_instance_2()
				flip_cube('f')
				flip_cube('f')
			
			elif (green_face[2] == 'g' and white_face[0] == 'r' and red_face[0] == 'y'):
				flip_cube('F')
				fix_corners_instance_1()
				flip_cube('f')
			
			#### 3 cases for the red/blue sides
			elif (red_face[2] == 'y' and white_face[6] == 'r' and blue_face[0] == 'b'):
				flip_cube('F')
				fix_corners_instance_2()
				flip_cube('f')
			
			elif (red_face[2] == 'b' and white_face[6] == 'y' and blue_face[0] == 'r'):
				fix_corners_instance_1()
				fix_corners_instance_1()
				back_inverted()
				fix_corners_instance_1()
			
			elif (red_face[2] == 'r' and white_face[6] == 'b' and blue_face[0] == 'y'):
				fix_corners_instance_1()
			
			else:
				back()  # move yellow on top of correct position
				
		##### if there are NO yellows on top and first layer isn't solved already
		elif (yellow_face[0] != 'y' or red_face[8] != 'r' or blue_face[6] != 'b' or
				 yellow_face[2] != 'y' or orange_face[6] != 'o' or blue_face[8] != 'b' or
				 yellow_face[8] != 'y' or orange_face[8] != 'o' or green_face[6] != 'g' or
				 yellow_face[6] != 'y' or red_face[6] != 'r' or blue_face[8] != 'g'):
			###### Bring all yellow corners up:
			# Blue and red corner
			if (yellow_face[0] != 'y' or red_face[8] != 'r' or blue_face[6] != 'b'):
				fix_corners_instance_3()
			
			# blue and orange corner
			elif (yellow_face[2] != 'y' or orange_face[6] != 'o' or blue_face[8] != 'b'):
				flip_cube('f')
				fix_corners_instance_3()
				flip_cube('F')
			
			# Orange and green corner
			elif (yellow_face[8] != 'y' or orange_face[8] != 'o' or green_face[6] != 'g'):
				flip_cube('f')
				flip_cube('f')
				fix_corners_instance_3()
				flip_cube('F')
				flip_cube('F')
			
			# Green and red corner
			elif (yellow_face[6] != 'y' or red_face[6] != 'r' or blue_face[8] != 'g'):
				flip_cube('F')
				fix_corners_instance_3()
				flip_cube('f')
			
		else:
		
			print "First Layer not Solved."
		
		

def cube_decide_add_edges():
	print ("Edges (Second Layer): ")

	global solve_stage 
	##/ Second layer done
	if (solve_stage == 4 and
	    green_face[3] == 'g' and green_face[5] == 'g' and
	    red_face[3] == 'r' and red_face[5] == 'r' and	
	    blue_face[3] == 'b' and blue_face[5] == 'b' and
	    orange_face[3] == 'o' and orange_face[5] == 'o'):
		
		print "Solved."
		solve_stage = 5
	
	elif(solve_stage == 4):
	
		##/ red3 --> 2blue
		if(red_face[1] == 'r' and white_face[3] == 'b'):
			flip_cube('F')
			add_edges_instance_2()	# two right
			flip_cube('f')
		
		##/ red2 --> 3blue
		elif(blue_face[1] == 'b' and white_face[7] == 'r'):

			add_edges_instance_1()	# two left
		

		## blue3 --> orange
		elif(blue_face[1] == 'b' and white_face[7] == 'o'):
			add_edges_instance_2()	# two right
		
		## blue --> 3orange
		elif(orange_face[1] == 'o' and white_face[5] == 'b'):
			flip_cube('f')
			add_edges_instance_1()	# two left
			flip_cube('F')
		
		## orange3 --> green
		elif(orange_face[1] == 'o' and white_face[5] == 'g'):
			flip_cube('f')
			add_edges_instance_2()	# two right
			flip_cube('F')
		
		## orange --> 3green
		elif(green_face[1] == 'g' and white_face[1] == 'o'):
			flip_cube('F')
			flip_cube('F')
			add_edges_instance_1()	# two left
			flip_cube('f')
			flip_cube('f')
		

		## green3 --> red
		elif(green_face[1] == 'g' and white_face[1] == 'r'):
			flip_cube('F')
			flip_cube('F')
			add_edges_instance_2()	# two right
			flip_cube('f')
			flip_cube('f')
		
		## green --> 3red
		elif(red_face[1] == 'r' and white_face[3] == 'g'):
		
			flip_cube('F')
			add_edges_instance_1()	# two left
			flip_cube('f')
		
		## # rotate top layer to match any missing colors
		elif (blue_face[3] == 'w' or blue_face[5] == 'w' or red_face[3] == 'w' or red_face[5] == 'w' or
			green_face[3] == 'w' or green_face[5] == 'w' or orange_face[3] == 'w' or orange_face[5] == 'w'):
		
			back()
		

		##/ bring incorrectly placed edges to the top again
		elif (blue_face[3] != 'b' or red_face[5] != 'r' or 
				 red_face[3] != 'r' or green_face[5] != 'g' or
		         green_face[3] != 'g' or orange_face[5] != 'o' or 
		         orange_face[3] != 'o' or blue_face[5] != 'b'):
		
			if(blue_face[3] != 'b' or red_face[5] != 'r'):
			
				flip_cube('F')
				add_edges_instance_3()
				flip_cube('f')
			
			elif(red_face[3] != 'r' or green_face[5] != 'g'):
			
				flip_cube('F')
				flip_cube('F')
				add_edges_instance_3()
				flip_cube('f')
				flip_cube('f')
			
			elif(green_face[3] != 'g' or orange_face[5] != 'o'):
			
				flip_cube('f')
				add_edges_instance_3()
				flip_cube('F')
			
			elif(orange_face[3] != 'o' or blue_face[5] != 'b'):
			
				add_edges_instance_3()
			
		
		else:
			print "second layer not solved."
		
	

def cube_decide_white_cross(): # looking for two whites, may be more efficient, but current revision get the job done
	
	print "White Cross: "

	global solve_stage 

	if (solve_stage == 5 and
	    white_face[1] == 'w' and
	    white_face[3] == 'w' and
	    white_face[5] == 'w' and
	    white_face[7] == 'w'):
	
		print "Solved."
		solve_stage = 6
	
	elif (blue_face[1] == 'w' or red_face[1] == 'w' or green_face[1] == 'w' or orange_face[1] == 'w'):
	
		#/ whties in connecting faces
		if(blue_face[1] == 'w' and orange_face[1] == 'w'):
			white_cross_on_top()
		
		elif(orange_face[1] == 'w' and green_face[1] == 'w'):
			back()
			white_cross_on_top()
		
		elif(green_face[1] == 'w' and red_face[1] == 'w'):
			back()
			back()
			white_cross_on_top()
		
		elif(red_face[1] == 'w' and blue_face[1] == 'w'):
			back_inverted()
			white_cross_on_top()
		
		#/ whites not on connecting face
		elif(blue_face[1] == 'w'):
			white_cross_on_top()
		
		elif(green_face[1] == 'w'):
			back()
			back()
			white_cross_on_top()
		
		elif(red_face[1] == 'w'):
			back_inverted()
			white_cross_on_top()
		
		elif(orange_face[1] == 'w'):
			back()
			white_cross_on_top()
		
		else:
			print "No white cross"
		
	

def cube_decide_white_top():

	print "White Face: "

	global solve_stage 

	if (white_face[0] == 'w' and
	    white_face[2] == 'w' and
	    white_face[6] == 'w' and
	    white_face[8] == 'w'):
	
		print "Solved."
		solve_stage = 7
	
	elif(solve_stage == 6):
	
		#################/ sune cases
		if (white_face[0] != 'w' and white_face[2] != 'w' and white_face[6] != 'w' and white_face[8] == 'w' or
		    white_face[0] != 'w' and white_face[2] != 'w' and white_face[6] == 'w' and white_face[8] != 'w' or
		    white_face[0] == 'w' and white_face[2] != 'w' and white_face[6] != 'w' and white_face[8] != 'w' or
		    white_face[0] != 'w' and white_face[2] == 'w' and white_face[6] != 'w' and white_face[8] != 'w'):
		
			# Any sune orientation is True
			#########/ left sune cases:
			if (white_face[0] != 'w' and white_face[2] != 'w' and white_face[6] != 'w' and white_face[8] == 'w' and red_face[0] == 'w' and blue_face[0] == 'w'):
				finish_white_face_instance_2()	# left sune
			
			elif(white_face[0] != 'w' and white_face[2] == 'w' and white_face[6] != 'w' and white_face[8] != 'w' and blue_face[0] == 'w' and orange_face[0] == 'w'):
				back()
				finish_white_face_instance_2() # left sune
			
			elif(white_face[0] == 'w' and white_face[2] != 'w' and white_face[6] != 'w' and white_face[8] != 'w' and orange_face[0] == 'w' and green_face[0] == 'w'):
				back()
				back()
				finish_white_face_instance_2() # left sune
			
			elif(white_face[0] != 'w' and white_face[2] != 'w' and white_face[6] == 'w' and white_face[8] != 'w' and green_face[0] == 'w' and red_face[0] == 'w'):
				back_inverted()
				finish_white_face_instance_2() # left sune
			
			######### right sune cases:
			elif (white_face[0] != 'w' and white_face[2] != 'w' and white_face[6] == 'w' and white_face[8] != 'w' and orange_face[2] == 'w' and blue_face[2] == 'w'):
				finish_white_face_instance_1() # right sune
			
			elif(white_face[0] == 'w' and white_face[2] != 'w' and white_face[6] != 'w' and white_face[8] != 'w' and blue_face[2] == 'w' and red_face[2] == 'w'):
				back_inverted()
				finish_white_face_instance_1() # right sune
			
			elif(white_face[0] != 'w' and white_face[2] == 'w' and white_face[6] != 'w' and white_face[8] != 'w' and red_face[2] == 'w' and green_face[2] == 'w'):
				back()
				back()
				finish_white_face_instance_1() # right sune
			
			elif(white_face[0] != 'w' and white_face[2] != 'w' and white_face[6] != 'w' and white_face[8] == 'w' and orange_face[2] == 'w' and green_face[2] == 'w'):
				back()
				finish_white_face_instance_1() # right sune
			
			else:
				print "We are sune-less!"
			
		
		#/ blinker or car
		elif (white_face[0] != 'w' and white_face[2] != 'w' and white_face[6] != 'w' and white_face[8] != 'w'):
			# car
			if (red_face[0] == 'w' and red_face[2] == 'w' and orange_face[0] == 'w' and orange_face[2] == 'w'):
				finish_white_face_instance_1()
			
			elif (blue_face[0] == 'w' and blue_face[2] == 'w' and green_face[0] == 'w' and green_face[2] == 'w'):
				back()
				finish_white_face_instance_1()
			
			# blinker
			if (red_face[0] == 'w' and red_face[2] == 'w' and blue_face[2] == 'w' and green_face[0] == 'w'):
				finish_white_face_instance_1()
			
			elif(blue_face[0] == 'w' and blue_face[2] == 'w' and red_face[0] == 'w' and orange_face[2] == 'w'):
				back()
				finish_white_face_instance_1()
			
			elif(orange_face[0] == 'w' and orange_face[2] == 'w' and blue_face[0] == 'w' and green_face[2] == 'w'):
				finish_white_face_instance_2()
			
			elif(green_face[0] == 'w' and green_face[2] == 'w' and orange_face[0] == 'w' and red_face[2] == 'w'):
				back_inverted()
				finish_white_face_instance_1()
			
		
		#### bowtie
		if (white_face[0] == 'w' and white_face[2] != 'w' and white_face[6] != 'w' and white_face[8] == 'w' or
		    white_face[0] != 'w' and white_face[2] == 'w' and white_face[6] == 'w' and white_face[8] != 'w'):
			if (blue_face[0] == 'w' and orange_face[2] == 'w'):
				finish_white_face_instance_1()
			
			elif (red_face[0] == 'w' and blue_face[2] == 'w'):
				back_inverted()
				finish_white_face_instance_1()
			
			if (green_face[0] == 'w' and red_face[2] == 'w'):
				back_inverted()
				back_inverted()
				finish_white_face_instance_1()
			
			if (orange_face[0] == 'w' and green_face[2] == 'w'):
				back()
				finish_white_face_instance_1()
			
		
		###/ chameleon
		if (white_face[0] != 'w' and white_face[2] == 'w' and white_face[6] != 'w' and white_face[8] == 'w' or
		    white_face[0] != 'w' and white_face[2] != 'w' and white_face[6] == 'w' and white_face[8] == 'w' or
		    white_face[0] == 'w' and white_face[2] != 'w' and white_face[6] == 'w' and white_face[8] != 'w' or
		    white_face[0] == 'w' and white_face[2] == 'w' and white_face[6] != 'w' and white_face[8] != 'w'):

			if (white_face[0] == 'w' and white_face[2] == 'w' and white_face[6] != 'w' and white_face[8] != 'w'):
				finish_white_face_instance_1()
			
			elif (white_face[0] != 'w' and white_face[2] != 'w' and white_face[6] == 'w' and white_face[8] == 'w'):
				back()
				back()
				finish_white_face_instance_1()
			
			elif (white_face[0] != 'w' and white_face[2] == 'w' and white_face[6] != 'w' and white_face[8] == 'w'):
				back_inverted()
				finish_white_face_instance_1()
			
			elif (white_face[0] == 'w' and white_face[2] != 'w' and white_face[6] == 'w' and white_face[8] != 'w'):
				back()
				finish_white_face_instance_1()
			
		

def cube_decide_oll():

	print "OLL: "

	global solve_stage 

	# 
	if (green_face[0] == 'o' and green_face[2] == 'o' and red_face[0] == 'g' and red_face[2] == 'g' and
	   	blue_face[0] == 'r' and blue_face[2] == 'r' and orange_face[0] == 'b' and orange_face[2] == 'b'):
		back()
	
	elif(green_face[0] == 'b' and green_face[2] == 'b' and red_face[0] == 'o' and red_face[2] == 'o' and
	   		blue_face[0] == 'g' and blue_face[2] == 'g' and orange_face[0] == 'r' and orange_face[2] == 'r'):
		back()
		back()
	
	elif(green_face[0] == 'r' and green_face[2] == 'r' and red_face[0] == 'b' and red_face[2] == 'b' and
	   	    blue_face[0] == 'o' and blue_face[2] == 'o' and orange_face[0] == 'g' and orange_face[2] == 'g'):
		back_inverted()
	

	if (green_face[0] == 'g' and green_face[2] == 'g' and red_face[0] == 'r' and red_face[2] == 'r' and
	   	blue_face[0] == 'b' and blue_face[2] == 'b' and orange_face[0] == 'o' and orange_face[2] == 'o'):
		print "Solved."
		solve_stage = 8
	

	elif (solve_stage == 7):
	
		# green on right cases
		if (blue_face[0] == 'b' and blue_face[2] == 'g' and orange_face[2] == 'b'):
			green_on_right()
		
		elif (red_face[0] == 'b' and red_face[2] == 'g' and blue_face[2] == 'b'):
			back_inverted()
			green_on_right()
		
		elif (green_face[0] == 'b' and green_face[2] == 'g' and red_face[2] == 'b'):
			back()
			back()
			green_on_right()
		
		elif (orange_face[0] == 'b' and orange_face[2] == 'g' and green_face[2] == 'b'):
			back()
			green_on_right()
		

		# green on left cases
		elif (blue_face[0] == 'g' and blue_face[2] == 'b' and red_face[0] == 'b'):
			green_on_left()
		
		elif (red_face[0] == 'g' and red_face[2] == 'b' and green_face[0] == 'b'):
			back_inverted()
			green_on_left()
		
		elif (green_face[0] == 'g' and green_face[2] == 'b' and orange_face[0] == 'b'):
			back()
			back()
			green_on_left()
		
		elif (orange_face[0] == 'g' and orange_face[2] == 'b' and blue_face[0] == 'b'):
			back()
			green_on_left()
		
		# last resort, 2 steps to reach PLL are needed
		# green on right
		else:
			print "last resort"
			if (blue_face[2] == 'g'):
				green_on_right()
			
			elif(orange_face[2] == 'g'):
				back()
				green_on_right()
			
			elif(green_face[2] == 'g'):
				back()
				back()
				green_on_right()
			
			elif(red_face[2] == 'g'):
				back_inverted()
				green_on_right()
			
			# green on left
			elif (blue_face[0] == 'g'):
				green_on_left()
			
			elif(orange_face[0] == 'g'):
				back()
				green_on_left()
			
			elif(green_face[0] == 'g'):
				back()
				back()
				green_on_left()
			
			elif(red_face[0] == 'g'):
				back_inverted()
				green_on_left()
			
		
	


def cube_decide_pll():

	
	
	print "PLL: "

	global solve_stage 

	#################/
	if (blue_face[1] == 'b' and red_face[1] == 'r' and green_face[1] == 'g' and orange_face[1] == 'o'):
		print "Solved."
		solve_stage = 9
	
	elif (solve_stage == 8):
		
		print "inside"
		# counter clockwise rotation cases
		if (red_face[1] == 'b' and blue_face[1] == 'o' and orange_face[1] == 'r'):
			ccw_rotation()
		
		elif (green_face[1] == 'r' and red_face[1] == 'b' and blue_face[1] == 'g'):
			flip_cube('F')
			ccw_rotation()
			flip_cube('f')
		
		elif (orange_face[1] == 'g' and green_face[1] == 'r' and red_face[1] == 'o'):
			flip_cube('F')
			flip_cube('F')
			ccw_rotation()
			flip_cube('F')
			flip_cube('F')
		
		elif (blue_face[1] == 'o' and orange_face[1] == 'g' and green_face[1] == 'b'):
			flip_cube('f')
			ccw_rotation()
			flip_cube('F')
		

		# clockwise rotation cases
		elif (red_face[1] == 'o' and blue_face[1] == 'r' and orange_face[1] == 'b'):
			cw_rotation()
		
		elif (green_face[1] == 'b' and red_face[1] == 'g' and blue_face[1] == 'r'):
			flip_cube('F')
			cw_rotation()
			flip_cube('f')
		
		elif (orange_face[1] == 'r' and green_face[1] == 'o' and red_face[1] == 'g'):
			flip_cube('F')
			flip_cube('F')
			cw_rotation()
			flip_cube('F')
			flip_cube('F')
		
		elif (blue_face[1] == 'g' and orange_face[1] == 'b' and green_face[1] == 'o'):
			flip_cube('f')
			cw_rotation()
			flip_cube('F')		
		
		# all four edges are bad
		elif (blue_face[1] != 'b' and red_face[1] != 'r' and green_face[1] != 'g' and orange_face[1] != 'o'):
			cw_rotation()
		
		else:	# there is a problem here
			print "Problem in Pll (else statement reached)"
		
	
	else:
		print "Error in pll_case_check()"
	

def cube_decide_solved():


	global solve_stage 
	global cube_solved

	# check if all sides have the correct color 
	for i in range(0, 9):
	
		if (yellow_face[i] != 'y'):
			cube_solved = False
		
		if (white_face[i] != 'w'):
			cube_solved = False
		
		if (blue_face[i] != 'b'):
			cube_solved = False
		
		if (red_face[i] != 'r'):
			cube_solved = False
		
		if (green_face[i] != 'g'):
			cube_solved = False
		
		if (orange_face[i] != 'o'):
			cube_solved = False
		
	
	if (cube_solved == True):
		print "The Whole Cube is solved!!!"
	
	else:
		print "There is a problem: the cube isn't solved!"
		cube_solved = False
	
	print_cube()
	solve_stage = 10



############# Script start ###################


enter_cube()
legal_cube_check()
print_cube()


###### put in function send_cube_state(): #########

# send cube string
print "sending cube string..."
raw_cube_string = generate_raw_cube()
send_raw_cube()



	

############# Main ##############################
solution_moves = []
solve_cube()
print "======================================"
print "START WITH FRONT:YELLOW AND UP:BLUE "
print "ROTATE THE CUBE ONLY IF YOU ARE ASKED SO! "
print "MOVES:"
print solution_moves
print "======================================"
print "TOTAL MOVES =", len(solution_moves)