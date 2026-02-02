''' Cada emoji de Lua representa uma fase da Lua.

Crie uma função moon_phase() que:

recebe uma string com o nome da fase

retorna o emoji correspondente

Mapeamento exigido:

'New Moon' → 🌑

'Waxing Crescent' → 🌒

'First Quarter' → 🌓

'Waxing Gibbous' → 🌔

'Full Moon' → 🌕

'Waning Gibbous' → 🌖

'Last Quarter' → 🌗

'Waning Crescent' → 🌘

Se o nome for inválido → retornar 'Invalid moon phase'.

Depois, testar assim:

answer = moon_phase('New Moon')
print(answer)


Saída esperada:

🌑
'''

def moon_phase(phase):
    phase_map = {
        'New Moon': '🌑',
        'Waxing Crescent': '🌒',
        'First Quarter': '🌓',
        'Waxing Gibbous': '🌔',
        'Full Moon': '🌕',
        'Waning Gibbous': '🌖',
        'Last Quarter': '🌗',
        'Waning Crescent': '🌘'
    }
    return phase_map.get(phase, "Invalid moon phase")

answer = moon_phase('New Moon')
print(answer)