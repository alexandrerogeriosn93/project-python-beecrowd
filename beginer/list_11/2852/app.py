from string import ascii_lowercase

vet_letters = ascii_lowercase
vet_vowels = "aeiou"

k = input()
n = int(input())

for c in range(n):
    message = input().split()
    
    vet_encrypt = []
    i = 0
    
    for word in message:
        if word[0] in vet_vowels:
            vet_encrypt.append(word)
        else:
            word_encrypted = ""
            
            for letter in word:
                expression = vet_letters[(vet_letters.index(k[i % len(k)]) + vet_letters.index(letter)) % 26]
                word_encrypted += expression
                i += 1
            
            vet_encrypt.append(word_encrypted)
    
    print(" ".join(vet_encrypt))
