from Exceptions import EmptyStockError, InvalidPriceError,  InvalidProductError, InvalidCategoryError, InvalidPathError
from Price import Price
from Stock import Stock
from time import sleep

# Função para obter preço válido (Price)
def getPrice(name: str) -> Price:
    # Realiza tentativa até que entrada seja válida
    while True:
        try:
            price = Price(input(f'Insira o valor do produto {name}: R$ '))
            return price
        # Preço inserido não é válido
        except InvalidPriceError as e:
            print(f'Preço inválido: {e}')
            sleep(1.5)

# Função para obter quantidade válida
def getQuantify(name: str) -> int:
    # Realiza tentativa até que entrada seja válida
    while True:
        try:
            quantify = int(input(f'Insira a quantidade em estoque do produto {name}: '))
            # Só retorna a quantidade se valor for inteiro e positivo
            if quantify >= 0:
                return quantify
            print('Quantidade inserida inválida. Quantidade deve não pode ser negativa.')
        # Quantidade inserida não é um inteiro
        except ValueError:
            print('Quantidade inserida inválida. Quantidade deve ser um valor inteiro.')
            sleep(1.5)

# Função para adicionar produtos no estoque
def appendProduct(stock: Stock):
    print()
    # Realiza captura de atributos do produto (Product)
    name = input('Insira o nome do produto: ')
    price = getPrice(name)
    quantify = getQuantify(name)
    category = input(f'Insira a categoria do produto {name}: ')
    stock.append_product(name, price, quantify, category)
    print('\nProduto adicionado com sucesso!')
    sleep(1.2)
            
# Função para exibir estoque
def displayStock(stock: Stock):
    print()
    try:
        print('Produtos em estoque:')
        for product in stock.get_products():
            print()
            print(product)
            sleep(2)
            
    except EmptyStockError:
        print('\nEstoque vazio.')
        sleep(1.2)
        
# Função para deletar produto do estoque
def deleteProduct(stock: Stock):
    print()
    # Captura ID do produto que deseja remover do estoque
    while True:
        try:
            id_product = int(input('Insira o ID do produto que deseja remover ou insira "0" para cancelar: '))
            if id_product == 0:
                print('\nOperação cancelada!')
                return
            stock.delete_product(id_product)
            print('Produto removido do estoque com sucesso!')
            sleep(1.2)
            return
        # ID inválido
        except ValueError as e:
            print(f'ID inserido inválido. {e}')
            sleep(1.5)
        # Produto não existe no estoque
        except InvalidProductError as e:
            print(f'Erro: {e}')
            sleep(1.5)
    
# Função que exibe o total em estoque
def totalValue(stock: Stock):
    print()
    print(f'Valor total em estoque: R$ {stock.get_total_value():.2f}')
    sleep(1.2)
    
# Função que lista todos os produtos por categoria
def listCategory(stock: Stock):
    # Captura a categoria buscada
    category = input('\nInsira a categoria buscada: ')
    # Verificação de categoria existente
    try:
        # Exibe todos os produtos pela categoria inserida
        print(f'\nProdutos em {category}:')
        for product in stock.get_by_category(category):
            print()
            print(product)
            sleep(2)
    # Categoria não existe
    except InvalidCategoryError as e:
        print(e)
        
# Função que carrega dados de estoque a partir de um JSON
def loadStock(stock: Stock):
    # Verifica se arquivo existe
    try:
        # Se arquivo existir, vai recarregar todo o estoque
        return stock.load_stock_json('stock.json')
    # Se arquivo não existir, apenas passa
    except InvalidPathError:
        pass
        
# Função que salva todas as alterações no arquivo JSON
def saveChanges(stock: Stock):
    stock.save_stock_json('stock.json')
    stock.save_category_json('stock_categories.json')
    
# Função que retorna se há alterações no estoque
def hasChange(stock: Stock) -> bool:
    return stock.get_change()
    
# Função para obter opção válida
def getOption():
    print()
    while True:
        try:
            return int(input('Insira a ação desejada: '))
        except ValueError:
            print('Opção inserida inválida. A escolha deve ser um valor inteiro.')
            
# Função para obter resposta de salvamento
def getAnswer():
    while True:
        answer = input('\nHá alterações não salvas no estoque. Deseja salvar? (S/N): ').upper()
        if answer == 'S' or answer == 'N':
            return answer
        print('Resposta inserida inválida. Insira somente "S" para Sim e "N" para Não.')
        sleep(1.5)
    
# Função principal que controla fluxo
def main():
    print('-'*10, 'Gerenciamento de estoque', '-'*10)
    print('\nCarregando sistema...')
    sleep(1)
    # Inicializa variáveis
    option = None
    stock = Stock()
    # Carrega estoque já salvo
    loadStock(stock)
    # Menu interativo com opções
    while option != 0:
        print(
            '\nOpções disponíveis:\n'
            '[1] Adicionar produto ao estoque\n'
            '[2] Listar todos os produtos do estoque\n'
            '[3] Remover produto do estoque\n'
            '[4] Relatório do valor total em estoque\n'
            '[5] Listar produtos por categoria\n'
            '[0] Sair do programa'
        )
        # Captura opção do usuário
        option = getOption()
        # Adiciona produto ao estoque
        if option == 1:
            appendProduct(stock)
        # Exibe produtos em estoque
        elif option == 2:
            displayStock(stock)
        # Deleta produto do estoque
        elif option == 3:
            deleteProduct(stock)
        # Exibe valor total em estoque
        elif option == 4:
            totalValue(stock)
        # Lista produtos por categoria
        elif option == 5:
            listCategory(stock)
        # Encerra programa
        elif option == 0:
            # Verifica se há alterações não salvas no estoque
            if hasChange(stock):
                # Captura resposta do usuário
                answer = getAnswer()
                # Se a respostar for 'S', realiza o salvamento
                if answer == 'S':
                    # Salva todas as alterações
                    saveChanges(stock)
                    print('Alterações salvas com sucesso!')
                    sleep(1.2)
            # Mensagem de encerramento do programa
            print('\nEncerrando programa...')
            sleep(1.2)
        # Exibe mensagem dizendo que a opção é inválida
        else:
            print('\nOpçao inserida inválida. Insira somente as opções listadas.')
            sleep(1.2)
    # Programa encerrado
    print('Programa encerrado!\n')
    

# Segurança
if __name__ == '__main__':
    main()