class Counter():
    count = 0

    def __init__(self, name=None):
        Counter.count += 1
        self.name = name

    @classmethod
    def get_count(cls):
        print(f"Total Number of Students: {cls.count}")
        return cls.count


st1 = Counter("noman")
st2 = Counter("ali")
st3 = Counter("ali")


Counter.get_count()
print(st1.name.capitalize())
print(st2.name.capitalize())