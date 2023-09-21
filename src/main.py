from ingestation.modules.misc.utils import InitParams


def main() -> None:
    init_params = InitParams()
    init_attrs = \
        [attr for attr in dir(init_params) if not any(attr.startswith(x) for x in ["_", "get"])]
    print_params = ", ".join([str(getattr(init_params, attr)) for attr in init_attrs])
    print("Welcome to ingeSTation project!")
    print(f"Started with: {print_params}")


def ingestation():
    return main()


if __name__ == "__main__":
    ingestation()
