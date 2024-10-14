import flet as ft
import threading

def main(page: ft.Page):
    page.title = "AlertDialog examples"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Oddiy dialogni 5 sekunddan keyin yopish funksiyasi
    def auto_close_dialog(dialog):
        threading.Timer(5.0, lambda: dialog.close()).start()

    # Oddiy dialog
    dlg = ft.AlertDialog(
        title=ft.Text("Hi, this is a non-modal dialog!"),
        on_dismiss=lambda e: page.add(ft.Text("Non-modal dialog dismissed")),
    )

    # Oddiy dialog ochilgandan keyin uni avtomatik yopish
    def open_dialog(e):
        page.open(dlg)
        auto_close_dialog(dlg)  # 5 sekunddan keyin dialogni yopish

    # Modal dialog uchun tugmalarni boshqarish funksiyasi
    def handle_close(e):
        page.close(dlg_modal)
        page.add(ft.Text(f"Modal dialog closed with action: {e.control.text}"))

    # Modal dialog
    dlg_modal = ft.AlertDialog(
        modal=True,
        title=ft.Text("Please confirm"),
        content=ft.Text("Do you really want to delete all those files?"),
        actions=[
            ft.TextButton("Yes", on_click=handle_close),
            ft.TextButton("No", on_click=handle_close),
        ],
        actions_alignment=ft.MainAxisAlignment.END,
        on_dismiss=lambda e: page.add(ft.Text("Modal dialog dismissed")),
    )

    # Dialoglarni ochuvchi tugmalar
    page.add(
        ft.ElevatedButton("Open dialog", on_click=open_dialog),
        ft.ElevatedButton("Open modal dialog", on_click=lambda e: page.open(dlg_modal)),
    )

ft.app(main)
