from flet import *

from components.cards.order_history_card import OrderHistoryItemList
from config.ui_manager import get_color
from constants import FOOD_HISTORY, BARLOW_SEMI_BOLD, FOOD, COUNT, PORTS, PRICE, \
    DETAIL

from config.translations import translate as _


class OrderHistoryContainer(Container):
    def __init__(self, food_history_list: OrderHistoryItemList):
        super().__init__(
            data=1,
            width=699,
            height=445,
            bgcolor=get_color("main_page_buttons_cont"),
            alignment=alignment.center,
            content=Container(
                width=680,
                height=405,
                border_radius=7,
                alignment=alignment.top_center,
                bgcolor=get_color("change_language_bgcolor"),
                # bgcolor='white',
                content=Column(
                    spacing=0,
                    width=660,
                    alignment=MainAxisAlignment.START,
                    controls=[
                        ###
                        Row(
                            spacing=0,
                            controls=[
                                Container(width=10),
                                ###
                                Text(
                                    value=_(FOOD_HISTORY),
                                    size=20,
                                    font_family=BARLOW_SEMI_BOLD,
                                    color=get_color("food_card_text_2"))
                            ]
                        ),
                        ###
                        Container(height=5),
                        ###
                        Row(
                            spacing=0,
                            width=660,
                            controls=[
                                ###
                                Container(width=20),
                                ###
                                Text(_(FOOD), color=get_color("food_card_text"), size=12, font_family=BARLOW_SEMI_BOLD,
                                     width=40, text_align=TextAlign.CENTER),
                                ###
                                Container(width=110),
                                ###
                                Text(_(COUNT), color=get_color("food_card_text"), size=12, font_family=BARLOW_SEMI_BOLD,
                                     width=70, text_align=TextAlign.CENTER),
                                ###
                                Container(width=15),
                                ###
                                Text(_(PORTS), color=get_color("food_card_text"), size=12, font_family=BARLOW_SEMI_BOLD,
                                     width=40, text_align=TextAlign.CENTER),
                                ###
                                Container(width=25),
                                ###
                                Text(_(PRICE), color=get_color("food_card_text"), size=12, font_family=BARLOW_SEMI_BOLD,
                                     width=37, text_align=TextAlign.CENTER),
                                ###
                                Container(width=110),
                                ###
                                Text(_(DETAIL), color=get_color("food_card_text"), size=12,
                                     font_family=BARLOW_SEMI_BOLD, width=90, text_align=TextAlign.CENTER),
                                ###
                                Container(width=90),
                                ###
                            ]
                        ),
                        ###
                        Container(height=7),
                        ###
                        Container(width=660, height=3, border_radius=3, bgcolor=get_color("payment_divider"),
                                  alignment=alignment.center),
                        ###
                        Container(height=7),
                        ###
                        food_history_list,
                        ###
                    ]
                )
            )
        )
