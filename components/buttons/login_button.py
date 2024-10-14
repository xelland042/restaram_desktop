from flet import *

from constants import ORANGE, WHITE, BARLOW_SEMI_BOLD
from page_urls import TABLES_URL


class LoginButton(TextButton):
    def __init__(self, text):
        super().__init__(
            content=Text(text, size=16, font_family=BARLOW_SEMI_BOLD),
            height=29.5,
            width=239,
            style=ButtonStyle(
                padding=0,
                shape=RoundedRectangleBorder(radius=3),
                color=WHITE,
                bgcolor=ORANGE,
            ),
            animate_size=30,
            on_click=lambda _: self.page.go(TABLES_URL)
        )


class LoginNavigationButton(TextButton):
    def __init__(self, text, route):
        super().__init__(
            content=Text(text, size=16, font_family=BARLOW_SEMI_BOLD),
            height=26,

            style=ButtonStyle(
                padding=2,
                shape=RoundedRectangleBorder(radius=4),
                color=WHITE,
                bgcolor=colors.TRANSPARENT,
                side=BorderSide(color=WHITE, width=1)
            ),
            on_click=lambda _: self.page.go(route)
        )
