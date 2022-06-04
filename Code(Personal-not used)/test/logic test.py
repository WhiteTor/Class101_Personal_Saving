import random

atrix = []

def init():
	global matrix
	matrix =[]
	for i in range(4):
		matrix.append([0] * 4)

	add_new_2()


def add_new_2():
	global matrix

# choosing a random index for
# row and column.
	r = random.randint(0, 3)
	c = random.randint(0, 3)

	matrix[r][c] = 2

	# while loop will break as the
	# random cell chosen will be empty
	# (or contains zero)
	while(matrix[r][c] != 0):
		r = random.randint(0, 3)
		c = random.randint(0, 3)

	# we will place a 2 at that empty
	# random cell.
	
	matrix[r][c] = 2

running = True

while running:
	init()

	command = input()

	if command == 'q' or command == 'Q':
		break