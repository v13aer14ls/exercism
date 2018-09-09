#Crie um programa que solicite o ano de nascimento do usuário (com 4 dígitos) e calcule sua idade (tem que converter o ano para inteiro antes de calcular). Imprima a frase: "Você tem X anos.", onde "X" é a idade calculada.
from datetime import datetime, date

print("INforme sua data de nascimento (dd mm yyyy)")
data_de_nascimento = datetime.strptime(input("--->"), "%d %m %Y")

def calcular_idade(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

idade = calcular_idade(data_de_nascimento)

print("Você tem %s anos." % idade )
