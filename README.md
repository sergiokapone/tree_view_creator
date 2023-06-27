# Directory Tree View Creator

This Python program generates an ASCII tree based on the directory structure of a given directory.

## Usage

1. Ensure you have Python installed on your system.
2. Clone this repository or download the `tree.py` file.
3. Open a terminal or command prompt and navigate to the directory where `tree.py` is located.
4. Run the program with the following command, replacing `<directory>` with the path to the directory you want to generate the tree for.
5. There is also an option to save to a file.
Add option `-w <file>` or `--write <file>`.  The file will be created in the `<directory>` with the given `<file>` name. If the option is not used, the tree will be displayed in the console.

```shell
python tree.py /path/to/your/directory -w file.txt
```

The program will generate an ASCII tree based on the contents of the specified directory and display it in the console.

## Example

```shell
├── hw10
│   ├── hw10
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── quotes
│   │   ├── migrations
│   │   ├── static
│   │   ├── templates
│   │   └── templatetags
│   ├── users
│   │   ├── migrations
│   │   ├── static
│   │   ├── templates
│   │   ├── views.py
│   │   └── views.py
│   ├── utils
│   └── manage.py
├── Dockerfile
├── Pipfile
├── Pipfile.lock
├── README.md
└── fly.toml
```
