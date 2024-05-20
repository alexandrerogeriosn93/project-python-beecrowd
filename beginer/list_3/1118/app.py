sum_notes, counter = 0, 0
continue_loop = True

while continue_loop:
    note = float(input())

    if note >= 0 and note <= 10:
        sum_notes += note
        counter += 1

        if counter == 2:
            print(f"media = {(sum_notes/2):.2f}")
            sum_notes, counter = 0, 0

            while True:
                print("novo calculo (1-sim 2-nao)")
                new_count = int(input())
                if new_count == 2:
                    continue_loop = False
                    break
                elif new_count == 1:
                    continue_loop = True
                    break
    else:
        print("nota invalida")
