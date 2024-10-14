from flet import *

from components.cards.card import Cards
from constants import BLUE_BG_COLOR, ACCOUNT, MENU
from components.buttons.main_page_buttons import MainPageButtons
from components.cards.order_history_card import OrderHistoryItemList
from components.container.category_buttons import FoodCategoryButtons
from components.container.order_history_container import OrderHistoryContainer
from page_urls import MAIN_PAGE_URL
from pages.main_page import MainPage
from pages.composition import FoodComposition
from page_urls import LOGIN_URL, CONTACT_URL, ABOUT_URL, TABLES_URL, FOOD_COMPOSITION
from pages.about import AboutPage
from pages.contact import ContactPage
from pages.login import SignInPage
from pages.tables import TablesPage

from config.translations import translate as _


def main(page: Page):
    page.fonts = {
        "Barlow-SemiBold": "/fonts/Barlow-SemiBold.ttf",
        "Barlow-Medium": "/fonts/Barlow-Medium.ttf",
        "Barlow-Regular": "/fonts/Barlow-Regular.ttf",
        "Barlow-Bold": "/fonts/Barlow-Bold.ttf",
        "Barlow-ExtraLight": "/fonts/Barlow-ExtraLight.ttf",
        "JosefinSans-Bold": "/fonts/JosefinSans-Bold.ttf",
        "JosefinSans-Medium": "/fonts/Barlow-Medium.ttf",
        "Arial-Black": "/fonts/ARIBLK.ttf",
        "Arial-Bold": "/fonts/ARIALBD.ttf",
    }

    page.horizontal_alignment = MainAxisAlignment.CENTER
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.padding = 0

    page.window_width = 960
    page.window_height = 600

    def route_change(route):
        page.views.clear()

        if page.route == LOGIN_URL:
            page.views.append(SignInPage(page))
        elif page.route == CONTACT_URL:
            page.views.append(ContactPage(page))
        elif page.route == ABOUT_URL:
            page.views.append(AboutPage(page))
        elif page.route == TABLES_URL:
            page.views.append(TablesPage(page))
        elif page.route == MAIN_PAGE_URL:
            page.views.append(MainPage(page))
        elif page.route == FOOD_COMPOSITION:
            page.views.append(FoodComposition(page))

        page.update()

    page.on_route_change = route_change
    page.go(LOGIN_URL)


app(target=main, assets_dir='assets')
