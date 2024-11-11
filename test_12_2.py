import module_12_2
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner_1 = module_12_2.Runner("Усэйн", 10)
        self.runner_2 = module_12_2.Runner("Андрей", 9)
        self.runner_3 = module_12_2.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            print(f'Тест: {test_key}')
            for key, value in test_value.items():
                print(f'{key}: {value.name}')

    def test_1(self):
        tour = module_12_2.Tournament(90, self.runner_1,  self.runner_3)
        self.all_results["1"] = tour.start()
        last_place = max(self.all_results["1"].keys())
        last_runner = self.all_results["1"][last_place]
        self.assertEqual(last_runner.name, 'Ник')

    def test_2(self):
        tour = module_12_2.Tournament(90, self.runner_2, self.runner_3)
        self.all_results["2"] = tour.start()
        last_place = max(self.all_results["2"].keys())
        last_runner = self.all_results["2"][last_place]
        self.assertEqual(last_runner.name, 'Ник')

    def test_3(self):
        tour = module_12_2.Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        self.all_results["3"] = tour.start()
        last_place = max(self.all_results["3"].keys())
        last_runner = self.all_results["3"][last_place]
        self.assertEqual(last_runner.name, 'Ник')


if __name__ == '__main__':
    unittest.main()
