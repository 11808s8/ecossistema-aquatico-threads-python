import threading
import time
from ser import Ser
from utils import utils

class Alga(Ser):



    def run(self):
        while(not utils.finalizou):
            
            utils.semaforos[self.id].acquire()
            if(utils.finalizou):
                print("finalizou " + str(self.id))
                break
            if(not utils.ser_existe_no_mundo(self)):
                utils.semaforos[(len(utils.semaforos)-1)].release()
                break
            
            utils.semaforos[(len(utils.semaforos)-1)].release()
            

    def __str__(self):
        # Printa o nome da classe, calorias e pos(x,y)
        return('Identificador: ' + str(self.id) +' ' +\
            type(self).__name__ + \
                ' x: ' + str(self.x) + ' y:' + str(self.y))
