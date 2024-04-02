import flet as ft
import flet_core


def ui_main(page):

    def add_command(e):
        pass

    def validate(e):
        if btn_add_command:
            pass

    def change_theme(e):
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
        page.update()


    # colors
    dark_grey = '#11212D'
    grey = '#253745'
    light_grey = '#4A5C6A'
    dark_blue = '#2B124C'
    purple = '#522B5B'
    peach = '#854F6C'
    sand = '#DFB6B2'
    skin = '#FBE4D8'
    used = '#F4ECF7'


    page.title = 'Smith'
    page.theme_mode = 'light'
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.window_width = 358         # 350
    page.window_height = 406        # 350
    # page.window_resizable = False

    btn_add_com = ft.ElevatedButton(text="Добавить")
    btn_del_com = ft.ElevatedButton(text="Удалить")
    label_field = ft.TextField(label='Введите команду', border_color=sand)
    btn_sunny = ft.IconButton(ft.icons.SUNNY, icon_color='PURPLE', on_click=change_theme)
    space = ft.IconButton(ft.icons.MENU, icon_color='PURPLE')

    page.add(

        ft.Container(
            width=320,
            height=220,
            padding=10,
            bgcolor=sand,
            border_radius=10,
            content=ft.Column(
                controls=[
                    ft.Row(
                        [
                            ft.Container(
                                width=300,
                                height=65,
                                padding=15,
                                bgcolor='#F4ECF7',
                                border_radius=10,
                                content=ft.Row(
                                    [
                                        space,
                                        ft.Text('Settings', size=26, color='#2C3E50'),
                                        btn_sunny
                                    ],
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                                )
                            ),
                        ]
                    ),


                    ft.Column(
                        [
                            ft.Checkbox(label='Озвучка помощника'),
                            ft.Checkbox(label='Ставь лайк'),
                            ft.Checkbox(label='Пнуть ветер'),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ]
            )
        ),

        ft.Container(
            width=320,
            height=76,
            padding=10,
            bgcolor='dark',
            border_radius=10,
            content=ft.Column(
                controls=[
                    ft.Row(
                        [
                            label_field
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ]
            )

        ),

        ft.Row(
            [
                btn_del_com,
                btn_add_com,
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY
        )
    )


ft.app(target=ui_main)































#             ft.IconButton(ft.icons.HOME, on_click=get_info),       # какие-то кнопки
#             ft.Icon(ft.icons.BACK_HAND),                           # иконки
#             user_field,
#             user_label,
#             ft.ElevatedButton(text='Click me', on_click=get_info),
#             ft.OutlinedButton(text='Click me', on_click=get_info),


