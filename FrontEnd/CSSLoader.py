class CSSLoader:
    def __init__(self):
        self._css = ""
        with open("styles.css", 'r') as f:
            for line in f:
                self._css += ("\n" + line)

    def get_css(self):
        return self._css