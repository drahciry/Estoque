# Importações de módulos e bibliotecas
from Exceptions import InvalidCategoryError, InvalidNameError, InvalidPriceError, InvalidQuantifyError
from Price import Price

class Product:
    # Método construtor
    def __init__(self, id: int, name: str, price: Price, quantify: int, category: str):
        self.__id = id
        self.set_name(name)
        self.set_price(price)
        self.set_quantify(quantify)
        self.set_category(category)

    # Método para obter ID
    def get_id(self):
        return self.__id

    # Método para modificar nome 
    def set_name(self, name: str):
        # Verifica se entrada é válida
        if not isinstance(name, str) or not name.strip():
            raise InvalidNameError('Nome inserido inválido (string vazia ou nula).')
        self.__name = name
        
    # Método para obter nome    
    def get_name(self):
        return self.__name
    
    # Método para modificar preço
    def set_price(self, price: Price):
        # Verifica se entrada é uma instância de Price
        if not isinstance(price, Price):
            raise InvalidPriceError('Objeto inserido não é uma instância de Price.')
        self.__price = price
    
    # Método para obter preço
    def get_price(self):
        return self.__price.get_price()
    
    # Método para modificar quantidade
    def set_quantify(self, quantify: int):
        # Verifica se entrada é um inteiro
        if not isinstance(quantify, int):
            raise InvalidQuantifyError('Valor deve ser um inteiro.')
        # Verifica se entrada não é negativa
        if quantify < 0:
            raise InvalidQuantifyError('Valor dever não deve ser um inteiro negativo.')
        self.__quantify = quantify
        
    # Método para obter quantidade
    def get_quantify(self):
        return self.__quantify
    
    # Método para modificar categoria
    def set_category(self, category: str):
        # Verifica se entrada é válida
        if not isinstance(category, str) or not category.strip():
            raise InvalidCategoryError('Categoria inserida inválida (string vazia ou nula).')
        self.__category = category

    # Método para obter categoria
    def get_category(self):
        return self.__category
    
    # Método para retornar um dicionário com todos os dados do produto
    def to_dict(self):
        return {
            "id": self.get_id(),
            "name": self.get_name(),
            "price": self.get_price(),
            "quantify": self.get_quantify(),
            "category": self.get_category()
        }
    
    # Método para exibir todos os dados do produto
    def __str__(self):
        return (f'ID do produto: {self.get_id():0>5}\n'
                f'Nome: {self.get_name()}\n'
                f'Preço: R$ {self.get_price():.2f}\n'
                f'Quantidade em estoque: {self.get_quantify()}\n'
                f'Categoria: {self.get_category()}')