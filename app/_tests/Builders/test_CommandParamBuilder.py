from unittest import TestCase
from app.Builders import BuilderCommandParams


class TestBuilderCommandParams(TestCase):

    _builder: BuilderCommandParams = BuilderCommandParams()
    _test_data_list: list = [
            ['a', 'test_value'],
            ['f'],
            ['-not_alias', 'test_value'],
            ['-not_alias_flag']
    ]
    _test_data_list_with_text_value: list = [
        ['a', 'test_value'],
        ['f'],
        ['-not_alias', 'test_value'],
        'text_value'
    ]
    _test_data_dict: dict = {
        '-a': 'test_value',
        '-f': None,
        '--not_alias': 'test_value',
        '--not_alias_flag': None
    }

    _test_data_dict_with_text_value: dict = {
        '-a': 'test_value',
        '-f': None,
        '--not_alias': 'test_value',
        '--not_alias_flag': None,
        'text_value': None,
        'text_value_with_change_key': 'this_display'
    }

    def test_build_params_from_list(self):
        expected: str = "-a test_value -f --not_alias test_value --not_alias_flag"
        results = self._builder.build_from_list(self._test_data_list)

        self.assertEqual(str(results), expected)

    def test_build_params_text_value_from_list(self):
        expected: str = "-a test_value -f --not_alias test_value text_value"
        results = self._builder.build_from_list(self._test_data_list_with_text_value)

        self.assertEqual(str(results), expected)

    def test_build_params_from_dict(self):
        expected: str = "-a test_value -f --not_alias test_value --not_alias_flag"
        results = self._builder.build_from_dict(self._test_data_dict)

        self.assertEqual(str(results), expected)

    def test_build_params_text_value_from_dict(self):
        expected: str = "-a test_value -f --not_alias test_value --not_alias_flag text_value this_display"
        results = self._builder.build_from_dict(self._test_data_dict_with_text_value)

        self.assertEqual(str(results), expected)
