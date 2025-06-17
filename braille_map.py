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
    'D': 'A',
    'DW': 'B',
    'DK': 'C',
    'DKO': 'D',
    'DO': 'E',
    'DWK': 'F',
    'DWKO': 'G',
    'DWO': 'H',
    'WK': 'I',
    'WKO': 'J',
    'DQ': 'K',
    'DWQ': 'L',
    'DQK': 'M',
    'DQKO': 'N',
    'DQO': 'O',
    'DWQK': 'P',
    'DWQKO': 'Q',
    'DWQO': 'R',
    'WQK': 'S',
    'WQKO': 'T',
    'DQP': 'U',
    'DWQP': 'V',
    'WKOP': 'W',
    'DQKP': 'X',
    'DQKOP': 'Y',
    'DQOP': 'Z'
}

# Ensure all keys are sorted alphabetically for uniform input handling
braille_char_map = {
    ''.join(sorted(k)): v for k, v in braille_char_map.items()
}
