from utils import settings
import threading
import time

class Ser(threading.Thread):

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
        self.tamanho_quadrado = (settings.w-self.largura_imagem)/settings.tamanho_matriz 
        self.altura_quadrado = (settings.h-self.altura_imagem)/settings.tamanho_matriz 
        self.matriz_x = [self.tamanho_quadrado*i for i in range(settings.tamanho_matriz)]
        self.matriz_y = [self.altura_quadrado*i for i in range(settings.tamanho_matriz)]

# Matrizes de movimentação para UM objeto. Colocar isso em CADA objeto



    def o_que_sou(self):
        return type(self).__name__.lower()

    '''
        Exibição da imagem do usuário na tela
    '''
    def exibe(self, screen):
        screen.blit(self.imagem,(self.matriz_x[self.x], self.matriz_y[self.y]))
