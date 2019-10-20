import threading
import time
from ser import Ser
import settings

class Alga(Ser):



    def run(self):
        while(not settings.finalizou):
            
            settings.semaforos[self.id].acquire()
            # print("Meu id: " )
            # print("finalizou " + str(self.id) + " Status: " + str(settings.finalizou))
            if(settings.finalizou):
                print("finalizou " + str(self.id))
                break
            if(not settings.ser_existe_no_mundo(self)):
                settings.semaforos[(len(settings.semaforos)-1)].release()
                break
            print(type(self).__name__ + " " + str(self.id))
            settings.semaforos[(len(settings.semaforos)-1)].release()
            time.sleep(1)

    def __str__(self):
        # Printa o nome da classe, calorias e pos(x,y)
        return('Identificador: ' + str(self.id) +' ' +\
            type(self).__name__ + \
                ' x: ' + str(self.x) + ' y:' + str(self.y))
