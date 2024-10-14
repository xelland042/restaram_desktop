from flet import *

from config.ui_manager import get_color
from constants import BARLOW_MEDIUM, WHITE, GRAY, ORANGE, BUTTON_NUMBER_BG_COLOR, MOUNTAIN_FIG, SERVICE, ALL
from config.translations import translate as _


class OrderHistoryPortion(Container):
    def __init__(self, ports_type: str):
        super().__init__(
            width=30,
            height=30,
            border_radius=4,
            border=border.all(2, WHITE),
            bgcolor=ORANGE,
            alignment=alignment.center,
            content=Text(value=ports_type, color=WHITE, size=10, font_family=BARLOW_MEDIUM)
        )


class OrderHistoryCard(Row):

    @staticmethod
    def truncate_text(text: str, max_length: int) -> str:
        if len(text) > max_length:
            return text[:max_length] + '...'
        return text

    def __init__(self, food_name: str, image_path: str, portion: str, price='0', amount=0,
                 description='Test Description'):
        super().__init__(
            spacing=0,
            controls=[
                ###
                Container(
                    alignment=alignment.center,
                    content=Image(
                        src=image_path,  # image path
                        border_radius=border_radius.all(50),
                        width=70,
                        height=70,
                        fit=ImageFit.CONTAIN
                    )
                ),
                ###
                Container(width=30),
                ###
                Column(
                    spacing=2,
                    width=80.5,
                    controls=[
                        ###
                        Text(
                            value=food_name,
                            size=18,
                            font_family=BARLOW_MEDIUM,
                            color=get_color("food_card_text_2"),
                        ),
                        ###
                        Text(
                            value=f'{price} so`m',
                            size=8,
                            font_family=BARLOW_MEDIUM,
                            color=GRAY,
                        )
                        ###
                    ]
                ),
                ###
                Container(width=15),
                ###
                Text(value=str(amount),
                     width=5,
                     size=12.5,
                     font_family=BARLOW_MEDIUM,
                     color=get_color("food_card_text_2"),
                     ),
                ###
                Container(width=46.5),
                ###
                OrderHistoryPortion(portion),
                ###
                Container(width=31),
                ###
                Text(
                    value=price,
                    width=45,
                    size=12,
                    font_family=BARLOW_MEDIUM,
                    color=get_color("food_card_text_2")
                ),
                ###
                Container(width=20),
                ###
                Container(
                    width=250,
                    height=30,
                    bgcolor=get_color("choosen_food_button_bgcolor_2"),
                    border_radius=4,
                    alignment=alignment.center,
                    border=border.all(width=2, color=get_color("choosen_food_border")),
                    content=Text(
                        value=self.truncate_text(description, 115),
                        size=8,
                        font_family=BARLOW_MEDIUM,
                        color=get_color("food_card_text")
                    )
                )
                ###
            ]
        )


class OrderHistoryItemList(Row):
    def __init__(self, item_list: list[dict], service: int, total: str):
        super().__init__(
            spacing=0,
            height=300,
            vertical_alignment=CrossAxisAlignment.END,
            controls=[
                ###
                Container(width=10),
                ###
                Container(
                    width=660,
                    height=300,
                    content=Column(
                        spacing=7,
                        on_scroll_interval=0,
                        scroll=ScrollMode.ADAPTIVE,
                        controls=[OrderHistoryCard(**item) for item in item_list]
                    )
                ),
            ]
        )
