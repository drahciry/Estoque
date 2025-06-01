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