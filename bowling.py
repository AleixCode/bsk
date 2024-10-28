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
        spare = False
        for frame in self.frames:
            if spare:
                total += frame.get_first_throw()
                spare = False

            if frame.is_spare():
                spare = True

            total += frame.score()
        return total

    def set_first_bonus_throw(self, bonus_throw: int) -> None:
        pass

    def set_second_bonus_throw(self, bonus_throw: int) -> None:
        pass
