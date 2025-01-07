import unittest
from tests_12_2 import Runner
from tests_12_2 import Tournament


def skip_frozen(test_method):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            return test_method(self, *args, **kwargs)
    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_frozen
    def test_walk(self):
        runner = Runner('Bob')
        for i in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @skip_frozen
    def test_run(self):
        runner = Runner('Jack')
        for i in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @skip_frozen
    def test_challenge(self):
        runner1 = Runner('Den')
        runner2 = Runner('San')
        for i in range(10):
            runner1.run()
            runner2.walk()
        self.assertNotEqual(runner1.distance, runner2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Usein", speed=10)
        self.runner2 = Runner("Andrey", speed=9)
        self.runner3 = Runner("Nik", speed=3)

    def test_run_1(self):
        # Забег: Усэйн и Ник
        tournament = Tournament(distance=90)
        tournament.participants.append(self.runner1)  # Усэйн
        tournament.participants.append(self.runner3)  # Ник

        # Запуск турнира
        results = tournament.start()

        # Сохранение результатов
        TournamentTest.all_results['test_run_1'] = results

        # Проверка, что последний бегун - Ник
        last_race_result = results[max(results.keys())]
        self.assertTrue(last_race_result.name == 'Nik')

    @skip_frozen
    def test_run_2(self):
        # Забег: Андрей и Ник
        tournament = Tournament(distance=90)
        tournament.participants.append(self.runner2)  # Андрей
        tournament.participants.append(self.runner3)  # Ник

        # Запуск турнира
        results = tournament.start()

        # Сохранение результатов
        TournamentTest.all_results['test_run_2'] = results

        # Проверка, что последний бегун - Ник
        last_race_result = results[max(results.keys())]
        self.assertTrue(last_race_result.name == "Nik")

    @skip_frozen
    def test_run_3(self):
        # Забег: Усэйн, Андрей и Ник
        tournament = Tournament(distance=90)
        tournament.participants.append(self.runner1)  # Усэйн
        tournament.participants.append(self.runner2)  # Андрей
        tournament.participants.append(self.runner3)  # Ник

        # Запуск турнира
        results = tournament.start()

        # Сохранение результатов
        TournamentTest.all_results['test_run_3'] = results

        # Проверка, что последний бегун - Ник
        last_race_result = results[max(results.keys())]
        self.assertTrue(last_race_result.name == "Nik")

    @classmethod
    def tearDownClass(cls):
        print("Результаты всех тестов:")
        for k, v in cls.all_results.items():
            formatted_results = {place: str(runner) for place, runner in v.items()}
            print(f"{formatted_results}")


if __name__ == '__main__':
    unittest.main()