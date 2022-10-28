from functions import *

print("######################")
print("Qual a data de vencimento?")
print("######################\n")

data_input = input("")
if len(data_input) == 10:
    print(verify_due(data_input))
else:
    print("Entrada inválida!")