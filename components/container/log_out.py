from flet import *
from config.translations import translate as _
from constants import BARLOW_BOLD, YES, LOG_OUT, NO
from page_urls import LOGIN_URL


class LogOut(CupertinoAlertDialog):
    def __init__(self):
        super().__init__(
            title=Text(
                value=_(LOG_OUT),
                text_align=TextAlign.CENTER,
                size=13,
                color=colors.WHITE,
                font_family=BARLOW_BOLD
            ),
            actions=[
                CupertinoDialogAction(
                    text=_(YES),
                    is_destructive_action=True,
                    on_click=lambda _: self.page.go(LOGIN_URL)
                ),
                CupertinoDialogAction(
                    text=_(NO),
                    on_click=self.dismiss_dialog
                ),
            ],
        )

    def dismiss_dialog(self, e):
        self.open = False
        e.control.page.update()

    def open_dlg(self, e):
        e.control.page.overlay.append(self)
        self.open = True
        e.control.page.update()
