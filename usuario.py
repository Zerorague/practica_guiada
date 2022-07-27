
class user():
    def __init__(self, id, name, password, lastName, address, comment) -> None:
        self.__id = id
        self.__name = name
        self.__password = password
        self.__lastName = lastName
        self.__address = address
        self.__comment = comment

    @property
    def getId(self):
        return self.__id

    @property
    def getName(self):
        return self.__name

    @property
    def getPassword(self):
        return self.__password

    @property
    def getLastName(self):
        return self.__lastName

    @property
    def getAddress(self):
        return self.__address

    @property
    def getComment(self):
        return self.__comment

    @getName.setter
    def setName(self, value):
        self.__name = value

    @getPassword.setter
    def setPassword(self, value):
        self.__password = value

    @getLastName.setter
    def setLastName(self, value):
        self.__lastName = value

    @getAddress.setter
    def setAddress(self, value):
        self.__address = value

    @getComment.setter
    def setComment(self, value):
        self.__comment = value
