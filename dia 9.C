#include<stdio.h>
#include<stdlib.h>
void soma (){
    int num1, num2, resultado;
    
    printf("Digite dois numeros:");

    scanf("%d %d",&num1, &num2);
    
    
    resultado = num1 + num2;
    
    
    printf("O resultado da soma de %d e %d e iqual a %d", num1, num2, resultado);   
}
int main(){
    
    for (int i = 0;  ; i++){
        
    if (i == 51){
        return 0;
        
}
        else {printf("%d\n", i);
    
            
} 

        
    }
}
