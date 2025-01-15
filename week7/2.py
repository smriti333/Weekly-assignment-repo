def union_letters(word1, word2):
    # Letters that appear in at least one of the two words
    return sorted(set(word1.lower()) | set(word2.lower()) - {' '})

def intersection_letters(word1, word2):
    # Letters that appear in both words
    return sorted(set(word1.lower()) & set(word2.lower()) - {' '})

def difference_letters(word1, word2):
    # Letters that appear in either word, but not in both
    return sorted(set(word1.lower()) ^ set(word2.lower()) - {' '})

if __name__ == "__main__":
    word1 = input("Enter the first word: ")
    word2 = input("Enter the second word: ")

    print("Union of letters:", union_letters(word1, word2))
    print("Intersection of letters:", intersection_letters(word1, word2))
    print("Difference of letters:", difference_letters(word1, word2))
