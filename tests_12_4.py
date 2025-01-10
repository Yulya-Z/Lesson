import logging
import unittest


class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class RunnerTest(unittest.TestCase):

    def setUp(self):
        self.logger = logging.getLogger()

    def test_walk(self):
        try:
            runner = Runner(name='Тестовый бегун', speed=-5)  # С отрицательной скоростью
        except ValueError as e:
            logging.warning("Неверная скорость для Runner: %s", e)
        else:
            logging.info('"test_walk" выполнен успешно')

    def test_run(self):
        try:
            runner = Runner(name=12345, speed=5)  # С неправильным типом для имени
        except TypeError as e:
            logging.warning("Неверный тип данных для объекта Runner: %s", e)
        else:
            logging.info('"test_run" выполнен успешно')

    def test_challenge(self):
        runner1 = Runner('John')
        runner2 = Runner('Harry')
        for _ in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)
        self.logger.info('"test_challenge" выполнен успешно')

if __name__ == '__main__':

    unittest.main()

logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding="utf-8",
                format="%(asctime)s | %(levelname)s | %(message)s")

first = Runner('Вося', 10)
second = Runner('Илья', 5)
third = Runner('Арсен', 10)
#
t = Tournament(101, first, second)
print(t.start())