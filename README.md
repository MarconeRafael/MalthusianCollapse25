# MalthusianCollapse25

Simulação baseada em sistemas caóticos e superpopulação, utilizando PyBox2D, PyGame e NEAT.

## Instalação
```bash
# Clone o repositório
git clone https://github.com/usuario/malthusiancollapse25.git

# Entre no diretório
cd malthusiancollapse25

# Crie e ative o ambiente virtual
python3 -m venv spring_creatures_env
source spring_creatures_env/bin/activate

# Instale as dependências
pip install -r requirements.txt


# Execute a simulação
python src/main.py
# Simulação MalthusianCollapse25

Este projeto simula as dinâmicas de sobrevivência de grupos humanos MalthusianCollapse25. Ele inclui interações complexas entre humanos, fontes de água, fontes de comida, plantas, poluição e grupos. Através dessa simulação, é possível observar como os recursos naturais e as ações humanas afetam o ambiente e a sobrevivência dos indivíduos.

## Classes Principais

### 1. **Humano**
Representa um ser humano no ambiente.

#### Atributos:
- `alimentacao`: Quantidade de comida disponível (carne, frutas, raízes).
- `agua`: Quantidade de água disponível.
- `poluicao`: Quantidade de poluição gerada pela atividade humana.
- `reproduzido`: Indica se o humano se reproduziu recentemente.
- `grupo`: O grupo ao qual o humano pertence (se for parte de algum).
- `localizacao`: Posição atual no ambiente.
- `saude`: Nível de saúde do humano, afetado pela poluição, alimentação e água.

#### Métodos:
- `consome_agua()`: Consome água, gerando poluição proporcional ao coeficiente de espalhamento e afetando a saúde.
- `consome_comida()`: Consome comida (grãos, frutas ou carne), gerando poluição proporcional à comida consumida e melhorando a saúde.
- `reproduz()`: Reproduz-se, consumindo comida e água, gerando poluição no local.
- `matar(outro_humano)`: Pode matar outro humano para roubar recursos, melhorando sua sobrevivência.
- `transporta_comida()`: Transporta comida para o local de alimentação, precisando de tempo e energia.
- `movimenta()`: Movimenta-se pelo ambiente, seja em busca de comida, água ou abrigo.
- `defende()`: Pode defender o grupo ou atacar outros humanos para proteger recursos.
- `abandonar_grupo()`: Decide abandonar o grupo para procurar um novo, levando comida ou recursos.
- `entrar_grupo()`: Decide entrar em outro grupo, aumentando suas chances de sobrevivência, mas dividindo recursos.

### 2. **FonteDeAgua**
Representa uma fonte de água no ambiente.

#### Atributos:
- `quantidade`: Quantidade de água disponível.
- `localizacao`: Posição no ambiente.
- `poluicao`: Quantidade de poluição gerada pela fonte, que se acumula com o uso.

#### Métodos:
- `disponibiliza_agua()`: Fornece água aos humanos, gerando poluição no processo.

### 3. **FonteDeProteina (Animal)**
Representa uma fonte de proteína animal no ambiente.

#### Atributos:
- `quantidade`: Quantidade de proteína disponível.
- `localizacao`: Posição no ambiente.
- `poluicao`: Quantidade de poluição gerada pela fonte.

#### Métodos:
- `consome_plantas()`: Consome plantas (herbívoro) para obter proteína.
- `produz_polucao()`: Gera poluição ao consumir plantas, que afeta a qualidade do ambiente.

### 4. **Planta**
Representa uma planta no ambiente.

#### Atributos:
- `quantidade`: Quantidade de plantas disponíveis.
- `localizacao`: Posição no ambiente.

#### Métodos:
- `produz_oxigenio()`: Produz oxigênio, essencial para a respiração dos humanos e outros seres vivos.
- `cresce()`: As plantas crescem lentamente, dependendo de condições ambientais.

### 5. **Poluicao**
Representa a poluição no ambiente.

#### Atributos:
- `nivel`: Nível de poluição no ambiente, que pode afetar a saúde e a reprodução.
- `coeficiente_espalhamento`: A taxa com que a poluição se espalha pelo ambiente.

#### Métodos:
- `espalha()`: A poluição se espalha pelo ambiente, afetando outros recursos (como fontes de água e plantas).

### 6. **Grupo**
Representa um grupo de humanos que colaboram entre si.

#### Atributos:
- `membros`: Lista de humanos que pertencem a este grupo.
- `recursos`: Quantidade de recursos disponíveis para o grupo (comida, água, proteína).
- `forca_defensiva`: A capacidade do grupo de defender seus recursos.
- `localizacao`: Localização do acampamento ou do grupo.

#### Métodos:
- `adicionar_membro(humano)`: Adiciona um humano ao grupo.
- `remover_membro(humano)`: Remove um membro do grupo.
- `distribuir_recursos()`: Divide os recursos entre os membros do grupo.
- `defender()`: O grupo pode defender seus recursos de outros grupos ou animais.
- `atacar(outro_grupo)`: Pode atacar outros grupos para roubar recursos.

## Interações e Dinâmicas

- **Humanos e Fontes de Água Limpa**: Humanos competem por acesso a fontes de água, que geram poluição ao ser consumidas, afetando a saúde e o ambiente.
- **Humanos e Fontes de Comida (Grãos, Frutas, Carne)**: Humanos consomem alimentos, gerando poluição, com a caça sendo mais poluente. A escassez de comida leva a conflitos.
- **Humanos e Grupos**: Grupos de humanos formam alianças ou rivalidades, disputando recursos e territórios.
- **Humanos e Animais**: Humanos caçam animais para proteína, o que gera poluição e afeta a população animal.
- **Poluição e o Ambiente**: A poluição afeta todos os aspectos do ambiente, tornando os recursos menos saudáveis e reduzindo a quantidade de alimentos e oxigênio.

## Dinâmica da Simulação

A simulação gira em torno de um ciclo contínuo de interação entre humanos, animais, plantas e poluição. Grupos humanos lutam por recursos, formam alianças ou disputam territórios, tudo isso enquanto tentam sobreviver em um ambiente caótico e muitas vezes hostil. A alimentação, a água e a caça desempenham papéis centrais, e a poluição gerada por esses processos pode acelerar o colapso ou gerar uma transformação no ecossistema, alterando permanentemente as possibilidades de sobrevivência.

## Como Executar

1. **Instalação**: Clone este repositório em sua máquina local.
2. **Execução**: Compile e execute o código para iniciar a simulação, observando as interações e dinâmicas entre as classes.

## Contribuições

Sinta-se à vontade para contribuir com o projeto, corrigindo bugs ou sugerindo melhorias. Envie um pull request com as suas alterações.

## Licença

Este projeto é licenciado sob a Licença apache 2.0. Consulte o arquivo LICENSE para mais detalhes.