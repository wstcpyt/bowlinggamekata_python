__author__ = 'yutongpang'


class Game:
    def __init__(self):
        self._rolls = [0] * 21
        self._currentRoll = 0

    def roll(self, pins):
        self._rolls[self._currentRoll] = pins
        self._currentRoll += 1

    def score(self):
        score = 0
        frame_index = 0
        for frame in range(0, 10):
            if self._is_strike(frame_index):
                score += 10 + self._strike_bonus(frame_index)
                frame_index += 1
            elif self._is_spare(frame_index):
                score += 10 + self._spare_bonus(frame_index)
                frame_index += 2
            else:
                score += self._sum_of_balls_in_frame(frame_index)
                frame_index += 2
        return score

    def _is_strike(self,frame_index):
        return self._rolls[frame_index] == 10

    def _is_spare(self, frame_index):
        return self._rolls[frame_index] + self._rolls[frame_index + 1] == 10

    def _sum_of_balls_in_frame(self,frame_index):
        return self._rolls[frame_index] + self._rolls[frame_index + 1]

    def _spare_bonus(self, frame_index):
        return self._rolls[frame_index + 2]

    def _strike_bonus(self, frame_index):
        return self._rolls[frame_index + 1] + self._rolls[frame_index + 2]
