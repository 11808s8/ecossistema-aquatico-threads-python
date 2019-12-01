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
       Será sempre o último semáforo na lista de semáforos
    """

    def __init__(self, id, screen, start_time, tempo_perde_calorias):
        threading.Thread.__init__(self)
        self.id = id
        self.screen = screen
        self.start_time = start_time
        self.time_since_enter_backup = 0
        self.time_since_enter = self.start_time
        self.tempo_perde_calorias = tempo_perde_calorias

    def run(self):
        # global finalizou
        while not utils.finalizou:
            utils.semaforos[self.id].acquire()
            
            # print('Tela liberada!' + str(self.id))
            
            Tela.leitura_quit(pygame.event.get(), True)
            
            

            proximo_semaforo = random.randint(0,(len(utils.semaforos)-2))
            while(not utils.verifica_existencia_e_validade_movimentos_id(proximo_semaforo)):
                proximo_semaforo = random.randint(0,(len(utils.semaforos)-2))
        
        
            self.__atualiza_tempos__()
            self.__tratamento_fome_mundo__()
            
            self.__exibe_mundo__(self.screen)
            
            if(utils.mundo_vazio() or utils.apenas_algas()):
                utils.finalizou = True
                for i in range(len(utils.semaforos)):
                    utils.semaforos[i].release()
                break
            
            time.sleep(0.1)
            utils.semaforos[proximo_semaforo].release()
            

    @staticmethod    
    def leitura_quit(events,release_semaforos=False):
        for event in events:
            if event.type == pygame.QUIT:
                utils.finalizou = True 

                if(release_semaforos):
                    # libera todos os locks
                    for i in range(len(utils.semaforos)):
                        utils.semaforos[i].release()
                    break
    
    def __tratamento_fome_mundo__(self):

        # Se o tempo que passou é maior/igual que o tempo necessário para sentir fome, decrementa calorias com base nisso
        if((int(self.time_since_enter) - int(self.time_since_enter_backup))>=self.tempo_perde_calorias):
            self.time_since_enter_backup = self.time_since_enter
            utils.decrementa_calorias()
        utils.limpa_mortos_de_fome()
    

    def __exibe_mundo__(self, screen):
        screen.fill(utils.COR_MAR)
        for x in range(utils.tamanho_matriz):
            for y in range(utils.tamanho_matriz):
                if(utils.mundo[x][y] != None):
                    utils.mundo[x][y].exibe(screen)
        
        seres_na_tela = utils.contador_seres_no_mundo()

        message = 'Tempo transcorrido: ' + '%i'%(self.time_since_enter)
        screen.blit(utils.FONT.render(message, True, utils.TEXT_COLOR), (0, 0))
        
        message = 'Seres no mundo: %i'%(seres_na_tela)
        message_seres = utils.FONT.render(message, True, utils.TEXT_COLOR)
        screen.blit(message_seres, ((utils.w-message_seres.get_width()), 0))
        
        pygame.display.flip()
    
    def __atualiza_tempos__(self):
        # self.time_since_enter_backup = self.time_since_enter
        self.time_since_enter = self.__tempo_desde_start_no_jogo__()


    def __tempo_desde_start_no_jogo__(self):
        return ((pygame.time.get_ticks() - self.start_time)/1000)