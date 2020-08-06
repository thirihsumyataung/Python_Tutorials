class App:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def itisanapp(self):
        print(f'{self.name} is an App.')

    def itsappVersion(self):
            print(f'{self.version} is a new {self.name} version')



class Apple(App):
    def itisapple(self):
        print(' Apple Application')


class Andriod(App):
    def itisanandriod(self):
        print(f'{self.name} is Andriod')


ios = Apple("IOS", 13.20897)
ios.itisanapp()
ios.itsappVersion()
ios.itisapple()





