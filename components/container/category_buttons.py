from flet import *

from components.buttons.main_page_button import FoodCategoryButton
from components.cards.card import Cards
from config.ui_manager import get_color
from constants import BLUE_BG_COLOR, MOUNTAIN_FIG

category_buttons_name = [
    'Salatlar',
    'Birinchi taom',
    'Ikkinchi taom',
    'Dessert',
    'Ichimliklar',
    'Ichimliklar 2',
    'Ichimliklar 3',
    'Ikkinchi taom 2',
]


class FoodCategoryButtons(Container):

    def __init__(self, cards: Cards):
        super().__init__(
            data=0,
            width=699,
            height=445,
            bgcolor=get_color("main_page_bgcolor"),
            content=Container(
                padding=10,
                content=Row(
                    spacing=0,
                    controls=[
                        Container(
                            padding=padding.only(top=25, left=0, right=0, bottom=0),
                            width=110,
                            content=Row(
                                spacing=0,
                                controls=[
                                    Stack(
                                        expand=True,
                                        controls=[
                                            Container(bgcolor=get_color("tab_divider"), width=1, expand=True,
                                                      offset=transform.Offset(88.5, -0.04)),
                                            Column(
                                                scroll=ScrollMode.HIDDEN,
                                                spacing=27,
                                                expand=True,
                                                controls=[
                                                    FoodCategoryButton(category_buttons_name[i], i) for i
                                                    in range(len(category_buttons_name))
                                                ])
                                        ]),
                                    Stack(
                                        alignment=alignment.center,
                                        controls=[
                                            Container(width=19.5)
                                        ]
                                    )
                                ])
                        ),
                        # Cards goes here
                        cards
                    ])
            )
        )
