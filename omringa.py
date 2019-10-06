import os
import re


board = []
for i in range(7):
	tmp = []
	for j in range(7):
		tmp.append(" ")
	board.append(tmp)
		
def noNeighbor(sign,i,j):
	if i<6:
		if board[i+1][j] == sign:
			return False
	if j<6:
		if board[i][j+1] == sign:
			return False
	if i>0:
		if board[i-1][j] == sign:
			return False
	if j>0:
		if board[i][j-1] == sign:
			return False
	return True

def printboard():
	print(" |",end="")
	for i in range(7):
		print(str(i)+"|",end="")
	print()
	for i in range(7):
		print(" ",end="")
		for j in range(7):
			print("+-",end="")
		print("+")
		print("ABCDEFG"[i]+"|",end="")
		for j in range(7):
			print(board[i][j]+"|",end="")
		print()
	print(" ",end="")
	for j in range(7):
		print("+-",end="")
	print("+")

os.system('cls' if os.name == 'nt' else 'clear')
a = input("Licytacja, gracz O podaje liczbe punkt, X zamyka oczy: ")
a = int(a)
os.system('cls' if os.name == 'nt' else 'clear')
b = input("Licytacja, gracz X podaje liczbe punkt, O zamyka oczy: ")
b = int(b)
os.system('cls' if os.name == 'nt' else 'clear')



pointsO = 0
pointsX = 0

print("Wyniki licytacji:")
print("O podal: " + str(a))
print("X podal: " + str(b))

if a < b:
	print("O wygral i dostaje punkty")
	pointsO = pointsO + a
elif a > b:
	print("X wygral i dostaje punkty")
	pointsX = pointsX + b
else:
	print("Remis, nikt nie dostaje punktow")

input("Wcisnij enter aby rozpoczac gre")


	
	
	

player = "O"
end = False
while not end:

	
	os.system('cls' if os.name == 'nt' else 'clear')
	printboard()
	print("Wynik gracza O: " + str(pointsO))
	print("Wynik gracza X: " + str(pointsX))
	
	print("Obecny gracz: " + player)
	move = input("Wpisz kolejny ruch: ")
	text = re.findall("[a-gA-G][0-6]",move)
	while len(text)==0:
		print("Niepoprawny ruch. Sprobuj ponownie.")
		move = input("Wpisz kolejny ruch: ")
		text = re.findall("[a-gA-G][0-6]",move)	
	text = text[0]
	
	
	for i in range(7):
		for j in range(7):
			#print(i,j,int("abcdefg".index(text[0].lower())),int(text[1]))
			if i == int("abcdefg".index(text[0].lower())) and j==int(text[1]):
				#print(i,j)
				if board[i][j] != " ":
					if player == "O":
						player = "X"
					else:
						player = "O"	
				else:
					board[i][j] = player
					if player=="O":
						pointsO += 1
						if noNeighbor("O",i,j):
							pointsO -= 5
					else:
						pointsX += 1
						if noNeighbor("X",i,j):
							pointsX -= 5
				
	if player == "O":
		player = "X"
	else:
		player = "O"
	licznik = 0
	for i in range(7):
		for j in range(7):
			if board[i][j] != " ":
				licznik += 1
	if licznik == 49:
		end = True
				
os.system('cls' if os.name == 'nt' else 'clear')
print("Koniec gry")
print("Wynik gracza O: " + str(pointsO))
print("Wynik gracza X: " + str(pointsX))
if pointsO > pointsX:
	print("Wygral gracz O")
elif pointsO < pointsX:
	print("Wygral gracz X")
else:
	print("Remis")

