import pygame

pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 게임 이름 설정
pygame.display.set_caption("지훈`s GAME")

running = True # 게임 진행중
while running:
    for event in pygame.event.get(): # 키보드, 마우스 동작(=이벤트) 체크해주는 코드. 그 이벤트에 맞게 프로그램 실행시켜주는 역할
        if event.type == pygame.QUIT:                   # 게임 창을 껐을 때
            running = False                             # 게임 진행X


pygame.quit() # 게임 종료