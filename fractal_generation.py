import turtle

'''
    Author: Jovani Brasil
    Email: jovanibrasil@gmail.com

'''


def thuemorse(iterations):
    '''
        Gerando a sequencia de Thue-Morse.

        @param  iterations  - numero de iteracoes
        @return result      - resultado final
    '''

    result = '1'
    
    for i in range(0, iterations-1):
        result += ''.join(['0' if c is '1' else '1' for c in result])

    return result


jovani = turtle.Turtle()

turtle.screensize(1240, 720)

jovani.hideturtle()
jovani.penup()
jovani.goto(150, 200)
jovani.pendown()

i = 0
for e in thuemorse(12):
    if e is '1':
        #step
        jovani.fd(4)
    else:
        #rotate
        jovani.left(60)
    i=i+1

print(i, " commands.")


ts = turtle.getscreen()

ts.getcanvas().postscript(file="duck.eps")