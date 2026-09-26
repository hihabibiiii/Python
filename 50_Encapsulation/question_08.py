# Question:
# Use @property.deleter decorator to handle attribute deletion.

class Config:
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_val):
        print(f"Setting value to: {new_val}")
        self.__value = new_val

    @value.deleter
    def value(self):
        print("Deleting value...")
        self.__value = None

cfg = Config(42)
print(f"Value: {cfg.value}")

cfg.value = 100
print(f"Value: {cfg.value}")

del cfg.value
print(f"After delete: {cfg.value}")
