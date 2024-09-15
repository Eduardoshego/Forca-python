import flet as ft

def main(page: ft.Page):
    page.bgcolor = ft.colors.BROWN_600
    page.update()
    
    
    page.add()
ft.app(target= main, assets_dir='assets')