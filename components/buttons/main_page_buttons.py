from flet import *

from config.ui_manager import get_color
from constants import BARLOW_SEMI_BOLD, WHITE, ORANGE, BLUE_BG_COLOR, BLACK_HOWL, MENU, ACCOUNT

from config.translations import translate as _


class MainPageButton(Container):

    @staticmethod
    def on_click_for_main_page_button(event: ControlEvent):
        all_buttons = event.control.parent.parent.parent.parent.controls
        main_page_data = event.control.parent.parent.parent.parent.parent.parent.parent.parent.parent.data
        main_page = event.control.parent.parent.parent.parent.parent.parent.parent.parent.parent
        page_containers = event.control.parent.parent.parent.parent.parent.parent.parent.parent.controls
        button = event.control
        container_ = event.control.parent.parent.controls[0].content
        for i in all_buttons:
            button_ = i.content.controls[1].content
            if button_.data['pressed']:
                button_.data['pressed'] = False
                button_.width = 97.5
                button_.bgcolor = colors.TRANSPARENT
                button_.content.controls = [button_.data['main_icon'], button_.data['text']]
                i.content.controls[0].content.offset.y = 1
            i.content.controls[0].update()
            i.content.controls[1].update()
        if button.data['pressed']:
            pass
        elif not button.data['pressed']:
            for main_page_container in main_page_data:
                if main_page_container['index'] == button.data['index']:
                    page_containers[-1] = main_page_container['container']
            button.data['pressed'] = True
            button.width = 45
            button.bgcolor = get_color("icon_button_color")
            button.content.controls = [button.data['second_icon']]
            container_.offset.y = 0
            main_page.update()
            button.update()
            container_.update()

    @staticmethod
    def create_background_container(index):
        if index == 0:
            offset_ = transform.Offset(0, 0)
        else:
            offset_ = transform.Offset(0, 1)
        return Container(
            data='container',
            width=97.5,
            alignment=alignment.center,
            content=Container(
                height=67.5,
                width=82,
                offset=offset_,
                animate_offset=animation.Animation(300, AnimationCurve.EASE),
                animate=animation.Animation(300, AnimationCurve.EASE),
                bgcolor=get_color("main_page_buttons_cont"),
                border=Border(
                    top=BorderSide(color=get_color("main_page_buttons_cont_bgcolor"), width=0),
                    left=BorderSide(color=get_color("main_page_buttons_cont_bgcolor"), width=0),
                    right=BorderSide(color=get_color("main_page_buttons_cont_bgcolor"), width=0),
                ),
                data=index,
                content=Row([
                    Container(
                        width=11,
                        bgcolor=get_color("main_page_buttons_cont_bgcolor"),
                        border_radius=BorderRadius(
                            top_left=0, top_right=0, bottom_left=0, bottom_right=10
                        ),
                    ),
                    Container(
                        width=60,
                        bgcolor=get_color("main_page_buttons_cont_bgcolor"),
                        content=Container(
                            bgcolor=get_color("main_page_buttons_cont"),
                            border=Border(
                                top=BorderSide(color=get_color("main_page_buttons_cont"), width=0),
                                left=BorderSide(color=get_color("main_page_buttons_cont"), width=0),
                                right=BorderSide(color=get_color("main_page_buttons_cont"), width=0),
                                bottom=BorderSide(color=get_color("main_page_buttons_cont"), width=0),
                            ),
                            border_radius=BorderRadius(
                                top_left=10, top_right=10, bottom_left=0, bottom_right=0
                            ),
                        )
                    ),
                    Container(
                        width=11,
                        bgcolor=get_color("main_page_buttons_cont_bgcolor"),
                        border_radius=BorderRadius(
                            top_left=0, top_right=0, bottom_left=10, bottom_right=0
                        ),
                    )
                ], spacing=0, alignment=alignment.center)
            )
        )

    def create_main_page_button(self, index: int, main_icon_src: str, second_icon_src: str, button_text: str):
        main_icon = Image(src=main_icon_src, width=20, height=20, color=get_color("main_icon_button_color"))
        second_icon = Image(src=second_icon_src, width=20, height=20, color=get_color("second_icon_button_color"))

        button_txt = Text(value=button_text, size=16, font_family=BARLOW_SEMI_BOLD, color=WHITE)

        return Container(
            width=97.5,
            height=62,
            alignment=alignment.center,
            content=Container(
                width=45 if index == 0 else 97.5,
                height=45,
                border_radius=8,
                border=border.all(2, get_color("icon_button_color")),
                bgcolor=get_color("icon_button_color") if index == 0 else colors.TRANSPARENT,
                on_click=self.on_click_for_main_page_button,
                animate=animation.Animation(300, AnimationCurve.EASE),
                data={
                    'index': index,
                    'main_icon': main_icon,
                    'second_icon': second_icon,
                    'text': button_txt,
                    'pressed': True if index == 0 else False,
                },
                content=Row(
                    spacing=12.5,
                    controls=[second_icon] if index == 0 else [main_icon, button_txt],
                    alignment=MainAxisAlignment.CENTER,
                )
            )
        )

    def __init__(self, index, main_icon_src, second_icon_src, button_text):
        super().__init__(
            alignment=alignment.center,
            width=97.5,
            height=67.5,
            content=Stack(controls=[
                self.create_background_container(index),
                self.create_main_page_button(index, main_icon_src, second_icon_src, button_text)
            ],
                alignment=alignment.center,
            )
        )


class MainPageButtons(Container):

    @staticmethod
    def create_buttons_using_buttons_data():
        buttons_data = [
            {'index': 0,
             'main_icon': 'home_icon.svg',
             'second_icon': 'home_icon_white.svg',
             'button_text': _(MENU)
             },
            {'index': 1,
             'main_icon': 'orange_pie_ch.svg',
             'second_icon': 'white_pie_ch.svg',
             'button_text': _(ACCOUNT)
             },
        ]

        buttons_ = []

        for button in buttons_data:
            buttons_.append(MainPageButton(
                index=button['index'],
                main_icon_src=button['main_icon'],
                second_icon_src=button['second_icon'],
                button_text=button['button_text'],
            )
            )
        return buttons_

    def __init__(self):
        super().__init__(
            alignment=alignment.bottom_center,
            padding=0,
            content=Row(controls=self.create_buttons_using_buttons_data(),
                        spacing=15.5)
        )
