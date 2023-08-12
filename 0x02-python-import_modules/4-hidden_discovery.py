import hidden_4


def print_hidden_names(module):
    for name in dir(module):
        if not name.startswith("__"):
            print(name)


if __name__ == "__main__":
    print_hidden_names(hidden_4)
