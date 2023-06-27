# Directory Tree View Creator

This Python program generates an ASCII tree based on the directory structure of a given directory.

## Usage

## Usage

To generate a directory tree, run the following command:

```shell
python main.py DIRECTORY [-w FILE] [-s {type,name}]
```

### Arguments

- `DIRECTORY`: The path to the directory for which you want to generate the tree.

### Options

- `-w FILE, --write FILE`: Write the tree to the specified file instead of printing it to the console.

- `-s {type,name}, --sort {type,name}`: Sort the tree by type (directories first) or by name. By default, the tree is sorted by type.

## Sorting

The tool provides two options for sorting the directory tree:

- **Type**: Directories are listed first, followed by files. This is the default sorting option.

- **Name**: Entries are sorted alphabetically by name.

To specify the sorting option, use the `-s` or `--sort` flag followed by either `type` or `name` as the argument.

### Sorting Examples

Sort by type (directories first):

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
