

def longest_words(filepath: str):
    """
    Search the longest words in file and return list (the longest words)
    and int (max length the words)
    """
    cnt = 0
    with open(f'{filepath}', 'r', encoding='utf-8') as mf:
        my_file_to_str = mf.read()
        lst_help = my_file_to_str.split()
        for i in lst_help:
            if len(i) > cnt:
                cnt = len(i)
        long_words = [j for j in lst_help if len(j) == cnt]
        print(f'The longest words {long_words} max length = {cnt}!')
    return longest_words


if __name__ == "__main__":
    file = 'article.txt'
    longest_words(file)
