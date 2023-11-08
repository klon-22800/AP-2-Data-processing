import os


def next(num_class: str) -> str:
    """
    The function returns the next element path by class label
    """
    path = os.path.join('dataset', num_class)
    class_names = os.listdir(path)
    class_names.append(None)
    for i in range(len(class_names)):
        if class_names[i] is not None:
            yield os.path.join(path, class_names[i])
        else:
            yield None


def main() -> None:
    print(*next('1'))


if __name__ == '__main__':
    main()
