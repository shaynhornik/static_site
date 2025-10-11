from textnode import TextNode, TextType

def main():
    test = TextNode("Anchor text", TextType.LINK, "https://www.boot.dev")
    print(test)

if __name__ == "__main__":
    main()
