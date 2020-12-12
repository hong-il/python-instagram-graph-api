"""
    @ Author    : hong-il
    @ Date      : 2020-12-12
    @ File name : main.py
    @ File path :
    @ Description :
"""


class Instagram:

    def __init__(self, dictionary):
        self.dictionary = dict()
        self.dictionary = dictionary

    def run(self):
        print(sum(self.dictionary.values()))


def main():
    dictionary = {"초코바": 1500, "메로나": 1000, "월드콘": 1300}
    instagram = Instagram(dictionary=dictionary)
    instagram.run()


if __name__ == '__main__':
    main()
