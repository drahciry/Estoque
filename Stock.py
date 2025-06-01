from Product import Product
from Exceptions import EmptyStockError, InvalidProductError, InvalidCategoryError

class Stock:
    def __init__(self):
        self.set_stock()
        self.__total_value = 0

    def set_stock(self):
        self.__stock = {
            "current_id": 0, # Contador para ID
            "products": {},  # Armazena todas os produtos
            "category": {}   # Armazena produtos por categoria
        }

    def get_stock(self):
        return self.__stock
    
    def get_products(self):
        if self.__is_empty():
            raise EmptyStockError('Estoque está vazio.')
        for product in self.__stock["products"].values():
            print(product)

    def get_total_value(self):
        return self.__total_value

    def __is_empty(self):
        return not self.__stock["products"]
    
    def append_product(self, product: Product):
        if not isinstance(product, Product):
            raise InvalidProductError('Objeto inserido não é uma instância de Product.')
        self.__total_value += product.get_price() * product.get_quantify()
        self.__stock["products"][str(product.get_id())] = product
        category = product.get_category()
        if not self.__stock["category"].get(category, None):
            self.__stock["category"][category] = list()
        self.__stock["category"][category].append(product)

    def delete_product(self, id: int):
        if not isinstance(id, int):
            raise ValueError('O ID deve ser um número inteiro.')
        if not self.__stock["products"].get(str(id), None):
            raise InvalidProductError(f'Produto de ID {id:0>5} não existe no estoque.')
        product = self.__stock["products"][str(id)]
        self.__total_value -= product.get_price() * product.get_quantify()
        del self.__stock["products"][str(id)]
        category = product.get_category()
        self.__stock["category"][category].remove(product)
        if not self.__stock["category"][category]:
            del self.__stock["category"][category]

    def list_category(self, category: str):
        if not self.__stock["category"].get(category, None):
            raise InvalidCategoryError('Categoria não registrada no estoque.')
        for product in self.__stock["category"][category]:
            print(product)