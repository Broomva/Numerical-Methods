__author__ = 'Didi'

# from sympy import *
import pygame
import time


def main():
    pygame.init()
    pantalla = pygame.display.set_mode([800, 600])
    pygame.display.set_caption("Riemman Game")
    salir = False
    clk = pygame.time.Clock()
    # Colores
    white = (255, 255, 255)
    red = (200, 0, 0)
    blue = (0, 0, 200)
    black = (0, 0, 0)

    #   x, y, z = symbols("x,y,z")

    recty = 30
    r1 = pygame.Rect(375, 0, 20, recty)
    r2 = pygame.Rect(355, 0, 20, recty)
    rectwin = pygame.Rect(100, 200, 600, 400)
    i = 30

    # Textos
    font = pygame.font.Font(None, 30)
    fontlow = pygame.font.Font(None, 20)
    Inicio = font.render("Bienvenido", 1, (1, 30, 20))
    JR = font.render("Juego de Riemman", 1, (1, 30, 20))
    Inst1 = font.render("Instrucciones:", 1, (1, 30, 20))
    Inst2 = fontlow.render("Elija la solucion a la integral", 1, (1, 30, 20))
    Inst3 = fontlow.render("que se muestra en pantalla", 1, (1, 30, 20))
    WinInst1 = fontlow.render("Ganara cuando el recuadro azul", 1, (1, 30, 20))
    WinInst2 = fontlow.render("llegue al final de la pantalla", 1, (1, 30, 20))
    WinText1 = font.render("", 1, (1, 30, 20))
    WinText2 = font.render("", 1, (1, 30, 20))
    Resd = font.render("Flecha Derecha", 1, (1, 30, 20))
    Resi = font.render("Flecha Izquierda", 1, (1, 30, 20))
    clear = font.render("", 1, (1, 30, 20))

    # Texto Res Int
    Resd1 = font.render("F(x)=x/2 + 1", 1, (1, 30, 20))
    Resi1 = font.render("F(x)=x^2/2 + x", 1, (1, 30, 20))

    # Integrales
    #  I1 = x + 1
    #  I2 = x ** 2 + 5
    #  I3 = log(x)
    #  I4 = x ** 3 + 5 * x ** 2 + x * 2

    # Solucion Integrales
    #  sI1 = integrate(I1)
    #  sI2 = integrate(I2)
    #  sI3 = integrate(I3)
    #  sI4 = integrate(I4)

    # Texto Integrales

    int1 = font.render("F(x)=x+1", 1, (1, 30, 20))
    int2 = font.render("F(x)=x^2+5", 1, (1, 30, 20))
    int3 = font.render("F(x)=ln(x)", 1, (1, 30, 20))
    int4 = font.render("F(x)=x^3+6*x^2+2*x", 1, (1, 30, 20))

    solgood = 0
    solbad = 0

    while not salir:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    salir = True

        clk.tick(20)
        pantalla.fill(white)
        pygame.draw.rect(pantalla, blue, r1)
        pygame.draw.rect(pantalla, red, r2)


        s = 0

        # Pregunta 1
        pantalla.blit(int1, (600, 20))
        pantalla.blit(Resd1, (500, 480))
        pantalla.blit(Resi1, (10, 480))
        pantalla.blit(Resi, (10, 450))
        pantalla.blit(Resd, (500, 450))
        pantalla.blit(WinText1, (400,300))
        pantalla.blit(WinText2, (400,350))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                solgood +=1
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                solbad = 1
        if solgood == 1:
            r1.inflate_ip(0, 250)
            solgood += 1
            i = 150
            int1 = font.render("F(x)=x^2+5", 1, (1, 30, 20))
            Resd1 = font.render("F(x)=x*3/3 + 5*x", 1, (1, 30, 20))
            Resi1 = font.render("F(x)=x/2 + x", 1, (1, 30, 20))
            pantalla.blit(int1, (600, 20))
            pantalla.blit(Resd1, (500, 480))
            pantalla.blit(Resi1, (10, 480))
            pantalla.blit(Resi, (10, 450))
            pantalla.blit(Resd, (500, 450))
        if solbad == 1:
            solbad = 0


        # Pregunta 2

        if solgood == 2:

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    solbad = 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    solgood += 1
            if solgood == 3:
                r1.inflate_ip(0, 250)
                solgood += 1
                i = 300
                int1 = font.render("F(x)=1/x", 1, (1, 30, 20))
                Resd1 = font.render("F(x)=log(x)", 1, (1, 30, 20))
                Resi1 = font.render("F(x)=x(log(x)-1)", 1, (1, 30, 20))
                Resd = font.render("Flecha Arriba", 1, (1, 30, 20))
                Resi = font.render("Flecha Abajo", 1, (1, 30, 20))
                pantalla.blit(int1, (600, 20))
                pantalla.blit(Resd1, (500, 480))
                pantalla.blit(Resi1, (10, 480))
                pantalla.blit(Resi, (10, 450))
                pantalla.blit(Resd, (500, 450))
            if solbad == 1:
                solbad = 0


        # Pregunta 3

        if solgood == 4:

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    solbad = 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    solgood += 1
            if solgood == 5:
                r1.inflate_ip(0, 250)
                solgood +=1
                i = 300
                int1 = font.render("F(x)=x^3+6*x^2+2*x", 1, (1, 30, 20))
                Resd1 = font.render("F(x)=x^4/4 + 3x^3 + x^2", 1, (1, 30, 20))
                Resi1 = font.render("F(x)=4x^4 + 3x^3 + 2*x^2", 1, (1, 30, 20))
                Resd = font.render("Flecha Abajo", 1, (1, 30, 20))
                Resi = font.render("Flecha Arriba", 1, (1, 30, 20))
                pantalla.blit(int1, (600, 20))
                pantalla.blit(Resd1, (500, 480))
                pantalla.blit(Resi1, (10, 480))
                pantalla.blit(Resi, (10, 450))
                pantalla.blit(Resd, (500, 450))
            if solbad == 1:
                solbad = 0

        # Pregunta 4

        if solgood == 6:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    solbad = 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    solgood += 1
            if solgood == 7:
                r1.inflate_ip(0, 400)
                WinText1 = font.render("Has Ganadado!", 1, (1, 30, 20))
                WinText2 = font.render("Funciones Evaluadas", 1, (1, 30, 20))
                pantalla.blit(WinText1, (400,300))
                pantalla.blit(WinText2, (400,350))

                int1 = font.render("F(x)=(2*x + x)^1/2 desde 0 hasta 1", 1, (1, 30, 20))
                Resd1 = font.render("F(x)= 1.50", 1, (1, 30, 20))
                Resi1 = font.render("F(x)=2/(3)^1/2", 1, (1, 30, 20))
                Resd = font.render("Tecla a", 1, (1, 30, 20))
                Resi = font.render("Tecla d", 1, (1, 30, 20))
                pantalla.blit(int1, (600, 20))
                pantalla.blit(Resd1, (500, 480))
                pantalla.blit(Resi1, (10, 480))
                pantalla.blit(Resi, (10, 450))
                pantalla.blit(Resd, (500, 450))
                solgood += 1


            if solbad == 1:
                solbad = 0

        if solgood == 8:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    solbad = 1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    solgood += 1
                    pygame.draw.rect(pantalla, red, r2)
            if solgood == 9:
                r2.inflate_ip(0, 150)
                solgood+=1
            if solbad == 1:
                solbad = 0

        pantalla.blit(Inicio, (10, 10))
        pantalla.blit(JR, (10, 30))
        pantalla.blit(Inst1, (10, 60))
        pantalla.blit(Inst2, (10, 90))
        pantalla.blit(Inst3, (10, 110))
        pantalla.blit(WinInst1, (10, 140))
        pantalla.blit(WinInst2, (10, 160))
        pygame.display.update()

    pygame.quit()


main()
