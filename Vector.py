from math import *


class Vector:
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value.__x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value.__y

    @property
    def z(self):
        return self.__z

    @z.setter
    def z(self, value):
        self.__z = value.__z

    @property
    def xyz(self):
        return self

    @xyz.setter
    def xyz(self, value):
        self.__x = value[0]
        self.__y = value[1]
        self.__z = value[2]

    @property
    #read only property
    def length(self):
        long = sqrt(pow(self.__x, 2) + pow(self.__y, 2) + pow(self.__z, 2))
        return long

    def normalization(self):
        l = self.length
        self.__x /= l
        self.__y /= l
        self.__z /= l

    def __init__(self):
        self.__x = 0
        self.__y = 0
        self.__z = 0

    def distance(self, another):
        deltax = self.__x - another.__x
        deltay = self.__y - another.__y
        deltaz = self.__z - another.__z
        d = pow(deltax, 2) + pow(deltay, 2) + pow(deltaz, 2)
        d = sqrt(d)
        return d

    def copy_from(self, another):
        self.__x = another.__x
        self.__y = another.__y
        self.__z = another.__z


if __name__ == "__main__":
    v1 = Vector()
    print(v1.xyz)

    v2 = Vector()
    v2.copy_from(v1)
    print(v2)
    v2.xyz = (2, 3, 4)
    print(v2.xyz)
    print('v1.x:', v1.x, 'v2.y', v2.y)

