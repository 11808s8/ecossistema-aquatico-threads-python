import random
from threading import Semaphore
import pygame

tamanho_matriz = 10
finalizou = False
mundo = [[None]*tamanho_matriz for i in range(tamanho_matriz)]
seres = ['alga','tubarao','foca','peixe']
seres_plural = ['algas','tubarões','focas','peixes']
direcoes = ['cima', 'baixo', 'esquerda', 'direita']

tamanho_sprite = 32
tamanho_fonte_calorias = 16

w = 640
h = 480

semaforos = []

FONT_NAME = "Arial"
FONT = pygame.font.SysFont(FONT_NAME, 20)
FONT_CALORIAS = pygame.font.SysFont(FONT_NAME, tamanho_fonte_calorias)
TEXT_COLOR = (255, 255, 0)
COR_MAR = (9, 150, 185)

ASSETS = './assets/'

def carrega_sprite(nome_arquivo_com_extensao):
    caminho = ASSETS + nome_arquivo_com_extensao
    return pygame.image.load(caminho)

def inicializa_semaforos(quantos):
    global semaforos  
    semaforos = [ Semaphore(0) for i in range(quantos) ]
    semaforos.append(Semaphore(1)) # Semáforo do print na tela

def posicao_tomada(x,y):
    if(mundo[x][y]!=None):
        return True
    return False


def coloca_em_posicao_aleatoria(ser):
    """ Retorna tupla com inteiros (x,y) do array do mundo
    """
    global mundo
    colocou = False
    x = -1
    y = -1
    while(not colocou):
        x = random.randint(0,(tamanho_matriz-1))
        y = random.randint(0,(tamanho_matriz-1))
        if(not posicao_tomada(x,y)):
            if(ser != None):
                mundo[x][y] = ser
            colocou = True
    return (x,y)

def limpa_posicao_especifica(x,y):
    global mundo
    mundo[x][y] = None

def coloca_em_posicao_especifica(animal):
    global mundo
    mundo[animal.x][animal.y] = animal

def ser_existe_no_mundo(ser):
    if(mundo[ser.x][ser.y] == None):
        return False
    elif(mundo[ser.x][ser.y].id == ser.id):
        return True
    return False

def contador_seres_no_mundo():
    global mundo
    contador = 0
    
    for x in range(tamanho_matriz):
        for y in range(tamanho_matriz):
            if(mundo[x][y] != None):
                contador+=1

    return contador
    
def verifica_existencia_e_validade_movimentos_id(id):
    animal = verifica_se_id_ser_existe_no_mundo(id)
    if(animal!=None):
        if(animal.o_que_sou() != 'alga' and retorna_movimento_valido(animal)!=None):
            return True
    return False

def verifica_se_id_ser_existe_no_mundo(id):
    
    for x in range(tamanho_matriz):
        for y in range(tamanho_matriz):
            if(mundo[x][y]!=None):
                if(mundo[x][y].id==id):
                    return mundo[x][y]
    return None


def retorna_movimento_valido(animal):
    
    valido = False
    direcao = None
    direcoes_ja_foi = []
    while(not valido):
        direcao = movimento_aleatorio()
        if(direcao not in direcoes_ja_foi):
            direcoes_ja_foi.append(direcao)
        
        if(verifica_validade_movimento(animal, tamanho_matriz, direcao)):
            (x,y) = retorna_coordenada_baseado_em_movimento(animal.x,animal.y,direcao)
            
            if(mundo[x][y]==None):
                valido = True
                
            elif(mundo[x][y].o_que_sou() in animal.O_QUE_COMO):
                valido= True

        if((len(direcoes_ja_foi)==len(direcoes)) and not valido):
            return None
    
    return direcao

def mundo_vazio():
    global mundo
    for x in range(tamanho_matriz):
        for y in range(tamanho_matriz):
            if(mundo[x][y] != None):
                return False
    return True

#@TODO: Quebrar essas 3 funções abaixo em uma ITERA RETORNO que recebe um CALLBACK e devolve o retorno
def apenas_algas():
    global mundo
    for x in range(tamanho_matriz):
        for y in range(tamanho_matriz):
            if(mundo[x][y] != None):
                if(mundo[x][y].o_que_sou() != 'alga'):
                    return False
    return True

def decrementa_calorias(tempo_atual, tempo_antigo):
    global mundo
    for x in range(tamanho_matriz):
        for y in range(tamanho_matriz):
            if(mundo[x][y] != None):
                if(mundo[x][y].o_que_sou() != 'alga'):
                    mundo[x][y].sente_fome()

def limpa_mortos_de_fome():
    global mundo
    for x in range(tamanho_matriz):
        for y in range(tamanho_matriz):
            if(mundo[x][y] != None):
                if(mundo[x][y].o_que_sou() != 'alga'):
                    if(mundo[x][y].morreu_de_fome()):
                        limpa_posicao_especifica(x,y)
                        # semaforos[(len(semaforos)-1)].release()
                        # break

def movimento_aleatorio():
    return random.choice(direcoes)


'''
    Verificação de validade de movimento
'''
def verifica_validade_movimento(animal, tamanho_mundo, movimento):
    (x,y) = retorna_coordenada_baseado_em_movimento(animal.x,animal.y,movimento)
    
    if(x>(tamanho_mundo-1) or x<0 or y>(tamanho_mundo-1) or y<0):
        return False

    return True
    
def retorna_coordenada_baseado_em_movimento(x,y,movimento):
    
    if(movimento=='cima'):
        y-=1 # invertido pois o Y = 0 é o topo do mundo, ou seja, de 9 para 8 estará subindo (por exemplo)
    elif(movimento=='baixo'):
        y+=1
    elif(movimento=='esquerda'):
        x-=1
    elif(movimento=='direita'):
        x+=1
    return (x,y)