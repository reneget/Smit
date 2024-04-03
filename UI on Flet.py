import flet as ft
import csv
import math


def ui_main(page):

    label_field = ft.TextField(label='Введите команду', border_color='#DFB6B2', hint_text='id/user/tech/link/time')

    def add_command(e):     # добавляем
        get_value = label_field.value.split()
        page.update()
        with open('commands_data.csv', 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(get_value)
        print('добавлено')
        print(get_value, type(get_value))


    def del_command(e):     # удаляем
        get_value = label_field.value.split()
        with open('commands_data.csv', 'r', newline='', encoding='utf-8') as csvfile:
            rows = list(csv.reader(csvfile))
        with open('commands_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            for row in rows:
                if row[0].strip() != get_value[0]:
                    writer.writerow(row)
        print('удалено')


    def change_theme(e):    # смена темы
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
        page.update()


    # clr colors
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
    page.window_resizable = False

    btn_add_com = ft.ElevatedButton(text="Добавить", on_click=add_command)
    btn_del_com = ft.ElevatedButton(text="Удалить", on_click=del_command)
    btn_sunny = ft.IconButton(ft.icons.SUNNY, icon_color='PURPLE', on_click=change_theme)
    space = ft.IconButton(ft.icons.MENU, icon_color='PURPLE')

    page.add(
        ft.Column(
            [
                ft.Container(
                    alignment=ft.alignment.center,
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_left,
                        end=ft.Alignment(0.8, 1),
                        colors=[
                            "0xffFFC7B4",
                            "0xffFFA080",
                        ],
                        tile_mode=ft.GradientTileMode.MIRROR,
                        rotation=math.pi / 3,
                    ),
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
                                    ft.Checkbox(label='Функция'),
                                    ft.Checkbox(label='Функция'),
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
                            ft.Column(
                                [
                                    label_field,
                                    ft.Row(
                                        [
                                            btn_del_com,
                                            btn_add_com,
                                        ],
                                        alignment=ft.MainAxisAlignment.SPACE_EVENLY
                                    )
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
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
    )



ft.app(target=ui_main)





























#             ft.IconButton(ft.icons.HOME, on_click=get_info),       # какие-то кнопки
#             ft.Icon(ft.icons.BACK_HAND),                           # иконки
#             user_field,
#             user_label,
#             ft.ElevatedButton(text='Click me', on_click=get_info),
#             ft.OutlinedButton(text='Click me', on_click=get_info),


