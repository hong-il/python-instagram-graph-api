"""
    @ Author    : hong-il
    @ Date      : 2020-12-12
    @ File name : main.py
    @ File path :
    @ Description :
"""

class Instagram:

    def __init__(self, dictionary):
        self.dict = dict

    def run(self):
        for d in self:
            print(f'{d}')


def main():
    dictionary = [
        {"이름": "안준석", "키": 170},
        {"이름": "김홍일", "키": 162},
        {"이름": "박상혁", "키": 155},
        {"이름": "표중희", "키": 207},
        {"이름": "박상언", "키": 177}
    ]
    Instagram.run(self=dictionary)


if __name__ == '__main__':
    main()