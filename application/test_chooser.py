from chooser import restaurantChooser
import unittest

class TestResturauntChooser(unittest.TestCase):
    
    def test_location_keyword_radius(self):
        """
        Small number of restaurants at chosen location make it easy to narrow down potential taco places within a 15 mile radius.
        If test passes then the search API is functioning
        """
        testLocation = restaurantChooser("Rockville, Indiana", "taco", "15")
        testLocation.run()
        knownList = ["Taco tequilas In Clinton", "Taco Bell", "Mario Brothers", "Benjamin's Family Dining"]
        print(testLocation.chosen['name'])
        self.assertIn(testLocation.chosen['name'], knownList)


if __name__ == '__main__':
    unittest.main()