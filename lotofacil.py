import flet as ft
import random
from time import sleep
from os import system as sys

def main(page: ft.Page):
    page.title = 'Lotofacil 1.0'
    page.vertical_alignment = ft.VerticalAlignment.CENTER
    lista_numeros=[]
       
        
    
    def create_list_of_drawn_numbers():
        list_of_draw_numbers = []
        for c in range(0, 15):
            while True:
                draw_number = random.randint(1,25)
                if draw_number not in list_of_draw_numbers:
                    list_of_draw_numbers.append(draw_number)
                    break
            # sleep(1)
            print(list_of_draw_numbers, c)
        sys('clear')
        list_of_draw_numbers_ordened = sorted(list_of_draw_numbers)
        return list_of_draw_numbers_ordened
        
     
    def create_containers_for_numbers_sorted(list):
        containers = []
        for c in range(0, len(list)):
            containers.append(
                    ft.Container(
                        height=40,
                        width=40,
                        # boder= 
                        bgcolor=ft.colors.WHITE,
                        border_radius=ft.border_radius.all(100),
                        alignment= ft.alignment.center,
                        content=ft.Text(
                            value=list[c],
                            color=ft.colors.PINK,
                            text_align=ft.TextAlign.CENTER,
                            size= 20
                        )
                    )
            )
            sleep(0.3)
            row.controls = containers
            row.update()
        
       
        return containers
    def click_sorteio(e):
        mensagem.value = "Um momento sorteando..."
        mensagem.update()
        lista_draw_numbers = create_list_of_drawn_numbers()
        create_containers_for_numbers_sorted(lista_draw_numbers)
        mensagem.value = 'Esses são seus 15 números gerados '
        mensagem.update()
    
    title = ft.Text(
        value='LOTOFACIL'
    )
    mensagem = ft.Text(value='Click no Botão sortear para gerar seus 15 números')
    button_sortear = ft.FilledButton(
        text='SORTEAR',
        on_click=click_sorteio
    )
    row = ft.Row(
        controls = create_containers_for_numbers_sorted(lista_numeros),
        alignment= ft.MainAxisAlignment.CENTER,
        wrap=True
    )
    text_nunmbers = ft.TextField(
        value= 'click em sortear'
    )
    col = ft.Column(
        alignment=ft.alignment.center,
        controls=[
            # text_nunmbers,
            title,
            mensagem,
            row,
            button_sortear,
        ]
    )
   
    #
    page.add(col)
    
ft.app(target=main, assets_dir='assets')