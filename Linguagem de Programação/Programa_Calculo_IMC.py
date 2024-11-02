
print()
print("Iniciando programa calculo de IMC - MFAJr")
print()

calcular_imc = lambda peso, altura: peso / (altura * altura)

peso = float(input("Informe seu peso (kg):").replace(",", "."))
while peso < 1:
  peso = float(input("\"Peso\" não pode ser menor que 1,00. Informe seu peso novamente:").replace(",", "."))

altura = float(input("Informe sua altura (m):").replace(",", "."))
while altura < 1:
  altura = float(input("\"altura\" não pode ser menor que 1,00. Informe sua altura novamente:").replace(",", "."))

imc =calcular_imc(peso, altura)

if imc < 18.5:
  descricao_imc = "Baixo peso"
elif imc>=18.5 and imc<25:
  descricao_imc = "Peso normal"
elif imc>=25 and imc<30:
  descricao_imc = "Sobrepeso"
elif imc>=30 and imc<35:
  descricao_imc = "Obesidade grau I"
elif imc>=35 and imc<40:
  descricao_imc = "Obesidade grau II"
else:
  descricao_imc = "Obesidade grau III"

imc = str(round(imc,2)).replace(".",",")

print()
print(f"Seu IMC é {imc} - {descricao_imc}")
print()
print("##############################################")
print("##     Tabela IMC (kg/m²) Classificação     ##")
print("##############################################")
print("## Menor que 18,5 Baixo peso                ##")
print("## De 18,5 a 24,9 Peso normal               ##")
print("## De 25 a 29,9 Sobrepeso                   ##")
print("## De 30 a 34,9 Obesidade grau I            ##")
print("## De 35 a 39.9 Obesidade grau II           ##")
print("## Igual ou maior que 40 Obesidade grau III ##")
print("##############################################")