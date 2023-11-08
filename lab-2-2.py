import os
import csv
import shutil

from progress.bar import IncrementalBar


def rename(new_folder_name: str) -> None:
    """
    The function renames files and changes the hierarchy
    """
    for i in range(1, 6):
        bar = IncrementalBar(f'Renaming class_{i}', max=1000)
        relative_path = os.path.relpath(f'{new_folder_name}')
        class_path = os.path.join(relative_path, str(i))
        names = os.listdir(class_path)
        relative_paths = []
        new_relative_paths = []
        for name in names:
            relative_paths.append(os.path.join(class_path, name))
        for name in names:
            new_relative_paths.append(
                os.path.join(relative_path, f'{i}_{name}'))
        for old_name, new_name in zip(relative_paths, new_relative_paths):
            bar.next()
            os.replace(old_name, new_name)
        os.chdir(f'{new_folder_name}')

        if os.path.isdir(str(i)):
            os.rmdir(str(i))

        os.chdir('..')


def move_dataset(old_folder_name: str, new_folder_name: str) -> None:
    """
    The function copies files to a new directory
    """
    old_path = os.path.relpath(f'{old_folder_name}')
    new_path = os.path.relpath(f'{new_folder_name}')
    shutil.copytree(old_path, new_path)


def new_make_csv(new_folder_name: str) -> None:
    """
    The function writes data to a csv file in the following format: absolute path, relative path, class label
    """
    bar = IncrementalBar(f'Writting csv', max=5000)
    work_catalog = os.getcwd()
    os.chdir(new_folder_name)
    names = os.listdir()
    os.chdir(work_catalog)
    f = open("paths2.csv", 'w')
    writer = csv.writer(f, delimiter=',', lineterminator='\n')
    for name in names:
        num_class = name[0]
        absolute_path = os.path.abspath(new_folder_name)
        absolute_path_file = os.path.join(absolute_path, name)
        relative_path = os.path.relpath(f'{new_folder_name}')
        relative_path_file = os.path.join(relative_path, name)
        writer.writerow([absolute_path_file, relative_path_file, num_class])
        bar.next()


def main() -> None:
    move_dataset('dataset', 'dataset2')
    rename('dataset2')
    new_make_csv('dataset2')


if __name__ == '__main__':
    main()
