#Crie um programa que solicite ao usuário que informe o valor do salário mínimo (converta para float) e armazene em uma variável chamada salario_minimo, em seguida solicite ao usuário quantos salários ele gostaria de ganhar (converta para float) e armazene em uma variável chamada pretensao. Imprima o valor do salário desejado pelo usuário desta forma:
#"Você pretende ganhar R$ x", onde x é o valor do salário multiplicado pela quantidade de salários pretendidos.

salario_minimo = float(input("Informe o valor do salario minimo: "))
pretensao = float(input("Informe quantos salarios você deseja : "))
valor = salario_minimo * pretensao

print("Você pretende ganhar R$ %s" % valor)
