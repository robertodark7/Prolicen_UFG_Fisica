
from turtle import *
BB = 3                  #selecione a complexidade
V = 10                  #selecione a velocidade do Grafico
tamanho = 400           #selecione o tamanho do Grafico


def snowflake(lengthSide, m):
    if m == 0:
        forward(lengthSide)
        return
    lengthSide /= 3
    snowflake(lengthSide, m-1)
    left(60)
    snowflake(lengthSide, m-1)
    right(120)
    snowflake(lengthSide, m-1)
    left(60)
    snowflake(lengthSide, m-1)


def fullSnowflake(lengthside, m):
    for i in range(3):
        snowflake(lengthside, m)
        right(120)

        
if __name__ == "__main__":     
    speed(V)                               
    length = tamanho
    penup()
    backward(length/8.0)
    pendown()
    color('Blue')
    fullSnowflake(length, BB)             
               
            
