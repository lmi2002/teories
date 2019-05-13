class A:
    count = 0

    def __init__(self):
        A.count += 1

    @staticmethod
    def exclaim():
        print("I'm an A!")

    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects.")


easy_a = A()
breezy_a = A()
wheezy_a = A()
A.kids()


class Quote:
    def __init__(self, person, words):
        self.person = person
        self.words = words

    def who(self):
        return self.person

    def says(self):
        return self.words + '.'


class QuestionQuote(Quote):
    def says(self):
        return self.words + '?'


class ExclamationQuote(Quote):
    def says(self):
        return self.words + '!'


hunter = Quote('Elmer Fudd', "I'm hunting wabbits")
print(hunter.who(), 'says:', hunter.says())
hunted1 = QuestionQuote('Bugs Bunny', "What's up, doc")
print(hunted1.who(), 'says:', hunted1.says())
hunted2 = ExclamationQuote('Daffy Duck', "It's rabbit season")
print(hunted2.who(), 'says:', hunted2.says())


class BabblingBrook:
    @staticmethod
    def who():
        return 'Brook'

    @staticmethod
    def says():
        return 'Babble'


brook = BabblingBrook()


def who_says(obj):
    print(obj.who(), 'says', obj.says())


who_says(hunter)
who_says(hunted1)
who_says(hunted2)
who_says(brook)


class Word:
    def __init__(self, text):
        self.text = text

    # def equals(self, word_2):
    #     #     print(self.text.lower() == word_2.text.lower())

    def __eq__(self, word_2):
        print(self.text.lower() == word_2.text.lower())

    def __add__(self, word_2):
        print(self.text + word_2.text)

    def __str__(self):
        return self.text

    def __repr__(self):
        return 'Word(' + self.text + ')'

w_1 = Word('Ha')
w_2 = Word('ha')
w_3 = Word('ah')

w_1 == w_2
print(w_1)

