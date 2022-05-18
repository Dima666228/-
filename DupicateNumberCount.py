A = int(input('Введіть ціле число A:'))
B = int(input('Введіть ціле число B:'))
C = int(input('Введіть ціле число С:'))


if A == B and B == C:
    print('3')
elif A == B or B == C or A == C:
    print('2')
else:
    print('0')