#mantainer = Guilherme
# Pyhton 3.x

def bissexto(ano):
	return (ano % 4 == 0 and (ano % 400  == 0 or ano % 100 !=0))

if __name__ == '__main__':
	if bissexto(int(input('Insira o ano a ser consultado : '))):
		print ("O ano é BISSEXTO")
	else:
		print ("O ano não é BISSEXTO ")
