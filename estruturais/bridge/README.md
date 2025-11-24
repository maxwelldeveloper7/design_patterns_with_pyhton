# Padrão Bridge - Sistema de Notificações

Este exemplo demonstra a implementação do padrão **Bridge** através de um sistema de notificações que separa a abstração (tipos de notificação) da implementação (meios de envio).

## O que é o Padrão Bridge?

O padrão Bridge desacopla uma abstração de sua implementação, permitindo que ambas variem independentemente. Ele é útil quando você quer evitar um vínculo permanente entre uma abstração e sua implementação.

## Estrutura do Código
![](../../assets/img/bridge.png)
### 1. Implementor (MessageSender)
```python
class MessageSender(ABC):
```
Interface abstrata que define o contrato para todas as implementações de envio de mensagem.

### 2. Implementações Concretas
- **EmailSender**: Envia mensagens via e-mail
- **SMSSender**: Envia mensagens via SMS

### 3. Abstração (Notification)
```python
class Notification:
```
Classe principal que utiliza uma implementação de `MessageSender` através de composição.

### 4. Abstração Refinada (UrgentNotification)
```python
class UrgentNotification(Notification):
```
Extensão da abstração base que adiciona comportamento específico (marca mensagens como urgentes).

## Como Executar

```bash
python exemplo_notification.py
```

## Saída Esperada

```
[Email] Para: usuario@dominio.com | Mensagem: Seu relatório está disponível.
[SMS] Para: 99999-9999 | Mensagem: [URGENTE] Falha no servidor detectada!
```

## Vantagens do Padrão Bridge

1. **Desacoplamento**: Abstração e implementação podem evoluir independentemente
2. **Flexibilidade**: Fácil adição de novos tipos de notificação ou meios de envio
3. **Reutilização**: Implementações podem ser compartilhadas entre diferentes abstrações
4. **Manutenibilidade**: Mudanças em uma parte não afetam a outra

## Exemplo de Extensão

Para adicionar um novo meio de envio (ex: WhatsApp):

```python
class WhatsAppSender(MessageSender):
    def send(self, recipient: str, message: str) -> None:
        print(f"[WhatsApp] Para: {recipient} | Mensagem: {message}")
```

Para adicionar um novo tipo de notificação:

```python
class ScheduledNotification(Notification):
    def notify(self, recipient: str, message: str) -> None:
        scheduled_message = f"[AGENDADO] {message}"
        self._sender.send(recipient, scheduled_message)
```