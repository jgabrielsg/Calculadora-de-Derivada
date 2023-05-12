import sympy as sym
from functions import *

x = sym.Symbol('x')
# print(sym.diff(x**5))

print('Bem vindo a calculadora de derivada 2000')
print('Cláudio = FLOP\n')

while True:
    
    print("[1] Trigonométricas")
    print("[2] Polinômios")
    print("[3] Exponenciais")
    print("[4] Logaritima")
    print("[5] Fechar")
    
    try:
        inp = input('Digite o quer fazer: ')
        inp = int(inp)
        if inp == 1:
            trigonometria()
        elif inp == 2:
            polinomio()
        elif inp == 3:
            exponencial()
        elif inp == 4:
            logaritimo()
        elif inp == 5:
            print("Adeus.")
            break
        else:
            print("Você não digitou um número que vale")
    except:
        print("Você não digitou um número")
