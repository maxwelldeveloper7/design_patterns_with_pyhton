# -------------------------------
# Interface esperada pelo sistema
# -------------------------------

class PaymentProcessor:
    """
    Interface padrão que o sistema moderno espera utilizar.
    Garante padronização e permite desacoplamento da implementação.
    """
    def process_payment(self, amount):
        raise NotImplementedError("A subclasse deve implementar process_payment().")


# -------------------------------
# Código legado (não pode ser alterado)
# -------------------------------

class LegacyPaymentSystem:
    """
    Biblioteca antiga com interface incompatível.
    O método make_transaction() possui outro nome e outra semântica.
    """
    def make_transaction(self, value):
        print(f"[LEGADO] Pagamento realizado no valor de R$ {value:.2f}")


# -------------------------------
# Adapter
# -------------------------------

class PaymentAdapter(PaymentProcessor):
    """
    Adapter que converte a interface legada para a interface moderna.
    Mantém o sistema desacoplado e evita reescrever código legado.
    """

    def __init__(self, legacy_system):
        # Guarda a instância do sistema legada.
        self._legacy_system = legacy_system

    def process_payment(self, amount):
        """
        Adapta a chamada do método moderno para o método legado.
        Este método faz a tradução entre as interfaces.
        """
        # Aqui ocorre a adaptação para a interface antiga.
        amount += 10  # Adiciona taxa de serviço
        self._legacy_system.make_transaction(amount)


# -------------------------------
# Uso prático do Adapter
# -------------------------------

# Sistema legada pré-existente
legacy = LegacyPaymentSystem()

# Adaptando a interface legada para o padrão moderno
payment_processor = PaymentAdapter(legacy)

# Agora, o sistema moderno usa o método que ele espera ter:
payment_processor.process_payment(150.00)
