class Box:
    def __init__(self, value):
        self.value = value


a = Box(1)
b = a
a.value = 2
print(b.value)
