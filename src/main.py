import pygame
import sys
from physics import PhysicsWorld  # Corrigido o nome da classe de PhysicsEngine para PhysicsWorld
from renderer import Renderer
from evolution import run_evolution  # Importação corrigida para chamar run_evolution do módulo evolution
from creatures import Creature
import time

# Função para inicializar o Pygame e o ambiente
def initialize_game():
    """
    Inicializa o Pygame e define as configurações iniciais do ambiente de simulação.
    """
    pygame.init()
    
    # Configurações iniciais
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Simulação de Criaturas - NEAT")
    
    clock = pygame.time.Clock()
    
    return screen, clock


# Função principal de execução da simulação
# main.py

def run_simulation():
    """
    Função para rodar a simulação: inicializa o mundo físico e o renderizador, e realiza a atualização contínua.
    """
    # Inicializa o mundo físico e cria algumas criaturas
    from physics import create_physics_environment
    physics_world, creatures = create_physics_environment()

    # Inicializa o renderizador
    renderer = Renderer(width=800, height=600)  # Passa largura e altura explicitamente

    # Loop de simulação
    running = True
    while running:
        physics_world.update(time_step=1/60)  # Atualiza o mundo físico
        renderer.update(physics_world, creatures)  # Atualiza o renderizador

    renderer.close()  # Fecha a janela ao final



# Função principal de execução do script
if __name__ == "__main__":
    run_simulation()
