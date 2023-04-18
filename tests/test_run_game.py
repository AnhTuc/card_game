import unittest
from unittest import mock
from dev.main import card_game, game_continue
from dev.card_game import CardGame
from dev.player import Player
from dev.helper import *
import os
import sys


class TestRun(unittest.TestCase):
    def setUp(self) -> None:
        self.player1 = Player(player_score=60, name='')
        self.game = CardGame()
    """
    Failed test in group of try and except
    """

    @mock.patch("builtins.print")
    @mock.patch("builtins.input")
    def test_game_continue_exit(self, fake_input, fake_print):
        """
        Test return if game continue
        """
        fake_input.side_effect = ['s']
        check_game_over = mock.Mock(return_value=False)
        with self.assertRaises(SystemExit) as cm:
            game_continue(house = self.game, player=self.player1)
            fake_print.assert_called_with("Closing card game ...")
        self.assertEqual(cm.exception.code, 1)

    @mock.patch("builtins.print")
    @mock.patch("builtins.input")
    def test_game_continue_exit(self, fake_input, fake_print):
        """
        Test return if game continue
        """
        fake_input.side_effect = ['s']
        check_game_over = mock.Mock(return_value=False)
        with self.assertRaises(SystemExit) as cm:
            game_continue(house = self.game, player=self.player1)
            fake_print.assert_called_with("Closing card game ...")
        self.assertEqual(cm.exception.code, 1)

    @mock.patch("builtins.input")
    def test_game_continue(self, fake_input):
        """
        Test return if game continue
        """
        fake_input.side_effect = ['s']
        check_game_over = mock.Mock(return_value=False)

        # with self.assertRaises(SystemExit) as cm:
        #     game_continue(house = self.game, player=self.player1)
        #     fake_print.assert_called_with("Closing card game ...")
        # self.assertEqual(cm.exception.code, 1)

    

if __name__ == "__main__":
    unittest.main()