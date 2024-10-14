from flet import *

from components.buttons.main_page_button import CallTheWaiterButton, ExitButton, ChangeLanguageButton
from components.buttons.main_page_buttons import MainPageButtons
from components.cards.card import Cards
from components.cards.order_history_card import OrderHistoryItemList
from components.container.category_buttons import FoodCategoryButtons
from components.container.order_history_container import OrderHistoryContainer
from components.container.payment_container import Payment
from config.ui_manager import get_color, set_theme, get_current_theme
from constants import BLUE_BG_COLOR, ORANGE, BARLOW_SEMI_BOLD, BLACK_HOWL, TABLE, LOGO, WHITE, JOSEFIN_SANS_BOLD, \
    SUCCESS_CHANGED_LANGUAGE, BLUE_BG_DARK, MENU, ACCOUNT, SUM, SUCCESS_CHANGED_THEME, JOSEFIN_SANS_MEDIUM
from page_urls import MAIN_PAGE_URL
from config.translations import translate as _, set_language

cards_data = [
    [
        [
            {'button_text': '1', 'button_description': f'40 000 {_(SUM)}', 'disabled': False},
            {'button_text': '0.7', 'button_description': f'35 000 {_(SUM)}', 'disabled': True},
        ],
        'food.png',
        'Bahor Salat',
        True
    ],
    [
        [
            {'button_text': '1', 'button_description': '40 000 so`m', 'disabled': False},
        ],
        'food.png',
        'Bahor Salat',
        True
    ],
    [
        [
            {'button_text': '0.7', 'button_description': '35 000 so`m', 'disabled': True},
        ],
        'food.png',
        'Bahor Salat Skidkada Skidka Skidka Skidka'
    ],
    [
        [
            {'button_text': '1', 'button_description': '40 000 so`m', 'disabled': False},
            {'button_text': '0.7', 'button_description': '35 000 so`m', 'disabled': False},
        ],
        'food.png',
        'Bahor Salat'
    ],
    [
        [
            {'button_text': '1', 'button_description': '40 000 so`m', 'disabled': False},
            {'button_text': '0.7', 'button_description': '35 000 so`m', 'disabled': False},
        ],
        'food.png',
        'Bahor Salat'
    ],
    [
        [
            {'button_text': '1', 'button_description': '40 000 so`m', 'disabled': False},
            {'button_text': '0.7', 'button_description': '35 000 so`m', 'disabled': False},
        ],
        'food.png',
        'Bahor Salat'
    ],
    [
        [
            {'button_text': '1', 'button_description': '40 000 so`m', 'disabled': False},
            {'button_text': '0.7', 'button_description': '35 000 so`m', 'disabled': False},
        ],
        'food.png',
        'Bahor Salat'
    ],
    [
        [
            {'button_text': '1', 'button_description': '40 000 so`m', 'disabled': False},
            {'button_text': '0.7', 'button_description': '35 000 so`m', 'disabled': False},
        ],
        'food.png',
        'Bahor Salat'
    ],
    [
        [
            {'button_text': '1', 'button_description': '40 000 so`m', 'disabled': False},
            {'button_text': '0.7', 'button_description': '35 000 so`m', 'disabled': False},
        ],
        'food.png',
        'Bahor Salat'
    ],
    [
        [
            {'button_text': '1', 'button_description': '40 000 so`m', 'disabled': False},
            {'button_text': '0.7', 'button_description': '35 000 so`m', 'disabled': False},
        ],
        'food.png',
        'Bahor Salat'
    ],
    [
        [
            {'button_text': '1', 'button_description': '40 000 so`m', 'disabled': False},
            {'button_text': '0.7', 'button_description': '35 000 so`m', 'disabled': False},
        ],
        'food.png',
        'Bahor Salat'
    ],
]

item_list = [
    {
        'food_name': 'Bahor Salat',
        'image_path': 'food.png',
        'portion': '1',
        'price': '39 000',
        'amount': 1
    },
    {
        'food_name': 'Bahor Salat',
        'image_path': 'food.png',
        'portion': '0.7',
        'price': '39 000',
        'amount': 2
    },
    {
        'food_name': 'Bahor Salat',
        'image_path': 'food.png',
        'portion': '1',
        'price': '39 000',
        'amount': 1
    },
    {
        'food_name': 'Bahor Salat',
        'image_path': 'food.png',
        'portion': '0.7',
        'price': '390 000',
        'amount': 2
    },
    {
        'food_name': 'Bahor Salat',
        'image_path': 'food.png',
        'portion': '1',
        'price': '390 000',
        'amount': 1
    },
    {
        'food_name': 'Bahor Salat',
        'image_path': 'food.png',
        'portion': '0.7',
        'price': '390 000',
        'amount': 2
    },
]

data = [
    {
        'container': FoodCategoryButtons(cards=Cards(cards_data)),
        'index': 0,
    },
    {
        'container': OrderHistoryContainer(
            OrderHistoryItemList(item_list=item_list, service=15, total='336 950')
        ),
        'index': 1,
    },
]


class MainPage(View):
    def change_theme(self, e):
        if get_current_theme() == 'light':
            set_theme("dark")
        elif get_current_theme() == 'dark':
            set_theme("light")

        snack_bar = SnackBar(
            bgcolor='#1F1D2B',
            duration=3000,
            content=Text(
                value=_(SUCCESS_CHANGED_THEME),
                font_family=JOSEFIN_SANS_MEDIUM,
                color=WHITE,
                size=15,
            )
        )
        self.page.overlay.append(snack_bar)
        snack_bar.open = True
        self.page.views.clear()
        self.page.views.append(MainPage(self.page))
        self.page.update()

    def __init__(self, page: Page):
        super().__init__(
            padding=0,
            route=MAIN_PAGE_URL,
            vertical_alignment=MainAxisAlignment.CENTER,
            horizontal_alignment=CrossAxisAlignment.CENTER
        )

        self.page = page

        self.page.theme = Theme(
            scrollbar_theme=ScrollbarTheme(
                track_color={
                    MaterialState.HOVERED: colors.TRANSPARENT,
                    MaterialState.DEFAULT: colors.TRANSPARENT,
                },
                track_border_color=colors.TRANSPARENT,
                thumb_color={
                    MaterialState.HOVERED: colors.TRANSPARENT,
                    MaterialState.DEFAULT: colors.TRANSPARENT,
                },
            )

        )

        self.body = Container(
            content=Row(
                spacing=0,
                data=data,
                controls=[
                    Column(
                        spacing=0,
                        controls=[
                            Container(
                                width=699, height=80, bgcolor=get_color("main_page_bgcolor"), content=Row(
                                    controls=[
                                        # Logo
                                        Container(
                                            content=Image(
                                                src=LOGO, width=132, height=71.5, color=get_color("logo_color")
                                            ),
                                            alignment=alignment.center,
                                            width=132,
                                            height=71.5
                                        ),
                                        ###
                                        Container(width=29.5),
                                        ###
                                        Container(
                                            width=111,
                                            height=40,
                                            border_radius=4,
                                            bgcolor=get_color("table_number_bgcolor"),
                                            border=border.all(2, ORANGE),
                                            alignment=alignment.center,
                                            content=Text(
                                                value=f'{_(TABLE)}-{16}',
                                                size=16,
                                                font_family=BARLOW_SEMI_BOLD,
                                                color=get_color("tables_button_text")
                                            )
                                        ),
                                        ###
                                        Container(width=20),
                                        ###
                                        CallTheWaiterButton(),
                                        ###
                                        Container(width=137),
                                        ###
                                        ExitButton()
                                        ###
                                    ]
                                )
                            ),
                            Container(
                                width=699,
                                height=75,
                                bgcolor=get_color("main_page_container"),
                                content=Row(
                                    spacing=0,
                                    controls=[
                                        ###
                                        Container(width=77),
                                        ###
                                        MainPageButtons(),
                                        ###
                                        Container(width=260.5),
                                        ###
                                        Container(
                                            on_click=self.change_theme,
                                            content=Image(
                                                width=30,
                                                height=30,
                                                src='sun.png' if get_current_theme() == 'dark' else 'moon.png'
                                            ),
                                        ),
                                        ###
                                        Container(width=30),
                                        ###
                                        ChangeLanguageButton(self.change_language)
                                    ]),
                            ),
                            FoodCategoryButtons(
                                cards=Cards(cards_data)
                            ),
                        ]
                    ),
                    Payment(10, full_price='90 540')
                ]
            )
        )
        self.controls = [self.body]

    def change_language(self, e):
        new_language = e.control.value
        set_language(new_language)

        snack_bar = SnackBar(  # noqa
            bgcolor=BLUE_BG_DARK,
            duration=3000,
            content=Text(
                value=_(SUCCESS_CHANGED_LANGUAGE),
                font_family=JOSEFIN_SANS_BOLD,
                color=WHITE,
                size=15,
            )
        )
        self.page.overlay.append(snack_bar)
        snack_bar.open = True

        self.page.views.clear()
        self.page.views.append(MainPage(self.page))

        self.page.locale_configuration = LocaleConfiguration(
            supported_locales=[
                Locale("uz", "UZ"),
                Locale("ru", "RU"),
                Locale("en", "EN"),
            ],
            current_locale=Locale("uz", "UZ"),
        )
        self.page.locale_configuration.current_locale = Locale(new_language)
        self.page.update()
