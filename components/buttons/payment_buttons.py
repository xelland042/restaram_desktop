from flet import *

from config.ui_manager import get_color
from constants import ORANGE, WHITE, BARLOW_SEMI_BOLD, MOUNTAIN_FIG, BLACK_HOWL, IN_HERE, TAKE_AWAY, CONTINUE_ORDER
from config.translations import translate as _


def on_click_event(event: ControlEvent):
    button = event.control
    buttons = event.control.parent.controls
    if button.data == 1:
        for button_ in buttons:
            print("button data:", button_.data)
    elif button.data == 0:
        for button_ in buttons:
            print("button data:", button_.data)
            if button_.data == 1:
                button_.data = 0
                button_.bgcolor = get_color("take_away_here_bgcolor")
                button_.border = border.all(1, get_color("take_away_here_bgcolor_bordr"))
                button_.content.controls[0].color = ORANGE
                button_.update()
                event.page.update()
        button.data = 1
        button.bgcolor = get_color("take_away_here_bgcolor_1")
        button.border = border.all(1, get_color("take_away_here_bgcolor_bordr_1"))
        button.content.controls[0].color = get_color("take_away_here_bgcolor_bordr_1_text")
    event.page.update()



class InRestaurantButton(Container):
    def __init__(self):
        super().__init__(
            on_click=on_click_event,
            data=1,
            width=109,
            height=30,
            bgcolor=get_color("take_away_here_bgcolor_1"),
            border_radius=4,
            border=border.all(1, get_color("take_away_here_bgcolor_bordr_1")),
            content=Row([
                Text(
                    _(IN_HERE),
                    size=12,
                    color=get_color("take_away_here_bgcolor_bordr_1_text"),
                    font_family=BARLOW_SEMI_BOLD
                )
            ], alignment=MainAxisAlignment.CENTER, vertical_alignment=CrossAxisAlignment.CENTER),
        )


class TakeAwayButton(Container):
    def __init__(self, ):
        super().__init__(
            on_click=on_click_event,
            data=0,
            width=109,
            height=30,
            bgcolor=get_color("take_away_here_bgcolor"),
            border_radius=4,
            border=border.all(1, get_color("take_away_here_bgcolor_bordr")),
            content=Row([
                Text(
                    _(TAKE_AWAY),
                    size=12,
                    color=ORANGE,
                    font_family=BARLOW_SEMI_BOLD
                )
            ], alignment=MainAxisAlignment.CENTER, vertical_alignment=CrossAxisAlignment.CENTER),
        )


class ContinueOrderButton(Container):
    def __init__(self):
        super().__init__(
            width=221,
            height=30,
            border_radius=7.5,
            bgcolor=get_color("icon_button_color"),
            alignment=alignment.center,
            content=Text(
                _(CONTINUE_ORDER),
                size=10,
                color=get_color("food_card_text"),
                font_family=BARLOW_SEMI_BOLD
            )
        )
