from bowling_error import BowlingError
from frame import Frame


class BowlingGame:

    def __init__(self):
        self.frames = []
    
    def add_frame(self, frame: Frame) -> None:
        if 10 <= len(self.frames):
            raise BowlingError
        self.frames.append(frame)

    def get_frame_at(self, i: int) -> Frame:
        if i >= len(self.frames):
            raise BowlingError
        return self.frames[i]

    def calculate_score(self) -> int:
        total = 0
        for i in range(0, len(self.frames)):
            if self.frames[i].is_spare() and i+1 < len(self.frames):
                self.frames[i].set_bonus(self.frames[i+1].get_first_throw())
            total += self.frames[i].score()

        return total

    def set_first_bonus_throw(self, bonus_throw: int) -> None:
        pass

    def set_second_bonus_throw(self, bonus_throw: int) -> None:
        pass
