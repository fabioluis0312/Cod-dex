#Variaveis

dna_sequence = ['GCT', 'AGC', 'AGG', 'TAA', 'ACT', 'CAT', 'TAT', 'CCC', 'ACG', 'GAA', 'ACC', 'GGA']

item_to_find = 'AGC'

item_found = False

#Loop para encontrar o codon na sequencia de DNA
for codon in dna_sequence:
    if codon == item_to_find:
        item_found = True
        break

#Imprimir resultado da busca
if item_found:
    print(f'Codon {item_to_find} encontrado na sequencia de DNA.')
else:
    print(f'Codon {item_to_find} nao encontrado na sequencia de DNA.')