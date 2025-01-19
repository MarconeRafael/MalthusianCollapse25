# creatures.py

import random
import math

class Creature:
    def __init__(self, name=None, x=0, y=0, speed=1.0, size=1.0, energy=100.0):
        """
        Inicializa uma nova criatura.
        
        :param name: Nome da criatura
        :param x: Posição x da criatura no ambiente
        :param y: Posição y da criatura no ambiente
        :param speed: Velocidade de movimento da criatura
        :param size: Tamanho da criatura
        :param energy: Energia inicial da criatura
        """
        self.name = name if name else f"Creature_{random.randint(1000, 9999)}"
        self.x = x
        self.y = y
        self.speed = speed
        self.size = size
        self.energy = energy
        self.age = 0
        self.health = 100  # Saúde da criatura (0 a 100)
        self.alive = True
    
    def move(self, direction, delta_time):
        """
        Move a criatura na direção especificada.
        
        :param direction: A direção para a qual a criatura deve se mover (em graus)
        :param delta_time: Tempo decorrido desde a última atualização
        """
        radians = math.radians(direction)
        self.x += self.speed * math.cos(radians) * delta_time
        self.y += self.speed * math.sin(radians) * delta_time
    
    def eat(self, food_amount):
        """
        A criatura come uma quantidade de comida, aumentando sua energia.
        
        :param food_amount: Quantidade de comida que a criatura consome
        """
        self.energy += food_amount
        self.energy = min(self.energy, 100.0)  # Energia não pode passar de 100
    
    def age_one_step(self):
        """
        A criatura envelhece um passo no tempo, perdendo energia e saúde.
        """
        self.age += 1
        self.energy -= 0.1  # Perda de energia a cada passo
        if self.energy <= 0:
            self.die()

    def die(self):
        """
        A criatura morre quando sua energia chega a 0 ou saúde atinge 0.
        """
        self.alive = False
        self.health = 0
    
    def reproduce(self, mate):
        """
        Reproduz-se com outra criatura, gerando uma nova criatura.
        
        :param mate: A criatura com a qual a criatura irá se reproduzir
        :return: Uma nova criatura, filha das duas criaturas
        """
        if self.alive and mate.alive:
            child_name = f"Creature_{random.randint(1000, 9999)}"
            child_x = (self.x + mate.x) / 2  # Média das posições dos pais
            child_y = (self.y + mate.y) / 2
            child_speed = (self.speed + mate.speed) / 2
            child_size = (self.size + mate.size) / 2
            child_energy = (self.energy + mate.energy) / 2
            
            return Creature(name=child_name, x=child_x, y=child_y, speed=child_speed, size=child_size, energy=child_energy)
        else:
            return None
    
    def __repr__(self):
        """
        Representação de string da criatura.
        """
        return f"<Creature {self.name} (Age: {self.age}, Energy: {self.energy}, Health: {self.health})>"

# Função para criar uma população inicial de criaturas
def create_population(pop_size):
    """
    Cria uma população inicial de criaturas.
    
    :param pop_size: Número de criaturas a serem geradas
    :return: Lista com as criaturas criadas
    """
    return [Creature(name=f"Creature_{i+1}", x=random.uniform(0, 100), y=random.uniform(0, 100)) for i in range(pop_size)]

