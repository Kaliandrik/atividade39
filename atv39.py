# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. 
# Em seguida, calcule a média anual das temperaturas e mostre a média calculada 
# juntamente com todas as temperaturas acima da média anual, e em que mês elas ocorreram 
# (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . )."

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
temperaturadosmeses = []
for i in meses:
    temperatura = float(input(f"Digite a temperatura de {i}: "))
    temperaturadosmeses.append(temperatura)
mediaanual = sum(temperaturadosmeses)/len(temperaturadosmeses)
print(f"A média anual das temperaturas é: {mediaanual}°")


print("Temperaturas que passaram da média anual:")
for i, temperatura in enumerate(temperaturadosmeses):
    if temperatura > mediaanual:
        print(f"{i + 1} – {meses[i]}: {temperatura}°")

    