import stats
import sys

#main loop
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    filepath = sys.argv[1]

    print('============ BOOKBOT ============')
    print(f"Analyzing book found at {filepath}...")
    print('----------- Word Count ----------')
    print(f'Found {stats.count_book_words(filepath)} total words')
    print('--------- Character Count -------')
    for char in stats.count_chars_and_sort(filepath):
        if char['char'].isalpha():
            print(f"{char['char']}: {char['num']}")
    print('============= END ===============')
