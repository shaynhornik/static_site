import sys
import os
import shutil
from textnode import TextNode, TextType
from generate_page import generate_page, generate_pages_recursive



def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    test = TextNode("Anchor text", TextType.LINK, "https://www.boot.dev")
    print(test)
    static_to_public("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)

def static_to_public(static, public):
    if os.path.exists(public):
        shutil.rmtree(public)
    os.mkdir(public)

    items_in_static = os.listdir(static)
    for item in items_in_static:
        source = os.path.join(static, item)
        destination = os.path.join(public, item)
        if os.path.isfile(source):
            shutil.copy(source, destination)
        if os.path.isdir(source):
            os.mkdir(destination)
            static_to_public(source, destination)




if __name__ == "__main__":
    main()
