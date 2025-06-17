# braille_map.py

# Braille dot numbers (1-6) mapped to QWERTY keys
dot_to_key = {
    1: 'D',
    2: 'W',
    3: 'Q',
    4: 'K',
    5: 'O',
    6: 'P'
}

# QWERTY key combinations mapped to letters
# Format: 'DW' means D (dot 1) + W (dot 2), i.e., dots [1,2] => letter B

braille_char_map = {
    'D': 'A',       # dot 1
    'DW': 'B',      # dots 1,2
    'DK': 'C',      # dots 1,4
    'DKQ': 'D',     # dots 1,4,3
    'DQ': 'E',
    'DKW': 'F',
    'DKWQ': 'G',
    'DWQ': 'H',
    'KW': 'I',
    'KWQ': 'J',
    'DO': 'K',
    'DWO': 'L',
    'DKO': 'M',
    'DKQO': 'N',
    'DQO': 'O',
    'DKWO': 'P',
    'DKWQO': 'Q',
    'DWQO': 'R',
    'KWO': 'S',
    'KWQO': 'T',
    'DOP': 'U',
    'DWOP': 'V',
    'KWQP': 'W',
    'DKOP': 'X',
    'DKQOP': 'Y',
    'DQOP': 'Z'
}

# Ensure all keys are sorted alphabetically for uniform input handling
braille_char_map = {
    ''.join(sorted(k)): v for k, v in braille_char_map.items()
}
