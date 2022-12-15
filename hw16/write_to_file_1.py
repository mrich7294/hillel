

if __name__ == "__main__":
    with open('my_file.txt', 'w', encoding='utf-8') as mf:
        my_str = input('The input string to write the file: ')
        while my_str != '':
            mf.write(my_str + '\n')
            print("Press 'Enter' to finish typing.")
            my_str = input('The input string to write the file: ')
