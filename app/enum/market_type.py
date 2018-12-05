from enum import Enum


class MarketType(Enum):
    top = 1
    one_top = 11
    normal_top = 12
    had_top = 13

    down = 2
    one_down = 11
    normal_down = 12
    had_down = 13

    normal = 0
