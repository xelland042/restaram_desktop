from flet import *

from components.background.login_background import LoginBackground
from components.container.login_navigation import NavigationContainer
from components.forms.registration_form import RegistrationForm

from constants import CONTACT_BACKGROUND
from page_urls import CONTACT_URL


class ContactPage(View):
    def __init__(self, page: Page):
        super(ContactPage, self).__init__(
            route=CONTACT_URL,
            padding=0,
            vertical_alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )

        self.page = page

        self.body = Stack(
            expand=True,

            controls=[
                LoginBackground(CONTACT_BACKGROUND),
                NavigationContainer(),
                Column(
                    alignment=MainAxisAlignment.CENTER,
                    spacing=0,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                        Row(
                            alignment=MainAxisAlignment.CENTER,
                            vertical_alignment=CrossAxisAlignment.CENTER,
                            controls=[RegistrationForm()]
                        )
                    ]
                )
            ]
        )
        self.controls = [self.body]
