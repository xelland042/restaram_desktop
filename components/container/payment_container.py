from flet import *

from components.buttons.payment_buttons import InRestaurantButton, TakeAwayButton, ContinueOrderButton
from config.ui_manager import get_color
from constants import BLUE_BG_DARK, BARLOW_SEMI_BOLD, WHITE, MOUNTAIN_FIG, GRAY, FOOD, COUNT, PRICE, SERVICE, ALL, \
    BARLOW_MEDIUM, ORANGE, ADD_COMMENT
from config.translations import translate as _


class ChosenFood(Container):

    @staticmethod
    def truncate_text(text: str, max_length: int) -> str:
        if len(text) > max_length:
            return text[:max_length] + '...'
        return text

    @staticmethod
    def on_clickk(event: ControlEvent):
        print(event.control)

    def __init__(self, food_name: str, price: str, commentary: str, count: int, food_image='assets/food.png',
                 portion='0.5'):
        super().__init__(
            height=105,
            bgcolor=get_color("choosen_food_bgcolor"),
            border_radius=9,
            border=border.all(1, get_color("choosen_food_border")),
            content=Container(
                padding=5,
                width=248,
                content=Column(
                    spacing=0,
                    controls=[
                        Row(
                            vertical_alignment=CrossAxisAlignment.START,
                            spacing=0,
                            controls=[
                                ###
                                Column(
                                    spacing=6,
                                    alignment=MainAxisAlignment.START,
                                    controls=[
                                        Image(src=food_image, width=30, height=30),
                                    ]
                                ),
                                ###
                                Container(width=36),
                                ###
                                Container(
                                    bgcolor=ORANGE,
                                    border_radius=8,
                                    border=border.all(1, WHITE),
                                    width=26,
                                    on_click=self.on_clickk,
                                    height=26,
                                    alignment=alignment.center,
                                    content=Text(portion, font_family=BARLOW_MEDIUM, size=10, color=WHITE)
                                ),
                                ###
                                Container(width=16),
                                ###
                                Container(
                                    bgcolor=get_color("choosen_food_button_bgcolor"),
                                    border_radius=8,
                                    border=border.all(1, get_color("choosen_food_button_border")),
                                    width=26,
                                    on_click=self.on_clickk,
                                    height=26,
                                    alignment=alignment.center,
                                    content=Text('-', font_family=BARLOW_MEDIUM, size=10,
                                                 color=get_color("choosen_food_button_text"))
                                ),
                                ###
                                Container(width=5),
                                ###
                                Container(
                                    bgcolor=get_color("choosen_food_button_bgcolor_2"),
                                    border_radius=8,
                                    border=border.all(1, get_color("choosen_food_button_border")),
                                    width=26,
                                    on_click=self.on_clickk,
                                    height=26,
                                    alignment=alignment.center,
                                    content=Text(str(count), font_family=BARLOW_MEDIUM, size=10,
                                                 color=get_color("choosen_food_button_text"))
                                ),
                                ###
                                Container(width=5),
                                ###
                                Container(
                                    bgcolor=get_color("choosen_food_button_bgcolor"),
                                    border_radius=8,
                                    border=border.all(1, get_color("choosen_food_button_border")),
                                    width=26,
                                    on_click=self.on_clickk,
                                    height=26,
                                    alignment=alignment.center,
                                    content=Text('+', font_family=BARLOW_MEDIUM, size=10,
                                                 color=get_color("choosen_food_button_text"))
                                ),
                                ###
                                Container(width=5),
                                ###
                                Container(height=26, width=35, alignment=alignment.center_left,
                                          content=Text(value=price, size=8, color=get_color("food_card_text_2"),
                                                       font_family=BARLOW_MEDIUM)
                                          )
                            ]
                        ),
                        ###
                        Container(height=10),
                        ###
                        Text(self.truncate_text(food_name, 52), font_family=BARLOW_MEDIUM,
                             color=get_color("food_card_text_2"), size=8),
                        ###
                        Container(height=15),
                        ###
                        Row(
                            spacing=0,
                            controls=[
                                ###
                                Container(
                                    scale=0.6,
                                    offset=transform.Offset(-0.20, -0.3),
                                    bgcolor=get_color("search_input_bgcolor"),
                                    border_radius=18,
                                    border=border.all(1, get_color("search_input_border")),
                                    width=337,
                                    alignment=alignment.center,
                                    content=Container(
                                        content=TextField(hint_text=_(ADD_COMMENT),
                                                          hint_style=TextStyle(font_family=BARLOW_MEDIUM,
                                                                               color=colors.with_opacity(0.6, get_color(
                                                                                   "search_input_text"))),
                                                          border_radius=18,
                                                          text_style=TextStyle(font_family=BARLOW_MEDIUM,
                                                                               color=get_color("search_input_text")),
                                                          cursor_color=get_color("search_input_text"),
                                                          border_color=colors.TRANSPARENT,
                                                          focused_border_color=get_color("search_input_text"),
                                                          fill_color=colors.TRANSPARENT,
                                                          hover_color=colors.TRANSPARENT)
                                    )
                                ),
                                ###
                                Container(
                                    offset=transform.Offset(-4.63, -0.53),
                                    width=28,
                                    height=28,
                                    on_click=self.on_clickk,
                                    bgcolor=get_color("red_trash_bgcolor"),
                                    border=border.all(1, get_color("red_trash_border")),
                                    border_radius=9,
                                    alignment=alignment.center,
                                    content=Image(src='red_trash.svg', width=11, height=11,
                                                  color=get_color("red_trash_color"))
                                )
                            ]
                        )
                    ]
                )
            )
        )


class Payment(Container):
    def __init__(self, service_fee: int, full_price: str):
        super().__init__(
            width=261,
            height=600,
            bgcolor=get_color("main_page_container"),
            alignment=alignment.top_right,
            content=Column(
                controls=[
                    ###
                    Container(height=25),
                    ###
                    Row(alignment=MainAxisAlignment.SPACE_BETWEEN,
                        width=235,
                        controls=[
                            ###
                            InRestaurantButton(),
                            ###
                            TakeAwayButton(),
                            ###
                        ]),
                    ###
                    Container(height=25),
                    ###
                    Row(
                        width=221,
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            Text(
                                _(FOOD),
                                size=9,
                                font_family=BARLOW_SEMI_BOLD,
                                color=WHITE
                            ),
                            Row(width=81,
                                alignment=MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    Text(_(COUNT), size=9, font_family=BARLOW_SEMI_BOLD, color=WHITE),
                                    Text(_(PRICE), size=9, font_family=BARLOW_SEMI_BOLD, color=WHITE),
                                ])
                        ]
                    ),
                    ###
                    Container(height=12),
                    ###
                    Container(height=2, width=221, bgcolor=get_color("take_away_here_bgcolor_bordr")),
                    ###
                    Container(height=12),
                    ###
                    Column(
                        alignment=MainAxisAlignment.CENTER,
                        auto_scroll=False,
                        scroll=ScrollMode.HIDDEN,
                        height=360,
                        controls=[
                            ChosenFood(food_name='Qovurma Lag`moq', price='40 000', commentary='commentary1',
                                       food_image='food.png', count=1),
                            ChosenFood(food_name='Coca Cola', price='30 000', commentary='commentary2',
                                       food_image='food.png', count=2),
                            ChosenFood(food_name='Some looong food name', price='999 000', commentary='commentary3',
                                       food_image='food.png', count=1),
                            ChosenFood(food_name='Qovurma Lag`moq', price='40 000', commentary='commentary1',
                                       food_image='food.png', count=1),
                            ChosenFood(food_name='Coca Cola', price='30 000', commentary='commentary2',
                                       food_image='food.png', count=2),
                            ChosenFood(food_name='Some looong food name Some looong food name Some looong',
                                       price='999 000', commentary='commentary3',
                                       food_image='food.png', count=1),
                        ]
                    ),
                    ###
                    Container(height=23),
                    ###
                    Column([
                        ###
                        Row([
                            Text(_(SERVICE), size=9, color=get_color("fee_price_text_color"),
                                 font_family=BARLOW_SEMI_BOLD),
                            Text(f'%{service_fee}', size=9, color=WHITE, font_family=BARLOW_SEMI_BOLD),
                        ], alignment=MainAxisAlignment.SPACE_BETWEEN),
                        ###
                        Container(height=7.5),
                        ###
                        Row([
                            Text(_(ALL), size=9, color=get_color("fee_price_text_color"), font_family=BARLOW_SEMI_BOLD),
                            Text(full_price, size=9, color=WHITE, font_family=BARLOW_SEMI_BOLD),
                        ], alignment=MainAxisAlignment.SPACE_BETWEEN),
                        ###
                    ], width=221, spacing=0),
                    ###
                    Container(height=20),
                    ###
                    ContinueOrderButton()
                ],
                spacing=0,
                horizontal_alignment=CrossAxisAlignment.CENTER
            )
        )
