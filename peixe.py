from animal import Animal

class Peixe(Animal):
    
    def __init__(self, id,imagem, rect, altura, largura, x=0 ,y=0,calorias=600):
        super().__init__( id,imagem, rect, altura, largura, x,y,calorias, ['alga'])
    