messages = {
	1: "Intervalo [0,25]",
	2: "Intervalo (25,50]",
	3: "Intervalo (50,75]",
	4: "Intervalo (75,100]",
	5: "Fora de intervalo"
}

n = float(input())

if 0.00 <= n <= 25.00:
	cod_message = 1
elif 25.00 < n <= 50.00:
	cod_message = 2
elif 50.00 < n <= 75.00:
	cod_message = 3
elif 75.00 < n <= 100.00:
	cod_message = 4
else:
	cod_message = 5

print(messages[cod_message])
