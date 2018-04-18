from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Scott has heard about a cool new online to-do app.
        # He goes to check out its homepage
        self.browser.get("http://localhost:8000")

        # He notices the page title and header mention to-do lists.
        self.assertIn("To-Do", self.browser.title)
        self.fail('Finish the test!')

        # He is invited to enter a to-do item straight away

        # He types "Buy peacock feathers" into a text box (Scott's hobby is tying fly-fishing lures)

        # When he hits enter, the page updates, and now the page lists:
        # "1. Buy peacock feathers" as an item in a to-do list

        # There is still a text box inviting him to add another item.
        # He enters "Use peacock feathers to make a fly" (Scott is very methodical)

        # The page updates again, and now shows both items on his list

        # Scott wonders whether the site will remember his list.
        # Then he sees that the site has generated a unique URL for him
        # There is some explanatory text to that effect

        # He visits that URL - his to-do list is still there

        # Satisfied, he goes back to sleep

if __name__ == '__main__':
    unittest.main()

