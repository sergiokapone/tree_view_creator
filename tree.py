import os
import argparse


def generate_tree(directory, prefix=""):
    files = os.listdir(directory)
    files.sort()  # Сортировка файлов для последовательного отображения

    tree_lines = []  # Список строк дерева

    for index, file in enumerate(files):
        path = os.path.join(directory, file)
        is_last = index == len(files) - 1

        if is_last:
            node = prefix + "└── " + file
            sub_prefix = prefix + "    "  # Префикс для поддиректорий
        else:
            node = prefix + "├── " + file
            sub_prefix = prefix + "│   "  # Префикс для поддиректорий

        tree_lines.append(node)

        if os.path.isdir(path):
            next_prefix = sub_prefix + "    "  # Дополнительный префикс для вложенных файлов
            sub_tree = generate_tree(path, prefix=next_prefix)
            tree_lines.extend(sub_tree)

    return tree_lines


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate ASCII tree based on a directory structure."
    )
    parser.add_argument(
        "directory", metavar="DIRECTORY", type=str, help="path to the directory"
    )
    parser.add_argument(
        "-w",
        "--write",
        metavar="FILE",
        type=str,
        help="write the tree to the specified file",
    )

    args = parser.parse_args()
    directory_path = args.directory

    tree = generate_tree(directory_path)
    tree_output = "\n".join(tree)

    if args.write:
        output_file = os.path.join(directory_path, args.write)
        with open(output_file, "w", encoding="utf-8") as file:
            file.write(tree_output)
        print(f"Tree has been written to '{output_file}' file.")
    else:
        print(tree_output)
