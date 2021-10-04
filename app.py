print('\n calculo das notas \n')

notas = [0, 0]

notas[0] = int(input('n1: '))
notas[1] = int(input('n2: '))

med = (notas[0]+notas[1])/2

print(med)

print(notas[0] + notas[1])

if(med <= 6):
    print('vagabundo')

else:
    print('brabo, apenas.')
