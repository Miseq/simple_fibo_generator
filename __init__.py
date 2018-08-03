class Generator:

    def __init__(self, max_value=100000):
        self.a, self.b = 0, 1
        self.max = max_value

    def __iter__(self):
        return self

    def __next__(self):

        if self.a > self.max:
            raise StopIteration

        fibo_number = self.a
        self.a, self.b = self.b, self.a + self.b

        return fibo_number


if __name__ == '__main__':
    Fib = Generator()
    for fibo in Fib:
        print(fibo)

