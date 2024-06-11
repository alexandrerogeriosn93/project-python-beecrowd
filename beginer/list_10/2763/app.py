import re

cpf = re.split("[\\.-]", input().strip())

for info in cpf:
    print(info)
