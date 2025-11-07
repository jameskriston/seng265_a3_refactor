from unittest import TestCase
from unittest import main
from blogging.post import Post

class PostTest(TestCase):

    def test_eq(self):
        post1 = Post(1, "post1 title", "post1 text")
        post1a = Post(1, "post1 title", "post1 text")
        post2 = Post(2, "post2 title", "post2 text")
        post2a = Post(2, "post1 title", "post2a text")
        post2b = Post(2, "post2b title", "post2 text")

        self.assertIsNotNone(post1, "post should exist")
        self.assertEqual(post1, post1a, "post1 = post1a")
        self.assertNotEqual(post2, post2a, "different titles")
        self.assertNotEqual(post2, post2b, "different text")

    def test_str(self):
        post1 = Post(1, "post1 title", "post1 text")

        self.assertIsNotNone(post1, "post should exist")
        self.assertEqual(str(post1), "1, post1 title, post1 text, {}, {}".format(post1.creation, post1.update), "post1 matches string")

    def test_repr(self):
        post1 = Post(1, "post1 title", "post1 text")

        self.assertIsNotNone(post1, "post should exist")
        self.assertEqual(repr(post1), "Post(1, post1 title, post1 text, {}, {})".format(post1.creation, post1.update), "post1 matches string")
        
    #add more tests here later


    if __name__ == '__main__':
        unittest.main()
