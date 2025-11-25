total = 0
while True:
    try:
        preco_item = float(input("Digite o preço do item (Digite 0 para finalizar o calculo): "))
        if preco_item == 0:
            break
        total += preco_item
    except ValueError:
        print("digite um número: ")

print(f"O total da compra é: R$ {total:.2f}")
