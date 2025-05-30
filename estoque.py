import json
import os
from time import sleep

def verificacao_int(mensagem_input, mensagem_erro):
    while True:
        try:
            valor = int(input(mensagem_input))
            if valor >= 0:
                return valor
            print(mensagem_erro)
            sleep(2)
        except ValueError:
            print('\nErro. Insira somente números inteiros.')
            sleep(2)

def verificacao_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor > 0:
                return valor
            print('\nEntrada inválida. Insira somente valores positivos.')
            sleep(2)
        except ValueError:
            print('\nErro. Insira somente números.')
            sleep(2)

def opcoes_menu():
    while True:
        print(
            '\n[1] Listar todos os produtos\n'
            '[2] Adicionar um novo produto\n'
            '[3] Atualizar as informações de um produto existente\n'
            '[4] Remover um produto\n'
            '[5] Relatório do valor total em estoque\n'
            '[6] Buscar um produto pelo nome\n'
            '[7] Listar produtos por categoria\n'
            '[8] Salvar as alterações\n'
            '[9] Sair do programa'
        )
        opcao = verificacao_int(
            '\nSelecione a ação pretendida: ',
            '\nEntrada inválida. Insira somente as opções listadas.'
            )
        if opcao in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return opcao
        print('\nEntrada inválida. Insira somente as opções listadas.')
        sleep(2)

def listar_produtos(estoque):
    if not len(estoque.get("produtos", [])) == 0:
        for produto in estoque.get('produtos', []):
            print(f"\nID: {produto.get('id', 'N/A'):0>5}", end=' | ')
            print(f"Nome: {produto.get('nome', 'N/A')}", end= ' | ')
            print(f"Preço: {produto.get('preco', 'N/A'):.2f}", end=' | ')
            print(f"Quantidade: {produto.get('quantidade', 'N/A')}", end=' | ')
            print(f"Categoria: {produto.get('categoria', 'N/A')}")
            sleep(2)
        return
    print('\nNão há produtos no estoque a serem listados.')
    sleep(2)

def adicionar_produto(estoque):
    nome = input('\nDigite o nome do novo produto: ')
    for produto in estoque.get("produtos", []):
        if produto["nome"].lower() == nome.lower():
            print(f'\nO produto {nome} já existe no estoque.')
            sleep(2)
            return estoque
    preco = verificacao_float('\nDigite o preço do novo produto: ')
    quantidade = verificacao_int(
        '\nDigite a quantidade disponível do novo produto: ',
        '\nEntrada inválida. Insira somente quantidades positivas.'
        )
    categoria = input('\nDigite a categoria do novo produto: ')
    id = max([produto["id"] for produto in estoque.get("produtos", [])], default=0) + 1
        
    if "produtos" in estoque:
        estoque["produtos"].append(
            {
                "id": id,
                "nome": nome,
                "preco": preco,
                "quantidade": quantidade,
                "categoria": categoria
                }
            )
        print('\nProduto adicionado com sucesso!')
        sleep(2)

        return estoque

def confirmacao():
    while True:
        resposta = input('\nDeseja realmente editar este produto? (S/N): ').upper()
        if resposta in ['S', 'N']:
            return True if resposta == 'S' else False
        print('\nEntrada inválida. Insira somente "S" para sim e "N" para não.')

def editar_produto(estoque):
    todos_id = [produto["id"] for produto in estoque.get('produtos', [])]    

    while True:
        id = verificacao_int(
            '\nDigite o ID do produto que deseja editar: ',
            '\nEntrada inválida. O ID deve ser inteiro e positivo.'
            )
        if id in todos_id:
            print('\nTodas as informações do produto:')
            produto = estoque.get('produtos', [])[id - 1]
            print(f"\nNome: {produto.get('nome', 'N/A')}", end= ' | ')
            print(f"Preço: {produto.get('preco', 'N/A')}", end=' | ')
            print(f"Quantidade: {produto.get('quantidade', 'N/A')}", end=' | ')
            print(f"Categoria: {produto.get('categoria', 'N/A')}")
            sleep(2)

            while True:
                print(
                    '\n[1] Editar nome\n'
                    '[2] Editar preço\n'
                    '[3] Editar quantidade\n'
                    '[4] Editar categoria'
                )
                opcao = verificacao_int(
                    '\nSelecione a ação pretendida: ',
                    '\nEntrada inválida. Insira somente as opções listadas.'
                    )
                if opcao in [1, 2, 3, 4]:
                        if opcao == 1:
                            novo_nome = input('\nDigite o novo nome do produto: ')
                            if confirmacao():
                                produto["nome"] = novo_nome
                                return estoque
                            return estoque
                        elif opcao == 2:
                            novo_preco = verificacao_float('\nDigite o novo preço do produto: ')
                            if confirmacao():
                                produto["preco"] = novo_preco
                                return estoque
                            return estoque
                        elif opcao == 3:
                            nova_quantidade = verificacao_int(
                                '\nDigite a nova quantidade disponível do produto: ',
                                '\nEntrada inválida. Insira somente quantidades positivas.'
                                )
                            if confirmacao():
                                produto["quantidade"] = nova_quantidade
                                return estoque
                            return estoque     
                        else:
                            nova_categoria = input('\nDigite a nova categoria do produto: ')
                            if confirmacao():
                                produto["categoria"] = nova_categoria
                                return estoque
                            return estoque                  
        print('\nEste ID não está disponível no estoque. Insira o ID novamente.')

def remover_produto(estoque):
    todos_id = [produto["id"] for produto in estoque.get('produtos', [])] 

    while True:
        id = verificacao_int(
            '\nDigite o ID do produto que deseja remover: ',
            '\nEntrada inválida. O ID deve ser inteiro e positivo.'
            )
        if id in todos_id:
            estoque.get("produtos", []).pop(id - 1)
            for produto in estoque.get('produtos', []):
                if produto['id'] > id:
                    produto['id'] -= 1
        return estoque

def buscar_produto(estoque):
    nome = input('\nDigite o nome do produto que deseja buscar: ')
    for produto in estoque.get('produtos', []):
        if produto.get('nome', '').lower() == nome.lower():
            print(f"\nNome: {produto.get('nome', 'N/A')}", end= ' | ')
            print(f"Preço: {produto.get('preco', 'N/A')}", end=' | ')
            print(f"Quantidade: {produto.get('quantidade', 'N/A')}", end=' | ')
            print(f"Categoria: {produto.get('categoria', 'N/A')}")
            sleep(2)
            return
    print(f'\nO produto {nome} não foi encontrado no estoque.')
    sleep(2)

def listar_categoria(estoque):
    categoria = input('\nDigite a categoria que deseja buscar: ')
    encontrou = False
    for produto in estoque.get('produtos', []):
        if produto.get('categoria', []).lower() == categoria.lower():
            print(f"\nNome: {produto.get('nome', 'N/A')}", end= ' | ')
            print(f"Preço: {produto.get('preco', 'N/A')}", end=' | ')
            print(f"Quantidade: {produto.get('quantidade', 'N/A')}", end=' | ')
            print(f"Categoria: {produto.get('categoria', 'N/A')}")
            encontrou = True
            sleep(2)
            
    if not encontrou:
        print(f'\nA categoria {categoria} não foi encontrada no estoque.')
        sleep(2)

def salvar_estoque(estoque):
    try:
        with open('estoque.json', 'w', encoding='utf-8') as arquivo:
            json.dump(estoque, arquivo, indent=4, ensure_ascii=False)
        print('\nAlterações salvas com sucesso!')
        return estoque
    except Exception as e:
        print(f'\nErro ao salvar as informações: {e}')

def valor_estoque(estoque):
    return sum(produto["preco"]*produto["quantidade"] for produto in estoque.get("produtos", []))

def main():
    try:
        if not os.path.exists('estoque.json'):
            with open('estoque.json', 'w', encoding='utf-8') as arquivo:
                json.dump({"produtos": []}, arquivo, indent=4, ensure_ascii=False)

        with open('estoque.json', 'r', encoding='utf-8') as arquivo:
            estoque = json.load(arquivo)
        
        while True:
            
            acoes = opcoes_menu()
            if acoes == 1:
                listar_produtos(estoque)
            elif acoes == 2:
                adicionar_produto(estoque)
            elif acoes == 3:
                editar_produto(estoque)
            elif acoes == 4:
                remover_produto(estoque)
            elif acoes == 5:
                valor_total = valor_estoque(estoque)
                print(f'O estoque atual tem um valor de R$ {valor_total:.2f}.')
                sleep(2)
            elif acoes == 6:
                buscar_produto(estoque)
            elif acoes == 7:
                listar_categoria(estoque)
            elif acoes == 8:
                salvar_estoque(estoque)
                sleep(2)
            else:
                print('\nO programa foi encerrado!\n')
                break
    except Exception as e:
        print(f'\nErro ao ler o o arquivo "estoque.json": {e}')

if __name__ == "__main__":
    main()
