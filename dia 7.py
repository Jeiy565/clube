
print('bem-vindo ao anti-para casa')
print('aqui você podera fazer a formula de bhaskara sem suar')
    
def delta (a, b, c):
    resultado1 = pow(b,2) - (4 * a * c)
    return resultado1
            
val_a = int(input('digite o valor de a: '))
val_b = int(input('digite o valor de b: '))
val_c = int(input('digite o valor de c: '))
    
d = delta(val_a, val_b, val_c)
    
print ('seu delta e igual a : ')
print (d)
        
def x1 (a, b, c):
    resultado2 = (-val_b - d) / 2 * val_a
    return resultado2
    
    
def x2 (a, b, c):
    resultado2 = (-val_b + d) / 2 * val_a
    return resultado2
            
result1 = x1(val_a, val_b, val_c)
result2 = x2(val_a, val_b, val_c)
        
print ('acabou as continhas, viu só, você nem cansou')
print (result1, result2)
        
            
