'''Método de lista	Descrição
.append()	Adicione um item ao final da lista
.clear()	Remova todos os itens da lista
.copy()	Retorne uma cópia superficial da lista
.count()	Retorna o número de vezes que o valor aparece na lista
.extend()	Anexa outra lista à lista atual estendendo-a
.index()	Retorna o índice de um valor dentro da lista
.insert()	Insira um item em uma posição especificada na lista
.pop()	Remova um item de uma posição especificada na lista
.remove()	Remova um item da lista com base no valor do item
.reverse()	Inverte a lista em vigor
.sort()	Classifica a lista no lugar'''

books = ['Harry Potter',
'1984',
'The Fault in Our Stars',
'The Mom Test',
'Life in Code'
]
books.append('Pachinko')
books.remove('The Fault in Our Stars')
books.pop(1)

print(books)

