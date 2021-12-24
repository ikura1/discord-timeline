# -*- coding: utf-8 -*-
from numpy.random import randint
import emoji
import time


class Game(object):
    """
    LifeGame
    """

    def __init__(self, field_length=32):
        self.field_length = field_length
        self.cell_length = field_length ** 2
        self.field = randint(0, 2, self.cell_length)
        self.alive = emoji.emojize(":sun_with_face:", use_aliases=True)
        self.dead = emoji.emojize(":new_moon_with_face:", use_aliases=True)

    def next_turn(self):
        new_field = []
        for i, cell in enumerate(self.field):
            value = self.is_alive(i)
            new_field.append(value)
        self.field = new_field

    def run(self, count=100):
        for _ in range(count):
            print(self.as_text())
            self.next_turn()
            time.sleep(0.5)

    def as_text(self):
        show_cells = [self.alive if v else self.dead for v in self.field]
        show_rows = [
            "".join(show_cells[i * self.field_length : (i + 1) * self.field_length])
            for i in range(self.field_length)
        ]
        return "\n".join(show_rows)

    def is_alive(self, index):
        value = self.field[index]
        sum_around = sum(self.around(index))
        conditions = [2, 3] if value else [3]
        return int(sum_around in conditions)

    def get_around_indexes(self, index):
        cells = [-self.field_length, self.field_length]
        if index % self.field_length != 0:
            cells.extend([-self.field_length - 1, -1, self.field_length - 1])
        if (index + 1) % self.field_length != 0:
            cells.extend([-self.field_length + 1, 1, self.field_length + 1])
        return list(map(lambda x: x + index, cells))

    def around(self, index):
        indexes = self.get_around_indexes(index)
        return [self.get_cell(i) for i in indexes]

    def get_cell(self, index):
        return self.field[index] if 0 <= index < self.cell_length else 0


if __name__ == "__main__":
    game = Game(14)
    game.run()
