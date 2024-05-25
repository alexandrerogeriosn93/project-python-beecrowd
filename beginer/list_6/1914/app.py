qt = int(input())

for i in range(qt):
    player_1, choice_1, player_2, choice_2 = input().split()
    n, m = map(int, input().split())
    sum_numbers = n + m

    if sum_numbers % 2 == 0 and choice_1 == "PAR":
        print(player_1)
    elif sum_numbers % 2 != 0 and choice_1 == "IMPAR":
        print(player_1)
    else:
        print(player_2)
