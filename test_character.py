import unittest
from character.character import Character
from unittest.mock import patch

class TestCharactersName(unittest.TestCase):

    @patch('builtins.input', return_value='Player1')
    def test_is_name_valid(self, mock_input):
        player1 = Character("Player1", 10, 10, 100, 50, 5, 5, 5, 5, 5, 5, "Warrior", [])
        self.assertEqual(player1.create_player(), "Player1")
    
    @patch('builtins.input', return_value='2')
    def test_is_name_too_short(self, mock_input):
        player4 = Character("2", 10, 10, 100, 50, 5, 5, 5, 5, 5, 5, "Warrior", [])
        self.assertEqual(player4.create_player(), "Name must be between 3 and 10 characters")

    @patch('builtins.input', return_value='Player12345')
    def test_is_name_too_long(self, mock_input):
        player4 = Character("Player12345", 10, 10, 100, 50, 5, 5, 5, 5, 5, 5, "Warrior", [])
        self.assertEqual(player4.create_player(), "Name must be between 3 and 10 characters")


if __name__ == '__main__':
    unittest.main()