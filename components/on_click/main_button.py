from flet import *

from constants import ORANGE, WHITE


def on_click_category_buttons(event: ControlEvent):
    button_ = event.control.parent.controls[1]
    container_ = event.control.parent.controls[0]
    all_buttons = event.control.parent.controls[1].parent.parent.parent.controls
    for button in all_buttons:
        if button.content.controls[1].data['pressed']:
            button.content.controls[1].data['pressed'] = False
            button.content.controls[1].width = 97.5
            button.content.controls[1].bgcolor = colors.TRANSPARENT
            button.content.controls[1].content = Row(controls=[button.content.controls[1].data['main_icon'],
                                                               button.content.controls[1].data['text']], spacing=0,
                                                     alignment=MainAxisAlignment.CENTER)
            button.content.controls[0].offset.y = 1
        button.content.controls[0].update()
        button.content.controls[1].update()
    if button_.data['pressed']:
        pass
    elif not button_.data['pressed']:
        button_.data['pressed'] = True
        button_.width = 45
        button_.bgcolor = ORANGE
        button_.content = Row(controls=[button_.data['second_icon']], spacing=0,
                              alignment=MainAxisAlignment.CENTER)
        container_.offset.y = 0
        button_.update()
        container_.update()
