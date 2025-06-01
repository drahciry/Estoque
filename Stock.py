# Importações de módulos e bibliotecas
from Exceptions import EmptyStockError, InvalidProductError, InvalidCategoryError, InvalidPathError
from Product import Product
from Price import Price
import json as j
import os

class Stock:
    # Método construtor
    def __init__(self):
        self.__stock = {
            "current_id": 0,  # Contador para ID (fica armazenado no dicionário para quando carregar de um JSON)
            "total_value": 0, # Armazena valor total em estoque
            "products": {},   # Armazena todas os produtos
            "category": {}    # Armazena produtos por categoria
        }

    # Método para obter todos os dados do estoque
    def get_stock(self):
        return self.__stock
    
    # Método para obter todos os produtos em estoque
    def get_products(self):
        # Verifica se estoque está cheio
        if self.__is_empty():
            raise EmptyStockError('Estoque está vazio.')
        # Retorna produtos em uma lista
        return self.__stock["products"].values()

    # Método para exibir todos os produtos em estoque
    def display_products(self):
        # Verifica se estoque está cheio
        if self.__is_empty():
            raise EmptyStockError('Estoque está vazio.')
        # Exibe produtos
        for product in self.__stock["products"].values():
            print(product)

    # Método para obter valor total em estoque
    def get_total_value(self):
        return self.__stock["total_value"]

    # Método para verificar se estoque está cheio
    def __is_empty(self):
        return not self.__stock["products"]
    
    # Método para adicionar novos produtos em estoque
    def append_product(self, product: Product):
        # Verifica se o produto inserido é uma instância de Product
        if not isinstance(product, Product):
            raise InvalidProductError('Objeto inserido não é uma instância de Product.')
        # Verifica se o produto já existe em estoque
        if product.get_id() in self.__stock["products"]:
            raise InvalidProductError(f'Produto com ID {product.get_id()} já existe no estoque.')
        # Incrementa o valor total em estoque
        self.__stock["total_value"] += product.get_price() * product.get_quantify()
        # Adiciona o produto ao estoque
        self.__stock["products"][str(product.get_id())] = product
        category = product.get_category()
        # Verifica se a categoria do produto já existe
        if not self.__stock["category"].get(category, None):
            self.__stock["category"][category] = list()
        # Armazena produto na sua categoria
        self.__stock["category"][category].append(product)

    # Método para deletar produto do estoque
    def delete_product(self, id: int):
        # Verifica se entrada é um int
        if not isinstance(id, int):
            raise ValueError('O ID deve ser um número inteiro.')
        # Verifica se o produto com ID inserido existe
        if not self.__stock["products"].get(str(id), None):
            raise InvalidProductError(f'Produto de ID {id:0>5} não existe no estoque.')
        product = self.__stock["products"][str(id)]
        # Decrementa do valor total que tem em estoque
        self.__stock["total_value"] -= product.get_price() * product.get_quantify()
        # Remove produto do estoque
        del self.__stock["products"][str(id)]
        category = product.get_category()
        # Remove produto da categoria que pertencia
        self.__stock["category"][category].remove(product)
        # Verifica se ainda existe produtos na categoria
        if not self.__stock["category"][category]:
            del self.__stock["category"][category]

    # Método para obter todos os produtos por categoria
    def get_by_category(self, category: str):
        # Verifica se a entrada é válida
        if not isinstance(category, str) or not category.strip():
            raise InvalidCategoryError('Categoria inserida inválida (string vazia ou nula).')
        # Verifica se a categoria existe no estoque
        if not self.__stock["category"].get(category, None):
            raise InvalidCategoryError('Categoria não registrada no estoque.')
        # Retorna uma lista com todos os produtos da categoria inserida
        return self.__stock["products"][category]

    # Método para listar todos os produtos por categoria
    def display_by_category(self, category: str):
        # Verifica se a entrada é válida
        if not isinstance(category, str) or not category.strip():
            raise InvalidCategoryError('Categoria inserida inválida (string vazia ou nula).')
        # Verifica se a categoria existe no estoque
        if not self.__stock["category"].get(category, None):
            raise InvalidCategoryError('Categoria não registrada no estoque.')
        # Lista todos os produtos da categoria inserida
        for product in self.__stock["category"][category]:
            print(product)

    # Método para salvar estoque em arquivo JSON
    def save_stock_json(self, path: str):
        # Cria dicionário para ser salvo em JSON
        dict_data = {
            "current_id": self.__stock["current_id"],
            "total_value": self.__stock["total_value"],
            "products": {
                pid: product.to_dict() for pid, product in self.__stock["products"].items()
            } # Obs: "category" não está incluída pois há um método separado para categorias
        }
        # Salva estoque em JSON
        with open(path, 'w', encoding='utf-8') as file:
            j.dump(dict_data, file, indent=4, ensure_ascii=False)

    # Método para salvar todos os produtos por categoria em JSON
    def save_category_json(self, path: str):
        # Cria dicionário para ser salvo em JSON
        dict_data = {
            category: [product.to_dict() for product in products] for category, products in self.__stock["category"].items()
        }
        # Salva produtos por categoria em JSON
        with open(path, 'w', encoding='utf-8') as file:
            j.dump(dict_data, file, indent=4, ensure_ascii=False)

    # Método para carregar estoque já salvo em JSON
    def load_stock_json(self, path: str):
        # Verifica se arquivo JSON existe
        if not os.path.exists(path):
            raise InvalidPathError(f'Arquivo "{path}" não existe.')
        # Carrega dados de arquivo JSON
        with open(path, 'r', encoding='utf-8') as file:
            dict_data = j.load(file)
        # Lê do arquivo JSON todos os produtos salvos
        for key in dict_data["products"].keys():
            data = dict_data["products"][key]
            # Adiciona produto no estoque
            self.append_product(Product(
                data["id"],
                data["name"],
                Price(data["price"]),
                data["quantify"],
                data["category"]
            ))
        # Atualiza o próximo ID
        self.__stock["current_id"] = dict_data["current_id"]