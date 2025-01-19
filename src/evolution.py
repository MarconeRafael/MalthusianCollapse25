# evolution.py

import random
import neat
import os
from creatures import Creature
from utils import calculate_fitness

class Evolution:
    def __init__(self, config_file='data/config/neat-config.txt'):
        """
        Inicializa o processo de evolução com as configurações fornecidas.

        :param config_file: Caminho para o arquivo de configuração do NEAT
        """
        # Carrega a configuração do NEAT
        self.config = neat.Config(
            neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, 
            neat.DefaultStagnation, config_file
        )
        self.population = neat.Population(self.config)

    def evaluate_creatures(self, creatures):
        """
        Avalia as criaturas em cada geração, calculando sua aptidão com base no comportamento.

        :param creatures: Lista de criaturas (objetos do tipo Creature)
        :return: Lista de aptidões calculadas para as criaturas
        """
        fitness_scores = []
        for creature in creatures:
            fitness = calculate_fitness(creature)
            fitness_scores.append(fitness)
            creature.fitness = fitness  # Armazena a aptidão da criatura
        return fitness_scores

    def run_generation(self, creatures):
        """
        Executa uma geração do algoritmo NEAT, evoluindo a população.

        :param creatures: Lista de criaturas atuais
        :return: Lista de criaturas evoluídas
        """
        # Avalia as criaturas da geração atual
        fitness_scores = self.evaluate_creatures(creatures)
        
        # Ordena as criaturas com base em sua aptidão
        sorted_creatures = sorted(zip(creatures, fitness_scores), key=lambda x: x[1], reverse=True)
        
        # Seleciona os melhores para reprodução
        selected_creatures = [creature for creature, _ in sorted_creatures[:len(creatures)//2]]
        
        # Cria uma nova geração utilizando o NEAT
        new_creatures = []
        for _ in range(len(creatures)):
            parent1, parent2 = random.sample(selected_creatures, 2)
            offspring = self.crossover(parent1, parent2)
            self.mutate(offspring)
            new_creatures.append(offspring)
        
        return new_creatures

    def crossover(self, parent1, parent2):
        """
        Realiza o cruzamento entre dois pais para gerar um filho.

        :param parent1: Criatura pai 1
        :param parent2: Criatura pai 2
        :return: Filhote gerado pelos pais
        """
        # Aqui, vamos apenas combinar os neurônios e pesos de maneira simples.
        # Uma implementação mais avançada usaria a topologia e as conexões reais do NEAT.
        return Creature()  # Criar um novo filhote (em uma versão real, seria um crossover das redes)

    def mutate(self, creature):
        """
        Aplica mutações na criatura.

        :param creature: Criatura a ser mutada
        """
        # Aqui, você pode adicionar mudanças aleatórias nos pesos ou na estrutura da rede neural.
        pass

    def save_generation(self, generation_number):
        """
        Salva a geração atual em um arquivo para análise futura.

        :param generation_number: Número da geração atual
        """
        # Você pode salvar o estado da população ou estatísticas da geração
        pass

    def load_generation(self, generation_number):
        """
        Carrega uma geração salva de um arquivo.

        :param generation_number: Número da geração a ser carregada
        :return: Geração carregada
        """
        # Carrega a geração salva
        pass


# Função para iniciar a evolução do NEAT
def run_evolution():
    """
    Função para rodar o processo de evolução: inicializa as criaturas e executa o processo de evolução.
    """
    # Inicializa a evolução com as configurações
    evolution = Evolution()

    # Número de gerações a serem simuladas
    num_generations = 100

    creatures = [Creature() for _ in range(10)]  # Inicia com 10 criaturas (exemplo)

    for generation in range(num_generations):
        print(f"Geração {generation+1}/{num_generations}")
        
        # Executa a evolução e gera a próxima geração
        creatures = evolution.run_generation(creatures)

        # Salva a geração após evolução (opcional)
        evolution.save_generation(generation)

        # Se necessário, carregue uma geração anterior
        # evolution.load_generation(generation)


# Função para rodar a evolução quando o arquivo for executado diretamente
if __name__ == "__main__":
    run_evolution()
