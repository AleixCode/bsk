import unittest

from bowling import BowlingGame
from bowling_error import BowlingError
from frame import Frame


class TestBowlingGame(unittest.TestCase):

    def test_game_spare_frames(self):
        game = BowlingGame()
        f0 = Frame(1, 9)
        f1 = Frame(3,6)
        f2 = Frame(7,2)
        f3 = Frame(3,6)
        f4 = Frame(4,4)
        f5 = Frame(5,3)
        f6 = Frame(3,3)
        f7 = Frame(4,5)
        f8 = Frame(8,1)
        f9 = Frame(2,6)

        game.add_frame(f0)
        game.add_frame(f1)
        game.add_frame(f2)
        game.add_frame(f3)
        game.add_frame(f4)
        game.add_frame(f5)
        game.add_frame(f6)
        game.add_frame(f7)
        game.add_frame(f8)
        game.add_frame(f9)

        self.assertEqual(88, game.calculate_score())

    def test_game_creation(self):
        f = Frame(1,5)
        game = BowlingGame()
        game.add_frame(f)
        self.assertEqual(f, game.get_frame_at(0))

    def test_game_empty(self):
        game = BowlingGame()
        self.assertRaises(BowlingError, game.get_frame_at, 0)

    def test_game_0_frames(self):
        f = Frame(1,5)
        game = BowlingGame()
        self.assertEqual(0, game.calculate_score())

    def test_game_points_sum(self):
        game = BowlingGame()
        f0 = Frame(1, 5)
        f1 = Frame(3,6)
        f2 = Frame(7,2)
        f3 = Frame(3,6)
        f4 = Frame(4,4)
        f5 = Frame(5,3)
        f6 = Frame(3,3)
        f7 = Frame(4,5)
        f8 = Frame(8,1)
        f9 = Frame(2,6)

        game.add_frame(f0)
        game.add_frame(f1)
        game.add_frame(f2)
        game.add_frame(f3)
        game.add_frame(f4)
        game.add_frame(f5)
        game.add_frame(f6)
        game.add_frame(f7)
        game.add_frame(f8)
        game.add_frame(f9)

        self.assertEqual(81, game.calculate_score())

    def test_game_more_than_10_frames(self):
        game = BowlingGame()
        f0 = Frame(1, 5)
        f1 = Frame(3,6)
        f2 = Frame(7,2)
        f3 = Frame(3,6)
        f4 = Frame(4,4)
        f5 = Frame(5,3)
        f6 = Frame(3,3)
        f7 = Frame(4,5)
        f8 = Frame(8,1)
        f9 = Frame(2,6)
        f10 = Frame(2, 6)

        game.add_frame(f0)
        game.add_frame(f1)
        game.add_frame(f2)
        game.add_frame(f3)
        game.add_frame(f4)
        game.add_frame(f5)
        game.add_frame(f6)
        game.add_frame(f7)
        game.add_frame(f8)
        game.add_frame(f9)

        self.assertRaises(BowlingError, game.add_frame, f10)

