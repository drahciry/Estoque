# Importações de módulos e bibliotecas
from Exceptions import EmptyStockError, InvalidProductError, InvalidCategoryError, InvalidPathError, InvalidPriceError
from Product import Product
from decimal import Decimal
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
        self.__change = False

    # Método para obter todos os dados do estoque
    def get_stock(self) -> dict:
        return self.__stock
    
    # Método para obter status de alteração
    def get_change(self) -> bool:
        return self.__change
    
    # Método para obter todos os produtos em estoque
    def get_products(self) -> list:
        # Verifica se estoque está cheio
        if self.__is_empty():
            raise EmptyStockError('Estoque está vazio.')
        # Retorna produtos em uma lista
        return self.__stock["products"].values()
    
    # Método para obter valor total em estoque
    def get_total_value(self) -> Decimal:
        return self.__stock["total_value"]

    # Método para verificar se estoque está cheio
    def __is_empty(self) -> bool:
        return not self.__stock["products"]
    
    # Método para adicionar novos produtos em estoque
    def append_product(self, name: str, price: Price, quantify: int, category: str):
        # Incrementa o ID
        self.__stock["current_id"] += 1
        # Instancia Product
        product = Product(self.__stock["current_id"], name, price, quantify, category)
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
        # Altera variável de controle de alteração
        self.__change = True

    # Método para deletar produto do estoque
    def delete_product(self, id: int):
        # Verifica se entrada é um int
        if not isinstance(id, int):
            raise ValueError('O ID deve ser um número inteiro.')
        # Verifica se entrada é maior que 0
        if id <= 0:
            raise ValueError('O ID deve ser maior que 0.')
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
        # Altera variável de controle de alteração
        self.__change = True

    # Método para obter todos os produtos por categoria
    def get_by_category(self, category: str):
        # Verifica se a entrada é válida
        if not isinstance(category, str) or not category.strip():
            raise InvalidCategoryError('Categoria inserida inválida (string vazia ou nula).')
        # Verifica se a categoria existe no estoque
        if not self.__stock["category"].get(category, None):
            raise InvalidCategoryError('Categoria não registrada no estoque.')
        # Retorna uma lista com todos os produtos da categoria inserida
        return self.__stock["category"][category]

    # Método para salvar estoque em arquivo JSON
    def save_stock_json(self, path: str):
        # Cria dicionário para ser salvo em JSON
        dict_data = {
            "total_value": self.__stock["total_value"],
            "products": {
                pid: product.to_dict() for pid, product in self.__stock["products"].items()
            } # Obs: "category" não está incluída pois há um método separado para categorias
        }
        # Salva estoque em JSON
        with open(path, 'w', encoding='utf-8') as file:
            j.dump(dict_data, file, indent=4, ensure_ascii=False)
        # Altera variável de controle de alteração
        self.__change = False

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
        # Limpa estoque para evitar duplicação
        self.__stock["products"].clear()
        self.__stock["category"].clear()
        # Variável que guardará maior ID atualizado
        max_id = 0
        # Lê do arquivo JSON todos os produtos salvos
        for data in dict_data["products"].values():
            # Cria produto com ID do arquivo carregado
            product = Product(
                int(data["id"]),
                data["name"],
                Price(data["price"]),
                data["quantify"],
                data["category"]
            )
            # Adiciona produto no estoque
            self.__stock["products"][str(product.get_id())] = product 
            category = product.get_category()
            # Verifica se a categoria do produto já existe
            if category not in self.__stock["category"]:
                self.__stock["category"][category] = list()
            # Armazena produto na sua categoria
            self.__stock["category"][category].append(product)
            # Acha o maior ID para atualizar contador
            if product.get_id() > max_id:
                max_id = product.get_id()
        # Atualiza contador
        self.__stock["current_id"] = max_id
        # Atualiza valor total em estoque
        self.__stock["total_value"] = dict_data.get("total_value", Decimal("0"))