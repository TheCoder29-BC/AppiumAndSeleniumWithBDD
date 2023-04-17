# 1. Import the Files
import unittest
from SeleniumFrameWork.Tests.test_contactFormTest import ContactFormTest
from SeleniumFrameWork.Tests.test_LocatorsPagePOMModel import EnterTextTest

# 2. Creathe the object of the Class using unitTest
CF = unittest.TestLoader().loadTestsFromTestCase(ContactFormTest)
ET = unittest.TestLoader().loadTestsFromTestCase(EnterTextTest)

# 3. Create TestSuite
regressiontest = unittest.TestSuite([CF,ET])

# 4. Call the Test Runner method
unittest.TextTestRunner(verbosity=1).run(regressiontest)
# Note : All the methods in test files should define in proper run order