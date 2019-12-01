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

# Quantidades de seres na tela
inputs = [0 for i in range(len(utils.seres))]

# Text Inputs
textinputs = [pygame_textinput.TextInput("","",35,True,(255,255,0)) for i in range(len(inputs))]
calorias_input = pygame_textinput.TextInput("","",35,True,(255,255,0))
calorias_perde_input = pygame_textinput.TextInput("","",35,True,(255,255,0))
tempo_perder_calorias_input = pygame_textinput.TextInput("","",35,True,(255,255,0))
tamanho_mapa_quadrados_input = pygame_textinput.TextInput("","",35,True,(255,255,0))


screen = pygame.display.set_mode((utils.w, utils.h))


calorias = utils.single_input_int_com_mensagem(screen,clock,calorias_input, 'Digite quantas calorias você quer por animal na simulação:')
calorias_perde = utils.single_input_int_com_mensagem(screen,clock,calorias_perde_input, 'Digite quantas calorias animal perde/ganha:')
tempo_perder_calorias = utils.single_input_int_com_mensagem(screen,clock,tempo_perder_calorias_input, 'De quantos em quantos segundos perde caloria:')
tamanho_matriz = utils.single_input_int_com_mensagem(screen,clock,tamanho_mapa_quadrados_input, 'Quadrados por linha (tamanho col == linha):')
utils.inicializa_mundo(tamanho_matriz)

#Lê os bicho
for i,textinput in enumerate(textinputs):
    inputs[i] = utils.single_input_int_com_mensagem(screen,clock,textinput, 'Número de %s para a execução da simulação:'%(utils.seres_plural[i]))


alga = utils.carrega_sprite('alga_32_32-1.png')
tubarao = utils.carrega_sprite('tubarao_32_32.png')
foca = utils.carrega_sprite('foca_32_32.png')
peixe = utils.carrega_sprite('peixe_32_32.png')


alga = pygame.transform.scale(alga,(utils.tamanho_sprite,utils.tamanho_sprite))
tubarao = pygame.transform.scale(tubarao,(utils.tamanho_sprite,utils.tamanho_sprite))
peixe = pygame.transform.scale(peixe,(utils.tamanho_sprite,utils.tamanho_sprite))
foca = pygame.transform.scale(foca,(utils.tamanho_sprite,utils.tamanho_sprite))


total_seres = 0
for quantidade_seres in inputs:
    for j in range(quantidade_seres):
        total_seres+=1

if(total_seres > (utils.tamanho_matriz*utils.tamanho_matriz)):
    print("-- Tamanho de seres excede o tamanho do tabuleiro! --")
    exit()

utils.inicializa_semaforos(total_seres)

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
            novo_ser = Peixe(ids,peixe,peixe.get_rect(),utils.tamanho_sprite,utils.tamanho_sprite,x,y,calorias,calorias_perde)
        elif(utils.seres[chave] == 'tubarao'):
            novo_ser = Tubarao(ids,tubarao,tubarao.get_rect(),utils.tamanho_sprite,utils.tamanho_sprite,x,y,calorias,calorias_perde)
        elif(utils.seres[chave] == 'foca'):
            novo_ser = Foca(ids,foca,foca.get_rect(),utils.tamanho_sprite,utils.tamanho_sprite,x,y,calorias,calorias_perde)
        utils.coloca_em_posicao_especifica(novo_ser)
        seres_objetos.append(novo_ser)
        
        # Incrementa os IDS para definir qual será o semáforo da tela (último)
        ids+=1
        

start_time = pygame.time.get_ticks()

tela = Tela(ids, screen, start_time,tempo_perder_calorias)

# Inicialização de threads
for ser in seres_objetos:
    ser.start()
tela.start()

# Fechamento de threads
for ser in seres_objetos:
    ser.join()
tela.join()

# quit()