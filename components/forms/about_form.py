from flet import *

from components.labels.login_labels import AboutLabel
from constants import WHITE, BACK_OPACITY_DARK, JOSEFIN_SANS_BOLD, \
    BARLOW_SEMI_BOLD, ABOUT_PHONE_ICON, ABOUT_TELEGRAM_ICON, SETTINGS_INFO, INFO, LOC_INFO
from config.translations import translate as _


class AboutForm(Container):
    def __init__(self):
        super().__init__(
            width=737,
            padding=padding.Padding(120, 40, 120, 40),
            border_radius=10,
            border=border.all(1, colors.with_opacity(0.45, WHITE)),
            bgcolor=colors.with_opacity(0.25, BACK_OPACITY_DARK),
            blur=Blur(12, 12, BlurTileMode.MIRROR),
            adaptive=True,

        )

        self.phone = AboutLabel(icon_src=ABOUT_PHONE_ICON, text='+998 00 000 00 00')
        self.phone2 = AboutLabel(icon_src=ABOUT_PHONE_ICON, text='+998 00 000 00 00')
        self.tg = AboutLabel(icon_src=ABOUT_TELEGRAM_ICON, text='https://t.me/@tolibov_asilbek')

        self.content = Column(
            alignment=MainAxisAlignment.START,
            horizontal_alignment=CrossAxisAlignment.START,
            controls=[
                Text(_(SETTINGS_INFO), size=24, color=WHITE, font_family=JOSEFIN_SANS_BOLD),
                Text(_(INFO), size=16, color=WHITE,
                     font_family=BARLOW_SEMI_BOLD),
                Column(
                    controls=[
                        self.phone,
                        self.phone2,
                    ]
                ),
                Text(_(LOC_INFO),
                     size=16, color=WHITE,
                     font_family=BARLOW_SEMI_BOLD),
                Column(
                    controls=[
                        self.tg,
                    ]
                ),
            ]

        )
