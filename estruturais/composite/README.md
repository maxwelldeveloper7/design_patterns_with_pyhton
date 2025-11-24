# Padrão Composite - Sistema de Arquivos

Este projeto demonstra a implementação do **Padrão Composite** em Python através de um sistema de arquivos simplificado.

## 📁 Sobre o Padrão Composite

O Padrão Composite permite tratar objetos individuais e composições de objetos de maneira uniforme. É especialmente útil quando você precisa trabalhar com estruturas hierárquicas em árvore.

## 🏗️ Estrutura do Código
![](../../assets/img/composite.png)
### Componentes Principais

- **`FileSystemComponent`** (ABC): Interface comum que define operações para arquivos e pastas
- **`File`** (Leaf): Representa arquivos simples sem filhos
- **`Directory`** (Composite): Representa pastas que podem conter outros componentes

### Funcionalidades

- ✅ Criação de arquivos e diretórios
- ✅ Adição/remoção de componentes em diretórios
- ✅ Exibição hierárquica da estrutura de pastas
- ✅ Tratamento uniforme de arquivos e pastas

## 🚀 Como Executar

```bash
python estruturais/composite/exemplo_files_directores.py
```

## 📋 Exemplo de Saída

```
[root]
  [imagens]
    - foto.png
  [documentos]
    - documento.pdf
    - dados.csv
```

## 💡 Vantagens do Padrão

- **Simplicidade**: Trata objetos simples e compostos uniformemente
- **Flexibilidade**: Fácil adição de novos tipos de componentes
- **Recursividade**: Operações são aplicadas recursivamente na árvore
- **Manutenibilidade**: Código mais limpo e organizado

## 🎯 Casos de Uso

- Sistemas de arquivos
- Interfaces gráficas (widgets aninhados)
- Estruturas organizacionais
- Menus hierárquicos
- Árvores de expressões matemáticas