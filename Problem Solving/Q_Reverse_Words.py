S = input()
words = S.split()
reversed_words = [word[::-1] for word in words]
print(" ".join(reversed_words))
