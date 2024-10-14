from flet import *

from components.buttons.tables_button import TablesButton
from components.container.tables_container import TablesContainer
from config.ui_manager import get_color
from constants import BLUE_BG_COLOR, LOGO, TABLE
from page_urls import TABLES_URL

from config.translations import translate as _

tables = TablesContainer()

for i in range(1, 30):
    tables.controls.append(
        TablesButton(value=f"{i} - {_(TABLE)}")
    )


class TablesPage(View):
    def __init__(self, page: Page):
        super().__init__(
            padding=0,
            route=TABLES_URL,
            vertical_alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )

        self.page = page

        self.body = Container(
            expand=True,
            padding=Padding(65, 0, 65, 30),
            bgcolor=get_color("tables_bgcolor"),
            content=Column(
                controls=[
                    Row(
                        vertical_alignment=CrossAxisAlignment.START,
                        controls=[
                            Image(src=LOGO, width=200, height=125)
                        ]

                    ),
                    Container(
                        padding=Padding(80, 45, 80, 45),
                        content=tables
                    )

                ]
            )

        )
        self.controls = [self.body]
