import unittest
import np
from day14_part2 import *

input_array = get_input("input_test.txt")
flattened_input = 'O....#....O.OO#....#.....##...OO.#O....O.O.....O#.O.#..O.#.#..O..#O..O.......O..#....###..#OO..#....'
tilted_north = ['OOOO.#.O..', 'OO..#....#', 'OO..O##..O', 'O..#.OO...', '........#.',
                '..#....#.#', '..O..#.O.O', '..O.......', '#....###..', '#....#....']
tilted_west =  ['O....#....', 'OOO.#....#', '.....##...', 'OO.#OO....', 'OO......#.',
                'O.#O...#.#', 'O....#OO..', 'O.........', '#....###..', '#OO..#....']
tilted_south = ['.....#....', '....#....#', '...O.##...', '...#......', 'O.O....O#O',
                'O.#..O.#.#', 'O....#....', 'OO....OO..', '#OO..###..', '#OO.O#...O']
tilted_east =  ['....O#....', '.OOO#....#', '.....##...', '.OO#....OO', '......OO#.',
                '.O#...O#.#', '....O#..OO', '.........O', '#....###..', '#..OO#....']

class Flatten(unittest.TestCase):
    def test_flatten(self):
        self.assertEqual(flatten(input_array), flattened_input)
