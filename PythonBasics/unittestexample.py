# unit test library from python
import unittest
from example import Example

# inheriting from unit test module
class MyTestCase(unittest.TestCase):
    # always start your unit test with name "test" at beginning
    def test_add(self):
        result = Example.add(self,10,20)
        self.assertEqual(result,30)

    def test_sub(self):
        result = Example.sub(self,20,10)
        self.assertEqual(result,10)
        
# to run from cmd line
# if __name__ == '__main__':
#     unittest.main()
