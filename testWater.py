import unittest
import water

class TestSolver(unittest.TestCase):

    def testGivenExample(self):
        input = { 'truck': 60, 'pipes': [ { 'name': 'pipe 1', 'cost': 10, 'litres': 20 }, { 'name': 'pipe 2', 'cost': 15, 'litres': 50 }, { 'name': 'pipe 3', 'cost': 4, 'litres': 25 }, { 'name': 'pipe 4', 'cost': 11, 'litres': 30 } ] }
        expected_pipes = set(['pipe 3', 'pipe 4'])
        expected_cost = 15
        actual = water.solve(input)
        self.assertEqual(expected_cost, actual['Cost'])
        self.assertEqual(expected_pipes, set(actual['Pipes']))


    def testSmallerLimit(self):
        input = { 'truck': 10, 'pipes': [ { 'name': 'pipe 3', 'cost': 4, 'litres': 2 }, { 'name': 'pipe 4', 'cost': 11, 'litres': 3 }, { 'name': 'pipe 1', 'cost': 1, 'litres': 4 }, { 'name': 'pipe 2', 'cost': 15, 'litres': 6} ] }
        expected_pipes = set(['pipe 1', 'pipe 2'])
        expected_cost = 16
        actual = water.solve(input)
        self.assertEqual(expected_cost, actual['Cost'])
        self.assertEqual(expected_pipes, set(actual['Pipes']))

    def testOnePipe(self):
        input = { 'truck': 10, 'pipes': [ { 'name': 'pipe 3', 'cost': 4, 'litres': 2 }] }
        expected_pipes = set(['pipe 3'])
        expected_cost = 4
        actual = water.solve(input)
        self.assertEqual(expected_cost, actual['Cost'])
        self.assertEqual(expected_pipes, set(actual['Pipes']))
