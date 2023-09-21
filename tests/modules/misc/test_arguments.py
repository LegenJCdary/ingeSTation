import pytest

from ingestation.modules.misc.arguments import CliInput


def create_unique_pairs(list_a: list, list_b: list, value: str) -> list:
    pairs = []
    for el_a in list_a:
        for el_b in list_b:
            pairs.append((el_a, el_b, value))
            pairs.append((el_b, value, el_a))

    return pairs


class TestArgumentParsingVerification(CliInput):

    parser = CliInput().create_parser()

    def test_verification_true(self):
        assert self.validate_arguments(self.parser.parse_args([]))["verification"] is True

    @pytest.mark.parametrize("option", CliInput.option_names["verification"])
    def test_verification_false(self, option):
        assert self.validate_arguments(self.parser.parse_args([option]))["verification"] is False


class TestArgumentParsingInExLists(CliInput):

    single_list = ["AB1234"]
    double_list = ["AB1234", "CD1234"]
    options = {
        "exclude": CliInput.option_names["exclude"],
        "include": CliInput.option_names["include"]
    }
    parser = CliInput().create_parser()

    @pytest.mark.parametrize("input_list", [single_list, double_list])
    @pytest.mark.parametrize("option", [*options.items()])
    def test_input_list_true(self, input_list, option):
        opt_type, opt_names = option
        for opt_name in opt_names:
            assert isinstance(self.validate_arguments(self.parser.parse_args([opt_name, *input_list]
                                                                             ))[opt_type], list)

    def test_input_list_false(self):
        arguments = self.validate_arguments(self.parser.parse_args([]))
        assert arguments["exclude"] is False
        assert arguments["include"] is False

    def test_lists_exclusive(self):
        with pytest.raises(TypeError) as exc:
            self.validate_inex_lists(self.double_list, self.double_list)

        assert str(exc.value) == "[CRITICAL]: Mutually exclusive lists were provided, use --help."\
                                 " Program will exit now."


class TestArgumentParsing(CliInput):

    parser = CliInput().create_parser()
    invalid_options = ["-en", "-ei", "-ie", "-in", "-ein", "-eni", "-ien", "-ine"]
    example_id = "AB1234"

    @pytest.mark.parametrize("option_pair", create_unique_pairs(CliInput.option_names
                             ["verification"], CliInput.option_names["exclude"], example_id))
    def test_exclude_options(self, option_pair):
        arguments = self.validate_arguments(self.parser.parse_args(option_pair))
        assert isinstance(arguments["exclude"], list)
        assert arguments["exclude"] == [self.example_id]
        assert arguments["include"] is False
        assert arguments["verification"] is False

    @pytest.mark.parametrize("option_pair", create_unique_pairs(CliInput.option_names
                             ["verification"], CliInput.option_names["include"], example_id))
    def test_include_options(self, option_pair):
        arguments = self.validate_arguments(self.parser.parse_args(option_pair))
        assert arguments["exclude"] is False
        assert isinstance(arguments["include"], list)
        assert arguments["include"] == [self.example_id]
        assert arguments["verification"] is False

    @pytest.mark.parametrize("joined", invalid_options)
    def test_short_option_cat(self, joined: str):
        with pytest.raises(TypeError) as exc:
            self.validate_arguments(self.parser.parse_args([joined]))

        assert str(exc.value) == "[CRITICAL]: Short options concatenation is not allowed. Program"\
                                 " will exit now."
