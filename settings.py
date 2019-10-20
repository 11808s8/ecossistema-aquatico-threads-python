import random
from threading import Semaphore

tamanho_matriz = 5
finalizou = False
mundo = [[None]*tamanho_matriz for i in range(tamanho_matriz)]
seres = ['alga','tubarao','foca','peixe']
direcoes = ['cima', 'baixo', 'esquerda', 'direita']

w = 640
h = 480

semaforos = []


def inicializa_semaforos(quantos):
    global semaforos  
    semaforos = [ Semaphore(0) for i in range(quantos) ]
    semaforos.append(Semaphore(1)) # Semáforo do print na tela

def posicao_tomada(x,y):
    if(mundo[x][y]!=None):
        return True
    return False

def coloca_em_posicao_aleatoria(id_ser,tipo_ser):
    global mundo
    colocou = False
    x = -1
    y = -1
    while(not colocou):
        x = random.randint(0,(tamanho_matriz-1))
        y = random.randint(0,(tamanho_matriz-1))
        if(not posicao_tomada(x,y)):
            mundo[x][y] = {'id':id_ser, 'tipo_ser':tipo_ser}
            colocou = True
    return (x,y)

def limpa_posicao_especifica(x,y):
    global mundo
    mundo[x][y] = None

def coloca_em_posicao_especifica(animal):
    global mundo
    mundo[animal.x][animal.y] = { 'id': animal.id, 'tipo_ser':animal.o_que_sou()}

def ser_existe_no_mundo(ser):
    print("====1")
    print(ser)
    print("====2")
    print(mundo[ser.x][ser.y])
    if(mundo[ser.x][ser.y] == None):
        return False
    elif(mundo[ser.x][ser.y]['id'] == ser.id):
        return True
    return False


def verifica_se_id_ser_existe_no_mundo(id):
    
    for x in range(tamanho_matriz):
        for y in range(tamanho_matriz):
            if(mundo[x][y]!=None):
                if(mundo[x][y]["id"]==id):
                    return True
    return False

def retorna_movimento_valido(animal):
    
    valido = False
    direcao = None
    
    while(not valido):
        direcao = movimento_aleatorio()
        if(verifica_validade_movimento(animal, tamanho_matriz, direcao)):
            (x,y) = retorna_coordenada_baseado_em_movimento(animal.x,animal.y,direcao)
            print(" X :" + str(x) + " Y : " + str(y))
            if(mundo[x][y]==None):
                valido = True
            elif(mundo[x][y]['tipo_ser'] in animal.O_QUE_COMO):
                valido= True
    
    return direcao

def mundo_vazio():
    global mundo
    for x in range(tamanho_matriz):
        for y in range(tamanho_matriz):
            if(mundo[x][y] != None):
                return False
    return True

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