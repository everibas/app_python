a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor: '))
print(type(a))
soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
#print('soma: ' + str(soma))
resultado = 'Soma: {soma}. ' \
            '\nsubtracao: {subtracao}. ' \
            '\nmultipicacao: {multiplicacao}.' \
            '\nDivisão: {divisao}.' \
            '\nResto: {resto}.'.format(soma=soma,
                                    subtracao=subtracao,
                                    multiplicacao=multiplicacao,
                                    divisao=divisao,
                                    resto=resto)
print(resultado)

x = '1'
# #print type(x)
# soma2 = int(x) + 1
# print(soma2)