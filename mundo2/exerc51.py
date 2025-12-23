n = input('Digite a frase: ').strip().replace(' ','').upper()
m = n[::-1]

flag = 0

for i in range(0,len(n)):
    if n[i] != m[i]:
        flag = 1

if flag == 1:
    print('não é palindromo')

else:
    print('é palindromo')
