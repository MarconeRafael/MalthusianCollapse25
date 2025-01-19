# physics.py

import pygame
import random
import math
import Box2D

class PhysicsWorld:
    def __init__(self, gravity=(0, -10)):
        """
        Inicializa o mundo físico, definindo a gravidade e criando o ambiente Box2D.

        :param gravity: Tupla representando a gravidade no mundo, por padrão (0, -10) para uma gravidade para baixo
        """
        self.world = Box2D.b2World(gravity=gravity)
        self.objects = []  # Lista para armazenar objetos interativos no mundo

    def create_static_boundary(self):
        """
        Cria os limites estáticos do mundo, como as paredes e o chão.
        """
        ground = self.world.CreateStaticBody(position=(0, 0))
        ground.CreateEdgeFixture(vertices=[(-50, -50), (50, -50)], friction=0.5)  # Chão
        ground.CreateEdgeFixture(vertices=[(-50, 50), (50, 50)], friction=0.5)  # Teto
        ground.CreateEdgeFixture(vertices=[(-50, -50), (-50, 50)], friction=0.5)  # Parede esquerda
        ground.CreateEdgeFixture(vertices=[(50, -50), (50, 50)], friction=0.5)  # Parede direita

    def create_creature(self, x, y, radius=1.0, density=1.0, friction=0.5):
        """
        Cria uma criatura no mundo com um formato circular e propriedades físicas.

        :param x: Posição x da criatura
        :param y: Posição y da criatura
        :param radius: Raio do corpo da criatura
        :param density: Densidade da criatura
        :param friction: Fator de atrito da criatura
        :return: Corpo da criatura no mundo físico
        """
        body = self.world.CreateDynamicBody(position=(x, y))
        shape = body.CreateCircleFixture(radius=radius, density=density, friction=friction)
        self.objects.append(body)
        return body

    def update(self, time_step=1/60):
        """
        Atualiza o mundo físico, aplicando as leis da física e simulando o movimento.

        :param time_step: Passo de tempo da simulação (em segundos)
        """
        self.world.Step(time_step, 10, 10)  # Simula o movimento no mundo
        for obj in self.objects:
            self.check_boundaries(obj)

    def check_boundaries(self, obj):
        """
        Verifica se o objeto saiu dos limites do mundo e aplica a colisão ou reinicia sua posição.

        :param obj: O objeto que será verificado
        """
        x, y = obj.position
        if x < -50 or x > 50 or y < -50 or y > 50:
            obj.position = (random.uniform(-20, 20), random.uniform(-20, 20))  # Reinicia a posição dentro dos limites

    def draw(self, screen):
        """
        Desenha os objetos no mundo físico utilizando PyGame.

        :param screen: Tela do PyGame para renderização
        """
        for obj in self.objects:
            x, y = obj.position
            radius = obj.fixtures[0].shape.radius
            pygame.draw.circle(screen, (255, 0, 0), (int(x * 10), int(y * 10)), int(radius * 10))

# Função para inicializar o mundo físico e criar criaturas
def create_physics_environment():
    """
    Inicializa o ambiente físico com as paredes e algumas criaturas.

    :return: Instância do mundo físico e a lista de criaturas criadas
    """
    physics_world = PhysicsWorld(gravity=(0, -10))
    physics_world.create_static_boundary()
    creatures = []
    for _ in range(5):  # Cria 5 criaturas para testar
        creature = physics_world.create_creature(random.uniform(-20, 20), random.uniform(-20, 20))
        creatures.append(creature)
    
    return physics_world, creatures
