from flet import *

from components.background.login_background import LoginBackground, AboutBackground
from components.container.login_navigation import NavigationContainer
from components.forms.about_form import AboutForm

from constants import ABOUT_BACKGROUND
from page_urls import ABOUT_URL


class AboutPage(View):
    def __init__(self, page: Page):
        super(AboutPage, self).__init__(
            route=ABOUT_URL,
            padding=0,
            vertical_alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )

        self.page = page

        self.body = Stack(
            expand=True,
            controls=[
                AboutBackground(ABOUT_BACKGROUND),
                NavigationContainer(),
                Column(
                    alignment=MainAxisAlignment.CENTER,
                    spacing=0,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                        Row(
                            alignment=MainAxisAlignment.CENTER,
                            vertical_alignment=CrossAxisAlignment.CENTER,
                            controls=[AboutForm()]
                        )
                    ]
                )
            ]
        )
        self.controls = [self.body]
