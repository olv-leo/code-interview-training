'''
A função TwoSum deve receber uma lista de n valores e um valor alvo e caso existam dois valores da lista que somados
resultem no valor alvo a função deve retornar a posição desses valores.
Testes:
>>> TwoSum([1, 4, 2, 5, 9, 7], 9)
[2, 5]
>>> TwoSum([1,1,1,1,1], 2)
[0, 4]
>>> TwoSum([2,4,15,21,8,2,1,0], 21)
[7, 3]
'''


def TwoSum(lista, valor_alvo):
    lista = [(posicao, numero) for posicao, numero in enumerate(lista)]
    lista_ordenada = sorted(lista, key=lambda x: x[1])

    while len(lista) >= 2:
        maior_valor = lista_ordenada[-1][1]
        menor_valor = lista_ordenada[0][1]
        soma_extremos = maior_valor + menor_valor

        if soma_extremos > valor_alvo:
            del lista_ordenada[-1]
        elif soma_extremos < valor_alvo:
            del lista_ordenada[0]
        else:
            return [lista_ordenada[0][0], lista_ordenada[-1][0]]
