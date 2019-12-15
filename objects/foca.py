from .animal import Animal

class Foca(Animal):
    
    def __init__(self, id,imagem, rect, altura, largura, x=0 ,y=0,calorias=600,quanto_perco_calorias=100):
        super().__init__( id,imagem, rect, altura, largura, x,y,calorias,quanto_perco_calorias, ['peixe'])
    