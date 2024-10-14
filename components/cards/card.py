from flet import *

from components.buttons.food_card_buttons import CardButtons
from config.ui_manager import get_color
from constants import BLACK_HOWL, ORANGE, ARIAL_BOLD, WHITE, CARD_FOOD_INFO, BARLOW_EXTRA_LIGHT, JOSEFIN_SANS_BOLD, \
    NO_FOOD, BLACK, BLUE_BG_COLOR
from page_urls import FOOD_COMPOSITION
from config.translations import translate as _


class CardObject(Container):
    def __init__(self, buttons_text: list[dict]):
        super().__init__(
            bgcolor=get_color("food_card_bgcolor"),
            border=border.all(0.5, ORANGE),
            border_radius=8,
            alignment=alignment.bottom_center,
            width=180,
            height=182.5,
            bottom=0,
            content=Column([CardButtons(buttons_text)],
                           horizontal_alignment=CrossAxisAlignment.STRETCH,
                           alignment=MainAxisAlignment.END
                           )
        )


class DisabledCardObject(Stack):
    def __init__(self):
        super().__init__(
            controls=[
                Container(
                    bgcolor=BLACK,
                    opacity=0.65,
                    border_radius=8,
                    width=180,
                    height=208,
                    expand=True
                ),
                Column(
                    [
                        Container(height=65),
                        Text(
                            value=_(NO_FOOD),
                            size=24,
                            color=WHITE,
                            font_family=JOSEFIN_SANS_BOLD,
                            text_align=TextAlign.CENTER
                        ),
                    ], horizontal_alignment=CrossAxisAlignment.CENTER, spacing=0
                )
            ]
        )


class CardsImageWithText(Column):
    @staticmethod
    def truncate_text(text: str, max_length: int) -> str:
        if len(text) > max_length:
            return text[:max_length] + '...'
        return text

    def __init__(self, card_image: str, food_name: str):
        super().__init__(
            alignment=MainAxisAlignment.START,
            spacing=5,
            controls=[
                ###
                Container(
                    Image(src=card_image, border_radius=border_radius.all(50),
                          width=120,
                          height=120,
                          fit=ImageFit.CONTAIN),
                    alignment=alignment.center
                ),
                Container(
                    padding=0,
                    content=Column(
                        controls=[
                            Text(
                                value=self.truncate_text(food_name, 40),
                                text_align=TextAlign.CENTER,
                                size=15,
                                color=get_color("food_card_text"),
                                font_family=ARIAL_BOLD
                            )
                        ],
                        alignment=alignment.top_center,
                    ),
                        alignment=alignment.top_center
                )
            ]
        )


class FoodCompositionClick(Container):
    def __init__(self):
        super().__init__(
            width=180,
            height=171,
            on_click=lambda _: self.page.go(FOOD_COMPOSITION),
        )


class Card(Container):
    @staticmethod
    def truncate_text(text: str, max_length: int) -> str:
        if len(text) > max_length:
            return text[:max_length] + '...'
        return text

    @staticmethod
    def card_contents(buttons_text: list[dict], card_image: str, food_name: str, disabled_card=False):
        if disabled_card is False:
            return [
                CardObject(buttons_text),
                CardsImageWithText(card_image, food_name),
                FoodCompositionClick(),
            ]
        else:
            return [
                CardObject(buttons_text),
                CardsImageWithText(card_image, food_name),
            ] + DisabledCardObject().controls

    def __init__(self, buttons_text: list[dict], card_image: str, food_name: str, disabled_card=False):
        super().__init__(
            width=180,
            height=208,
            content=Stack(controls=self.card_contents(buttons_text, card_image, food_name, disabled_card),
                          alignment=alignment.top_center)
        )


class Cards(Container):

    @staticmethod
    def create_buttons(buttons_data: list[list[list[dict, ...], str, str], ...]):
        result = []
        for button in buttons_data:
            button_ = button[0]
            image_ = button[1]
            food_name = button[2]
            if len(button) == 4:
                disabled = button[3]
            else:
                disabled = False
            result.append(Card(button_, image_, food_name, disabled))
        return result

    def __init__(self, buttons_: list):
        super().__init__(
            padding=0,
            offset=transform.Offset(-0.015, 0),
            width=580,
            height=445,
            bgcolor=get_color("main_page_bgcolor"),
            alignment=alignment.center,
            content=Row(
                scroll=ScrollMode.HIDDEN,
                auto_scroll=False,
                spacing=15,
                run_spacing=5,
                wrap=True,
                controls=self.create_buttons(buttons_)
            )
        )
