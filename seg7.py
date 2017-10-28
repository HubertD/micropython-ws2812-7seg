class Seg7:
    def __init__(self, np, h1, h2, h3, v1, v2, v3, v4):
        self.np = np
        self.bars = [h1, h2, h3, v1, v2, v3, v4]
        self.digits = [
            0b1011111,  # 0
            0b0000101,  # 1
            0b1110110,  # 2
            0b1110101,  # 3
            0b0101101,  # 4
            0b1111001,  # 5
            0b1111011,  # 6
            0b1000101,  # 7
            0b1111111,  # 8
            0b1111101,  # 9
        ]   # HHHVVVV
            # 1231234

    def paint(self, bar_id, color):
        for i in self.bars[bar_id]:
            self.np[1 + ord(i)] = color

    def clear(self, bar_id):
        self.paint(bar_id, (0, 0, 0))

    def set(self, digit, color):
        data = self.digits[digit]
        for i in range(7):
            if (data & (1 << i)) != 0:
                self.paint(6-i, color)
            else:
                self.clear(6-i)
