import unittest
from textnode import TextNode, TextType, split_nodes_image, text_node_to_html_node, split_nodes_delimiter, text_to_textnodes


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("hi",TextType.BOLD)
        node2 = TextNode("hi",TextType.ITALIC)
        self.assertNotEqual(node,node2)

    def test_url(self):
        node = TextNode("a",TextType.BOLD,"http")
        node2 = TextNode("a",TextType.BOLD)
        self.assertNotEqual(node,node2)

    def test_emptyname(self):
        node = TextNode("",TextType.BOLD)
        node2 = TextNode("",TextType.BOLD)
        self.assertEqual(node, node2)

    def test_node_convertor(self):
        text_node = TextNode("Hello!",TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == None
        assert html_node.value == "Hello!"

    def test_split_nodes(self):
        res_list = split_nodes_delimiter(
        [TextNode("Hello `code` and `more code`", TextType.TEXT)
        ,TextNode("Just plain text", TextType.TEXT)
        ,TextNode("**hello world**", TextType.BOLD)]
        ,"`",TextType.CODE)
        self.assertEqual(len(res_list),6)

        self.assertEqual(res_list[0].text, "Hello ")
        self.assertEqual(res_list[0].text_type, TextType.TEXT)

        self.assertEqual(res_list[1].text, "code")
        self.assertEqual(res_list[1].text_type, TextType.CODE)

        self.assertEqual(res_list[2].text, " and ")
        self.assertEqual(res_list[2].text_type, TextType.TEXT)

        self.assertEqual(res_list[3].text, "more code")
        self.assertEqual(res_list[3].text_type, TextType.CODE)

        self.assertEqual(res_list[4].text, "Just plain text")
        self.assertEqual(res_list[4].text_type, TextType.TEXT)

        self.assertEqual(res_list[5].text, "**hello world**")
        self.assertEqual(res_list[5].text_type, TextType.BOLD)

    def test_split_nodes_image(self):
        text_node = TextNode("This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",TextType.TEXT)
        image = split_nodes_image([text_node])
        self.assertEqual(len(image),4)

    def test_text_to_textnodes(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        test = text_to_textnodes(text)
        self.assertEqual(len(test),10)

        self.assertEqual(test[0].text, "This is ")
        self.assertEqual(test[0].text_type, TextType.TEXT)

        self.assertEqual(test[1].text, "text")
        self.assertEqual(test[1].text_type, TextType.BOLD)

        self.assertEqual(test[2].text, " with an ")
        self.assertEqual(test[2].text_type, TextType.TEXT)

        self.assertEqual(test[3].text, "italic")
        self.assertEqual(test[3].text_type, TextType.ITALIC)

        self.assertEqual(test[4].text, " word and a ")
        self.assertEqual(test[4].text_type, TextType.TEXT)

        self.assertEqual(test[5].text, "code block")
        self.assertEqual(test[5].text_type, TextType.CODE)

        self.assertEqual(test[6].text, " and an ")
        self.assertEqual(test[6].text_type, TextType.TEXT)
        
        self.assertEqual(test[7].text, "obi wan image")
        self.assertEqual(test[7].text_type, TextType.IMAGE)
        self.assertEqual(test[7].url,"https://i.imgur.com/fJRm4Vk.jpeg")

        self.assertEqual(test[8].text, " and a ")
        self.assertEqual(test[8].text_type, TextType.TEXT)

        self.assertEqual(test[9].text, "link")
        self.assertEqual(test[9].text_type, TextType.LINK)
        self.assertEqual(test[9].url,"https://boot.dev")


if __name__ == "__main__":
    unittest.main()