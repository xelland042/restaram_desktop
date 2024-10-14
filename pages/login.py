from flet import *

from components.background.login_background import LoginBackground
from components.container.login_navigation import NavigationContainer
from components.forms.login_form import LoginForm
from constants import LOGIN_BACKGROUND
from page_urls import LOGIN_URL


class SignInPage(View):
    def __init__(self, page: Page):
        super(SignInPage, self).__init__(
            padding=0,
            route=LOGIN_URL,
            vertical_alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )

        self.page = page

        self.body = Stack(
            expand=True,
            controls=[
                LoginBackground(LOGIN_BACKGROUND),
                NavigationContainer(),
                Column(
                    alignment=MainAxisAlignment.CENTER,
                    spacing=0,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    controls=[

                        Row(
                            alignment=MainAxisAlignment.CENTER,
                            vertical_alignment=CrossAxisAlignment.CENTER,
                            controls=[LoginForm()]
                        )
                    ]
                )
            ]
        )
        self.controls = [self.body]
