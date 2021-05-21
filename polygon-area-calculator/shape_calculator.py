class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = 2 * self.width + 2 * self.height
        return perimeter

    def get_diagonal(self):
        diag = (self.width**2 + self.height**2)**.5
        return diag

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        s = ''
        for i in range(self.height):
            s += '*' * self.width + '\n'
        return s

    def get_amount_inside(self, other):
        return (self.width // other.width) * (self.height // other.height)

    def __str__(self):
        return "Rectangle(width={}, height={})".format(self.width, self.height)


class Square(Rectangle):
    def __init__(self, length):
        self.width = length
        self.height = length

    def set_side(self, length):
        self.height = length
        self.width = length

    def set_height(self, length):
        self.height = length
        self.width = length

    def set_width(self, length):
        self.height = length
        self.width = length

    def __str__(self):
        return "Square(side={})".format(self.width)
