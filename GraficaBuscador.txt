import pygame
import math

pygame.init()

# Configurar la ventana
screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Automata Buscador de palabras")

# Configurar el color de fondo
background_color = (255, 255, 255)

# Configurar la fuente
font = pygame.font.Font(None, 20)

# Configurar los círculos
circle_radius = 35
#q0
circle_center = (50, 330)
#WEB
circle1_center = (150,200)
circle2_center = (250,200)
circle3_center = (350,200)
#master
circle4_center = (450,100)
circle5_center = (550,100)
circle6_center = (650,100)
circle7_center = (750,100)
circle8_center = (850,100)
circle9_center = (950,100)
#site
circle10_center = (450,300)
circle11_center = (550,300)
circle12_center = (650,300)
circle13_center = (750,300)

#pageweb
circle14_center = (150,400)
circle15_center = (250,400)
circle16_center = (350,400)
circle17_center = (450,400)
circle18_center = (550,400)
circle19_center = (650,400)
circle20_center = (750,400)
#ebay
circle21_center = (150,500)
circle22_center = (250,500)
circle23_center = (350,500)
circle24_center = (450,500)

#net
circle25_center = (150,600)
circle26_center = (250,600)
circle27_center = (350,600)


# Configurar la línea
line0_start = (50,330)
line0_end = (150,200)

###WEB
line1_start = (150,200)
line1_end = (250,200)

line2_start = (250,200)
line2_end = (350,200)

##MAster
line3_start = (350,200)
line3_end = (450,100)

line4_start = (450,100)
line4_end = (550,100)

line5_start = (550,100)
line5_end = (650,100)

line6_start = (650,100)
line6_end = (750,100)

line7_start = (750,100)
line7_end = (850,100)

line8_start = (850,100)
line8_end = (950,100)

#Site
line9_start = (350,200)
line9_end = (450,300)

line10_start = (450,300)
line10_end = (550,300)

line11_start = (450,300)
line11_end = (550,300)

line12_start = (550,300)
line12_end = (650,300)

line13_start = (650,300)
line13_end = (750,300)

#pageweb

line14_start = (50,330)
line14_end = (150,400)

line15_start = (150,400)
line15_end = (250,400)

line16_start = (250,400)
line16_end = (350,400)

line17_start = (350,400)
line17_end = (450,400)

line18_start = (450,400)
line18_end = (550,400)

line19_start = (550,400)
line19_end = (650,400)

line20_start = (650,400)
line20_end = (750,400)

#ebay
line21_start = (50,330)
line21_end = (150,500)

line22_start = (150,500)
line22_end = (250,500)

line23_start = (250,500)
line23_end = (350,500)

line24_start = (350,500)
line24_end = (450,500)



#Net
line25_start = (50,330)
line25_end = (150,600)

line26_start = (150,600)
line26_end = (250,600)

line27_start = (250,600)
line27_end = (350,600)

#Asi mismo

line28_start = (50,330)
line28_end = (10,300)

line29_start = (10,300)
line29_end = (58,338)

#Todos a q0
line30_start = (50,330)
line30_end = (150,200)
line31_start = (50,330)
line31_end = (250,200)
line32_start = (50,330)
line32_end = (350,200)

line33_start = (50,330)
line33_end = (450,100)
line34_start = (50,330)
line34_end = (550,100)
line35_start = (50,330)
line35_end = (650,100)
line36_start = (50,330)
line36_end = (750,100)
line37_start = (50,330)
line37_end = (850,100)
line38_start = (50,330)
line38_end = (950,100)


# Renderizar el texto

text0 = font.render("q0", True, (255,255,255))
text1 = font.render("q1", True, (255, 255, 255))
text2 = font.render("q2", True, (255, 255, 255))
text3 = font.render("q3", True, (255, 255, 255))
text4 = font.render("q4", True, (255, 255, 255))
text5 = font.render("q5", True, (255, 255, 255))
text6 = font.render("q6", True, (255, 255, 255))
text7 = font.render("q7", True, (255, 255, 255))
text8 = font.render("q8", True, (255, 255, 255))
text9 = font.render("q9", True, (255, 255, 255))
text10 = font.render("q10", True, (255,255,255))
text11 = font.render("q11", True, (255, 255, 255))
text12 = font.render("q12", True, (255, 255, 255))
text13 = font.render("q13", True, (255, 255, 255))
text14 = font.render("q14", True, (255, 255, 255))
text15 = font.render("q15", True, (255, 255, 255))
text16 = font.render("q16", True, (255, 255, 255))
text17 = font.render("q17", True, (255, 255, 255))
text18 = font.render("q18", True, (255, 255, 255))
text19 = font.render("q19", True, (255, 255, 255))
text10 = font.render("q10", True, (255, 255, 255))
text11 = font.render("q11", True, (255, 255, 255))
text12 = font.render("q12", True, (255, 255, 255))
text13 = font.render("q13", True, (255, 255, 255))
text14 = font.render("q14", True, (255, 255, 255))
text15 = font.render("q15", True, (255, 255, 255))
text16 = font.render("q16", True, (255, 255, 255))
text17 = font.render("q17", True, (255, 255, 255))
text18 = font.render("q18", True, (255, 255, 255))
text19 = font.render("q19", True, (255, 255, 255))
text20 = font.render("q20", True, (255, 255, 255))
text21 = font.render("q21", True, (255, 255, 255))
text22 = font.render("q22", True, (255, 255, 255))
text23 = font.render("q23", True, (255, 255, 255))
text24 = font.render("q24", True, (255, 255, 255))
text25 = font.render("q25", True, (255, 255, 255))
text26 = font.render("q26", True, (255, 255, 255))
text27 = font.render("q27", True, (255, 255, 255))
text28 = font.render("Σ-{w,p,e,n}", True, (0, 0, 0))
text29 = font.render("w", True, (0, 0, 0))
text30 = font.render("p", True, (0, 0, 0))
text31 = font.render("e", True, (0, 0, 0))
text32 = font.render("n", True, (0, 0, 0))
text33 = font.render("e", True, (0, 0, 0))
text34 = font.render("b", True, (0, 0, 0))
text35 = font.render("m", True, (0, 0, 0))
text36 = font.render("a", True, (0, 0, 0))
text37 = font.render("p", True, (0, 0, 0))
text38 = font.render("e", True, (0, 0, 0))
text39 = font.render("n", True, (0, 0, 0))
text40 = font.render("e", True, (0, 0, 0))
text41 = font.render("b", True, (0, 0, 0))
text42 = font.render("m", True, (0, 0, 0))
text43 = font.render("a", True, (0, 0, 0))

# Obtener los rectángulos de texto
text0_rect = text0.get_rect()
text1_rect = text1.get_rect()
text2_rect = text2.get_rect()
text3_rect = text3.get_rect()
text4_rect = text4.get_rect()
text5_rect = text5.get_rect()
text6_rect = text6.get_rect()
text7_rect = text7.get_rect()
text8_rect = text8.get_rect()
text9_rect = text9.get_rect()
text10_rect = text10.get_rect()
text11_rect = text11.get_rect()
text12_rect = text12.get_rect()
text13_rect = text13.get_rect()
text14_rect = text14.get_rect()
text15_rect = text15.get_rect()
text16_rect = text16.get_rect()
text17_rect = text17.get_rect()
text18_rect = text18.get_rect()
text19_rect = text19.get_rect()
text20_rect = text20.get_rect()
text21_rect = text21.get_rect()
text22_rect = text22.get_rect()
text23_rect = text23.get_rect()
text24_rect = text24.get_rect()
text25_rect = text25.get_rect()
text26_rect = text26.get_rect()
text27_rect = text27.get_rect()
text28_rect = text28.get_rect()
text29_rect = text29.get_rect()
text30_rect = text30.get_rect()
text31_rect = text30.get_rect()
text32_rect = text30.get_rect()

# Centrar los textos en los círculos

text0_rect.center = circle_center
text1_rect.center = circle1_center
text2_rect.center = circle2_center
text3_rect.center = circle3_center
text4_rect.center = circle4_center
text5_rect.center = circle5_center
text6_rect.center = circle6_center
text7_rect.center = circle7_center
text8_rect.center = circle8_center
text9_rect.center = circle9_center
text10_rect.center = circle10_center
text11_rect.center = circle11_center
text12_rect.center = circle12_center
text13_rect.center = circle13_center
text14_rect.center = circle14_center
text15_rect.center = circle15_center
text16_rect.center = circle16_center
text17_rect.center = circle17_center
text18_rect.center = circle18_center
text19_rect.center = circle19_center
text20_rect.center = circle20_center
text21_rect.center = circle21_center
text22_rect.center = circle22_center
text23_rect.center = circle23_center
text24_rect.center = circle24_center
text25_rect.center = circle25_center
text26_rect.center = circle26_center
text27_rect.center = circle27_center
text28_rect.center = (35,280)
text29_rect.center = (80,250)
text30_rect.center = (90,350)
text31_rect.center = (90,450)
text32_rect.center = (90,550)
# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
	# Llenar la superficie de la pantalla con el color de fondo
    screen.fill(background_color)

    # Dibujar la línea
    pygame.draw.line(screen, (0, 0, 0), line0_start, line0_end)
    pygame.draw.line(screen, (0, 0, 0), line1_start, line1_end)
    pygame.draw.line(screen, (0, 0, 0), line2_start, line2_end)
    pygame.draw.line(screen, (0, 0, 0), line3_start, line3_end)
    pygame.draw.line(screen, (0, 0, 0), line4_start, line4_end)
    pygame.draw.line(screen, (0, 0, 0), line5_start, line5_end)
    pygame.draw.line(screen, (0, 0, 0), line6_start, line6_end)
    pygame.draw.line(screen, (0, 0, 0), line7_start, line7_end)
    pygame.draw.line(screen, (0, 0, 0), line8_start, line8_end)
    pygame.draw.line(screen, (0, 0, 0), line9_start, line9_end)
    pygame.draw.line(screen, (0, 0, 0), line10_start, line10_end)
    pygame.draw.line(screen, (0, 0, 0), line11_start, line11_end)
    pygame.draw.line(screen, (0, 0, 0), line12_start, line12_end)
    pygame.draw.line(screen, (0, 0, 0), line13_start, line13_end)
    pygame.draw.line(screen, (0, 0, 0), line14_start, line14_end)
    pygame.draw.line(screen, (0, 0, 0), line15_start, line15_end)
    pygame.draw.line(screen, (0, 0, 0), line16_start, line16_end)
    pygame.draw.line(screen, (0, 0, 0), line17_start, line17_end)
    pygame.draw.line(screen, (0, 0, 0), line18_start, line18_end)
    pygame.draw.line(screen, (0, 0, 0), line19_start, line19_end)
    pygame.draw.line(screen, (0, 0, 0), line20_start, line20_end)
    pygame.draw.line(screen, (0, 0, 0), line21_start, line21_end)
    pygame.draw.line(screen, (0, 0, 0), line22_start, line22_end)
    pygame.draw.line(screen, (0, 0, 0), line23_start, line23_end)
    pygame.draw.line(screen, (0, 0, 0), line24_start, line24_end)
    pygame.draw.line(screen, (0, 0, 0), line25_start, line25_end)
    pygame.draw.line(screen, (0, 0, 0), line26_start, line26_end)
    pygame.draw.line(screen, (0, 0, 0), line27_start, line27_end)
    pygame.draw.line(screen, (0, 0, 0), line28_start, line28_end)
    pygame.draw.line(screen, (0, 0, 0), line29_start, line29_end)
    pygame.draw.line(screen, (0, 0, 0), line30_start, line30_end)
    pygame.draw.line(screen, (0, 0, 0), line31_start, line31_end)
    pygame.draw.line(screen, (0, 0, 0), line32_start, line32_end)
    pygame.draw.line(screen, (0, 0, 0), line33_start, line33_end)
    pygame.draw.line(screen, (0, 0, 0), line34_start, line34_end)
    pygame.draw.line(screen, (0, 0, 0), line0_start, line5_end)
    pygame.draw.line(screen, (0, 0, 0), line0_start, line6_end)
    pygame.draw.line(screen, (0, 0, 0), line0_start, line7_end)
    pygame.draw.line(screen, (0, 0, 0), line0_start, line8_end)
    pygame.draw.line(screen, (0, 0, 0), line0_start, line9_end)
    pygame.draw.line(screen, (0, 0, 0), line0_start, line10_end)
    pygame.draw.line(screen, (0, 0, 0), line0_start, line11_end)
    pygame.draw.line(screen, (0, 0, 0), line0_start, line12_end)
    pygame.draw.line(screen, (0, 0, 0), line0_start, line13_end)
    pygame.draw.line(screen, (0, 0, 0), line0_start, line15_end)
    pygame.draw.line(screen, (0, 0, 0), line0_start, line16_end)
    pygame.draw.line(screen, (0, 0, 0), line0_start, line17_end)
    pygame.draw.line(screen, (0, 0, 0), line0_start, line18_end)
    pygame.draw.line(screen, (0, 0, 0), line0_start, line19_end)
    pygame.draw.line(screen, (0, 0, 0), line0_start, line20_end)
    pygame.draw.line(screen, (0, 0, 0), line0_start, line21_end)
    pygame.draw.line(screen, (0, 0, 0), line0_start, line22_end)
    pygame.draw.line(screen, (0, 0, 0), line0_start, line23_end)
    pygame.draw.line(screen, (0, 0, 0), line0_start, line24_end)
    pygame.draw.line(screen, (0, 0, 0), line0_start, line25_end)
    pygame.draw.line(screen, (0, 0, 0), line0_start, line26_end)
    pygame.draw.line(screen, (0, 0, 0), line0_start, line27_end)
    pygame.draw.line(screen, (0, 0, 0), line1_start, line5_end)
    pygame.draw.line(screen, (0, 0, 0), line1_start, line6_end)
    pygame.draw.line(screen, (0, 0, 0), line1_start, line7_end)
    pygame.draw.line(screen, (0, 0, 0), line1_start, line8_end)
    pygame.draw.line(screen, (0, 0, 0), line1_start, line9_end)
    pygame.draw.line(screen, (0, 0, 0), line1_start, line10_end)
    pygame.draw.line(screen, (0, 0, 0), line1_start, line11_end)
    pygame.draw.line(screen, (0, 0, 0), line1_start, line12_end)
    pygame.draw.line(screen, (0, 0, 0), line1_start, line13_end)
    pygame.draw.line(screen, (0, 0, 0), line1_start, line15_end)
    pygame.draw.line(screen, (0, 0, 0), line1_start, line16_end)
    pygame.draw.line(screen, (0, 0, 0), line1_start, line17_end)
    pygame.draw.line(screen, (0, 0, 0), line1_start, line18_end)
    pygame.draw.line(screen, (0, 0, 0), line1_start, line19_end)
    pygame.draw.line(screen, (0, 0, 0), line1_start, line20_end)
    pygame.draw.line(screen, (0, 0, 0), line1_start, line21_end)
    pygame.draw.line(screen, (0, 0, 0), line1_start, line22_end)
    pygame.draw.line(screen, (0, 0, 0), line1_start, line23_end)
    pygame.draw.line(screen, (0, 0, 0), line1_start, line24_end)
    pygame.draw.line(screen, (0, 0, 0), line1_start, line25_end)
    pygame.draw.line(screen, (0, 0, 0), line1_start, line26_end)
    pygame.draw.line(screen, (0, 0, 0), line1_start, line27_end)
    pygame.draw.line(screen, (0, 0, 0), line15_start, line2_end)
    pygame.draw.line(screen, (0, 0, 0), line15_start, line3_end)
    pygame.draw.line(screen, (0, 0, 0), line15_start, line4_end)
    pygame.draw.line(screen, (0, 0, 0), line15_start, line5_end)
    pygame.draw.line(screen, (0, 0, 0), line15_start, line6_end)
    pygame.draw.line(screen, (0, 0, 0), line15_start, line7_end)
    pygame.draw.line(screen, (0, 0, 0), line15_start, line8_end)
    pygame.draw.line(screen, (0, 0, 0), line15_start, line9_end)
    pygame.draw.line(screen, (0, 0, 0), line15_start, line10_end)
    pygame.draw.line(screen, (0, 0, 0), line15_start, line11_end)
    pygame.draw.line(screen, (0, 0, 0), line15_start, line12_end)
    pygame.draw.line(screen, (0, 0, 0), line15_start, line13_end)
    pygame.draw.line(screen, (0, 0, 0), line15_start, line15_end)
    pygame.draw.line(screen, (0, 0, 0), line15_start, line16_end)
    pygame.draw.line(screen, (0, 0, 0), line15_start, line17_end)
    pygame.draw.line(screen, (0, 0, 0), line15_start, line18_end)
    pygame.draw.line(screen, (0, 0, 0), line15_start, line19_end)
    pygame.draw.line(screen, (0, 0, 0), line15_start, line20_end)
    pygame.draw.line(screen, (0, 0, 0), line15_start, line21_end)
    pygame.draw.line(screen, (0, 0, 0), line15_start, line22_end)
    pygame.draw.line(screen, (0, 0, 0), line15_start, line23_end)
    pygame.draw.line(screen, (0, 0, 0), line15_start, line24_end)
    pygame.draw.line(screen, (0, 0, 0), line15_start, line25_end)
    pygame.draw.line(screen, (0, 0, 0), line15_start, line26_end)
    pygame.draw.line(screen, (0, 0, 0), line15_start, line27_end)
    pygame.draw.line(screen, (0, 0, 0), line22_start, line2_end)
    pygame.draw.line(screen, (0, 0, 0), line22_start, line3_end)
    pygame.draw.line(screen, (0, 0, 0), line22_start, line4_end)
    pygame.draw.line(screen, (0, 0, 0), line22_start, line5_end)
    pygame.draw.line(screen, (0, 0, 0), line22_start, line6_end)
    pygame.draw.line(screen, (0, 0, 0), line22_start, line7_end)
    pygame.draw.line(screen, (0, 0, 0), line22_start, line8_end)
    pygame.draw.line(screen, (0, 0, 0), line22_start, line9_end)
    pygame.draw.line(screen, (0, 0, 0), line22_start, line10_end)
    pygame.draw.line(screen, (0, 0, 0), line22_start, line11_end)
    pygame.draw.line(screen, (0, 0, 0), line22_start, line12_end)
    pygame.draw.line(screen, (0, 0, 0), line22_start, line13_end)
    pygame.draw.line(screen, (0, 0, 0), line22_start, line15_end)
    pygame.draw.line(screen, (0, 0, 0), line22_start, line16_end)
    pygame.draw.line(screen, (0, 0, 0), line22_start, line17_end)
    pygame.draw.line(screen, (0, 0, 0), line22_start, line18_end)
    pygame.draw.line(screen, (0, 0, 0), line22_start, line19_end)
    pygame.draw.line(screen, (0, 0, 0), line22_start, line20_end)
    pygame.draw.line(screen, (0, 0, 0), line22_start, line21_end)
    pygame.draw.line(screen, (0, 0, 0), line22_start, line22_end)
    pygame.draw.line(screen, (0, 0, 0), line22_start, line23_end)
    pygame.draw.line(screen, (0, 0, 0), line22_start, line24_end)
    pygame.draw.line(screen, (0, 0, 0), line22_start, line25_end)
    pygame.draw.line(screen, (0, 0, 0), line22_start, line26_end)
    pygame.draw.line(screen, (0, 0, 0), line22_start, line27_end)
    pygame.draw.line(screen, (0, 0, 0), line26_start, line2_end)
    pygame.draw.line(screen, (0, 0, 0), line26_start, line3_end)
    pygame.draw.line(screen, (0, 0, 0), line26_start, line4_end)
    pygame.draw.line(screen, (0, 0, 0), line26_start, line5_end)
    pygame.draw.line(screen, (0, 0, 0), line26_start, line6_end)
    pygame.draw.line(screen, (0, 0, 0), line26_start, line7_end)
    pygame.draw.line(screen, (0, 0, 0), line26_start, line8_end)
    pygame.draw.line(screen, (0, 0, 0), line26_start, line9_end)
    pygame.draw.line(screen, (0, 0, 0), line26_start, line10_end)
    pygame.draw.line(screen, (0, 0, 0), line26_start, line11_end)
    pygame.draw.line(screen, (0, 0, 0), line26_start, line12_end)
    pygame.draw.line(screen, (0, 0, 0), line26_start, line13_end)
    pygame.draw.line(screen, (0, 0, 0), line26_start, line15_end)
    pygame.draw.line(screen, (0, 0, 0), line26_start, line16_end)
    pygame.draw.line(screen, (0, 0, 0), line26_start, line17_end)
    pygame.draw.line(screen, (0, 0, 0), line26_start, line18_end)
    pygame.draw.line(screen, (0, 0, 0), line26_start, line19_end)
    pygame.draw.line(screen, (0, 0, 0), line26_start, line20_end)
    pygame.draw.line(screen, (0, 0, 0), line26_start, line21_end)
    pygame.draw.line(screen, (0, 0, 0), line26_start, line22_end)
    pygame.draw.line(screen, (0, 0, 0), line26_start, line23_end)
    pygame.draw.line(screen, (0, 0, 0), line26_start, line24_end)
    pygame.draw.line(screen, (0, 0, 0), line26_start, line25_end)
    pygame.draw.line(screen, (0, 0, 0), line26_start, line26_end)
    pygame.draw.line(screen, (0, 0, 0), line26_start, line27_end)


    # Dibujar los círculos
    pygame.draw.circle(screen, (0, 0, 0), circle_center, circle_radius)
    pygame.draw.circle(screen, (0, 0, 0), circle1_center, circle_radius)
    pygame.draw.circle(screen, (0, 0, 0), circle2_center, circle_radius)
    pygame.draw.circle(screen, (0, 0, 0), circle3_center, circle_radius)
    pygame.draw.circle(screen, (0, 0, 0), circle3_center, 40,2)
    pygame.draw.circle(screen, (0, 0, 0), circle4_center, circle_radius)
    pygame.draw.circle(screen, (0, 0, 0), circle5_center, circle_radius)
    pygame.draw.circle(screen, (0, 0, 0), circle6_center, circle_radius)
    pygame.draw.circle(screen, (0, 0, 0), circle7_center, circle_radius)
    pygame.draw.circle(screen, (0, 0, 0), circle8_center, circle_radius)
    pygame.draw.circle(screen, (0, 0, 0), circle9_center, circle_radius)
    pygame.draw.circle(screen, (0, 0, 0), circle9_center, 40,2)
    pygame.draw.circle(screen, (0, 0, 0), circle10_center, circle_radius)
    pygame.draw.circle(screen, (0, 0, 0), circle11_center, circle_radius)
    pygame.draw.circle(screen, (0, 0, 0), circle12_center, circle_radius)
    pygame.draw.circle(screen, (0, 0, 0), circle13_center, circle_radius)
    pygame.draw.circle(screen, (0, 0, 0), circle14_center, circle_radius)
    pygame.draw.circle(screen, (0, 0, 0), circle13_center, 40,2)
    pygame.draw.circle(screen, (0, 0, 0), circle15_center, circle_radius)
    pygame.draw.circle(screen, (0, 0, 0), circle16_center, circle_radius)
    pygame.draw.circle(screen, (0, 0, 0), circle17_center, circle_radius)
    pygame.draw.circle(screen, (0, 0, 0), circle18_center, circle_radius)
    pygame.draw.circle(screen, (0, 0, 0), circle19_center, circle_radius)
    pygame.draw.circle(screen, (0, 0, 0), circle20_center, circle_radius)
    pygame.draw.circle(screen, (0, 0, 0), circle20_center, 40,2)
    pygame.draw.circle(screen, (0, 0, 0), circle21_center, circle_radius)
    pygame.draw.circle(screen, (0, 0, 0), circle22_center, circle_radius)
    pygame.draw.circle(screen, (0, 0, 0), circle23_center, circle_radius)
    pygame.draw.circle(screen, (0, 0, 0), circle24_center, 40,2)
    pygame.draw.circle(screen, (0, 0, 0), circle24_center, circle_radius)
    pygame.draw.circle(screen, (0, 0, 0), circle25_center, circle_radius)
    pygame.draw.circle(screen, (0, 0, 0), circle26_center, circle_radius)
    pygame.draw.circle(screen, (0, 0, 0), circle27_center, circle_radius)
    pygame.draw.circle(screen, (0, 0, 0), circle27_center, 40,2)

    # Dibujar los textos en los círculos
    screen.blit(text0, text0_rect)
    screen.blit(text1, text1_rect)
    screen.blit(text2, text2_rect)
    screen.blit(text3, text3_rect)
    screen.blit(text4, text4_rect)
    screen.blit(text5, text5_rect)
    screen.blit(text6, text6_rect)
    screen.blit(text7, text7_rect)
    screen.blit(text8, text8_rect)
    screen.blit(text9, text9_rect)
    screen.blit(text10, text10_rect)
    screen.blit(text11, text11_rect)
    screen.blit(text12, text12_rect)
    screen.blit(text13, text13_rect)
    screen.blit(text14, text14_rect)
    screen.blit(text15, text15_rect)
    screen.blit(text16, text16_rect)
    screen.blit(text17, text17_rect)
    screen.blit(text18, text18_rect)
    screen.blit(text19, text19_rect)
    screen.blit(text20, text20_rect)
    screen.blit(text21, text21_rect)
    screen.blit(text22, text22_rect)
    screen.blit(text23, text23_rect)
    screen.blit(text24, text24_rect)
    screen.blit(text25, text25_rect)
    screen.blit(text26, text26_rect)
    screen.blit(text27, text27_rect)
    screen.blit(text28, text28_rect)
    screen.blit(text29, text29_rect)
    screen.blit(text30, text30_rect)
    screen.blit(text31, text31_rect)
    screen.blit(text32, text32_rect)


    # Actualizar la pantalla
    pygame.display.update()


