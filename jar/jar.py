
class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError

        self._capacity = capacity
        self._size = 0
        self.c = "🍪"

    def __str__(self):

        return self.c * self.size

    def deposit(self, n):
        if n > self._capacity or n + self._size > self._capacity:
            raise ValueError
        self._size = self._size + n


    def withdraw(self, n):
        if n > self._capacity or n > self._size:
            raise ValueError
        self._size = self._size - n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

def main():
    jar = Jar()
    jar.deposit(13)

    print(jar)
    print(jar.capacity)
    print(jar.size)


if __name__ == "__main__":
    main()



