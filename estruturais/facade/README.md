# Sistema de Pedidos - Padrão Facade

Este projeto demonstra a implementação do padrão de design **Facade** em Python através de um sistema de e-commerce que simplifica o processo complexo de criação de pedidos.

## Sobre o Padrão Facade

O padrão Facade fornece uma interface unificada e simplificada para um conjunto de interfaces mais complexas em um subsistema. Ele define uma interface de nível mais alto que torna o subsistema mais fácil de usar.

## Estrutura do Sistema
![](../../assets/img/facade.png)
### Subsistemas Complexos

#### `InventorySystem` (Sistema de Estoque)
- `check_stock(product_id)`: Verifica disponibilidade do produto

#### `PaymentSystem` (Sistema de Pagamento)
- `process_payment(value)`: Processa o pagamento do pedido

#### `InvoiceSystem` (Sistema de Nota Fiscal)
- `generate_invoice(product_id, value)`: Emite nota fiscal

#### `ShippingSystem` (Sistema de Entrega)
- `arrange_delivery(product_id)`: Organiza a entrega do produto

### `OrderFacade` (Fachada)
Interface simplificada que coordena todos os subsistemas:
- `place_order(product_id, value)`: Executa todo o fluxo de pedido

## Fluxo do Pedido

1. **Verificação de estoque** - Confirma disponibilidade
2. **Processamento de pagamento** - Valida e processa pagamento
3. **Emissão de nota fiscal** - Gera documentação fiscal
4. **Organização da entrega** - Prepara envio do produto

## Como Usar

```python
# Instanciando subsistemas
inventory = InventorySystem()
payment = PaymentSystem()
invoice = InvoiceSystem()
shipping = ShippingSystem()

# Criando a fachada
order_service = OrderFacade(inventory, payment, invoice, shipping)

# Cliente usa apenas um método simples
order_service.place_order(product_id=123, value=299.90)
```

## Execução

```bash
python exemplo_facade.py
```

**Saída esperada:**
```
[Estoque] Verificando disponibilidade do produto 123...
[Pagamento] Processando pagamento de R$ 299.90...
[Nota Fiscal] Emitindo NF para produto 123 no valor de R$299.90.
[Entrega] Organizando envio do produto 123 para o cliente.

[Pedido] Pedido concluído com sucesso!
```

## Vantagens do Facade

- **Simplicidade**: Interface única para operações complexas
- **Desacoplamento**: Cliente não precisa conhecer subsistemas internos
- **Manutenibilidade**: Mudanças internas não afetam o cliente
- **Reutilização**: Fachada pode ser usada por diferentes clientes

## Casos de Uso Práticos

- APIs que agregam múltiplos serviços
- Sistemas de e-commerce com múltiplas etapas
- Bibliotecas que simplificam frameworks complexos
- Interfaces para sistemas legados com múltiplos componentes

## Diferença Sem o Facade

Sem o padrão, o cliente precisaria:
```python
# Cliente gerenciando toda a complexidade
if inventory.check_stock(123):
    if payment.process_payment(299.90):
        invoice.generate_invoice(123, 299.90)
        shipping.arrange_delivery(123)
```

Com o Facade, apenas:
```python
# Cliente usa interface simples
order_service.place_order(123, 299.90)
```