from flet import *

from components.buttons.login_button import LoginNavigationButton
from constants import LOGO, CONTACT, ABOUT, LOGIN
from page_urls import ABOUT_URL, CONTACT_URL, LOGIN_URL


class TablesContainer(Row):
    def __init__(self):
        super().__init__(
            wrap=True,
            scroll=ScrollMode.AUTO,
            spacing=15,
            height=330,
            run_spacing=30,
            expand=True
        )
