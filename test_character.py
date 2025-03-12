import unittest
from character import Character
from unittest.mock import patch

class TestCharactersName(unittest.TestCase):

    @patch('builtins.input', return_value='Player1')
    def test_IsNameValid(character, mock_input):
        player1 = Character("Player1", 10, 10, 100, 50, 5, 5, 5, 5, 5, 5, "Warrior", [])
        character.assertEqual(player1.createAPlayer(), "Player1")
    
    @patch('builtins.input', return_value='2')
    def test_IsNameTooShort(character, mock_input):
        player4 = Character("2", 10, 10, 100, 50, 5, 5, 5, 5, 5, 5, "Warrior", [])
        character.assertEqual(player4.createAPlayer(), "Name must be between 3 and 10 characters")

    @patch('builtins.input', return_value='Player12345')
    def test_IsNameTooLong(character, mock_input):
        player4 = Character("Player12345", 10, 10, 100, 50, 5, 5, 5, 5, 5, 5, "Warrior", [])
        character.assertEqual(player4.createAPlayer(), "Name must be between 3 and 10 characters")


if __name__ == '__main__':
    unittest.main()