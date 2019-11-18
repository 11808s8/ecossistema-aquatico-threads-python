from libs import pygame_textinput
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
from utils import utils

pygame.init()
pygame.display.set_caption('Ecossistema Aquático')
# semaforo = Semaphore()
# print(utils.mundo)
# Para o TEMPO


clock = pygame.time.Clock()

# @TODO: Colocar um START_TIME para quando o USUÁRIO decidir iniciar o game


seres_objetos = []
inputs = [0 for i in range(len(utils.seres))]
textinputs = [pygame_textinput.TextInput("","",35,True,(255,255,0)) for i in range(len(inputs))]

calorias_input = pygame_textinput.TextInput("","",35,True,(255,255,0))
screen = pygame.display.set_mode((utils.w, utils.h))
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
    screen.blit(utils.FONT.render(message, True, utils.TEXT_COLOR), (0,(utils.h/2)))
    screen.blit(calorias_input.get_surface(),(utils.FONT.size(message)[0],(utils.h/2)))
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
        message = 'Digite quantas %s você quer na simulação:'%(utils.seres[i])
        
        # Exibe a menssagem na tela
        screen.blit(utils.FONT.render(message, True, utils.TEXT_COLOR), (0,(utils.h/2)))
        # Exibe input logo após a mensagem na tela
        screen.blit(textinput.get_surface(),(utils.FONT.size(message)[0],(utils.h/2)))
        pygame.display.flip()
        clock.tick(100)


bola = utils.carrega_sprite('bola.png')
alga = utils.carrega_sprite('alga.png')
tubarao = utils.carrega_sprite('tubarao.png')
# peixe = utils.carrega_sprite('peixe.png')
foca = utils.carrega_sprite('foca.png')
# bola = utils.carrega_sprite('peixe_32_32.png')
# alga = utils.carrega_sprite('peixe_32_32.png')
# tubarao = utils.carrega_sprite('peixe_32_32.png')
peixe = utils.carrega_sprite('peixe_32_32.png')
# foca = utils.carrega_sprite('peixe_32_32.png')

tamanho_sprite = 100
alga = pygame.transform.scale(alga,(tamanho_sprite,tamanho_sprite))
tubarao = pygame.transform.scale(tubarao,(tamanho_sprite,tamanho_sprite))
peixe = pygame.transform.scale(peixe,(tamanho_sprite,tamanho_sprite))
foca = pygame.transform.scale(foca,(tamanho_sprite,tamanho_sprite))
bola = pygame.transform.scale(bola,(tamanho_sprite,tamanho_sprite))

total_seres = 0
for quantidade_seres in inputs:
    for j in range(quantidade_seres):
        total_seres+=1

utils.inicializa_semaforos(total_seres)
print(utils.semaforos)
# quit()
# print(seres)
ids=0
finalizou = False
for chave,quantidade_seres in enumerate(inputs):
    print("Qtd animais " + str(quantidade_seres))
    for j in range(quantidade_seres):
        # (x, y) = utils.coloca_em_posicao_aleatoria(ids,utils.seres[chave])
        (x, y) = utils.coloca_em_posicao_aleatoria(None)
        if(utils.seres[chave] == 'alga'):
            novo_ser = Alga(ids,alga,alga.get_rect(),10,20,x,y)
        elif(utils.seres[chave] == 'peixe'):
            novo_ser = Peixe(ids,peixe,peixe.get_rect(),10,20,x,y,calorias)
        elif(utils.seres[chave] == 'tubarao'):
            novo_ser = Tubarao(ids,tubarao,tubarao.get_rect(),10,20,x,y,calorias)
        elif(utils.seres[chave] == 'foca'):
            novo_ser = Foca(ids,foca,foca.get_rect(),10,20,x,y,calorias)
        # novo_ser.exibe(screen)
        utils.coloca_em_posicao_especifica(novo_ser)
        seres_objetos.append(novo_ser)
        ids+=1
# pygame.display.flip()
# input()
# print(utils.mundo)
# quit()

start_time = pygame.time.get_ticks()

tela = Tela(ids, screen, start_time)
print(" ID TELA " + str(ids))
print("Semaforo liberado: " + str((len(utils.semaforos)-1)))
# utils.semaforos[(len(utils.semaforos)-1)].release()
for ser in seres_objetos:
    ser.start()
print(seres_objetos)
tela.start()
for ser in seres_objetos:
    ser.join()

tela.join()
quit()