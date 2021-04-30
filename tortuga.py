import turtle

def main():
	ventana = turtle.Screen()
	dewin   = turtle.Turtle()

	make_square(dewin)
	turtle.mainloop()

def make_square(dewin):
	length = int(input("Writhe the square's size: "))
	for i in range (4):
		gire_lados(dewin,length)

def gire_lados(dewin,length):
	dewin.forward(length)
	dewin.left(90)


if __name__ == '__main__':
	main()
