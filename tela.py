from utils import utils
import threading
import random
import time
import pygame


class Tela(threading.Thread):
    """Classe que define as funcionalidades da tela da simulação.
       Funciona como extensão do módulo de threading do Python3,
       Implementando um sistema de semáforos.
       (tem seu semáforo específico na lista de semáforos da aplicação)
    """

    def __init__(self, id, screen, start_time):
        threading.Thread.__init__(self)
        self.id = id
        self.screen = screen
        self.start_time = start_time
        self.time_since_enter_backup = self.start_time
        self.time_since_enter = self.start_time

    def run(self):
        # global finalizou
        while not utils.finalizou:
            utils.semaforos[self.id].acquire()
            
            # print('Tela liberada!' + str(self.id))
            
            Tela.leitura_quit(pygame.event.get(), True)
            
            

            proximo_semaforo = random.randint(0,(len(utils.semaforos)-2))
            while(not utils.verifica_existencia_e_validade_movimentos_id(proximo_semaforo)):
                proximo_semaforo = random.randint(0,(len(utils.semaforos)-2))
        
        
            for i in range(utils.tamanho_matriz):
                print(utils.mundo[i])
            
            
            utils.decrementa_calorias(int(self.time_since_enter), int(self.time_since_enter_backup))
            utils.limpa_mortos_de_fome()
            self.__exibe_mundo__(self.screen)
            
            if(utils.mundo_vazio() or utils.apenas_algas()):
                utils.finalizou = True
                for i in range(len(utils.semaforos)):
                    utils.semaforos[i].release()
                break
            
            # print("Chama o próximo: " + str(proximo_semaforo))
            utils.semaforos[proximo_semaforo].release()
            # time.sleep(1)

    @staticmethod    
    def leitura_quit(events,release_semaforos=False):
        for event in events:
            if event.type == pygame.QUIT:
                utils.finalizou = True 

                if(release_semaforos):
                    # libera todos os locks
                    for i in range(len(utils.semaforos)):
                        # print("liberando " + str(i))
                        utils.semaforos[i].release()
                    break
    
    def __exibe_mundo__(self, screen):
        screen.fill(utils.COR_MAR)
        for x in range(utils.tamanho_matriz):
            for y in range(utils.tamanho_matriz):
                if(utils.mundo[x][y] != None):
                    utils.mundo[x][y].exibe(screen)
        
        seres_na_tela = utils.contador_seres_no_mundo()

        self.time_since_enter_backup = self.time_since_enter

        self.time_since_enter = self.__tempo_desde_start_no_jogo__()
        message = 'Tempo transcorrido: ' + '%i'%(self.time_since_enter)
        screen.blit(utils.FONT.render(message, True, utils.TEXT_COLOR), (0, 0))
        
        message = 'Seres no mundo: %i'%(seres_na_tela)
        message_seres = utils.FONT.render(message, True, utils.TEXT_COLOR)
        screen.blit(message_seres, ((utils.w-message_seres.get_width()), 0))
        
        pygame.display.flip()
    
    def __tempo_desde_start_no_jogo__(self):
        return ((pygame.time.get_ticks() - self.start_time)/1000)