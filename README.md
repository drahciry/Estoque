# 📦 Sistema de Gerenciamento de Estoque — Python

Bem-vindo ao **Sistema de Gerenciamento de Estoque**, um projeto robusto feito em Python, usando **Programação Orientada a Objetos**, **validação de dados rigorosa** e **persistência de informações** em arquivos JSON.

---

## 🚀 Funcionalidades

- ✅ **Cadastro de Produtos:** nome, preço, quantidade e categoria, com validação de entradas.
- ✅ **Gerenciamento Completo:** adição e remoção de produtos, listagem geral, consulta por categoria e cálculo do valor total do estoque.
- ✅ **Persistência de Dados:** salva o estoque em arquivo `.json` e carrega automaticamente ao iniciar.
- ✅ **Interface Interativa:** menu amigável via terminal, com confirmações e mensagens claras.

---

## 🗂️ Estrutura do Projeto

```
├── Exceptions.py   # Exceções customizadas
├── Price.py        # Classe Price para tratar preços com precisão decimal
├── Product.py      # Classe Product com validações de atributos
├── Stock.py        # Classe Stock com toda a lógica de estoque
├── main.py         # Ponto de entrada: interface interativa via terminal
├── README.md       # Este arquivo
├── stock.json      # (Gerado automaticamente) Base de dados persistente
```

---

## ⚙️ Pré-requisitos

- Python **3.10+**
- Nenhuma biblioteca externa (usa apenas `decimal`, `json`, `os`).

---

## 📥 Como Executar

1. **Clone o repositório ou baixe os arquivos:**

   ```bash
   git clone https://github.com/seuusuario/seurepositorio.git
   cd seurepositorio
   ```

2. **Execute o arquivo principal:**

   ```bash
   python main.py
   ```

3. **Use o menu interativo para gerenciar o estoque.**

---

## 💾 Salvando e Carregando

- **Salvar:** o sistema pergunta se deseja salvar as alterações antes de sair.
- **Arquivo:** os dados são salvos em `stock.json`.
- **Carregar:** o estoque é carregado automaticamente ao iniciar, caso o arquivo exista.

---

## 🧩 Principais Classes

### 🔑 Product

- Contém ID, nome, preço (objeto `Price`), quantidade e categoria.
- Valida todos os atributos para garantir integridade.

### 💲 Price

- Usa `decimal.Decimal` para cálculos monetários sem perda de precisão.
- Valida valores positivos e formato correto.

### 📦 Stock

- Gerencia produtos e categorias.
- Mantém o valor total do estoque sempre atualizado.
- Permite exportar os dados em JSON (por ID ou por categoria).

---

## 👨‍💻 Autor

Desenvolvido por **Richard**, estudante de Ciência da Computação da UERJ.

---

## 📜 Licença

Este projeto é **open-source**. Fique à vontade para usar, estudar, melhorar e compartilhar!

---