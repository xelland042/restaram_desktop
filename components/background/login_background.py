from flet import *
import flet.map as map

from constants import BACK_OPACITY_DARK


class LoginBackground(Container):
    def __init__(self, image_src):
        super().__init__(
            expand=True,
            image_src=image_src,
            image_fit=ImageFit.COVER,
            bgcolor=BACK_OPACITY_DARK,
            opacity=0.3,
        )


class AboutBackground(Container):
    def __init__(self, image_src):
        super().__init__(
            expand=True,
            bgcolor=BACK_OPACITY_DARK,
            opacity=0.3,
            padding=0,
            alignment=Alignment(0, 0),

            content=Column(
                expand=True,
                spacing=0,
                controls=[
                    Image(src=image_src, height=500, width=960, fit=ImageFit.COVER),
                    map.Map(
                        height=100,
                        expand=True,
                        configuration=map.MapConfiguration(
                            initial_center=map.MapLatitudeLongitude(41.2995, 69.2401),
                            initial_zoom=16,
                            interaction_configuration=map.MapInteractionConfiguration(
                                flags=map.MapInteractiveFlag.ALL
                            ),

                        ),
                        layers=[
                            map.TileLayer(
                                url_template="https://tile.openstreetmap.org/{z}/{x}/{y}.png",
                                on_image_error=lambda e: print("TileLayer Error"),
                            ),

                        ],
                    ),
                ]
            )
        )
