# Sistema de Processamento de Pagamentos - Padrão Adapter

Este projeto demonstra a implementação do padrão de design **Adapter** em Python através de um sistema de processamento de pagamentos que integra código legado com interfaces modernas.

## Sobre o Padrão Adapter

O padrão Adapter permite que classes com interfaces incompatíveis trabalhem juntas, convertendo a interface de uma classe em outra interface esperada pelos clientes.

## Estrutura do Código
![](../../assets/img/adapter.png)
### `PaymentProcessor` (Interface)
Interface padrão que define o contrato esperado pelo sistema moderno:
- `process_payment(amount)`: Método padronizado para processar pagamentos

### `LegacyPaymentSystem` (Sistema Legado)
Biblioteca antiga com interface incompatível:
- `make_transaction(value)`: Método legado com nome e semântica diferentes

### `PaymentAdapter` (Adapter)
Classe que adapta a interface legada para a interface moderna:
- Implementa `PaymentProcessor`
- Encapsula `LegacyPaymentSystem`
- Traduz chamadas entre as interfaces

## Como Funciona

```python
# Sistema legado existente
legacy = LegacyPaymentSystem()

# Adapter que conecta legado ao moderno
payment_processor = PaymentAdapter(legacy)

# Uso da interface moderna
payment_processor.process_payment(150.00)
```

## Execução

```bash
python exemplo_process_payment.py
```

**Saída esperada:**
```
[LEGADO] Pagamento realizado no valor de R$ 160.00
```

## Vantagens do Adapter

- **Reutilização**: Aproveita código legado sem modificações
- **Desacoplamento**: Isola diferenças de interface
- **Flexibilidade**: Permite evolução gradual do sistema
- **Manutenibilidade**: Centraliza adaptações em uma classe

## Casos de Uso

- Integração com APIs de terceiros
- Migração gradual de sistemas legados
- Compatibilidade entre versões de bibliotecas
- Padronização de interfaces heterogêneas