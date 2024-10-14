from flet import *

from components.labels.login_labels import RegisterLabel
from constants import WHITE, BACK_OPACITY_DARK, PHONE_ICON, MAIL_ICON, TELEGRAM_ICON, BARLOW_SEMI_BOLD, BARLOW_MEDIUM, \
    REGISTRATION, PARTNERSHIP
from config.translations import translate as _


class RegistrationForm(Container):
    def __init__(self):
        super().__init__(
            width=320,
            padding=padding.Padding(47.5, 40, 47.5, 45),
            border_radius=10,
            border=border.all(1, colors.with_opacity(0.45, WHITE)),
            bgcolor=colors.with_opacity(0.25, BACK_OPACITY_DARK),
            blur=Blur(12, 12, BlurTileMode.MIRROR),
            adaptive=True

        )

        self.phone = RegisterLabel(icon_src=PHONE_ICON, text='+998 00 000 00 00')
        self.telegram = RegisterLabel(icon_src=TELEGRAM_ICON, text='@telegramuser')
        self.email = RegisterLabel(icon_src=MAIL_ICON, text='aaaaaaaaaa@gmail.com')

        self.content = Column(
            alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER,
            controls=[
                Text(_(REGISTRATION), size=24, color=WHITE, font_family=BARLOW_SEMI_BOLD),
                Text(_(PARTNERSHIP), size=12, color=WHITE, font_family=BARLOW_MEDIUM),
                Column(
                    alignment=MainAxisAlignment.START,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    controls=[
                        self.phone,
                        self.telegram,
                        self.email,
                    ]
                )

            ]

        )
