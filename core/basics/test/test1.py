from unittest import TestCase
from .sample1 import Car

class TestCar(TestCase):
    def setUp(self) -> None:
        self.car_instance = Car("ford")

    def test_car_can_move(self):
        self.assertEqual(self.car_instance.move(), "the ford can move")

    def test_car_health(self):
        self.assertTrue(self.car_instance.car_health())

    def test_car_need_repair(self):
        self.assertFalse(self.car_instance.car_need_rapair())

    def test_car_error(self):
        with self.assertRaises(ValueError):
            self.car_instance.car_error()

