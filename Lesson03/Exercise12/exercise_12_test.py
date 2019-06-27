import unittest
import import_ipynb
import datetime

class Test(unittest.TestCase):
    def setUp(self):
        # For some reason importing the notebook globally stops the tests from being registered correctly.
        # Putting the import in the setUp method appears to solve this.
        import Exercise12
        self.exercises = Exercise12

    def test(self):
        self.assertEqual(self.exercises.add_suffix('.co.uk'), 'google.co.uk')
        
if __name__ == '__main__':
    unittest.main()
