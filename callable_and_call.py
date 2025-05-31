class Multiplier():
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return self.factor * value
    

obj = Multiplier(5)

print(obj(5))
print(callable(obj))