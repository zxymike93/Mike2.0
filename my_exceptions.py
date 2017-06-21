class Error(Exception):
    """一般会写一个父类, 并且命名为 Error"""
    pass


class InputError(Error):
    """输入错误

    属性:
        expression -- 引起错误的 input 语句
        message -- 错误信息
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message
