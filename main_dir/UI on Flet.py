import flet as ft


def ui_main(page):
    page.title = 'flet app'
    page.theme_mode = 'dark'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    user_label = ft.Text('Текст')                                                       # текст
    user_field = ft.TextField(value="0", width=150, text_align=ft.TextAlign.CENTER)     # поле ввода

    def get_info(e):
        user_label.value = user_field.value
        page.update()


    page.add(
        ft.Row(    # создает ряд
            [
                ft.IconButton(ft.icons.HOME, on_click=get_info),       # какие-то кнопки
                ft.Icon(ft.icons.BACK_HAND),                           # иконки
                user_field,
                user_label,
                ft.ElevatedButton(text='Click me', on_click=get_info),
                ft.OutlinedButton(text='Click me', on_click=get_info),
                ft.Checkbox(label='Норм?', value=True)

            ],
            alignment=ft.MainAxisAlignment.CENTER   # расположение данного ряда на окне
        )
    )




ft.app(target=ui_main)
