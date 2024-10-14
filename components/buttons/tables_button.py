from flet import *

from config.ui_manager import get_color
from constants import ORANGE, JOSEFIN_SANS_BOLD, WHITE, TABLE
from config.translations import translate as _

from page_urls import MAIN_PAGE_URL


class TablesButton(TextButton):
    def __init__(self, value):
        super().__init__(
            content=Text(
                value=value,
                font_family=JOSEFIN_SANS_BOLD,
                size=30
            ),
            height=60,
            width=155,

            style=ButtonStyle(
                padding=0,
                shape=RoundedRectangleBorder(radius=3),
                color=get_color("tables_button_text"),
                bgcolor=get_color("tables_button_bgcolor"),
                side=BorderSide(width=1, color=ORANGE),

            ),
            on_click=lambda _: self.page.go(MAIN_PAGE_URL)
        )
