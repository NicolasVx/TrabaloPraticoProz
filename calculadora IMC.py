altura = float (input ("Informe o valor da sua altura: "))  
peso = float (input ("Infome o seu peso: "))

imc = peso/(altura*altura)

print("Seu IMC é: ", imc)

if imc < 18.5:
     print("Abaixo do peso!")
elif imc < 24.9:
     print("Peso normal!")
elif imc < 29.9:
     print("Sobrepeso!")
else:
     print("Obeso!")
    

#if imc < 18.5:
#        print("Abaixo do peso!")
#else:
#    if imc < 24.9:
#        print("Peso normal!")
#    else:
#        if imc < 29.9:
#            print("Sobrepeso!")
#        else:
#            print("Obeso!")