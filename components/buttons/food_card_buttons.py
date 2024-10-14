from flet import *

from constants import ARIAL_BOLD, BARLOW_EXTRA_LIGHT, PHILIPPINE_BROWN, ORANGE, WHITE, BARLOW_BOLD, BARLOW_MEDIUM


class CardButton(TextButton):

    @staticmethod
    def get_radius_of_button(left, right):
        if left is True and right is False:
            return BorderRadius(top_left=0, top_right=0, bottom_left=8, bottom_right=0)
        elif left is False and right is True:
            return BorderRadius(top_left=0, top_right=0, bottom_left=0, bottom_right=8)
        else:
            return BorderRadius(top_left=0, top_right=0, bottom_left=8, bottom_right=8)

    def __init__(self, button_text: str, button_description: str, disabled=False, left=False, right=False):
        super().__init__(
            disabled=disabled,
            text=button_text,
            content=Column(
                spacing=2,
                alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Text(value=button_text, size=13, font_family=BARLOW_BOLD, expand=True),
                    Text(value=button_description, size=7, font_family=BARLOW_MEDIUM, expand=True),
                ]
            ),
            expand=True,
            height=37,
            style=ButtonStyle(
                padding=2,
                bgcolor=PHILIPPINE_BROWN if disabled is True else ORANGE,
                color=WHITE,
                side=BorderSide(color=ORANGE, width=1),
                shape=RoundedRectangleBorder(
                    radius=self.get_radius_of_button(left, right)
                )
            )
        )


class CardButtons(Row):
    """
    buttons_text should look like this:
    {'button_text': 'Dummy Button Text (1, 0.7)', 'button_description': 'Some Dummy Button Description (35 000 so`m,\
 40 000 so`m)', 'disabled': False (True, False)}
    """

    @staticmethod
    def create_buttons_for_card(buttons_text: list[dict]):
        if len(buttons_text) == 1:
            button_text = buttons_text[0]
            disabled = button_text['disabled'] if button_text['disabled'] else False
            return [
                CardButton(button_text=button_text['button_text'],
                           button_description=button_text['button_description'],
                           disabled=disabled)]
        elif len(buttons_text) == 2:
            button_text_1 = buttons_text[0]
            button_text_2 = buttons_text[1]
            disabled_1 = button_text_1['disabled'] if button_text_1['disabled'] else False
            disabled_2 = button_text_2['disabled'] if button_text_2['disabled'] else False
            return [
                CardButton(button_text=button_text_1['button_text'],
                           button_description=button_text_1['button_description'],
                           disabled=disabled_1, left=True),
                CardButton(button_text=button_text_2['button_text'],
                           button_description=button_text_2['button_description'],
                           disabled=disabled_2, right=True)
            ]

    def __init__(self, buttons_text: list[dict]):
        super().__init__(
            controls=self.create_buttons_for_card(buttons_text),
            spacing=1,
            alignment=MainAxisAlignment.CENTER,
            vertical_alignment=CrossAxisAlignment.END,
            expand=True,
        )
