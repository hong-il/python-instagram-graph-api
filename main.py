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
        self.dictionary['안준석'] = 172

    def run(self):
        for k, v in self.dictionary.items():
            print(f'{k} : {v}')


def main():
    dictionary = {"이름": "안준석", "키": 178}
    instagram = Instagram(dictionary=dictionary)
    instagram.run()


if __name__ == '__main__':
    main()