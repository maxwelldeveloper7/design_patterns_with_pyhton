# Sistema de Soldados em Jogo - Padrão Flyweight

Este projeto demonstra a implementação do padrão de design **Flyweight** em Python através de um sistema de jogo que gerencia múltiplos soldados de forma eficiente em memória.

## Sobre o Padrão Flyweight

O padrão Flyweight é usado para minimizar o uso de memória quando se trabalha com um grande número de objetos similares. Ele separa o estado em duas partes: **intrínseco** (compartilhado) e **extrínseco** (único por objeto).

## Estrutura do Sistema
![](../../assets/img/flyweight.png)
### `SoldierType` (Flyweight)
Armazena o **estado intrínseco** compartilhado entre soldados:
- `name`: Nome da classe do soldado (ex: "Infantaria")
- `weapon`: Arma padrão do tipo
- `texture`: Arquivo de textura (dados pesados compartilhados)
- `render(x, y)`: Renderiza o soldado recebendo coordenadas como parâmetro

### `SoldierFactory` (Flyweight Factory)
Gerencia a criação e reutilização dos Flyweights:
- `get_soldier_type()`: Retorna um tipo existente ou cria um novo
- `_soldier_types`: Dicionário que armazena os tipos criados

### `Soldier` (Context)
Contém o **estado extrínseco** único de cada soldado:
- `x, y`: Posição específica do soldado
- `soldier_type`: Referência ao Flyweight compartilhado
- `draw()`: Desenha o soldado usando o tipo compartilhado

## Estados Intrínseco vs Extrínseco

### Estado Intrínseco (Compartilhado)
- Nome da classe do soldado
- Tipo de arma
- Texturas e modelos 3D
- Animações e sons

### Estado Extrínseco (Único)
- Posição (x, y)
- Pontos de vida
- Velocidade atual
- Status específico

## Como Usar

```python
# Criando tipos compartilhados (Flyweights)
infantry_type = SoldierFactory.get_soldier_type(
    "Infantaria", "Rifle", "infantry_texture.png"
)
sniper_type = SoldierFactory.get_soldier_type(
    "Sniper", "Sniper Rifle", "sniper_texture.png"
)

# Criando soldados com posições únicas
soldiers = [
    Soldier(10, 20, infantry_type),  # Mesmo tipo, posição diferente
    Soldier(15, 25, infantry_type),  # Reutiliza o mesmo Flyweight
    Soldier(20, 30, sniper_type),    # Tipo diferente
]

# Renderizando todos os soldados
for soldier in soldiers:
    soldier.draw()
```

## Execução

```bash
python exemplo_flyweight.py
```

**Saída esperada:**
```
[Renderizando] Infantaria com arma Rifle usando textura 'infantry_texture.png' na posição (10, 20)
[Renderizando] Infantaria com arma Rifle usando textura 'infantry_texture.png' na posição (15, 25)
[Renderizando] Sniper com arma Sniper Rifle usando textura 'sniper_texture.png' na posição (20, 30)
```

## Vantagens do Flyweight

- **Economia de memória**: Compartilha dados pesados entre objetos
- **Performance**: Reduz overhead de criação de objetos
- **Escalabilidade**: Permite milhares de objetos similares
- **Organização**: Separa claramente estado compartilhado do único

## Economia de Memória

### Sem Flyweight
- 1000 soldados = 1000 cópias de texturas e modelos
- Uso excessivo de memória

### Com Flyweight
- 1000 soldados = poucos tipos compartilhados + 1000 posições
- Economia significativa de memória

## Casos de Uso Práticos

- **Jogos**: Personagens, projéteis, partículas
- **Editores de texto**: Caracteres com formatação
- **Sistemas gráficos**: Ícones e símbolos repetidos
- **Simulações**: Objetos com propriedades similares

## Considerações Importantes

- Use quando há muitos objetos similares
- Estado intrínseco deve ser imutável
- Estado extrínseco é passado como parâmetro
- Factory garante reutilização adequada