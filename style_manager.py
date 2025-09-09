class StyleManager:
    def __init__(self):
        self.styles = {
            "Default": ("color: black; background-color: white;", "background-color: white; border: 4px solid white;"),
            "Pixelated": ("color: black; background-color: white; font-family: Courier;", "background-color: #8b0000; border: 4px solid #8b0000;"),
            "Dark": ("color: white; background-color: black;", "background-color: gray; border: 4px solid gray;"),
            "Highlighted": ("color: red; background-color: white;", "background-color: #8b0000; border: 4px solid #8b0000;"),
            "Blue Glow": ("color: white; background-color: #001f3f; text-shadow: 2px 2px 8px cyan;", "background-color: #001f3f; border: 4px solid cyan;"),
            "Big Bold": ("color: black; background-color: lightgray; font-weight: bold;", "background-color: lightgray; border: 4px solid black;"),
            "Minimalist": ("color: #333; background-color: #fafafa;", "background-color: #fafafa; border: 2px solid #ccc;"),
            "Custom": ("", "border: 4px solid #555; background-color: white;")
        }

    def get_style_names(self):
        return list(self.styles.keys())

    def get_style(self, style_name, font, size, custom_css):
        if style_name == "Custom":
            css = custom_css if custom_css else "color: black; background-color: white;"
            return (f"font-size: {size}px; font-family: {font}; {css}", self.styles["Custom"][1])
        else:
            base_css, frame = self.styles[style_name]
            return (f"font-size: {size}px; font-family: {font}; {base_css}", frame)
