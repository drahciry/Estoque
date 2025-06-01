from decimal import Decimal, InvalidOperation
from Exceptions import InvalidPriceError

class Price:
    def __init__(self, price: str):
        self.set_price(price)

    def set_price(self, price: str):
        if not isinstance(price, str) or not price.strip():
            raise InvalidPriceError('Preço inserido inválido (string vazia ou nula).')
        try:
            value = Decimal(price)
        except InvalidOperation:
            raise InvalidPriceError('Valor não é um número decimal válido.')
        if value <= 0:
            raise InvalidPriceError('Valor deve ser um número decimal positivo.')
        self.__price = value

    def get_price(self):
        return self.__price