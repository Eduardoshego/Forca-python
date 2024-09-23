import flet as ft
import string
import random
from time import sleep


def main(page: ft.Page):
    page.bgcolor = ft.colors.BROWN
    avaliable_words = ['pera', 'uva', 'maçã' 'melão', 'limão', ]
    choice = random.choice(avaliable_words).upper()

    def validate_choice(e):
        if e.control.content.value in choice:
            for pos,  letter in enumerate(choice):
                if e.control.content.value == letter:
                    word.controls[pos] = letter_to_guess(letter=letter)
                    word.update()
        else:
            victim.data = victim.data + 1
            if victim.data < 7:
                victim.src = f'images/hangman_{victim.data}.png'
                victim.update()
            else:
                victim.src = f'images/hangman_{victim.data}.png'
                page.update()
                sleep(0.5)
                page.open(dlg)

    def letter_to_guess(letter):
        return ft.Container(
            height=50,
            width=50,
            border_radius=ft.border_radius.all(5),
            alignment=ft.alignment.center,
            bgcolor=ft.colors.AMBER,
            content=ft.Text(
                value=letter,
                color=ft.colors.WHITE,
                size=25,
                text_align=ft.TextAlign.CENTER,
                weight=ft.FontWeight.BOLD
            )
        )
    dlg = ft.AlertDialog(
        title=ft.Text("Você perdeu! :("),
    )

    victim = ft.Image(
        data=0,
        src='images/hangman_0.png',
        repeat=ft.ImageRepeat.NO_REPEAT,
        height=200
    )

    word = ft.Row(
        controls=[
            letter_to_guess('_') for letter in choice
        ]
    )

    keyboard = ft.Container(
        col={'xs': 12, 'lg': 6, },
        image_src='images/keyboard.png',
        image_repeat=ft.ImageRepeat.NO_REPEAT,
        image_fit=ft.ImageFit.FILL,
        padding=ft.padding.only(top=150, left=80, right=80, bottom=50),
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.VerticalAlignment.CENTER,
            wrap=True,
            controls=[
                ft.Container(
                    height=35,
                    width=35,
                    border_radius=ft.border_radius.all(100),
                    alignment=ft.alignment.center,
                    content=ft.Text(
                        value=letter,
                        color=ft.colors.WHITE,
                        size=25,
                        text_align=ft.TextAlign.CENTER,

                        weight=ft.FontWeight.BOLD


                    ),
                    gradient=ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=[ft.colors.AMBER, ft.colors.DEEP_ORANGE]
                    ),
                    on_click=validate_choice

                ) for letter in string.ascii_uppercase
            ]
        )

    )
    scene = ft.Image(
        col=12,
        src='images/scene.png'
    )
    game = ft.Container(
        col={'xs': 12, 'lg': 6},
        padding=ft.padding.all(50),
        content=ft.Column(
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment .CENTER,
            controls=[
                victim,
                word

            ]
        )
    )

    layout = ft.ResponsiveRow(
        controls=[
            scene,
            game,
            keyboard,
            scene

        ]
    )

    page.add(layout)


ft.app(target=main, assets_dir='assets')
