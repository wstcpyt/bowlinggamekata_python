__author__ = 'yutongpang'
from unittest import TestCase
from bowlinggame import Game


class BowlingGameTest(TestCase):
    def setUp(self):
        self.g = Game()

    def rollMany(self, n, pins):
        for i in range(0, n):
            self.g.roll(pins)

    def test_gutter_game(self):
        self.rollMany(20, 0)
        self.assertEquals(0, self.g.score())

    def test_all_ones(self):
        self.rollMany(20, 1)
        self.assertEquals(20, self.g.score())

    def test_one_spare(self):
        self.roll_spare()
        self.g.roll(3)
        self.rollMany(17, 0)
        self.assertEquals(16, self.g.score())

    def test_one_strike(self):
        self.roll_strike()
        self.g.roll(3)
        self.g.roll(4)
        self.rollMany(16, 0)
        self.assertEquals(24, self.g.score())

    def test_perfect_game(self):
        self.rollMany(12, 10)
        self.assertEquals(300, self.g.score())

    def roll_strike(self):
        self.g.roll(10)

    def roll_spare(self):
        self.g.roll(5)
        self.g.roll(5)