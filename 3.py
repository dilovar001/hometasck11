def TwoLetters(letter):
    first_two_letters = letter[:2]
    res = 2*(first_two_letters + "... ")+letter+"?"
    print(res)
letter = input()
TwoLetters(letter)