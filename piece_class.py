class Piece:
    index = 0
    number = 0 #1,2,3
    shape = 0 #ovals, sprouts, and diamonds
    color = 0 #green, yellow/red, pink/purple
    shading = 0 #striped, outlined, and filled
    
    def __init__(self, index, number, shape, color, shading):
        self.index = index
        self.number = number
        self.shape = shape
        self.color = color
        self.shading = shading

    def toString(self):
        return str(self.index) + " :: " + str(self.number) + " | " + str(self.shape) + " | " + str(self.color) + " | " + str(self.shading)
