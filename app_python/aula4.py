for num in range(101):
    div = 0
    for x in range(1,num+1):
        resto = num % x
       # print(num,resto)
        if resto == 0:
            div = div + 1

    if div == 2:
        print(num)
    # else:
    #     print('Numero {} não é primo'.format(num))

# # Numeros primos
# a = int(input('Entre com o numero'))
#
# div = 0
# for x in range(1,a+1):
#     resto = a % x
#     print(a,resto)
#     if resto == 0:
#         div = div + 1
#
# if div == 2
#     print('Numero {} é primo'.format(a))
# else:
#     print('Numero {} não é primo'.format(a))