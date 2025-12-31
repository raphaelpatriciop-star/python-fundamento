# Programa para Infomar o Dia de Rodizio da placa
# Autor: Raphael Patricio Pereira
# Data: 29/12/2025

print ("Ola Seja bem vindo Vou informar o dia de rodizio de seu veiculo")
print ("Por favor Digite a Sua Placa")
placa = input("Digite sua placa:")

digito = placa[-1]
if not digito.isdigit():
        print ("placa invalida")
else :
        dia = int(digito) 
        semana = ""
        if dia == 1 or dia == 2:
         semana = ("segunda-feira")
        elif dia == 3 or dia == 4:
         semana = ("terca-feira")
        elif dia == 5 or dia == 6 :
         semana = ("quarta-feira")
        elif dia == 7 or dia == 8:
         semana = ("quinta feira")
        elif dia == 9 or dia == 0 :
         semana = ("sexta feira") 

        print ("Aqui esta seu dia de rodizio")
        print ( "O seu dia da semana de rodizio é", semana)

