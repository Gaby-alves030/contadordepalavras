import io
import unicodedata
import re
from collections import Counter


def load_text_file(contador.txt):
    with io.open(contador.txt, 'r', encoding='utf-8') as file:
        return file.read()


def remove_accents(contador.txt):
    return unicodedata.normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII')


def get_words(contador.txt):
    return re.findall(r'\b\w+\b', text)


def count_words(words):
    return Counter(words)


def rank_words(word_counts):
    return sorted(word_counts.items(), key=lambda x: x[1], reverse=True)


def show_word_counts(word_counts):
    for word, count in word_counts:
        print(f'{word}: {count}')


def find_word(word_counts, query):
    if query in word_counts:
        print(f'{query}: {word_counts[query]}')
    else:
        print(f'A palavra "{query}" não foi encontrada.')


def show_most_common(word_counts):
    most_common_word, count = word_counts.most_common(1)[0]
    print(f'A palavra mais comum é "{most_common_word}" com {count} aparições.')


def show_least_common(word_counts):
    least_common_word, count = word_counts.most_common()[-1]
    print(f'A palavra menos comum é "{least_common_word}" com {count} aparições.')


def show_menu():
    print('\nMENU')
    print('1 - Exibir texto sem acentos')
    print('2 - Exibir contagem de palavras')
    print('3 - Buscar uma palavra')
    print('4 - Exibir a palavra mais comum')
    print('5 - Exibir a palavra menos comum')
    print('0 - Encerrar a aplicação')


filename = input('Digite o nome do arquivo: ')
text = load_text_file(contador.txt)

while True:
    show_menu()
    choice = input('Escolha uma opção: ')

    if choice == '0':
        break
    elif choice == '1':
        text_without_accents = remove_accents(text)
        print(text_without_accents)
    elif choice == '2':
        words = get_words(text)
        word_counts = count_words(words)
        word_counts_ranked = rank_words(word_counts)
        show_word_counts(word_counts_ranked)
    elif choice == '3':
        words = get_words(text)
        word_counts = count_words(words)
        query = input('Digite a palavra que deseja buscar: ')
        find_word(word_counts, query)
    elif choice == '4':
        words = get_words(text)
        word_counts = count_words(words)
        show_most_common(word_counts)
    elif choice == '5':
        words = get_words(text)
        word_counts = count_words(words)
        show_least_common(word_counts)
    else:
        print('Opção inválida.')
