from Price import Price
from Exceptions import InvalidCategoryError, InvalidNameError, InvalidPriceError

class Product:
    def __init__(self, id: int, name: str, price: Price, quantify: int, category: str):
        self.__id = id
        self.set_name(name)
        self.set_price(price)
        self.set_quantify(quantify)
        self.set_category(category)

    def get_id(self):
        return self.__id

    def set_name(self, name: str):
        if not isinstance(name, str) or not name.strip():
            raise InvalidNameError('Nome inserido inválido (string vazia ou nula).')
        self.__name = name
        
    def get_name(self):
        return self.__name
    
    def set_price(self, price: Price):
        if not isinstance(price, Price):
            raise InvalidPriceError('Objeto inserido não é uma instância de Price.')
        self.__price = price
        
    def get_price(self):
        return self.__price.get_price()
    
    def set_quantify(self, quantify: int):
        if not isinstance(quantify, int):
            raise ValueError('Valor deve ser um inteiro.')
        if quantify < 0:
            raise ValueError('Valor dever não deve ser um inteiro negativo.')
        self.__quantify = quantify
        
    def get_quantify(self):
        return self.__quantify
    
    def set_category(self, category: str):
        if not isinstance(category, str) or not category.strip():
            raise InvalidCategoryError('Categoria inserida inválida (string vazia ou nula).')
        self.__category = category

    def get_category(self):
        return self.__category
    
    def to_dict(self):
        return {
            "id": self.get_id(),
            "name": self.get_name(),
            "price": self.get_price(),
            "quantify": self.get_quantify(),
            "category": self.get_category()
        }
    
    def __str__(self):
        exit = (f'ID do produto: {self.get_id():0>5}\n'
            f'Nome: {self.get_name()}\n'
            f'Preço: R$ {self.get_price():.2f}\n'
            f'Quantidade em estoque: {self.get_quantify()}\n'
            f'Categoria: {self.get_category()}')
        return exit