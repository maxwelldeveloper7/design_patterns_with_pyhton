# Sistema de Acesso a Dados Sensíveis - Padrão Proxy

Este projeto demonstra a implementação do padrão de design **Proxy** em Python através de um sistema que controla o acesso a dados sensíveis com autenticação e cache.

## Sobre o Padrão Proxy

O padrão Proxy fornece um substituto ou representante para outro objeto, controlando o acesso a ele. O proxy mantém a mesma interface do objeto original, mas adiciona funcionalidades como controle de acesso, cache ou lazy loading.

## Estrutura do Sistema
![](../../assets/img/proxy.png)
### `SensitiveDataService` (Subject Interface)
Interface comum que define o contrato:
- `get_data()`: Método para obter dados sensíveis

### `RealSensitiveDataService` (Real Subject)
Implementação concreta que acessa o recurso real:
- Simula operação pesada (acesso a servidor remoto)
- Retorna dados confidenciais

### `SensitiveDataProxy` (Proxy)
Controla o acesso ao serviço real implementando:
- **Autenticação**: Verifica credenciais do usuário
- **Cache**: Evita chamadas desnecessárias ao serviço real
- **Controle de acesso**: Nega acesso a usuários não autorizados

## Funcionalidades do Proxy

### 1. Controle de Acesso
```python
def _is_authenticated(self) -> bool:
    return self.user == "admin" and self.password == "1234"
```

### 2. Cache Simples
- Primeira chamada: acessa o serviço real
- Chamadas subsequentes: retorna dados do cache

### 3. Interface Transparente
- Cliente usa o proxy como se fosse o serviço real
- Mesma interface, funcionalidades adicionais

## Como Usar

```python
# Tentativa com credenciais inválidas
proxy_invalid = SensitiveDataProxy("guest", "1111")
print(proxy_invalid.get_data())  # Acesso negado

# Acesso com credenciais válidas
proxy_valid = SensitiveDataProxy("admin", "1234")
print(proxy_valid.get_data())    # Primeira chamada - acessa serviço real
print(proxy_valid.get_data())    # Segunda chamada - usa cache
```

## Execução

```bash
python exemplo_proxy.py
```

**Saída esperada:**
```
Tentativa com usuário inválido:
[Proxy] Acesso negado: credenciais inválidas.

Acesso com usuário válido:
[Proxy] Cache vazio. Buscando dados no serviço real...
[RealService] Acessando dados sensíveis no servidor remoto...
DADOS SIGILOSOS: Relatórios confidenciais.
[Proxy] Retornando dados do cache.
DADOS SIGILOSOS: Relatórios confidenciais.
```

## Tipos de Proxy

### 1. Protection Proxy (Usado no exemplo)
- Controla acesso baseado em permissões
- Implementa autenticação e autorização

### 2. Virtual Proxy
- Lazy loading de objetos pesados
- Cria objeto real apenas quando necessário

### 3. Caching Proxy
- Armazena resultados de operações caras
- Melhora performance evitando reprocessamento

### 4. Remote Proxy
- Representa objeto em espaço de endereço diferente
- Usado em sistemas distribuídos

## Vantagens do Proxy

- **Segurança**: Controla acesso a recursos sensíveis
- **Performance**: Cache reduz chamadas custosas
- **Transparência**: Cliente não percebe a diferença
- **Flexibilidade**: Adiciona funcionalidades sem alterar o objeto real

## Casos de Uso Práticos

- **Sistemas de autenticação**: Controle de acesso a APIs
- **Cache de dados**: Otimização de consultas a banco
- **Lazy loading**: Carregamento sob demanda de recursos
- **Logging e auditoria**: Registro de acessos a recursos
- **Rate limiting**: Controle de frequência de chamadas

## Diferença Entre Padrões

### Proxy vs Decorator
- **Proxy**: Controla acesso ao objeto
- **Decorator**: Adiciona comportamentos ao objeto

### Proxy vs Adapter
- **Proxy**: Mesma interface do objeto original
- **Adapter**: Converte interfaces incompatíveis

## Considerações de Implementação

- Proxy deve implementar a mesma interface do objeto real
- Cuidado com vazamentos de memória em cache
- Considere thread-safety em ambientes concorrentes
- Implemente estratégias de invalidação de cache quando necessário