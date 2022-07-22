def duplicate_encode(word):
    # breckets = ""
    word = word.lower()
    # for letter in word:
    #     if word.count(letter) == 1:
    #         breckets += "("
    #     else:
    #         breckets += ")"
    # print(breckets)
    return "".join("(" if word.count(letter) == 1 else ")" for letter in word.lower())


print(duplicate_encode("abccDLL"))
