import os
import csv


class Iterator:
    def __init__(self, num_class):
        self.counter = 0
        self.num_class = num_class
        path = os.path.join('dataset', self.num_class)
        self.data = os.listdir(path)
        self.limit = len(self.data)

    def __next__(self):
        if self.counter < self.limit:
            path = os.path.join(self.num_class, self.data[self.counter])
            self.counter += 1
            return path
        else:
            return None


def main() -> None:
    class_5 = Iterator("5")

    for i in range(1002):
        print(next(class_5))


if __name__ == '__main__':
    main()
