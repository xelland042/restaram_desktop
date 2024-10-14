from flet import *

from components.buttons.food_composition import Price, ButtonNumber, DecrementButton, IncrementButton, Basket
from constants import MEALCOMPOSITION, MEAL_COMPOSITION_COLOR, BARLOW_SEMI_BOLD, MEAL_NAME_COLOR, BARLOW_MEDIUM, PORTS, \
    JOSEFIN_SANS_BOLD, PORTS07, BLUE_BG_COLOR, ORANGE, WHITE, PORTS01

from config.translations import translate as _


class Right(Column):
    def __init__(self, food_name):
        def toggle_buttons(selected_button):
            for button in port_buttons:
                button.bgcolor = BLUE_BG_COLOR if button != selected_button else ORANGE
                button.update()

        port_buttons = []

        port_buttons.append(
            Container(
                content=Text(
                    value=PORTS07,
                    size=17,
                    weight=FontWeight.W_500,
                    color=WHITE,
                    expand=True,
                    text_align=TextAlign.CENTER
                ),
                width=36,
                height=36,
                bgcolor=ORANGE,
                border_radius=border_radius.all(4),
                border=border.all(0.5, WHITE),
                alignment=alignment.center,
                on_click=lambda e: toggle_buttons(port_buttons[0])
            )
        )

        port_buttons.append(
            Container(
                content=Text(
                    value=PORTS01,
                    size=17,
                    weight=FontWeight.W_500,
                    color=WHITE,
                    expand=True,
                    text_align=TextAlign.CENTER
                ),
                width=36,
                height=36,
                bgcolor=BLUE_BG_COLOR,
                border_radius=border_radius.all(4),
                border=border.all(0.5, WHITE),
                alignment=alignment.center,
                on_click=lambda e: toggle_buttons(port_buttons[1])
            )
        )

        def product_row():
            res = []
            for i in range(10):
                row = Row(
                    controls=[
                        Text(value="Go'sht", color="white", size=16),
                        Text(value="300gr", color="white", size=12),
                    ],
                    alignment=MainAxisAlignment.SPACE_BETWEEN
                )
                res.append(row)
            return res

        price = Price(value="40000")
        button_number = ButtonNumber(value="1")
        decrement_button = DecrementButton(button_number, price)
        increment_button = IncrementButton(button_number, price)
        basket_button = Basket()
        super().__init__(
            controls=[
                Row(
                    controls=[
                        Column(
                            controls=[
                                Text(
                                    value=_(MEALCOMPOSITION),
                                    size=20,
                                    color=MEAL_COMPOSITION_COLOR,
                                    weight=FontWeight.W_600,
                                ),
                                Text(
                                    value=food_name,
                                    size=18,
                                    color=MEAL_NAME_COLOR,
                                    weight=FontWeight.W_500,
                                ),
                                Container(
                                    height=10
                                ),
                            ],
                            spacing=5,
                            horizontal_alignment=CrossAxisAlignment.CENTER
                        ),
                    ],
                    alignment=MainAxisAlignment.CENTER
                ),
                Row(
                    controls=[
                        Text(
                            value=PORTS,
                            size=20,
                            color=MEAL_NAME_COLOR,
                            weight=FontWeight.W_700,
                        ),
                        *port_buttons
                    ],
                    alignment=MainAxisAlignment.CENTER,
                    spacing=12.5
                ),
                Container(
                    width=10,
                    height=10
                ),
                Container(
                    content=Column(
                        controls=product_row(),
                        scroll=ScrollMode.ALWAYS,
                        alignment=MainAxisAlignment.CENTER
                    ),
                    width=400,
                    height=250,
                    margin=margin.only(left=15)
                ),
                Container(
                    content=Row(
                        controls=[
                            price,
                            Container(width=11),
                            decrement_button,
                            button_number,
                            increment_button,
                            Container(width=11),
                            basket_button
                        ],
                        expand=True,
                        alignment=MainAxisAlignment.CENTER,
                        vertical_alignment=CrossAxisAlignment.END,
                        spacing=10
                    ),
                    margin=margin.only(top=30)
                ),
            ],
            expand=True
        )
