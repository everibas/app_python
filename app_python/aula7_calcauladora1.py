# metodo retorna. é uma funcã0
# metodos auxiliam a não re-gerar codigo

class Calculadora:
    # Sempre que instanciar a classe calculadora vai passar
    # pelo metodo init
    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b

if __name__ == '__main__':
#
# print(soma(1,2))
# print(soma(3,4))
# print(subtracao(10,2))
# print(multiplicacao(10,2))
# print(divisao(10,2))

    # Instanciando a classe Calculadora
    calculadora = Calculadora(10,2)
    print(calculadora.valor_a)
    print(calculadora.valor_b)
    print(calculadora.soma())
    print(calculadora.subtracao())
    print(calculadora.multiplicacao())
    print(calculadora.divisao())