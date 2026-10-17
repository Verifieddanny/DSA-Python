class Cookie:
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return f"This cookie is {self.color}."

    def get_color(self):
        return self.color

    def set_color(self, new_color):
        self.color = new_color


cookie1 = Cookie("brown")
print(cookie1)  # Output: This cookie is brown.
cookie1.set_color("chocolate chip")
print(cookie1)  # Output: This cookie is chocolate chip.