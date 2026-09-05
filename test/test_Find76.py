from src.Types import DataType
from src.Find76 import Find76
import pytest


class TestFind76:
    @pytest.fixture()
    def dataset1(self) -> tuple[DataType, set[str]]:
        data: DataType = {
            "Абрамов Петр Сергеевич":
                [
                    ("английский", 21),
                    ("математика", 76),
                    ("русский язык", 76),
                    ("программирование", 76)
                ],
            "Петров Игорь Владимирович":
                [
                    ("математика", 76),
                    ("русский язык", 76),
                    ("программирование", 76),
                    ("литература", 76)
                ]
        }
        suitable_students = set([
            "Абрамов Петр Сергеевич",
            "Петров Игорь Владимирович"
        ])
        return data, suitable_students

    def test_init_find76(self, dataset1: tuple[DataType,
                                               set[str]]) -> None:
        finder = Find76(dataset1[0])
        assert dataset1[0] == finder.data

    def test_find_multiple(self, dataset1: tuple[DataType, set[str]]) -> None:
        student = Find76(dataset1[0]).find()
        assert student in dataset1[1]

    def test_find_none(self, dataset1: tuple[DataType, set[str]]) -> None:
        data: DataType = {
            "Абрамов Петр Сергеевич":
                [
                    ("английский", 21),
                    ("математика", 76),
                    ("русский язык", 76),
                    ("программирование", 84)
                ],
            "Петров Игорь Владимирович":
                [
                    ("математика", 48),
                    ("русский язык", 22),
                    ("программирование", 76),
                    ("литература", 76)
                ]
        }
        suitable_students = set([
            "Не найдено студентов, у которых 3+ предметов с 76 баллов"
        ])
        student = Find76(dataset1[0]).find()
        assert student in dataset1[1]
