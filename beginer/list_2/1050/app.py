code = int(input())
ddds = {
    11: "Sao Paulo",
    19: "Campinas",
    21: "Rio de Janeiro",
    27: "Vitoria",
    31: "Belo Horizonte",
    32: "Juiz de Fora",
    61: "Brasilia",
    71: "Salvador",
}

print(ddds[code] if code in ddds else "DDD nao cadastrado")
