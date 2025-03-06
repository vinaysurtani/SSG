import sys
from copy_static import copy_static
from generate_page import generate_page,generate_pages_recursive
from textnode import TextNode, TextType

def main():
    basepath = sys.argv[1]
    if not sys.argv[1]:
        basepath = '/'
    #node = TextNode('This is a text node',TextType.BOLD_TEXT,'https://www.boot.dev')
    #print(node)
    copy_static()
    #generate_page('/mnt/c/Users/VINAY/OneDrive/Desktop/boot_dev/workspace/github.com/vinaysurtani/SSG/content/index.md', '/mnt/c/Users/VINAY/OneDrive/Desktop/boot_dev/workspace/github.com/vinaysurtani/SSG/template.html', '/mnt/c/Users/VINAY/OneDrive/Desktop/boot_dev/workspace/github.com/vinaysurtani/SSG/public/index.html')
    generate_pages_recursive('/mnt/c/Users/VINAY/OneDrive/Desktop/boot_dev/workspace/github.com/vinaysurtani/SSG/content/', '/mnt/c/Users/VINAY/OneDrive/Desktop/boot_dev/workspace/github.com/vinaysurtani/SSG/template.html', '/mnt/c/Users/VINAY/OneDrive/Desktop/boot_dev/workspace/github.com/vinaysurtani/SSG/docs/', basepath)


main()