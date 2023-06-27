import os
import argparse


def generate_tree(directory, prefix=""):
    files = os.listdir(directory)
    files.sort()  # Сортування файлів для послідовного відображення

    for index, file in enumerate(files):
        path = os.path.join(directory, file)
        is_last = index == len(files) - 1

        if is_last:
            node = prefix + "└── " + file
            sub_prefix = prefix + "    "  # Префікс для піддиректорій
        else:
            node = prefix + "├── " + file
            sub_prefix = prefix + "│   "  # Префікс для піддиректорій

        print(node)

        if os.path.isdir(path):
            next_prefix = sub_prefix + "    "  # Додатковий префікс для вкладених файлів
            generate_tree(path, prefix=next_prefix)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate ASCII tree based on a directory structure."
    )
    parser.add_argument(
        "directory", metavar="DIRECTORY", type=str, help="path to the directory"
    )

    args = parser.parse_args()
    directory_path = args.directory

    generate_tree(directory_path)
