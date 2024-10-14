from flet import *

from components.buttons.food_composition import ButtonNumber, Price, IncrementButton, DecrementButton, Basket
from components.container.components_right import Right
from components.container.image_galery import ImageGallery
from constants import BLUE_BG_DARK
from page_urls import FOOD_COMPOSITION


class FoodComposition(View):
    def __init__(self, page: Page):
        super().__init__(
            padding=0,
            route=FOOD_COMPOSITION,
        )

        self.page = page
        self.body = Container(
            expand=True,
            bgcolor=BLUE_BG_DARK,
            content=Row(
                controls=[
                    Container(
                        margin=20,
                        width=420,
                        content=ImageGallery()
                    ),
                    VerticalDivider(color="#fafafa"),
                    Container(
                        width=480,
                        margin=margin.only(left=0, bottom=10, top=20),
                        content=Right(food_name="shashlik"),

                    )
                ],
                vertical_alignment=CrossAxisAlignment.START
            )

        )

        self.controls = [self.body]
