# utils.py

import math
import random

# Função para converter unidades (por exemplo, metros para centímetros)
def convert_units(value, from_unit, to_unit):
    conversion_factors = {
        ("m", "cm"): 100,
        ("cm", "m"): 0.01,
        ("kg", "g"): 1000,
        ("g", "kg"): 0.001,
        # Adicionar mais conversões conforme necessário
    }

    try:
        factor = conversion_factors[(from_unit, to_unit)]
        return value * factor
    except KeyError:
        raise ValueError(f"Conversão não suportada entre {from_unit} e {to_unit}")

# Função para inicializar a população de criaturas
def initialize_population(pop_size, creature_class, *args, **kwargs):
    """
    Inicializa uma população de criaturas.
    
    :param pop_size: Número de criaturas a serem criadas
    :param creature_class: Classe das criaturas a serem instanciadas
    :param args: Argumentos adicionais a serem passados para a classe
    :param kwargs: Argumentos nomeados adicionais para a classe
    :return: Lista de criaturas
    """
    return [creature_class(*args, **kwargs) for _ in range(pop_size)]

# Função para gerar um número aleatório entre dois valores
def random_range(min_value, max_value):
    return random.uniform(min_value, max_value)

# Função para calcular a distância euclidiana entre dois pontos (x1, y1) e (x2, y2)
def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Função para normalizar um valor entre 0 e 1
def normalize(value, min_value, max_value):
    """
    Normaliza um valor dentro do intervalo [min_value, max_value] para [0, 1].
    
    :param value: Valor a ser normalizado
    :param min_value: Valor mínimo do intervalo original
    :param max_value: Valor máximo do intervalo original
    :return: Valor normalizado
    """
    return (value - min_value) / (max_value - min_value) if max_value != min_value else 0

# Função para gerar um identificador único para objetos (por exemplo, criaturas)
def generate_unique_id(prefix="creature"):
    timestamp = int(random.uniform(1000000, 9999999))  # Gera um número aleatório de 7 dígitos
    return f"{prefix}_{timestamp}"

# Função para carregar configurações a partir de um arquivo de texto
def load_config(file_path):
    """
    Carrega um arquivo de configuração no formato texto e retorna um dicionário.
    
    :param file_path: Caminho para o arquivo de configuração
    :return: Dicionário contendo as configurações
    """
    config = {}
    try:
        with open(file_path, 'r') as f:
            for line in f:
                # Ignora linhas vazias ou de comentário
                if line.strip() and not line.startswith("#"):
                    key, value = line.strip().split('=')
                    config[key.strip()] = value.strip()
    except FileNotFoundError:
        print(f"Arquivo de configuração não encontrado: {file_path}")
    return config
# utils.py

def calculate_fitness(creature):
    """
    Calcula a aptidão de uma criatura com base em seu comportamento ou atributos.

    :param creature: A criatura para a qual a aptidão será calculada
    :return: O valor da aptidão
    """
    # Lógica de cálculo de aptidão, por exemplo, baseada em atributos da criatura
    # Este é um exemplo básico, você pode ajustar conforme a necessidade
    return creature.energy * 0.1  # Exemplo simples de cálculo de aptidão
