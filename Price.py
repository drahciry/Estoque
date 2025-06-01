# Importações de módulos e bibliotecas
from decimal import Decimal, InvalidOperation
from Exceptions import InvalidPriceError

class Price:
    # Método construtor
    def __init__(self, price: str):
        self.set_price(price)

    # Método para modificar preço
    def set_price(self, price: str):
        # Verifica se entrada é válida
        if not isinstance(price, str) or not price.strip():
            raise InvalidPriceError('Preço inserido inválido (string vazia ou nula).')
        # Verifica se entrada é numérica
        try:
            value = Decimal(price)
        except InvalidOperation:
            raise InvalidPriceError('Valor não é um número decimal válido.')
        # Verifica se entrada é positiva
        if value <= 0:
            raise InvalidPriceError('Valor deve ser um número decimal positivo.')
        self.__price = value

    # Método para obter preço
    def get_price(self):
        return self.__price