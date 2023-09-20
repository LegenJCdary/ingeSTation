from typing import Optional


def print_something(something: Optional[str]) -> None:
    print(something)


def main():
    print_something("Welcome to ingeSTation project!")


def ingestation():
    return main()


if __name__ == "__main__":
    ingestation()
