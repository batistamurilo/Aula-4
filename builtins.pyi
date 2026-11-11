# Exercicio 1- positivo, negativo ou zero

numero = int(input("Digite um numero inteiro:" ))
if numero > 0:
    print ("O numero é positivo.")
elif numero <0:
    print("O numero e negativo.")
else:
    print("O numero é 0")
  
# Exercicio 2 : classificação de triângulos
lado1 = float(input( "Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

# Verifica se os lados podem formar um triângulo
# A soma de dois lados deve ser sempre maior que o terceiro lado

if lado1 == lado2 == lado3 == lado1:
        print ("equilatero.")
elif lado1 != lado2 != lado3 !=lado1:  
       print("escaleno.")
else:
       print('isoceles')
        
   
    
    
                   
    
#Exercicio 3: Verifique se o usuário é maior de idade e pode entrar no show
                    
idade = int(input("Digite sua idade: "))

if idade >=18:
    print("Você pode entrar no show")
else:
    print("Você é menor de idade não pode")
    