from flet import *

from constants import WHITE, BACK_OPACITY_DARK, MAIL_ICON, PASSWORD_ICON, BARLOW_SEMI_BOLD, EMAIL, PASSWORD, LOGIN
from components.buttons.login_button import LoginButton
from components.inputs.login_input import LoginInput
from config.translations import translate as _


class LoginForm(Container):
    def __init__(self):
        super().__init__(
            width=305,
            height=285,
            padding=padding.Padding(32, 40, 32, 40),
            border_radius=10,
            border=border.all(1, colors.with_opacity(0.45, WHITE)),
            bgcolor=colors.with_opacity(0.25, BACK_OPACITY_DARK),
            blur=Blur(12, 12, BlurTileMode.MIRROR),

        )

        self.email = LoginInput(password=False, label=_(EMAIL), icon_src=MAIL_ICON,
                                can_reveal_password=False).build()
        self.password = LoginInput(password=True, label=_(PASSWORD), icon_src=PASSWORD_ICON,
                                   can_reveal_password=True).build()

        self.content = Column(
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                Text(_(LOGIN), size=24, color=WHITE, font_family=BARLOW_SEMI_BOLD),
                self.email,
                self.password,
                Divider(color=colors.TRANSPARENT),
                LoginButton(text=_(LOGIN)),
            ]

        )
