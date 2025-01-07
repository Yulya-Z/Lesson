import unittest
from module_12 import tests_12_3


Runner_Tournament = unittest.TestSuite()
Runner_Tournament.addTest(unittest.TestLoader().loadTestsFromModule(tests_12_3))
test = unittest.TextTestRunner(verbosity=2)
test.run(Runner_Tournament)

