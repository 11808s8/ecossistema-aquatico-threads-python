from utils import settings
import threading
import random
import time
import pygame


class Tela(threading.Thread):


    def __init__(self, id, screen, start_time):
        threading.Thread.__init__(self)
        self.id = id
        self.screen = screen
        self.start_time = start_time
        self.time_since_enter_backup = self.start_time
        self.time_since_enter = self.start_time

    def run(self):
        # global finalizou
        while not settings.finalizou:
            settings.semaforos[self.id].acquire()
            # if(self.finalizou):
            #     break
            print('Tela liberada!' + str(self.id))
            
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    settings.finalizou = True 

                    # libera todos os locks
                    for i in range(len(settings.semaforos)):
                        print("liberando " + str(i))
                        settings.semaforos[i].release()
                    break
            

            proximo_semaforo = random.randint(0,(len(settings.semaforos)-2))
            while(not settings.verifica_existencia_e_validade_movimentos_id(proximo_semaforo)):
                proximo_semaforo = random.randint(0,(len(settings.semaforos)-2))
        
        
            for i in range(settings.tamanho_matriz):
                print(settings.mundo[i])
            
            
            settings.decrementa_calorias(int(self.time_since_enter), int(self.time_since_enter_backup))
            settings.limpa_mortos_de_fome()
            self.__exibe_mundo__(self.screen)
            
            if(settings.mundo_vazio() or settings.apenas_algas()):
                settings.finalizou = True
                for i in range(len(settings.semaforos)):
                    print("liberando " + str(i))
                    settings.semaforos[i].release()
                break
            
            print("Chama o próximo: " + str(proximo_semaforo))
            settings.semaforos[proximo_semaforo].release()
            # time.sleep(1)
            
    
    def __exibe_mundo__(self, screen):
        screen.fill(settings.COR_MAR)
        for x in range(settings.tamanho_matriz):
            for y in range(settings.tamanho_matriz):
                if(settings.mundo[x][y] != None):
                    settings.mundo[x][y].exibe(screen)
        
        seres_na_tela = settings.contador_seres_no_mundo()

        self.time_since_enter_backup = self.time_since_enter

        self.time_since_enter = self.__tempo_desde_start_no_jogo__()
        message = 'Tempo transcorrido: ' + '%i'%(self.time_since_enter)
        screen.blit(settings.FONT.render(message, True, settings.TEXT_COLOR), (0, 0))
        
        message = 'Seres no mundo: %i'%(seres_na_tela)
        message_seres = settings.FONT.render(message, True, settings.TEXT_COLOR)
        screen.blit(message_seres, ((settings.w-message_seres.get_width()), 0))
        
        pygame.display.flip()
    
    def __tempo_desde_start_no_jogo__(self):
        return ((pygame.time.get_ticks() - self.start_time)/1000)