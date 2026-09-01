opcao = ""
produtos = []
while opcao != "4":
    print("===== CAIXA =====")
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Ver produtos")
    print("4 - Finalizar compra")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nomeProduto = input("Qual o nome do produto? ")
        precoProduto = float(input("Qual o preço do produto? "))
        quantidadeComprada = int(input("Quantas unidades será comprada? "))
    
        produto = {
        "nome": nomeProduto,
        "preco": precoProduto,
        "quantidade": quantidadeComprada
        }
        produtos.append(produto)
     
    elif opcao == "2":
        itenRemover = int(input("Qual item deseja remover? (Digite o número correspondente) "))
        indiceRemover = itenRemover - 1
        produtoRemover = produtos[indiceRemover]
        del produtos[indiceRemover]
        print("Produto removido:", produtoRemover["nome"])

    elif opcao == "3":
        for i, produto in enumerate(produtos, start=1):
            print(i, "-", produto["nome"])
            print(f"Preço R$ {produto["preco"]:.2f}")
            print(f"Quantidade: {produto["quantidade"]}")

    elif opcao == "4":
         total = 0
         for produto in produtos:
            subtotal = produto["preco"] * produto["quantidade"]
            total = total + subtotal

         print(f"Total: R$ {total:.2f}")
         print("Sair")






