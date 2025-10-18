import os
import shutil
from textnode import TextNode, TextType

def main():
    test = TextNode("Anchor text", TextType.LINK, "https://www.boot.dev")
    print(test)
    static_to_public("static", "public")

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
