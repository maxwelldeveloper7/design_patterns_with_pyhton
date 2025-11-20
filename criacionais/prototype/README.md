# Padrão Prototype - Exemplo de Documento

## Visão Geral
Este exemplo demonstra a implementação do **Padrão Prototype** para criar novos objetos clonando instâncias existentes. O padrão é útil quando a criação de objetos é custosa ou quando você precisa de objetos similares com pequenas variações.

## Estrutura do Padrão
![](../../assets/img/prototype.png)
### Interface Prototype
- `Prototype` - Interface base que define o método `clone()`

### Prototype Concreto
- `Document` - Classe que implementa a clonagem e representa um documento personalizável

## Principais Benefícios

1. **Performance** - Evita o custo de criação de objetos complexos do zero
2. **Flexibilidade** - Permite criar variações de objetos existentes
3. **Simplicidade** - Reduz a necessidade de subclasses para variações
4. **Configuração Dinâmica** - Objetos podem ser configurados em tempo de execução

## Implementação

### Clonagem Profunda
O exemplo usa `copy.deepcopy()` para garantir que estruturas mutáveis (como dicionários) sejam clonadas corretamente:

```python
def clone(self):
    return copy.deepcopy(self)
```

### Uso Prático
```python
# Documento base (protótipo)
prototype_doc = Document(
    title="Template Básico",
    content="Conteúdo padrão do documento.",
    metadata={"author": "Sistema", "version": 1}
)

# Criando variações por clonagem
invoice = prototype_doc.clone()
invoice.title = "Nota Fiscal"
invoice.metadata["document_type"] = "NFe"

report = prototype_doc.clone()
report.title = "Relatório Financeiro"
report.metadata["document_type"] = "Report"
```

## Saída
```
Document(title=Nota Fiscal, content=Conteúdo padrão do documento., metadata={'author': 'Sistema', 'version': 1, 'document_type': 'NFe'})
Document(title=Relatório Financeiro, content=Conteúdo padrão do documento., metadata={'author': 'Sistema', 'version': 1, 'document_type': 'Report'})
```

## Quando Usar
- Quando a criação de objetos é custosa (conexões de rede, cálculos complexos)
- Quando você precisa de muitos objetos similares com pequenas diferenças
- Quando você quer evitar a criação de muitas subclasses
- Quando objetos precisam ser configurados dinamicamente
- Quando você tem um conjunto de objetos pré-configurados como templates