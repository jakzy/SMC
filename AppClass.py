import AppClass_sm


class AppClass:
    def __init__(self):
        self.__counter = 0
        self.__length = 0
        self.__substring = ''
        self.__c = ''
        self._fsm = AppClass_sm.AppClass_sm(self)
        self._is_acceptable = False
        self._fsm.enterStartState()

    def ClearSMC(self):
        self.CounterZero()
        self.LengthZero()
        self.ClearSubstring()
        self._is_acceptable = True

    def CheckString(self, string):
        self._fsm.Start()
        # Uncomment to see debug output.
        #self._fsm.setDebugFlag(True)
        for c in string:
            self.__substring += c
            if c.isupper() and c.isalpha():
                self._fsm.UpperLiter()
            elif c.isalpha():
                self._fsm.Liter()
            elif c.isdigit():
                self._fsm.Digit()
            elif c == '$':
                self._fsm.Dollar()
            elif c == '\\':
                self._fsm.Slash()
            elif c == '\n':
                self._fsm.Endl()
                break
            else:
                self._fsm.Unknown()
        self._fsm.EOS()
        return self._is_acceptable

    def Acceptable(self):
        self._is_acceptable = True

    def Unacceptable(self):
        self._is_acceptable = False

    def CounterInc(self):
        self.__counter += 1

    def CounterZero(self):
        self.__counter = 0

    def LengthInc(self):
        self.__length += 1

    def LengthZero(self):
        self.__length = 0

    def isValidServer(self):
        return self.__counter <= 15

    def isValidName(self):
        return self.__counter <= 32

    def isValidString(self):
        return self.__length <= 100

    def isCounterNotZero(self):
        return self.__counter > 0

    def isAbsAddress(self):
        return self.__length <= 2

    def ClearSubstring(self):
        self.__substring = ''