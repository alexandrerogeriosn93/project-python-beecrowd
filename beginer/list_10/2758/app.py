from struct import pack, unpack

A, B = map(float, input().split())
C, D = map(float, input().split())

A_bytes = pack("f", A)
B_bytes = pack("f", B)
C_bytes = pack("d", C)
D_bytes = pack("d", D)

A_float = unpack("f", A_bytes)[0]
B_float = unpack("f", B_bytes)[0]
C_double = unpack("d", C_bytes)[0]
D_double = unpack("d", D_bytes)[0]

print("A = %f, B = %f" % (A_float, B_float))
print("C = %lf, D = %lf" % (C_double, D_double))
print("A = %.1f, B = %.1f" % (A_float, B_float))
print("C = %.1lf, D = %.1lf" % (C_double, D_double))
print("A = %.2f, B = %.2f" % (A_float, B_float))
print("C = %.2lf, D = %.2lf" % (C_double, D_double))
print("A = %.3f, B = %.3f" % (A_float, B_float))
print("C = %.3lf, D = %.3lf" % (C_double, D_double))
print("A = %.3E, B = %.3E" % (A_float, B_float))
print("C = %.3E, D = %.3E" % (C_double, D_double))
print("A = %.0f, B = %.0f" % (A_float, B_float))
print("C = %.0lf, D = %.0lf" % (C_double, D_double))
