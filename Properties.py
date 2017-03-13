import Vector


class Properties:

    def __init__(self):
        self.__pressure = 0
        self.__temperature = 0
        self.__density = 0
        self.gama = 1.4

    @property
    def p(self):
        return self.__pressure

    @p.setter
    def p(self, value):
        self.__pressure = value

    @property
    def t(self):
        return self.__temperature

    @t.setter
    def t(self, value):
        self.__temperature = value.__temperature



