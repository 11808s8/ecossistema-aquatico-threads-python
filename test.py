import pygame_textinput
import pygame
import time
from random import randrange
from foca import Foca
from alga import Alga 
from tubarao import Tubarao
from peixe import Peixe
import random
# from threading import Semaphore
from tela import Tela
import settings

pygame.init()
pygame.display.set_caption('Ecossistema Aquático')
# semaforo = Semaphore()
# print(settings.mundo)
# Para o TEMPO


clock = pygame.time.Clock()

# @TODO: Colocar um START_TIME para quando o USUÁRIO decidir iniciar o game


seres_objetos = []
inputs = [0 for i in range(len(settings.seres))]
textinputs = [pygame_textinput.TextInput("","",35,True,(255,255,0)) for i in range(len(inputs))]

calorias_input = pygame_textinput.TextInput("","",35,True,(255,255,0))
screen = pygame.display.set_mode((settings.w, settings.h))
calorias = 600
# textinput.update(events)


        
        # Exibe a menssagem na tela
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            quit()
    if(calorias_input.update(events)):
            calorias = int(calorias_input.get_text())
            calorias_input.clear_text()
            break
    screen.fill((0,0,0))
    message = 'Digite quantas calorias você quer por animal na simulação:'
    screen.blit(settings.FONT.render(message, True, settings.TEXT_COLOR), (0,(settings.h/2)))
    screen.blit(calorias_input.get_surface(),(settings.FONT.size(message)[0],(settings.h/2)))
    pygame.display.flip()
    clock.tick(100)
# Lê entradas

for i,textinput in enumerate(textinputs):
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                quit()
        if(textinput.update(events)):
            inputs[i] = int(textinput.get_text())
            textinput.clear_text()
            break
        screen.fill((0,0,0))
        message = 'Digite quantas %s você quer na simulação:'%(settings.seres[i])
        
        # Exibe a menssagem na tela
        screen.blit(settings.FONT.render(message, True, settings.TEXT_COLOR), (0,(settings.h/2)))
        # Exibe input logo após a mensagem na tela
        screen.blit(textinput.get_surface(),(settings.FONT.size(message)[0],(settings.h/2)))
        pygame.display.flip()
        clock.tick(100)


bola = pygame.image.load('bola.png')
alga = pygame.image.load('alga.png')
tubarao = pygame.image.load('tubarao.png')
peixe = pygame.image.load('peixe.png')
foca = pygame.image.load('foca.png')

tamanho_bola = 100
alga = pygame.transform.scale(alga,(tamanho_bola,tamanho_bola))
tubarao = pygame.transform.scale(tubarao,(tamanho_bola,tamanho_bola))
peixe = pygame.transform.scale(peixe,(tamanho_bola,tamanho_bola))
foca = pygame.transform.scale(foca,(tamanho_bola,tamanho_bola))
bola = pygame.transform.scale(bola,(tamanho_bola,tamanho_bola))

total_seres = 0
for quantidade_seres in inputs:
    for j in range(quantidade_seres):
        total_seres+=1

settings.inicializa_semaforos(total_seres)
print(settings.semaforos)
# quit()
# print(seres)
ids=0
finalizou = False
for chave,quantidade_seres in enumerate(inputs):
    print("Qtd animais " + str(quantidade_seres))
    for j in range(quantidade_seres):
        # (x, y) = settings.coloca_em_posicao_aleatoria(ids,settings.seres[chave])
        (x, y) = settings.coloca_em_posicao_aleatoria(None)
        if(settings.seres[chave] == 'alga'):
            novo_ser = Alga(ids,alga,alga.get_rect(),10,20,x,y)
        elif(settings.seres[chave] == 'peixe'):
            novo_ser = Peixe(ids,peixe,peixe.get_rect(),10,20,x,y,calorias)
        elif(settings.seres[chave] == 'tubarao'):
            novo_ser = Tubarao(ids,tubarao,tubarao.get_rect(),10,20,x,y,calorias)
        elif(settings.seres[chave] == 'foca'):
            novo_ser = Foca(ids,foca,foca.get_rect(),10,20,x,y,calorias)
        # novo_ser.exibe(screen)
        settings.coloca_em_posicao_especifica(novo_ser)
        seres_objetos.append(novo_ser)
        ids+=1
# pygame.display.flip()
# input()
# print(settings.mundo)
# quit()

start_time = pygame.time.get_ticks()

tela = Tela(ids, screen, start_time)
print(" ID TELA " + str(ids))
print("Semaforo liberado: " + str((len(settings.semaforos)-1)))
# settings.semaforos[(len(settings.semaforos)-1)].release()
for ser in seres_objetos:
    ser.start()
tela.start()
for ser in seres_objetos:
    ser.join()

tela.join()
quit()

# textinput = pygame_textinput.TextInput("","",35,True,(255,255,0))

# Matrizes de movimentação para UM objeto. Colocar isso em CADA objeto
matriz_x = [tamanho_quadrado*i for i in range(tamanho_matriz)]
matriz_y = [altura_quadrado*i for i in range(tamanho_matriz)]

print(matriz_x)
print(matriz_y)

# while(not verifica_validade_movimento(f,tamanho_matriz,dir))
# f.movimenta(random.choice(direcoes))
# print(v)


print(f)
f.start()
t.start()
f.join()
t.join()
# print(matriz)
# quit()

# quit()

roda = True
x=0
y=0
incrementoX = 0.3
incrementoY = 0.3
i=0
while roda==True:
    
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            roda = False

    if(roda):
        if(bola_rect.x == w-tamanho_bola ):
            incrementoX = -1
        if(bola_rect.y == h-tamanho_bola ):
            incrementoY = -1
        if(bola_rect.x == 0 ):
            incrementoX = 1
        if(bola_rect.y == 0 ):
            incrementoY = 1
        screen.fill((0,0,0))
        r = randrange(tamanho_matriz)
        bola_rect.x = matriz_x[r]
        # print(r)
        r = randrange(tamanho_matriz)
        bola_rect.y = matriz_y[r]
        # print(r)
        # i+=1
        # if(i==tamanho_matriz):
        #     i=0
        # print(matriz[])
        # bola_rect.y += incrementoY
        
        time_since_enter = (pygame.time.get_ticks() - start_time)/1000
        message = 'Tempo transcorrido: ' + '%i'%(time_since_enter)
        screen.blit(FONT.render(message, True, TEXT_COLOR), (0, 0))
        
        # textinput.update(events)
        screen.blit(textinput.get_surface(),(200,200))
        
        # if(textinput.update(events)):
        #     print(textinput.get_text())
        #     textinput.clear_text()
        f.exibe(screen)

        # pygame.display.flip()
        
        pygame.display.flip()
        clock.tick(100)
        # time.sleep(1)
