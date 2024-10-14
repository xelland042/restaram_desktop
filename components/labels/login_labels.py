from flet import *

from constants import BARLOW_SEMI_BOLD


class RegisterLabel(Container):
    def __init__(self, icon_src, text):
        super(RegisterLabel, self).__init__(
            padding=Padding(0, 10, 0, 10),
            alignment=Alignment(0, 0),
            content=Row(
                alignment=MainAxisAlignment.START,
                vertical_alignment=CrossAxisAlignment.CENTER,
                spacing=25,
                controls=[
                    Image(src=icon_src, width=12, height=12),
                    Text(
                        value=text,
                        font_family=BARLOW_SEMI_BOLD,
                        size=16,
                    )
                ]
            )
        )


class AboutLabel(Container):
    def __init__(self, icon_src, text):
        super(AboutLabel, self).__init__(
            padding=Padding(left=40, right=40, top=6, bottom=6),
            alignment=Alignment(0, 0),

            content=Row(
                alignment=MainAxisAlignment.START,
                vertical_alignment=CrossAxisAlignment.CENTER,
                spacing=15,
                controls=[
                    Image(src=icon_src, width=20, height=20),
                    Text(
                        value=text,
                        font_family=BARLOW_SEMI_BOLD,
                        size=16,
                    )
                ]
            )
        )
