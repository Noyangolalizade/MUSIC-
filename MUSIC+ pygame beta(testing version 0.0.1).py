import pygame
import webbrowser

pygame.init()

screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption('MUSIC +')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
screen.fill(("gray22"))

sampadlogo1 = pygame.image.load('sampadlogo.png')

sampadlogo1 = pygame.transform.scale(sampadlogo1,(sampadlogo1.get_width() // 10,sampadlogo1.get_height() // 10))

tutorial_keys = pygame.image.load('t.keys.png')
tutorial_keys = pygame.transform.scale(tutorial_keys,(tutorial_keys.get_width() // 1.1,tutorial_keys.get_height() // 1.1))

github = pygame.image.load('github.jpg')

github = pygame.transform.scale(github,(github.get_width() // 5,github.get_height() // 5))

chat = pygame.image.load('chat.jpg')

chat = pygame.transform.scale(chat,(chat.get_height()//5.7,chat.get_width()//6.2))

about = pygame.image.load('about.jpg')

about = pygame.transform.scale(about,(about.get_height()//3.5,about.get_width()//3))

test = pygame.image.load('test.png')

test = pygame.transform.scale(test,(test.get_height()//0.5,test.get_width()//3))

chrome = pygame.image.load('chromevent.png')

chrome = pygame.transform.scale(chrome,(chrome.get_height()//0.27,chrome.get_width()//7))

chrome2 = pygame.image.load('o.png')

chrome2 = pygame.transform.scale(chrome2,(chrome2.get_height()//0.5,chrome2.get_width()//2))

chrome3 = pygame.image.load('haha.png')

chrome3 = pygame.transform.scale(chrome3,(chrome3.get_height()//0.2,chrome3.get_width()//7))

chrome4= pygame.image.load('img.png')

chrome4 = pygame.transform.scale(chrome4,(chrome4.get_height()//1,chrome4.get_width()//5))

chrome5= pygame.image.load('img2.png')

chrome5 = pygame.transform.scale(chrome5,(chrome5.get_height()//1.3,chrome5.get_width()//4))

event= pygame.image.load('event.png')

event = pygame.transform.scale(event,(event.get_height()//1.1,event.get_width()//1.8))

event2= pygame.image.load('eftkhar.png')

event2 = pygame.transform.scale(event2,(event2.get_height()//2,event2.get_width()//3.5))

event3= pygame.image.load('eftkhr.png')

event3 = pygame.transform.scale(event3,(event3.get_height()//0.5,event3.get_width()//1.5))

download = pygame.image.load("download.jpg")

download = pygame.transform.scale(download,(download.get_height()//16,download.get_width()//18))

sampadx = 870
sampady = 468

tkeysx = 10
tkeysy = 50

githubx = 900
githuby = -15

chatx = 830
chaty = 15

testx = 830
testy = 90

chromx = 0
chromy = 430

chromx2 = 140
chromy2 = 510

chromx3 = 140
chromy3 = 440

chromx4 = 250
chromy4 = 230

eventx = 695
eventy = 435

eventx2 = 670
eventy2 = 24.5

event3x = -220
event3y = -70

downloadx = 750
downloady = 16.5

github_rect = github.get_rect(topleft=(githubx, githuby))

chat_rect = chat.get_rect(topleft=(chatx,chaty))

sampad_rect = sampadlogo1.get_rect(topleft=(sampadx,sampady))

chrome_rect = chrome2.get_rect(topleft=(chromx2,chromy2))

eft_rect = event2.get_rect(topleft=(eventx2,eventy2))

download_rect = download.get_rect(topleft=(downloadx,downloady))

def somethings():
    screen.blit(sampadlogo1,(sampadx,sampady))
    screen.blit(tutorial_keys,(tkeysx,tkeysy))
    screen.blit(github,(githubx,githuby))
    screen.blit(chat,(chatx,chaty))
    screen.blit(chrome,(chromx,chromy))
    screen.blit(chrome2,(chromx2,chromy2))
    screen.blit(chrome3,(chromx3,chromy3))
    screen.blit(event,(eventx,eventy))
    screen.blit(event2,(eventx2,eventy2))
    screen.blit(download,(downloadx,downloady))
    pygame.draw.rect(screen, "black", (0, 50, 20, 147))
 
def texts():
    x5 = 150    
    y5 = 300
    x52 = 120
    y52 = 350
    font = pygame.font.SysFont("Bookman Old Style", 40, "bold")
    
    # white bottons--------------------
    
    text = font.render("x", True, "white")
    screen.blit(text, (150, 300))
    
    text = font.render("x", True, "white")
    screen.blit(text, (x5+60, y5))
    
    text = font.render("x", True, "white")
    screen.blit(text, (x5+180, y5))
    
    text = font.render("x", True, "white")
    screen.blit(text, (x5+243, y5))    
    
    text = font.render("x", True, "white")
    screen.blit(text, (x5+303, y5))    
    
    text = font.render("x", True, "white")
    screen.blit(text, (x5+425, y5))    
    
    text = font.render("x", True, "white")
    screen.blit(text, (x5+485, y5))    
    
    text = font.render("x", True, "white")
    screen.blit(text, (x5+608, y5))    
    
    text = font.render("x", True, "white")
    screen.blit(text, (x5+668, y5))
    
    text = font.render("x", True, "white")
    screen.blit(text, (x5+728, y5))
    
    
    
    # black bottons---------------------
    
    text = font.render("x", True, "black")
    screen.blit(text, (x52, y52))
    
    text = font.render("x", True, "black")
    screen.blit(text, (x52+60, y52))
    
    text = font.render("x", True, "black")
    screen.blit(text, (x52+120, y52))
    
    text = font.render("x", True, "black")
    screen.blit(text, (x52+180, y52))

    text = font.render("x", True, "black")
    screen.blit(text, (x52+240, y52))

    text = font.render("x", True, "black")
    screen.blit(text, (x52+300, y52))

    text = font.render("x", True, "black")
    screen.blit(text, (x52+360, y52))

    text = font.render("x", True, "black")
    screen.blit(text, (x52+420, y52))
    
    text = font.render("x", True, "black")
    screen.blit(text, (x52+480, y52))
    
    text = font.render("x", True, "black")
    screen.blit(text, (x52+480, y52))
    
    text = font.render("x", True, "black")
    screen.blit(text, (x52+540, y52))
    
    text = font.render("x", True, "black")
    screen.blit(text, (x52+610, y52))
    
    text = font.render("x", True, "black")
    screen.blit(text, (x52+670, y52))
    
    text = font.render("x", True, "black")
    screen.blit(text, (x52+730, y52))

    text = font.render("x", True, "black")
    screen.blit(text, (x52+790, y52))
    
    screen.blit(text, (x5, y5))
    
x = 900
y = 61
z = 250
x2 = 876
x3 = 100
pygame.draw.rect(screen, "white", (x, z, 50, 150))
pygame.draw.rect(screen, "white", (x-y, z, 50, 150))
pygame.draw.rect(screen, "white", (x-2*y, z, 50, 150))
pygame.draw.rect(screen, "white", (x-3*y, z, 50, 150))
pygame.draw.rect(screen, "white", (x-4*y, z, 50, 150))
pygame.draw.rect(screen, "white", (x-5*y, z, 50, 150))
pygame.draw.rect(screen, "white", (x-6*y, z, 50, 150))
pygame.draw.rect(screen, "white", (x-7*y, z, 50, 150))
pygame.draw.rect(screen, "white", (x-8*y, z, 50, 150))
pygame.draw.rect(screen, "white", (x-9*y, z, 50, 150))
pygame.draw.rect(screen, "white", (x-10*y, z , 50, 150))
pygame.draw.rect(screen, "white", (x-11*y, z , 50, 150))
pygame.draw.rect(screen, "white", (x-12*y, z, 50, 150))
pygame.draw.rect(screen, "white", (x-13*y, z, 50, 150))
    
pygame.draw.rect(screen, "black", (x2, z, 35, x3))
pygame.draw.rect(screen, "black", (x2-60, z, 35, x3))
pygame.draw.rect(screen, "black", (x2-120, z, 35, x3))
pygame.draw.rect(screen, "black", (x2-243, z, 35, x3))
pygame.draw.rect(screen, "black", (x2-303, z, 35, x3))
pygame.draw.rect(screen, "black", (x2-425, z, 35, x3))
pygame.draw.rect(screen, "black", (x2-485, z, 35, x3))
pygame.draw.rect(screen, "black", (x2-550, z, 35, x3))
pygame.draw.rect(screen, "black", (x2-670, z, 35, x3))
pygame.draw.rect(screen, "black", (x2-730, z, 35, x3))
    
somethings()
texts()
    
show_image = False
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if github_rect.collidepoint(event.pos):
                webbrowser.open("https://github.com/Noyangolalizade/MUSIC-") 
            if chat_rect.collidepoint(event.pos):
                webbrowser.open("musicc.nikan.noyan@gmail.com") 
            if sampad_rect.collidepoint(event.pos):
                webbrowser.open("https://sampad.gov.ir")
            if download_rect.collidepoint(event.pos):
                webbrowser.open("https://github.com/Noyangolalizade/MUSIC-/archive/refs/heads/main.zip")
            if chrome_rect.collidepoint(event.pos):
                webbrowser.open("https://docs.google.com/forms/d/1k_8-Jjv1hxAN4qs2x7mivrYQzTRWc_XUMK0G-Cx0YrA")  
                show_image = True
                if show_image:
                    screen.blit(chrome4,(chromx4,chromy4))
                    screen.blit(chrome5,(320,360))
            show_image2 = False
            if eft_rect.collidepoint(event.pos):
                show_image2 = True
                if show_image2:
                    screen.blit(event3,(event3x,event3y))
                if show_image2:
                    show_image2 = False
    

    
    pygame.display.update()

