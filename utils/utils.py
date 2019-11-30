import random
from threading import Semaphore
import pygame

finalizou = False
mundo = None


seres = ['alga','tubarao','foca','peixe']
seres_plural = ['algas','tubarões','focas','peixes']
direcoes = ['cima', 'baixo', 'esquerda', 'direita']

tamanho_sprite = 100
tamanho_fonte_calorias = 16

w = 640
h = 480

semaforos = []
tamanho_matriz = 0
FONT_NAME = "Arial"
FONT = pygame.font.SysFont(FONT_NAME, 20)
FONT_CALORIAS = pygame.font.SysFont(FONT_NAME, tamanho_fonte_calorias)
TEXT_COLOR = (255, 255, 0)
COR_MAR = (9, 150, 185)

ASSETS = './assets/'

def inicializa_mundo(tam_matriz):
    global tamanho_matriz
    tamanho_matriz = tam_matriz
    global mundo
    global tamanho_sprite
    mundo = [[None]*tamanho_matriz for i in range(tamanho_matriz)]
    if((tamanho_matriz*tamanho_matriz)>25):
        tamanho_sprite = 48
    

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


# Fiz essa função pra encapsular as outras, que iteravam sobre o mundo com o msm comportamento sem considerar algas
def iteracao_mundo_strategy(tipo_funcao):
    global mundo
    for x in range(tamanho_matriz):
        for y in range(tamanho_matriz):
            if(mundo[x][y] != None):
                if(mundo[x][y].o_que_sou() != 'alga'):
                    if(tipo_funcao=='apenas_algas'):
                        return False
                    elif(tipo_funcao=='decrementa_calorias'):
                        mundo[x][y].sente_fome()  
                    elif(tipo_funcao=='limpa_mortos_de_fome'):
                        if(mundo[x][y].morreu_de_fome()):
                            limpa_posicao_especifica(x,y)
    if(tipo_funcao=='apenas_algas'):
        return True
                    
def apenas_algas():
    return iteracao_mundo_strategy('apenas_algas')

def decrementa_calorias():
    iteracao_mundo_strategy('decrementa_calorias')

def limpa_mortos_de_fome():
    iteracao_mundo_strategy('limpa_mortos_de_fome')

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


def single_input_int_com_mensagem(screen,clock,input_surface,mensagem):
    entrada = 0
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                quit()
        if(input_surface.update(events)):
                entrada = int(input_surface.get_text())
                input_surface.clear_text()
                break
        screen.fill((0,0,0))
        # message = 
        screen.blit(FONT.render(mensagem, True, TEXT_COLOR), (40,(h/2)))
        screen.blit(input_surface.get_surface(),(FONT.size(mensagem)[0]+40,(h/2)))
        pygame.display.flip()
        clock.tick(100)
    return entrada
        