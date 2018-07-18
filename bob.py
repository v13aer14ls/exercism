# Python 3.x
# Mantainer = Guilherme Amaral

speech = input("Say something to Bob : ")

if speech.strip()== "":
	print ("Fine. Be that way!")
elif speech.endswith("?") and speech.isupper():
	print ("Calm down, I know what I'm doing!")
elif speech.isupper():
	print ("Woah, chill out!")
elif speech.endswith("?"):
	print ("Sure.")
else:
	print ("Whatever.")
