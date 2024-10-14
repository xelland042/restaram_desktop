from flet import *

from constants import WHITE, BARLOW_MEDIUM


class LoginInput(object):
    def __init__(self, icon_src, label, password, can_reveal_password):
        self.label = TextField(
            expand=True,
            height=24,
            label=label,
            label_style=TextStyle(
                size=17,
                font_family=BARLOW_MEDIUM,
                color=WHITE,

            ),
            max_lines=1,
            border_color=colors.TRANSPARENT,
            password=password,
            text_size=17,
            can_reveal_password=can_reveal_password
        )
        self.icon = Image(src=icon_src, width=14, height=41, color=WHITE)
        self.body = Container(
            expand=True,
            padding=0,
            margin=0,
            alignment=Alignment(0, 0),
            content=Column(
                spacing=0,
                expand=True,
                controls=[
                    Row(
                        alignment=MainAxisAlignment.CENTER,
                        vertical_alignment=CrossAxisAlignment.CENTER,
                        controls=[
                            self.icon,
                            self.label,
                        ]
                    ),
                    Divider(height=0.5, color=WHITE)  # Set margin to eliminate space
                ]
            )
        )

    def build(self):
        return self.body
