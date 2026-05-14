class Text:
    def render(self):
        return "Normal text"

class TextDecorator:
    def __init__(self, text_component):
        self._text_component = text_component

    def render(self):
        return self._text_component.render()

class BoldDecorator(TextDecorator):
    def render(self):
        return f"<b>{super().render()}</b>"

class ItalicDecorator(TextDecorator):
    def render(self):
        return f"<i>{super().render()}</i>"

if __name__ == "__main__":
    text = Text()
    print("Base:", text.render())
    
    bold_text = BoldDecorator(text)
    print("Bold:", bold_text.render())
    
    italic_bold_text = ItalicDecorator(bold_text)
    print("Italic + Bold:", italic_bold_text.render())
