def is_unlucky_number(n):
    str_n = str(n)

    for i in range(len(str_n) - 1):
        if str_n[i] == "1" and str_n[i + 1] == "3":
            return True
    
    return False

n = int(input().strip())
print(f"{n} es de Mala Suerte" if is_unlucky_number(n) else f"{n} NO es de Mala Suerte")
