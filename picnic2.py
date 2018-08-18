print('''The class is going on a picnic and in order to be invited you must bring
one item on Jess\' list. Jess has made rules as to what you can and
cannot bring. You must figure out what the rule is in order to come on the
picnic. Jess will be bringing an orange.''')


def question():
    return input("What will you bring?\n")


def start_vowel(x):
    """This tells you if the input starts with a vowel."""
    vowel = ('aeiou')
    word_start = x[0]
    for number in range(5, -1, -1):
        if number > 5 and word_start in vowel:
            return "You can bring this on the picnic! What else would you like to bring?"
        else:
            return "Sorry, you can't bring that. Try again. You have {} guesses remaining".format(number - 1)
    else:
        print("You have used all of your guesses, you cannot come.")


def main():
    result = question()
    answer = start_vowel(x=result)
    print(answer)


if __name__ == '__main__':
        main()
