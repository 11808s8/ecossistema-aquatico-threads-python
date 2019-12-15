from .utils import utils
import threading
import time

class Ser(threading.Thread):
    ''' Classe principal de implementação de threads
        classes de animais e algas herdarão dela
        e implementarão seus próprios métodos RUN (onde roda a thread quando dá start)
    '''
    def __init__(self, id,imagem, rect, altura, largura, x=0 ,y=0):
        threading.Thread.__init__(self)
        self.imagem = imagem
        self.rect = rect
        self.altura_imagem = altura
        self.largura_imagem = largura
        self.x = x
        self.y = y
        self.id = id
        # self.semaforos = semaforos
        self.tamanho_quadrado = (utils.w-self.largura_imagem)/utils.tamanho_matriz 
        self.altura_quadrado = (utils.h-self.altura_imagem)/utils.tamanho_matriz 
        self.matriz_x = [self.tamanho_quadrado*i for i in range(utils.tamanho_matriz)]
        self.matriz_y = [self.altura_quadrado*i for i in range(utils.tamanho_matriz)]

# Matrizes de movimentação para UM objeto. Colocar isso em CADA objeto



    def o_que_sou(self):
        return type(self).__name__.lower()

    '''
        Exibição da imagem do usuário na tela
    '''
    def exibe(self, screen):
        screen.blit(self.imagem,(self.matriz_x[self.x], self.matriz_y[self.y]))
