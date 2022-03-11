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
    _test_data_dict: dict = {
        'a': 'test_value',
        'f': None,
        '-not_alias': 'test_value',
        '-not_alias_flag': None
    }

    def test_build_params_from_list(self):
        expected: str = "-a test_value -f --not_alias test_value --not_alias_flag"
        results = self._builder.build_from_list(self._test_data_list)

        self.assertEqual(str(results), expected)

    def test_build_params_from_dict(self):
        expected: str = "-a test_value -f --not_alias test_value --not_alias_flag"
        results = self._builder.build_from_struct(self._test_data_dict)

        self.assertEqual(str(results), expected)
