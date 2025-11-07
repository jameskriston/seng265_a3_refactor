from unittest import TestCase
from unittest import main
from blogging.blog import Blog

class BlogTest(TestCase):

    def test_eq(self):
        blog1 = Blog(1, "blog1 name", "blog1_url", "blog1@gmail.com")
        blog1a = Blog(1, "blog1 name", "blog1_url", "blog1@gmail.com")
        blog2 = Blog(2, "blog2 name", "blog2_url", "blog2@gmail.com")
        blog2a = Blog(2, "blog2 name", "blog2_url", "blog2a@gmail.com")
        blog2b = Blog(2, "blog2 name", "blog2b_url", "blog2@gmail.com")
        blog2c = Blog(2, "blog2c name", "blog2_url", "blog2@gmail.com")

        self.assertIsNotNone(blog1, "blog 1 should exist")
        self.assertEqual(blog1, blog1a, "blog1 = blog1a")
        self.assertNotEqual(blog2, blog2a, "different emails")
        self.assertNotEqual(blog2, blog2b, "different urls")
        self.assertNotEqual(blog2, blog2c, "different names")
    
    def test_str(self):
        blog1 = Blog(1, "blog1 name", "blog1_url", "blog1@gmail.com")
        
        self.assertIsNotNone(blog1, "blog1 should exist")
        self.assertEqual(str(blog1), "1, blog1 name, blog1_url, blog1@gmail.com, []", "blog1 matches string")

    def test_repr(self):
        blog1 = Blog(1, "blog1 name", "blog1_url", "blog1@gmail.com")

        self.assertIsNotNone(blog1, "blog1 should exist")
        self.assertEqual(repr(blog1), "Blog(1, blog1 name, blog1_url, blog1@gmail.com, [])", "blog1 matches string")
        #add more tests here later


    if __name__ == '__main__':
        unittest.main()
