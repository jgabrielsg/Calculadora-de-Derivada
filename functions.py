import sympy as sym

def trigonometria():
    while True:
        print("[1] seno")
        print("[2] cosseno")
        print("[3] tangente")
        
        try:
            inp = input("Qual função quer usar? ")
            inp = int(inp)
            print("Tipo 2x + 1 digite '2*x + 1'.\n")
            if inp == 1:
                dentro_seno = input("Digite o que quiser dentro do seno: ")
                print(sym.diff(dentro_seno))
                print(sym.diff(sym.sin(dentro_seno)))
                break
            elif inp == 2:
                dentro_cosseno = input("Digite o que quiser dentro do cosseno: ")
                print(sym.diff(dentro_cosseno))
                print(sym.diff(sym.cos(dentro_cosseno)))
                break
            elif inp == 3:
                dentro_tangente = input("Digite o que quiser dentro da tangente: ")
                print(sym.diff(dentro_tangente))
                print(sym.diff(sym.sin(dentro_tangente)))
                break
            else:
                print("Você não digitou um número que vale")
        except:
            print("Você não digitou algo que vale")

def polinomio():
    while True:
        
        print("Digite seu polinômio: ")
        print("Tipo 2x + 1 digite '2*x + 1'.\nE 2x^3 + 2 digite '2*x**3 + 2'.")
        
        try:
            polinom = input("Escreva-o: ")
            print(sym.diff(polinom))
            break
        except:
            print("Você não digitou algo que vale")


def exponencial():
    while True:
        
        print("Digite seu exponencial: ")
        print("Tipo 2^x digite '2**x'.\n")
        
        try:
            expo = input("Escreva-o: ")
            print(sym.diff(expo))
            break
        except:
            print("Você não digitou algo que vale")

def logaritimo():
    while True:
        
        print("[1] Logarítimo")
        print("[2] Logarítimo Natural")
        
        try:
            inp = input("Qual função quer usar? ")
            inp = int(inp)
            print("Tipo 2x + 1 digite '2*x + 1'.\n")
            
            if inp == 1:
                base = input("Qual a base do seu log? ")
                fator = input("Qual seu fator dentro do log? ")
                print(sym.diff(sym.log(fator, base)))
                break
            
            elif inp == 2:
                fatorln = input("Digite o que quiser dentro do logaritimo natural?: ")
                print(sym.diff(sym.ln(fatorln)))
                break
            
            else:
                print("Você não digitou um número que vale")
        except:
            print("Você não digitou algo que vale")
