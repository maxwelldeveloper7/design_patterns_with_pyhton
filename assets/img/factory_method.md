@startuml
title Factory Method - Sistema de Notificações

' Interfaces e Classes Abstratas
interface Notificacao {
    +enviar(mensagem: str)
}

abstract class NotificacaoCreator {
    +enviar_notificacao(mensagem: str)
    +factory_method(): Notificacao
}

' Produtos Concretos
class NotificacaoEmail {
    +enviar(mensagem: str)
}

class NotificacaoSMS {
    +enviar(mensagem: str)
}

class NotificacaoPush {
    +enviar(mensagem: str)
}

' Criadores Concretos
class EmailCreator {
    +factory_method(): Notificacao
}

class SMSCreator {
    +factory_method(): Notificacao
}

class PushCreator {
    +factory_method(): Notificacao
}

' Relacionamentos (Herança)
NotificacaoCreator <|-- EmailCreator
NotificacaoCreator <|-- SMSCreator
NotificacaoCreator <|-- PushCreator

Notificacao <|-- NotificacaoEmail
Notificacao <|-- NotificacaoSMS
Notificacao <|-- NotificacaoPush

' Dependências
NotificacaoCreator --> Notificacao : cria

@enduml
