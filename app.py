import flet as ft
import string   

def main(page: ft.Page):
    list_images = ('')
    page.bgcolor = ft.colors.BROWN
     
    victim = ft.Image(
        data= 0,
        src='images/hangman_5.png',
        repeat= ft.ImageRepeat.NO_REPEAT,
        height=200
    )
    
    
    word = ft.Container()
    
    keyboard = ft.Container(
        col= {'xs': 12, 'lg': 6, },
        image_src = 'images/keyboard.png',
        image_repeat= ft.ImageRepeat.NO_REPEAT,
        image_fit = ft.ImageFit.FILL,
        padding = ft.padding.only(top=150, left=80, right=80, bottom=50),
        content = ft.Row(
            alignment= ft.MainAxisAlignment.CENTER,
            vertical_alignment=ft.VerticalAlignment.CENTER,
            wrap= True,
            controls=[
                ft.Container(
                    height= 35,
                    width=35,
                    border_radius = ft.border_radius.all(100),
                    alignment = ft.alignment.center,
                    content = ft.Text(
                        value = letter,
                        color = ft.colors.WHITE,
                        size =  25,
                        text_align= ft.TextAlign.CENTER,
                        
                        weight=ft.FontWeight.BOLD
                        
                        
                    ),
                    gradient= ft.LinearGradient(
                        begin=ft.alignment.top_center,
                        end = ft.alignment.bottom_center,
                        colors=[ft.colors.AMBER,ft.colors.DEEP_ORANGE]
                    )
                ) for letter in string.ascii_uppercase
            ]
        )   
        
    )
    scene = ft.Image(
         col=12,
         src='images/scene.png'
         )
    game = ft.Container(
        col={'xs':12, 'lg':6},
        padding = ft.padding.all(50),
        content =  ft.Column(
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
ft.app(target= main, assets_dir='assets')