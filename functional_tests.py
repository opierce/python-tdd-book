from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Chrome()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Edith goes to check this new site she was referred to
		self.browser.get('http://localhost:8000')

		# Edith notices the title of the app in the status bar
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')

		# She is invited to start a to-do item right away

		# She types "Buy peacock feathers" into a text box

		# When she hits enter, the page updates, and now the pages lists
		# "1: Buy peacock feathers" as an item in a to-do list

		# Another text box invites her to add another item. She
		# enters "Use peacock feathers to make a fly" (Edith is very methodical)

		# The page updates again, and now shows both items on her list

		# Edith wonders whether the site will still remember her list. Then she sees
		# that the site has generated a unique URL for her -- there is some
		# explanatory text to that effect.

		# She visits that URL - her to-do list is still there.

		# Satisfied, she goes back to sleep.
		browser.quit()

if __name__ == '__main__':
	unittest.main()



