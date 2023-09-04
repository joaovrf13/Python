salario = float(input('Qual é o salario do funcionario? R$'))
novo = salario + (salario * 15 / 100)

print('O funcionario que recebia R${}, passa a receber R${} com o aumento de 15% '.format(salario,novo))