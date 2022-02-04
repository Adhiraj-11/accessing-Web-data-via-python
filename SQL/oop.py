class Dog():
    def __init__(self, name):
        print("hello")
        self.name = name

    def speak(self):
        print("hi i am", self.name)

Konran = Dog("Konran")

Konran.speak()
