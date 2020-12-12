"""
    @ Author    : hong-il
    @ Date      : 2020-12-12
    @ File name : logging.py
    @ File path : 
    @ Description : 
"""
# -*- coding: utf-8 -*-
import logging
import logging.config
import logging.handlers

import colorlog


class Logging:

    def __init__(self, logger_name='DefaulLoggingtLog'):
        # 로그 인스턴스생성 및 로그 레벨 설정
        self.logger = logging.getLogger(logger_name)

        self.logger.setLevel(logging.INFO)
        self.logger.setLevel(logging.DEBUG)

        # 파일핸들러와 스트림 핸들러 설정 - 10*1024*1024 = 10Mb
        self.loger_StreamHandler = logging.StreamHandler()
        self.loger_FileHandler = logging.handlers.RotatingFileHandler(
            filename=u"./log/{logger_name}.log".format(logger_name=logger_name),
            maxBytes=10 * 1024 * 1024,
            backupCount=5,
            encoding="utf-8"
        )
        # self.FileHandler = logging.handlers.TimedRotatingFileHandler(filename="./log/Log.log", when="midnight", interval=1, encoding="utf-8")

        self.loger_StreamHandler.setLevel(logging.DEBUG)
        self.loger_FileHandler.setLevel(logging.DEBUG)

        # 핸들러 로그 포맷 설정
        # 기본 로그 포맷
        self.LogFormat = f'[%(asctime)s][%(levelname)-8s](%(filename)-20s:%(lineno)4d) --- %(message)s'

        # 스트림 핸들러 컬러포맷 설정
        self.ColorFormaer = colorlog.ColoredFormaer(
            # '%(log_color)s' + LogFormat,
            '%(log_color)s[%(asctime)s][%(levelname)-8s](%(filename)-20s:%(lineno)4d)%(reset)s ---%(message_log_color)s %(message)s',
            reset=True,
            log_colors={
                'DEBUG': 'fg_bold_cyan',
                'INFO': 'fg_white',
                'WARNING': 'fg_bold_yellow',
                'ERROR': 'fg_bold_red',
                'CRITICAL': 'fg_bold_red,bg_blue',
            },
            secondary_log_colors={
                'message': {
                    'DEBUG': 'fg_yellow',
                    'INFO': 'fg_white',
                    'WARNING': 'fg_yellow',
                    'ERROR': 'fg_bold_red',
                    'CRITICAL': 'fg_bold_red'
                }
            }
        )
        # StreamFormaer = logging.Formaer(LogFormat)
        self.loger_StreamHandler.setFormaer(self.ColorFormaer)

        self.FileLogFormaer = logging.Formaer(self.LogFormat)
        self.loger_FileHandler.setFormaer(self.FileLogFormaer)

        # 핸들러를 로깅에 추가
        self.logger.addHandler(self.loger_StreamHandler)
        self.logger.addHandler(self.loger_FileHandler)

        # with open('logging.json', 'rt') as f:
        #     config = json.load(f)

    def __enter__(self):
        return self

    def get_logger(self):
        return self.logger


if __name__ == '__main__':
    try:
        # Logging = Logging('Loger')
        # Log = Logging.get_logger()
        Log = Logging("Loger").get_logger()

        # a = 1/0

        Log.debug('test')
        Log.info('test')
        Log.info(__file__)
        Log.info('한글이 잘 나와야 함')

    except Exception as e:
        Log.exception('Got')

