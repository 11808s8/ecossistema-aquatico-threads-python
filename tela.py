import settings
import threading
import random
import time
import pygame


class Tela(threading.Thread):

    def __init__(self, id):
        threading.Thread.__init__(self)
        self.id = id

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
            if(settings.mundo_vazio()):
                settings.finalizou = True
                for i in range(len(settings.semaforos)):
                    print("liberando " + str(i))
                    settings.semaforos[i].release()
                    break

            proximo_semaforo = random.randint(0,(len(settings.semaforos)-2))
            while(not settings.verifica_se_id_ser_existe_no_mundo(proximo_semaforo)):
                proximo_semaforo = random.randint(0,(len(settings.semaforos)-2))
        
        
            for i in range(settings.tamanho_matriz):
                print(settings.mundo[i])
            print("Chama o próximo: " + str(proximo_semaforo))
            settings.semaforos[proximo_semaforo].release()
            time.sleep(1)
            
    