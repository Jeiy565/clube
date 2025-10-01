def triangulo ():
    base = int(input("digite o valor da base"))
    altura = int(input("digite o valor da altura"))
    return (base*altura/2)
def quadrado ():
    lado = input("digite o valor do lado do quadrado:")
    resultado = lado**2
    return resultado
def retangulo ():
    base = int(input('digite o valor de base'))    
    altura = int(input('digite o valor da altura:'))
    resultado = base*altura
    return resultado
def trapezio ():
    baseMa = int(input("digite o valor da base"))
    baseME = int(input("digite o valor da base")) 
    altura = int(input("digite o valor da altura"))
    resultado = (baseMa + baseMe)*altura/2
    return resultado
def circulo ():
    pi = 3.14
    raio = int(input('digite o valor do raio'))
    resultado = pi*(raio**2)
    resultado = int(resultado)
    return resultado
def menu():    
    escolha = input('''qual area vc quer calcular?
        t - triangulo
        q - quadrado
        r - retangulo
        c - circulo
        tr - trapezio
        escolha: ''')
    
    if escolha == 'q':
        area = quadrado()
    
    elif escolha == 't':
        area = triangulo()
    elif escolha == 'r':
        area = retangulo()
    elif escolha == 'tr':
        area = trapezio
    elif escolha == 'c':
        area = circulo
        
    print (f"A area e de {area}")
    
    escolha = input('quer calcular a area de novo?)(s/n)').lowwer()    
    if escolha[0] == 's':
        menu()    

    
menu()   
