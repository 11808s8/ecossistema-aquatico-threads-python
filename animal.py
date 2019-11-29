import threading
import time
from ser import Ser
from utils import utils

class Animal(Ser):
    
    FOME = 100

    def __init__(self, id,imagem, rect, altura, largura, x=0 ,y=0,calorias=600, O_QUE_COMO = []):
        super().__init__(id,imagem, rect, altura, largura, x ,y)
        self.calorias = calorias
        self.O_QUE_COMO = O_QUE_COMO


    def run(self):
        while(not utils.finalizou):
            utils.semaforos[self.id].acquire()
            print("finalizou " + str(self.id) + " Status: " + str(utils.finalizou))

            # @TODO: falta verificar se morri de fome e decrementar fome
            if(utils.finalizou):
                print("finalizou " + str(self.id))
                break

            if(not utils.ser_existe_no_mundo(self)):
                utils.semaforos[(len(utils.semaforos)-1)].release()
                break
        
            direcao = utils.retorna_movimento_valido(self)
            if(direcao==None):
                utils.semaforos[(len(utils.semaforos)-1)].release()    
            (x,y) = utils.retorna_coordenada_baseado_em_movimento(self.x,self.y,direcao)
            if(utils.mundo[x][y] != None):
                # if(utils.mundo[x][y]['tipo_ser'] in self.O_QUE_COMO):
                if(utils.mundo[x][y].o_que_sou() in self.O_QUE_COMO):
                    self.se_alimentou()
            # else:
            #     self.sente_fome()
            
            x_antigo = self.x
            y_antigo = self.y 
            self.movimenta(direcao)
            utils.coloca_em_posicao_especifica(self)
            utils.limpa_posicao_especifica(x_antigo, y_antigo)

            print(type(self).__name__ + " " + str(self.id) + " X " + str(self.x) + " Y " + str(self.y))
            utils.semaforos[(len(utils.semaforos)-1)].release()


    def __str__(self):
        # Printa o nome da classe, calorias e pos(x,y)
        return('Identificador: ' + str(self.id) +' ' +\
            type(self).__name__ + \
            ' calorias: ' + str(self.calorias) + \
                ' x: ' + str(self.x) + ' y:' + str(self.y))

    '''
        Movimentação do animal
    '''
    def movimenta(self, direcao):
        if(direcao=='cima'):
            self.y-=1
        elif(direcao=='baixo'):
            self.y+=1
        elif(direcao=='esquerda'):
            self.x-=1
        elif(direcao=='direita'):
            self.x+=1
        else:
            raise Exception('Direção desconhecida!')

    '''
        Incremento da fome
    '''
    def sente_fome(self):
        # print("Chamou")
        # input()
        self.calorias -= self.FOME
    
    def se_alimentou(self):
        self.calorias += self.FOME


    '''
        Verificação se o Animal morreu de fome
    '''
    def morreu_de_fome(self):
        if(self.calorias<=0):
            return True
        return False

    def exibe(self, screen):
        super().exibe(screen)
        message = 'Calorias: ' + '%i'%(self.calorias)
        # screen.blit(utils.FONT.render(message, True, utils.TEXT_COLOR), (self.matriz_x[self.x], self.matriz_y[self.y]+self.tamanho_quadrado/2))
        screen.blit(utils.FONT.render(message, True, utils.TEXT_COLOR), (self.matriz_x[self.x], self.matriz_y[self.y]-20))
        # screen.blit(self.imagem,(, ))