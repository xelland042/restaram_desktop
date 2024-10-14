from flet import *

from constants import BLUE_BG_COLOR


class MainPageBackground(Container):
    def __init__(self):
        super().__init__(
            bgcolor=BLUE_BG_COLOR,
        )
