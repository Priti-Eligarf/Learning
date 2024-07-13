"""

Abstract Method

"""
from abc import ABC, abstractmethod


class WebDriver(ABC):

    @abstractmethod
    def click(self):
        pass


class ChromeDriver(WebDriver):

    def capturScreenshot(self):
        print("Capturing Screenshot")

    def click(self):
        print("Chrome screenshot")


class EdgeDriver():

    def capturScreenshot(self):
        print("Capturing Screenshot")

    def click(self):
        print("Edge screenshot")


obj = ChromeDriver()
obj.capturScreenshot()
obj.click()

ob = EdgeDriver()
ob.capturScreenshot()
ob.click()






class Animal(ABC):
    @abstractmethod
    def disp(self):
        pass
    @abstractmethod
    def add(self):
        None


class Tiger(Animal):

    def disp(self):
        print("tiger disp method")

    def add(self):
        print("Tiger add method")


class Elephant(Animal):

    def disp(self):
        print("Elephant disp method")

    def add(self):
        print("Tiger add method")

c = Tiger()
c.disp()

                   # c.add()


