WORD_LIST = "sowpods_letters.txt"
word_list = open(WORD_LIST).readlines()
word_list = [word.lower().strip() for word in word_list]

scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2,
          "f": 4, "g": 2, "h": 4, "i": 1, "j": 8,
          "k": 5, "l": 1, "m": 3, "n": 3, "o": 1,
          "p": 3, "q": 10, "r": 1, "s": 1, "t": 1,
          "u": 1, "v": 4, "w": 3, "x": 8, "y": 4,
          "z": 10}
