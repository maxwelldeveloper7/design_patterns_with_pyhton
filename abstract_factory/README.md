# Padrão Abstract Factory - Exemplo de Plataforma Mobile

## Visão Geral
Este exemplo demonstra a implementação do **Padrão Abstract Factory** para criar componentes de UI multiplataforma. O padrão fornece uma interface para criar famílias de objetos relacionados sem especificar suas classes concretas.

## Estrutura do Padrão
![](../assets/img/abstraic_factory.png)
### Produtos Abstratos
- `Botao` - Classe base abstrata para botões
- `Checkbox` - Classe base abstrata para caixas de seleção

### Produtos Concretos
- **Componentes Android:**
  - `AndroidBotao` - Botão no estilo Android
  - `AndroidCheckbox` - Checkbox no estilo Android
- **Componentes iOS:**
  - `IOSBotao` - Botão no estilo iOS
  - `IOSCheckbox` - Checkbox no estilo iOS

### Abstract Factory
- `UIFactory` - Define métodos para criar componentes de UI

### Fábricas Concretas
- `AndroidFactory` - Cria componentes específicos do Android
- `IOSFactory` - Cria componentes específicos do iOS

### Cliente
- `Aplicacao` - Usa a fábrica para criar e renderizar componentes de UI

## Principais Benefícios

1. **Independência de Plataforma** - O código cliente trabalha com abstrações, não implementações concretas
2. **Consistência** - Garante que todos os componentes pertencem à mesma família de plataforma
3. **Fácil Extensão** - Novas plataformas podem ser adicionadas sem modificar código existente
4. **Baixo Acoplamento** - Cliente depende apenas de interfaces abstratas

## Exemplo de Uso

```python
# Escolhe a plataforma (pode vir de config, API, etc.)
plataforma = "android"

if plataforma == "android":
    factory = AndroidFactory()
else:
    factory = IOSFactory()

# Cria aplicação com a fábrica escolhida
app = Aplicacao(factory)
app.renderizar_tela()
```

## Saída
```
Desenhando botão no estilo Android.
Desenhando checkbox no estilo Android.
```

## Quando Usar
- Quando você precisa criar famílias de produtos relacionados
- Quando você quer garantir compatibilidade de produtos dentro de uma família
- Quando você precisa suportar múltiplas plataformas ou variantes
- Quando você quer desacoplar o código cliente das classes de produtos concretas