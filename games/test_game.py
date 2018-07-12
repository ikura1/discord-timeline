import unittest
from lifegame import Game


class MyTestCase(unittest.TestCase):
    def test_kaso(self):
        field = [
            0, 0, 0,
            0, 1, 0,
            0, 0, 0
        ]
        game = Game(3)
        game.field = field
        flg = game.is_alive(4)
        self.assertEqual(flg, 0)

    def test_kamitu(self):
        field = [
            1, 1, 1,
            0, 1, 1,
            0, 0, 0
        ]
        game = Game(3)
        game.field = field
        flg = game.is_alive(4)
        print(game.get_around_indexes(4))
        self.assertEqual(sum(game.around(4)), 4)
        self.assertEqual(flg, 0)

    def test_ikita(self):
        field = [
            0, 1, 1,
            0, 1, 0,
            0, 0, 0
        ]
        game = Game(3)
        game.field = field
        flg = game.is_alive(4)
        self.assertEqual(flg, 1)

    def test_umareta(self):
        field = [
            0, 0, 1,
            0, 0, 1,
            0, 0, 1
        ]
        game = Game(3)
        game.field = field
        flg = game.is_alive(4)
        self.assertEqual(flg, 1)


if __name__ == '__main__':
    unittest.main()
