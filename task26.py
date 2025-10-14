def count_vowels(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    
    vowels_count = {
        'а': 0,
        'н': 0,
        'т': 0,
        'о': 0,
        'с': 0
    }
    
    for char in content.lower():
        if char in vowels_count:
            vowels_count[char] += 1
    
    for vowel, count in vowels_count.items():
        print(f"Количество букв {vowel} - {count}")


count_vowels('dump.txt')
