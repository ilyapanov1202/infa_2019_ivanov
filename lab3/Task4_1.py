from graph import *

#руки
penColor(255, 233, 210)
brushColor(255, 233, 210)
polygon([(30, 80), (130, 370), (150, 370), (50, 80)])
polygon([(470, 80), (370, 370), (350, 370), (450, 80)])

#кисти
penColor(255, 233, 210)
brushColor(255, 233, 210)
circle(45, 80, 25)
circle(455, 80, 25)

#зелёный прямоугольник
penColor(0, 0, 0)
brushColor(0, 255, 0)
rectangle(0, 0, 500, 80)

#тело
penColor(255, 233, 210)
brushColor("#cd5700")
circle(250, 480, 150)

#уберёмизлишки
penColor(255, 255, 255)
brushColor(255, 255, 255)
rectangle(0, 460, 500, 800)

#голова
penColor(255, 233, 210)
brushColor(255, 233, 210)
circle(250, 250, 120)

#белкиглаз
penColor(0, 0, 0)
brushColor(114, 190, 255)
circle(215, 225, 25)
circle(285, 225, 25)

#зрачки
penColor(0, 0, 0)
brushColor(0, 0, 0)
circle(215, 230, 7)
circle(285, 230, 7)

#нос
penColor(0, 0, 0)
brushColor("#8d4100")
polygon([(250, 270), (240, 254), (260, 254)])

#рот
penColor(0, 0, 0)
brushColor("#ff1a1a")
polygon([(250, 320), (190, 280), (310, 280)])

#рукава
penColor(0, 0, 0)
brushColor("#cd5700")
polygon([(150, 400), (110, 390), (105, 350), (150, 325), (175, 355)])
polygon([(350, 400), (390, 390), (395, 350), (350, 325), (325, 355)])

#волосы
penColor(0, 0, 0)
brushColor(255, 0, 255)
polygon([(145, 152), (155, 180), (173, 160)])
polygon([(158, 140), (168, 167), (186, 150)])
polygon([(180, 128), (182, 155), (203, 140)])



run()