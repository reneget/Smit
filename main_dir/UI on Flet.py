import flet as ft


def ui_main(page):
    page.title = 'flet app'
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.window_width = 350
    page.window_height = 350
    page.window_resizable = False

    btn_add_command = ft.OutlinedButton(text='Добавить')
    label_field = ft.TextField(label='Введите команду')

    def validate(e):
        if btn_add_command:
            pass


    def change_theme(e):
        page.theme_mode = 'light' if page.theme_mode == 'dark' else 'dark'
        page.update()


    page.add(
        ft.Row(
            [
                ft.Text('Settings', size=20),
                ft.IconButton(ft.icons.SUNNY, on_click=change_theme)
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        ),
        ft.Column(
            [
                ft.Checkbox(label='Озвучка помощника'),
                ft.Checkbox(label='хззхзхз'),
                ft.Checkbox(label='ыуаыаыуа'),
                label_field
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                btn_add_command
            ],
            alignment=ft.MainAxisAlignment.CENTER
        )
    )

ft.app(target=ui_main)


# user_label = ft.Text('Текст')                                                       # текст
# user_field = ft.TextField(value="0", width=150, text_align=ft.TextAlign.CENTER)     # поле ввода
#
# def get_info(e):
#     user_label.value = user_field.value
#     page.update()
#
#
# page.add(
#     ft.Row(    # создает ряд
#         [
#             ft.IconButton(ft.icons.HOME, on_click=get_info),       # какие-то кнопки
#             ft.Icon(ft.icons.BACK_HAND),                           # иконки
#             user_field,
#             user_label,
#             ft.ElevatedButton(text='Click me', on_click=get_info),
#             ft.OutlinedButton(text='Click me', on_click=get_info),
#             ft.Checkbox(label='Норм?', value=True)
#
#         ],
#         alignment=ft.MainAxisAlignment.CENTER   # расположение данного ряда на окне
#     )
# )
