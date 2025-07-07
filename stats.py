def get_book_text(filepath):
    with open(filepath,"r") as f:
        lines = f.read()
    return lines
def count_book_words(filepath):
    with open(filepath,"r") as f:
        words = f.read()
        word_count = words.split()
    return len(word_count)
def count_characters(filepath):
    char_dict = {}
    with open(filepath,"r") as f:
        words = f.read()
        for char in words:
                char = char.lower()
                if char in char_dict:
                    char_dict[char] += 1
                else:
                    char_dict[char] = 1
    return char_dict
def count_chars_and_sort(filepath):
    list = []
    get_dict = count_characters(filepath)
    for k in get_dict:
        list.append({'char':k,'num':get_dict[k]})
    def sort_on(items):
        return items['num']
    list.sort(reverse=True,key=sort_on)
    return list
