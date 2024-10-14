from flet import *

from components.on_click.main_button import on_click_category_buttons
from constants import Icon_ARROW_BACK
from page_urls import MAIN_PAGE_URL

images = [
    "assets/img.png",
    "assets/img_1.png",
    "assets/img_2.png",
]


class ImageGallery(Column):
    def __init__(self):
        self.current_index = 0
        self.image_display_widget = self.image_display()

        super().__init__(
            alignment=MainAxisAlignment.CENTER,
            controls=[
                Row(
                    controls=[
                        IconButton(
                            icon=icons.ARROW_BACK,
                            icon_size=20,
                            icon_color=Icon_ARROW_BACK,
                            on_click=lambda _: self.page.go(MAIN_PAGE_URL)

                        )
                    ],
                    # expand=True,
                    alignment=MainAxisAlignment.START,

                ),
                Container(
                    margin=margin.only(top=15, bottom=10),
                    content=Row(
                        controls=[
                            self.prev_button(),
                            self.image_display_widget,
                            self.next_button(),
                        ],
                        alignment=MainAxisAlignment.CENTER,
                    ),
                ),

                Row(
                    self.thumbnails(),
                    alignment=MainAxisAlignment.CENTER,
                    spacing=30,
                ),
            ],
        )

    def image_display(self):
        return Container(
            content=Image(
                src=images[self.current_index],
                width=300,
                height=300,
                fit=ImageFit.CONTAIN
            ),
            alignment=alignment.center,
            border_radius=border_radius.all(10),
            bgcolor="#1F1D2B",
        )

    def next_button(self):
        return IconButton(
            icon=icons.ARROW_FORWARD,
            on_click=self.next_image,
            icon_color=colors.WHITE
        )

    def prev_button(self):
        return IconButton(
            icon=icons.ARROW_BACK,
            on_click=self.prev_image,
            icon_color=colors.WHITE
        )

    def thumbnails(self):
        return [
            Container(
                content=Image(src=image, width=131, height=131, fit=ImageFit.CONTAIN),
                on_click=lambda e, index=i: self.update_image(index),
            )
            for i, image in enumerate(images)
        ]

    def update_image(self, index: int):
        self.current_index = index
        self.image_display_widget.content.src = images[self.current_index]
        self.update()

    def next_image(self, e):
        new_index = (self.current_index + 1) % len(images)
        self.update_image(new_index)

    def prev_image(self, e):
        new_index = (self.current_index - 1) % len(images)
        self.update_image(new_index)
