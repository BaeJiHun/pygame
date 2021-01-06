import pygame

pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 게임 이름 설정
pygame.display.set_caption("지훈`s GAME")

# 배경 이미지 불러오기
background = pygame.image.load("D:/jihoon_python/python_game/background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("D:/jihoon_python/python_game/character.png")
character_size = character.get_rect().size   # 이미지 크기
character_width = character_size[0]         # 캐릭터 가로크기
character_height = character_size[1]       # 캐릭터 세로크기
character_x_pos = screen_width / 2 - character_width / 2   # 화면 가로의 절반 크기에 캐릭터 위치
character_y_pos = screen_height - character_height      # 화면 세로 크기의 가장 아래에 캐릭터 위치

running = True # 게임 진행중
while running:
    for event in pygame.event.get(): # 키보드, 마우스 동작(=이벤트) 체크해주는 코드. 그 이벤트에 맞게 프로그램 실행시켜주는 역할
        if event.type == pygame.QUIT:                   # 게임 창을 껐을 때
            running = False                             # 게임 진행X

    screen.blit(background, (0,0))          # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update()                 # 배경 채우기

pygame.quit() # 게임 종료