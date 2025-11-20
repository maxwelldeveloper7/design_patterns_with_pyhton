# Padrão Factory Method - Sistema de Notificação

Esta implementação demonstra o padrão de design Factory Method usando um sistema de notificação que pode enviar mensagens através de diferentes canais (Email, SMS, Push).

## Visão Geral do Padrão

O padrão Factory Method fornece uma interface para criar objetos sem especificar suas classes exatas. Ele delega a criação de objetos para subclasses, promovendo baixo acoplamento e extensibilidade.

## Componentes
![](../../assets/img/factory_method.png)

### Interface do Produto
- **`Notificacao`**: Classe base abstrata que define a interface comum para todos os tipos de notificação
  - `enviar(mensagem: str)`: Método abstrato que deve ser implementado pelos produtos concretos

### Produtos Concretos
- **`NotificacaoEmail`**: Envia notificações via email
- **`NotificacaoSMS`**: Envia notificações via SMS
- **`NotificacaoPush`**: Envia notificações push

### Criador
- **`NotificacaoCreator`**: Classe criadora abstrata que define o método factory
  - `factory_method()`: Método abstrato para criar objetos de notificação
  - `enviar_notificacao(mensagem: str)`: Método de alto nível que usa o método factory

### Criadores Concretos
- **`EmailCreator`**: Cria instâncias de notificação por email
- **`SMSCreator`**: Cria instâncias de notificação por SMS  
- **`PushCreator`**: Cria instâncias de notificação push

## Exemplo de Uso

```python
# Criar criadores específicos de notificação
email = EmailCreator()
sms = SMSCreator()
push = PushCreator()

# Enviar notificações usando a mesma interface
email.enviar_notificacao("Sua matrícula foi confirmada.")
sms.enviar_notificacao("Código de verificação: 8421.")
push.enviar_notificacao("Nova atualização disponível!")
```

## Benefícios

- **Extensibilidade**: Fácil de adicionar novos tipos de notificação sem modificar o código existente
- **Baixo Acoplamento**: O código cliente depende apenas de abstrações, não de implementações concretas
- **Responsabilidade Única**: Cada criador é responsável por criar um tipo de notificação
- **Princípio Aberto/Fechado**: Aberto para extensão (novos tipos de notificação) mas fechado para modificação

## Executando o Código

```bash
python notification.py
```

Saída esperada:
```
[E-MAIL] Enviando mensagem: Sua matrícula foi confirmada.
[SMS] Enviando mensagem: Código de verificação: 8421.
[PUSH] Enviando mensagem: Nova atualização disponível!
```