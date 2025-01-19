# renderer.py

import pygame
from physics import PhysicsWorld

class Renderer:
    def __init__(self, width=800, height=600, title="Simulação de Criaturas"):
        """
        Inicializa o renderizador para a simulação.

        :param width: Largura da tela de renderização
        :param height: Altura da tela de renderização
        :param title: Título da janela de renderização
        """
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))  # Usa as variáveis passadas
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()

    def draw_world(self, physics_world, creatures):
        """
        Desenha o mundo físico e as criaturas na tela.

        :param physics_world: Mundo físico (PhysicsWorld)
        :param creatures: Lista de criaturas (objetos dinâmicos)
        """
        # Limpa a tela para o fundo preto
        self.screen.fill((0, 0, 0))
        
        # Desenha os limites do mundo (já desenhados no PhysicsWorld)
        physics_world.draw(self.screen)

        # Desenha cada criatura como um círculo vermelho
        for creature in creatures:
            x, y = creature.position
            radius = creature.fixtures[0].shape.radius
            # Redimensiona a posição e o raio de acordo com a escala da tela
            pygame.draw.circle(self.screen, (255, 0, 0), (int(x * 20) + 400, int(y * 20) + 300), int(radius * 20))

        # Atualiza a tela com os desenhos feitos
        pygame.display.update()

    def handle_events(self):
        """
        Trata os eventos de entrada do usuário, como o fechamento da janela.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

    def update(self, physics_world, creatures):
        """
        Atualiza o estado do mundo e redesenha a tela.
        """
        self.handle_events()
        self.draw_world(physics_world, creatures)
        self.clock.tick(60)  # Limita a taxa de quadros a 60 FPS

    def close(self):
        """
        Fecha a janela do PyGame.
        """
        pygame.quit()


# Função principal para inicializar o renderizador e a simulação
def run_simulation():
    """
    Função para rodar a simulação: inicializa o mundo físico e o renderizador, e realiza a atualização contínua.
    """
    # Inicializa o mundo físico e cria algumas criaturas
    from physics import create_physics_environment
    physics_world, creatures = create_physics_environment()

    # Inicializa o renderizador
    renderer = Renderer()  # Passa os valores padrão para largura e altura

    # Loop de simulação
    running = True
    while running:
        physics_world.update(time_step=1/60)  # Atualiza o mundo físico
        renderer.update(physics_world, creatures)  # Atualiza o renderizador

    renderer.close()  # Fecha a janela ao final


# Se esse arquivo for executado diretamente, a simulação será iniciada
if __name__ == "__main__":
    run_simulation()
