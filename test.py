from libs import pygame_textinput
import pygame
import time
from random import randrange
from foca import Foca
from alga import Alga 
from tubarao import Tubarao
from peixe import Peixe
import random
from tela import Tela
from utils import utils

pygame.init()
pygame.display.set_caption('Ecossistema Aquático')
# Para o TEMPO

clock = pygame.time.Clock()

seres_objetos = []
inputs = [0 for i in range(len(utils.seres))]
textinputs = [pygame_textinput.TextInput("","",35,True,(255,255,0)) for i in range(len(inputs))]

calorias_input = pygame_textinput.TextInput("","",35,True,(255,255,0))
screen = pygame.display.set_mode((utils.w, utils.h))
calorias = 600
    
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
    screen.blit(utils.FONT.render(message, True, utils.TEXT_COLOR), (40,(utils.h/2)))
    screen.blit(calorias_input.get_surface(),(utils.FONT.size(message)[0]+40,(utils.h/2)))
    pygame.display.flip()
    clock.tick(100)

# Lê entradas
for i,textinput in enumerate(textinputs):
    while True:
        events = pygame.event.get()
        Tela.leitura_quit(events)
        if(utils.finalizou):
            exit()

        if(textinput.update(events)):
            inputs[i] = int(textinput.get_text())
            textinput.clear_text()
            break
        screen.fill((0,0,0))
        message = 'Número de %s para a execução da simulação:'%(utils.seres_plural[i])
        
        # Exibe a menssagem na tela
        screen.blit(utils.FONT.render(message, True, utils.TEXT_COLOR), (40,(utils.h/2)))
        # Exibe input logo após a mensagem na tela
        screen.blit(textinput.get_surface(),(utils.FONT.size(message)[0]+40,(utils.h/2)))
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


alga = pygame.transform.scale(alga,(utils.tamanho_sprite,utils.tamanho_sprite))
tubarao = pygame.transform.scale(tubarao,(utils.tamanho_sprite,utils.tamanho_sprite))
peixe = pygame.transform.scale(peixe,(utils.tamanho_sprite,utils.tamanho_sprite))
foca = pygame.transform.scale(foca,(utils.tamanho_sprite,utils.tamanho_sprite))
bola = pygame.transform.scale(bola,(utils.tamanho_sprite,utils.tamanho_sprite))

total_seres = 0
for quantidade_seres in inputs:
    for j in range(quantidade_seres):
        total_seres+=1

if(total_seres > (utils.tamanho_matriz*utils.tamanho_matriz)):
    print("-- Tamanho de seres excede o tamanho do tabuleiro! --")
    exit()

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
            novo_ser = Alga(ids,alga,alga.get_rect(),utils.tamanho_sprite,utils.tamanho_sprite,x,y)
        elif(utils.seres[chave] == 'peixe'):
            novo_ser = Peixe(ids,peixe,peixe.get_rect(),utils.tamanho_sprite,utils.tamanho_sprite,x,y,calorias)
        elif(utils.seres[chave] == 'tubarao'):
            novo_ser = Tubarao(ids,tubarao,tubarao.get_rect(),utils.tamanho_sprite,utils.tamanho_sprite,x,y,calorias)
        elif(utils.seres[chave] == 'foca'):
            novo_ser = Foca(ids,foca,foca.get_rect(),utils.tamanho_sprite,utils.tamanho_sprite,x,y,calorias)
        # novo_ser.exibe(screen)
        utils.coloca_em_posicao_especifica(novo_ser)
        seres_objetos.append(novo_ser)
        
        # Incrementa os IDS para definir qual será o semáforo da tela (último)
        ids+=1
        

start_time = pygame.time.get_ticks()

tela = Tela(ids, screen, start_time)

# Inicialização de threads
for ser in seres_objetos:
    ser.start()
tela.start()

# Fechamento de threads
for ser in seres_objetos:
    ser.join()
tela.join()

# quit()