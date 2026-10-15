import re
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold == True: 
        text = text.casefold()
    else:
        text = text.lower()
    
    if yo2e == True:
        text = text.replace("Ё", "Е").replace("ё","е")

    text = re.sub(r"\s+", " ", text).strip()

    return text

test_array_1 = [
    "ПрИвЕт\nМИр\t",
    "ёжик, Ёлка",
    "Hello\r\nWorld",
    "  двойные   пробелы  "
]
#for word in test_array_1:
#    print(normalize(word))

def tokenize(text: str) -> list[str]:
    words = re.findall(r"\w+(?:-\w+)*", text)
    return words 

test_array_2 = [
    "ПрИвЕт\nМИр\t",
    "hello,world!!!",
    "по-настоящему круто",
    "2025 год",
    "emoji 😀 не слово"
]
#for word in test_array_2:
#    print(tokenize(normalize(word)))

def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for word in tokens:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return dict(sorted(freq.items()))

test_array_3 = [
    ["a","b","a","c","b","a"],
    ["bb","aa","bb","aa","cc"]
]

#for token in test_array_3:
#    print(count_freq(token))

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    words = list(freq.items())
    words = sorted(words, key=lambda x: (-x[1], x[0]))
    return words[:n]

test_array_4 = [
    ["a","b","a","c","b","a"],
    ["bb","aa","bb","aa","cc"]
]
#for token in test_array_4:
#    print(top_n(count_freq(token), n=2))