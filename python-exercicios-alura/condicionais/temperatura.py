# Lucas trabalha em TI e precisa garantir que a temperatura de uma sala de servidores não ultrapasse 25°C. Ele quer um programa que receba a temperatura atual como entrada e, se necessário, exiba uma mensagem de alerta.

temperatura = int(input("Informe o valor da temperatura atual (°C) -->"))

if (temperatura > 25):
    print("ALERTA: A temperatura está acima do limite permitido (25 °C)")