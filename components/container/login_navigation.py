from flet import *

from components.buttons.login_button import LoginNavigationButton
from constants import LOGO, CONTACT, ABOUT, LOGIN
from page_urls import ABOUT_URL, CONTACT_URL, LOGIN_URL
from config.translations import translate as _


class NavigationContainer(Container):
    def __init__(self):
        super().__init__(
            expand=True,
            padding=45,
            margin=7,
            alignment=Alignment(0, -1),
            content=Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=CrossAxisAlignment.START,
                controls=[
                    Image(src=LOGO, width=163.5, height=88.5),
                    Row(
                        spacing=30,
                        controls=[
                            LoginNavigationButton(_(LOGIN), LOGIN_URL),
                            LoginNavigationButton(_(CONTACT), CONTACT_URL),
                            LoginNavigationButton(_(ABOUT), ABOUT_URL),
                        ]
                    )
                ]

            )
        )
