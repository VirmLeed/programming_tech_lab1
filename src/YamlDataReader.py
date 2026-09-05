from Types import DataType
from DataReader import DataReader
from yaml import load, Loader


class YamlDataReader(DataReader):
    def __init__(self) -> None:
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        with open(path, encoding='utf-8') as file:
            input = load(file, Loader)
            try:
                for item in input:
                    name, scores = list(item.items())[0]
                    self.students[name] = []
                    for subject, score in scores.items():
                        self.students[name].append((subject, score))
            except:
                raise ValueError("Invalid input file for YamlDataReader")

        return self.students
