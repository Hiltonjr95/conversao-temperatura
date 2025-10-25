from conversoes import *


while True:
   
   print("""Escolha uma opção :
        1 - Celcius para Fahrenheit
        2 - Celcius para Kelvin
        3 - Fahrenheit para Celcius
        4 - Fahrenheit para Kelvin 
        5 - Kelvin para Celcius
        6 - Kelvin para Fahrnheit
 """)
 


   #entrada de dados
   opcao = input("Digite uma opção: ")
   #validação caso o usuário digite uma string
   if not opcao.isdigit():
    print("Digite uma opção válida! ")
    continue
   opcao = int(opcao)
    
   #validação caso o usuário não digite um número entre 1 e 6
   if opcao < 1 and opcao > 6:
    print("Digite um número entre 1 e 6! ")
    continue


   if opcao == 1:
    temp_celcius =float(input("Digite a temperatura em Celcius: "))
    temp_fahrenheit = celcius_p_fahrenheit(temp_celcius)

    print(f"A temperatura {temp_celcius} graus Celcius é igual a {temp_fahrenheit} graus Fahrenheit.")
    break

   elif opcao == 2:
    temp_celcius =float(input("Digite a temperatura em Celcius: "))
    temp_kelvin = celcius_p_kelvin(temp_celcius)

    print(f"A temperatura {temp_celcius} graus Celcius é igual a {temp_kelvin} graus Kelvin.")
    break

   elif opcao == 3:
      temp_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
      temp_celcius = fahrenheit_p_celcius(temp_fahrenheit) 
      print(f"A temperatura {temp_fahrenheit} graus Fahrenheit é igual a {temp_celcius} graus Celcius.")
      break
   
   elif opcao == 4:
      temp_fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
      temp_kelvin = fahrenheit_p_kelvin(temp_fahrenheit)
      print(f"A temperatura {temp_fahrenheit} graus Fahrenheit é igual a {temp_kelvin} graus Kelvin.")
      break

   elif opcao == 5:
      temp_kelvin = float(input("Digite a temperatura em Kelvin: "))
      temp_celcius = kelvin_p_celcius(temp_kelvin)
      print(f"A temperatura {temp_kelvin} graus Kelvin é igual a {temp_celcius} graus Celcius.")
      break
   
   elif opcao == 6:
      temp_kelvin = float(input("Digite a temperatura em Kelvin: "))
      temp_fahrenheit = kelvin_p_fahrenheit(temp_kelvin)
      print(f"A temperatura {temp_kelvin} graus Kelvin é igual a {temp_fahrenheit} graus Fahrenheit.")
      break
      

      
