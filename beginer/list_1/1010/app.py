cod_1, qty_1, value_1 = map(str, input().split())
cod_2, qty_2, value_2 = map(str, input().split())

cod_1, qty_1, value_1 = int(cod_1), int(qty_1), float(value_1)
cod_2, qty_2, value_2 = int(cod_2), int(qty_2), float(value_2)

total = qty_1 * value_1 + qty_2 * value_2

print(f"VALOR A PAGAR: R$ {total:.2f}")
