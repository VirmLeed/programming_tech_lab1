from Types import DataType


class Find76:
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data

    def find(self) -> str:
        output = "Не найдено студентов, у которых 3+ предметов с 76 баллов"
        for name, scores in self.data.items():
            num_76 = 0
            for subject, score in scores:
                if score == 76:
                    num_76 += 1
            if num_76 >= 3:
                output = name
                break

        return output
