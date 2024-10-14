from flet import *

from components.container.log_out import LogOut
from config.ui_manager import get_color
from constants import BELL_ICON, BARLOW_SEMI_BOLD, LIGHT_GREEN, EXIT_ICON, ORANGE, UZBEK_LAGUAGE, ARIAL_BLACK, WHITE, \
    WAITER_CALL, JOSEFIN_SANS_BOLD, SUCCESS_CHANGED_LANGUAGE, BLUE_BG_DARK, MEAL_COMPOSITION_COLOR
from config.translations import translate as _, get_current_language, set_language
from pages.login import SignInPage


class CallTheWaiterButton(Container):
    def __init__(self):
        super().__init__(
            content=Row([
                Image(src=BELL_ICON, width=20, height=20),
                Text(
                    _(WAITER_CALL),
                    size=16,
                    font_family=BARLOW_SEMI_BOLD,
                    color=WHITE
                )
            ],
                alignment=MainAxisAlignment.CENTER,
                vertical_alignment=CrossAxisAlignment.CENTER
            ),
            height=40,
            width=169.5,
            bgcolor=LIGHT_GREEN,
            border_radius=10,
            shadow=BoxShadow(
                blur_radius=10,
                color=LIGHT_GREEN,
                spread_radius=1,
                blur_style=ShadowBlurStyle.SOLID
            )
        )


class ExitButton(Container):
    def __init__(self):
        super().__init__(
            content=Image(src=EXIT_ICON, width=20, height=20),
            height=40,
            width=40,
            border_radius=8,
            bgcolor=colors.TRANSPARENT,
            alignment=alignment.center,
            on_click=lambda e: LogOut().open_dlg(e)

        )


class ChangeLanguageButton(Dropdown):
    def __init__(self, change_language):
        super().__init__(
            width=63,
            height=43.74,
            border_radius=8.5,
            bgcolor=get_color("change_language_bgcolor"),
            border_color=ORANGE,
            value=get_current_language(),
            on_change=change_language,
            options=[
                dropdown.Option(
                    key='uz',
                    content=Image(src="uzb.svg", height=20, width=20),
                ),
                dropdown.Option(
                    key='ru',
                    content=Image(src="ru.svg", height=20, width=20),
                ),
                dropdown.Option(
                    key='en',
                    content=Image(src="eng.svg", height=20, width=20),
                ),
            ],
        )


class ContinueOrder(Container):
    def __init__(self, button_text):
        super().__init__(
            width=221,
            height=30,
            border_radius=7.5,
            bgcolor=ORANGE,
            alignment=alignment.center,
            content=Text(button_text, size=10, font_family=BARLOW_SEMI_BOLD)
        )


class FoodCategoryButton(Row):

    @staticmethod
    def on_click_move_indicator(event: ControlEvent):
        indicator_ = event.control.content.controls[1]
        button = event.control.content.controls[0]
        buttons_ = event.control.parent.parent
        if indicator_.opacity == 1:
            pass
        else:
            for button_ in buttons_.controls:
                indicator__ = button_.controls[0].content.controls[1]
                button__ = button_.controls[0].content.controls[0]
                if indicator__.opacity == 1:
                    indicator__.opacity = 0
                if button__.color == ORANGE:
                    button__.color = get_color("tab_text")
                    button__.update()
                    indicator__.update()
            indicator_.opacity = 1
            button.color = ORANGE
            indicator_.update()
            button.update()

    def __init__(self, name: str, index: int):
        super().__init__(
            controls=[
                Container(
                    data=index,
                    on_click=self.on_click_move_indicator,
                    expand=True,
                    alignment=alignment.center_left,
                    height=54,
                    content=Row(
                        controls=[
                            Text(f'{name}', size=12, color=ORANGE if index == 0 else get_color("tab_text"), font_family=ARIAL_BLACK,
                                 width=130, expand=True),
                            Container(
                                bgcolor=ORANGE,
                                width=3,
                                height=54,
                                border_radius=3,
                                animate_opacity=animation.Animation(200, animation.AnimationCurve.EASE),
                                opacity=1 if index == 0 else 0,
                            )
                        ]
                    )
                )
            ]
        )
