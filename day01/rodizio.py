# Programa para Informar o Dia de Rodízio da Placa
# Autor: Raphael Patricio Pereira
# Data: 29/12/2025

# exibe informações na Tela Boas vindas rsrs
print ("Ola Seja bem vindo Vou informar o dia de rodizio de seu veiculo")
print ("Por favor Digite a Sua Placa")

# entrada da variável placa (tipo string)
placa = input("Digite sua placa:")

# aqui digito recebe placa o ultimo digito da string ex :[-1]
digito = placa[-1]

# Aqui valida a condição se o digito nao for numero armazendo para no if 
if not digito.isdigit():
        print ("placa invalida")

#codiçao para conveter o digito em  varivel inteiro dia e criar e validar a semana com respectivo numero 
else :
        dia = int(digito) 
        semana = ""
        if dia == 1 or dia == 2: #  PODE USAR   EX:(if dia in (1, 2):) CODIGO FICA MAIS LIMPO 
         semana = ("segunda-feira")
        elif dia == 3 or dia == 4:
         semana = ("terca-feira")
        elif dia == 5 or dia == 6 :
         semana = ("quarta-feira")
        elif dia == 7 or dia == 8:
         semana = ("quinta feira")
        elif dia == 9 or dia == 0 :
         semana = ("sexta feira") 
# exibe msg na tela e informa o dia da semana 
        print ("Aqui esta seu dia de rodizio")
        print ( "O seu dia da semana de rodizio é", semana)


