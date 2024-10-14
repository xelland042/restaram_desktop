import flet as ft

from constants import PLUS, WHITE, BARLOW_MEDIUM, INCREMENT_BG_COLOR, MINUS, JOSEFIN_SANS_BOLD, BASKET_BG_COLOR, ORANGE, \
    BUTTON_NUMBER_BG_COLOR


class IncrementButton(ft.TextButton):
    def __init__(self, button_number, price, **kwargs):
        super().__init__(
            content=ft.Text(
                value=PLUS,
                size=18,
                color=WHITE,
                weight=ft.FontWeight.W_500,
                expand=True,
                text_align=ft.TextAlign.CENTER
            ),
            width=36,
            height=42,
            style=ft.ButtonStyle(
                bgcolor=INCREMENT_BG_COLOR,
                shape=ft.RoundedRectangleBorder(radius=4),
                side=ft.BorderSide(0.5, WHITE)
            ),
            on_click=lambda e: [self.increment(e), self.increment_price(e)],
            **kwargs
        )
        self.button_number = button_number
        self.price = price
        self.price_meal = int(self.price.content.value)

    def increment(self, e):
        new_value = str(int(self.button_number.content.value) + 1)
        self.button_number.update_value(new_value)
        self.page.update()

    def increment_price(self, e):
        self.price.content.value = str(int(self.price.content.value) + self.price_meal)
        self.page.update()


class DecrementButton(ft.TextButton):
    def __init__(self, button_number, price, **kwargs):
        super().__init__(
            content=ft.Text(
                value=MINUS,
                size=18,
                color=WHITE,
                weight=ft.FontWeight.W_700,
                expand=True,
                text_align=ft.TextAlign.CENTER
            ),
            width=36,
            height=42,
            style=ft.ButtonStyle(
                bgcolor=INCREMENT_BG_COLOR,
                shape=ft.RoundedRectangleBorder(radius=4),
                side=ft.BorderSide(0.5, WHITE)
            ),
            on_click=lambda e: [self.decrement(e), self.decrement_price(e)],
            **kwargs
        )
        self.button_number = button_number
        self.price = price
        self.price_meal = int(self.price.content.value)

    def decrement(self, e):
        if int(self.button_number.content.value) > 0:
            new_value = str(int(self.button_number.content.value) - 1)
            self.button_number.update_value(new_value)
        self.page.update()

    def decrement_price(self, e):
        if int(self.price.content.value) > 0:
            self.price.content.value = str(int(self.price.content.value) - self.price_meal)
        self.page.update()


class Basket(ft.IconButton):
    def __init__(self, **kwargs):
        super().__init__(
            content=ft.Icon(
                name=ft.icons.SHOPPING_CART_OUTLINED,
                color=WHITE,
                disabled=True,
                expand=True,
                size=17,
            ),
            width=36,
            height=42,
            style=ft.ButtonStyle(
                bgcolor=BASKET_BG_COLOR,
                shape=ft.RoundedRectangleBorder(radius=8),
                side=ft.BorderSide(0.5, ORANGE)
            )
        )


class ButtonNumber(ft.Container):
    def __init__(self, value, **kwargs):
        super().__init__(
            content=ft.Text(
                value=value,
                color=WHITE,
                weight=ft.FontWeight.W_500,
                size=17,
                text_align=ft.TextAlign.CENTER,
            ),
            width=36,
            height=42,
            bgcolor=BUTTON_NUMBER_BG_COLOR,
            border_radius=ft.border_radius.all(8),
            border=ft.border.all(0.5, WHITE),
            alignment=ft.alignment.center,
            **kwargs
        )

    def update_value(self, new_value):
        self.content.value = new_value
        self.update()


class Price(ft.Container):
    def __init__(self, value, **kwargs):
        super().__init__(
            content=ft.Text(
                value=value,
                color=WHITE,
                weight=ft.FontWeight.W_500,
                size=17,
                expand=True,
                text_align=ft.TextAlign.CENTER
            ),
            width=70,
            height=41,
            bgcolor=BASKET_BG_COLOR,
            border_radius=ft.border_radius.all(8),
            border=ft.border.all(0.5, ORANGE),
            alignment=ft.alignment.center,
            **kwargs)
