import stats

#main loop
filepath = 'books/frankenstein.txt'


print('============ BOOKBOT ============')
print(f"Analyzing book found at {filepath}...")
print('----------- Word Count ----------')
print(f'Found {stats.count_book_words(filepath)} total words')
print('--------- Character Count -------')
for char in stats.count_chars_and_sort(filepath):
    if char['char'].isalpha():
        print(f"{char['char']}: {char['num']}")
print('============= END ===============')