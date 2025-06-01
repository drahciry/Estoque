# Módulo para criação de exceções e erros

class InvalidCategoryError(Exception):
    def __init__(self, message: str):
        super().__init__(message)

class InvalidPriceError(Exception):
    def __init__(self, message: str):
        super().__init__(message)

class InvalidNameError(Exception):
    def __init__(self, message: str):
        super().__init__(message)

class EmptyStockError(Exception):
    def __init__(self, message: str):
        super().__init__(message)

class InvalidProductError(Exception):
    def __init__(self, message: str):
        super().__init__(message)

class InvalidPathError(Exception):
    def __init__(self, message: str):
        super().__init__(message)

class InvalidQuantifyError(Exception):
    def __init__(self, message: str):
        super().__init__(message)