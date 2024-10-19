from abc import ABC, abstractmethod


class TouchScreenLaptop(ABC):
    def __init__(self, name: str, model: str):
        self.name = name
        self.model = model

    @abstractmethod
    def scroll(self):
        pass

    @abstractmethod
    def click(self):
        pass


class HP(TouchScreenLaptop):
    def __init__(self, name: str, model: str):
        super().__init__(name, model)

    def scroll(self):
        print("Hp scrolling....")


class DELL(TouchScreenLaptop):
    def __init__(self, name: str, model: str):
        super().__init__(name, model)

    def scroll(self):
        print("Dell scrolling....")


class HpNotebook(HP):
    def __init__(self, name: str, model: str, SSDEnabled: bool):
        super().__init__(name, model)
        self.SSDEnabled = SSDEnabled

    def click(self):
        print("Clicking on HpNotebook...")


class DELLNotebook(DELL):
    def __init__(self, name: str, model: str, CTypeEnabled: bool):
        super().__init__(name, model)
        self.CTypeEnabled = CTypeEnabled

    def click(self):
        print("Clicking on DELLNotebook...")


if __name__ == "__main__":
    hpn = HpNotebook("HP G245", "G245", False)
    dln = DELLNotebook("DELL INSPIRON", "INSPIRON 3000 series", True)

    hpn.scroll()
    hpn.click()
    dln.scroll()
    dln.click()
    print(hpn.name)
    print(dln.name)
    print(hpn.SSDEnabled)
    print(dln.CTypeEnabled)
