
continuar = "sim"
produtos = []

while continuar == "sim":
    nomeProduto = input("Qual o nome do produto? ")
    precoProduto = float(input("Qual o preço do produto? "))
    quantidadeComprada = int(input("Quantas unidades será comprada? "))
    produto = {
    "nome": nomeProduto,
    "preco": precoProduto,
    "quantidade": quantidadeComprada

}

    produtos.append(produto)
    continuar = input("Deseja adicionar outro produto? (sim/não) ")
    
total = 0

for produto in produtos:
    print(produto["nome"])
    print(produto["preco"])
    print(produto["quantidade"])
    subtotal = produto["preco"] * produto["quantidade"]
    total = total + subtotal

print(f"Total: R$ {total:.2f}")
