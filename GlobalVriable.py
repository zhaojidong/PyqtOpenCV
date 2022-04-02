
class globalValue():
    def __init__(self):
        self.FileInfo = ''
        self.DebugFlag = True
        self.Data = 1
        self.binProThreshold = 255
        self.binProMaxValue = 255
        self.shouFlag = False

    def debugPrint(self,strInfo):
        if self.DebugFlag == True:
            print(str(strInfo))
        else:
            pass


# -*- coding: utf-8 -*-

def global_init():  # 初始化
    global _global_dict
    _global_dict = {
        'binProThreshold': '',
        'binProMaxValue': '',
        'FileInfo': ''
    }


def set_value(key, value):
    _global_dict[key] = value


def get_value(key, defValue=None):
    return _global_dict[key]
    # except KeyError: