from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lab04.io_txt_csv import read_text, write_csv
import argparse
import csv
from pathlib import Path

def get_frequencies(text: str) -> dict[str, int]:
    """Нормализует текст и подсчитывает частоты слов."""
    text = normalize(text)
    words = tokenize(text)
    freq = count_freq(words)
    return freq

def sort_frequencies(freq: dict[str, int]) -> list[tuple[str, int]]:
    """Сортирует слова по частоте и алфавиту."""
    return sorted(freq.items(), key=lambda item: (-item[1], item[0]))


def main():
    parser = argparse.ArgumentParser(
        description="Создание отчёта о частоте слов"
    )

    parser.add_argument("--in", dest="input_path", default="data/input.txt")
    parser.add_argument("--out", default="data/report.csv")
    parser.add_argument("--encoding", default="utf-8")

    args = parser.parse_args()

    try:
        text = read_text(args.input_path, encoding=args.encoding)
    except (OSError, UnicodeError) as error:
        print(f"Ошибка чтения файла: {error}")
        return

    freq = get_frequencies(text)
    sorted_words = sort_frequencies(freq)

    try:
        write_csv(sorted_words, args.out, header=("word", "count"))
    except OSError as error:
        print(f"Ошибка записи файла: {error}")
        return

    print(f"Всего слов: {sum(freq.values())}")
    print(f"Уникальных слов: {len(freq)}")
    print("Топ-5:")

    for word, count in top_n(freq, 5):
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()