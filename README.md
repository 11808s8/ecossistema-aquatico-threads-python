# Ecossistema Aquático utilizando Threads em Python!

![](/artifacts/ecossistema-aquatico.gif)

Aplicação que simula um ecossistema aquático contendo algas, peixes, focas e tubarões! <br>

O sistema possui uma cadeia alimentar: <br>
Tubarões devoram focas e peixes. <br>
Focas devoram peixes. <br>
Peixes devoram algas. <br>

Animais possuem um contador de calorias que decresce a cada N segundos (definido pelo usuário) e aumenta a cada ser que devoram, de acordo com sua cadeia alimentar. <br>

Os movimentos de cada animal são aleatórios nas seguintes possíveis direções: cima, baixo, esquerda, direita. <br>

A simulação acaba quando restam apenas algas ou não há mais seres vivos no ecossistema. <br>

O tamanho do oceano é configurável através de entrada (se n==5, oceano terá escala 5x5) <br>


## Implementação
Cada ser no ecossistema funciona em uma thread diferente, com sua sincronia de funcionamento garantida por uma lista de semáforos.<br>
(A tela também é uma Thread! Ela centraliza tarefas importantes da aplicação, como limpeza de seres mortos, decremento de calorias...) <br>

## Running

Com o [Pipenv](https://github.com/pypa/pipenv), só instalar os pacotes do pipenv file e executar ```python3 run.py``` na pasta raíz do projeto.


### Sobre
Trabalho desenvolvido para a disciplina de Programação Concorrente (semestre 4/2019) do curso de Ciência da Computação da Universidade de Caxias do Sul.

Arte dos seres feita pelo autor.<br><br>
