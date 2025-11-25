# Sistema de Mensagens com Criptografia e Compressão - Padrão Decorator

Este projeto demonstra a implementação do padrão de design **Decorator** em Python através de um sistema de envio de mensagens que permite adicionar funcionalidades como criptografia e compressão de forma dinâmica.

## Sobre o Padrão Decorator

O padrão Decorator permite adicionar novos comportamentos a objetos de forma dinâmica, sem alterar sua estrutura. É uma alternativa flexível à herança para estender funcionalidades.

## Estrutura do Código
![](../../assets/img/decorator.png)
### `MessageService` (Component)
Interface abstrata que define o contrato para envio de mensagens:
- `send(message)`: Método para enviar mensagens

### `BasicMessageService` (Concrete Component)
Implementação básica do serviço de mensagens:
- Envia mensagens sem processamento adicional

### `MessageDecorator` (Decorator Abstrato)
Classe base para todos os decoradores:
- Mantém referência ao componente original
- Delega chamadas para o objeto encapsulado

### Decoradores Concretos

#### `EncryptedMessageDecorator`
Adiciona criptografia às mensagens:
- Inverte o texto como exemplo de "pseudo-criptografia"
- Processa antes de delegar ao próximo componente

#### `CompressedMessageDecorator`
Adiciona compressão às mensagens:
- Remove espaços como exemplo de compressão simples
- Processa antes de delegar ao próximo componente

## Como Usar

```python
# Serviço básico
service = BasicMessageService()

# Apenas criptografia
encrypted_service = EncryptedMessageDecorator(service)

# Compressão + Criptografia (combinação)
compressed_encrypted = EncryptedMessageDecorator(
    CompressedMessageDecorator(service)
)

# Envio das mensagens
service.send("Mensagem simples.")
encrypted_service.send("Mensagem confidencial.")
compressed_encrypted.send("Mensagem com compressão e criptografia.")
```

## Execução

```bash
python exemplo_cript_compress.py
```

**Saída esperada:**
```
Enviando mensagem: Mensagem simples.
Enviando mensagem: .laicnedifnoc megasneM
Enviando mensagem: .aifargotpirceeoãsserpmocomegasneM
```

## Vantagens do Decorator

- **Flexibilidade**: Combina funcionalidades dinamicamente
- **Responsabilidade única**: Cada decorator tem uma função específica
- **Extensibilidade**: Fácil adição de novos comportamentos
- **Composição**: Permite múltiplas combinações de funcionalidades

## Casos de Uso Práticos

- Sistemas de logging com diferentes níveis
- Processamento de dados com múltiplas transformações
- APIs com autenticação, cache e validação
- Interfaces gráficas com bordas, sombras e efeitos