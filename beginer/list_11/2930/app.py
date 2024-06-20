e, d = map(int, input().split())

if e > d:
    print("Eu odeio a professora!")
elif e < d - 2:
    print("Muito bem! Apresenta antes do Natal!")
else:
    print("Parece o trabalho do meu filho!")
    print("Fail! Entao eh nataaaaal!" if e > 21 else "TCC Apresentado!")
