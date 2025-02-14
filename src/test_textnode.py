import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq_type(self):
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node2, node3)

    def test_neq_txt(self):
        node2 = TextNode("This is a text node", TextType.BOLD)
        node3 = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(node2, node3)

    def test_neq_url(self):
        node2 = TextNode("This is a text node", TextType.BOLD, url="https://www.marsdude.com")
        node3 = TextNode("This is another text node", TextType.BOLD)
        self.assertNotEqual(node2, node3)
    



if __name__ == "__main__":
    unittest.main()