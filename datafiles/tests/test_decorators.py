# pylint: disable=unused-variable

# import logging
from dataclasses import dataclass, is_dataclass
from unittest.mock import patch

from datafiles import decorators


# import log


def describe_datafile():
    def it_turns_normal_class_into_dataclass(expect):
        class Normal:
            pass

        cls = decorators.datafile("<pattern>")(Normal)

        expect(is_dataclass(cls)).is_(True)

    def it_can_reuse_existing_dataclass(expect):
        @dataclass
        class Existing:
            pass

        cls = decorators.datafile("")(Existing)

        expect(id(cls)) == id(Existing)

    def it_maps_to_dataclass_without_paranthesis(expect):
        class Sample:
            pass

        cls = decorators.datafile(Sample)

        expect(is_dataclass(cls)).is_(True)

    def it_forwards_arguments_dataclass_decorator(expect):
        class Sample:
            pass

        cls = decorators.datafile(order=True)(Sample)

        expect(is_dataclass(cls)).is_(True)

    def it_does_not_log_by_default(expect):
        @dataclass
        class Sample:
            key: int
            name: str

        # with patch.object(log, 'debug') as log2:
        #     decorators.datafile("{self.key}.yml")(Sample)
        #     print(log2.mock_calls)
        #     expect(len(log2.mock_calls)) == 0

        with patch('log.utils.ensure_initialized') as init:
            decorators.datafile("{self.key}.yml")(Sample)
            print(init.mock_calls)
            expect(len(init.mock_calls)) == 0
