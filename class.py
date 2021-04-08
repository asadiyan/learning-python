class Teddy:
    quantity = 200

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def change_color(self, color):
        print("this the method")
        self.color = color


teddy1 = Teddy("hamid", "red")
print(teddy1.color)
teddy1.change_color("brown")
print(teddy1.color)
