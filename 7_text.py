import pygame

pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 게임 이름 설정
pygame.display.set_caption("지훈`s GAME")

# FPS
clock = pygame.time.Clock()

# 배경 이미지 불러오기
background = pygame.image.load("D:\\jihoon_python\\python_game\\background.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("D:\\jihoon_python\\python_game\\character.png")
character_size = character.get_rect().size  # 이미지 크기
character_width = character_size[0]  # 캐릭터 가로크기
character_height = character_size[1]  # 캐릭터 세로크기
character_x_pos = screen_width / 2 - character_width / 2  # 화면 가로의 절반 크기에 캐릭터 위치
character_y_pos = screen_height - character_height  # 화면 세로 크기의 가장 아래에 캐릭터 위치

# 이동할 좌표
to_x = 0
to_y = 0

# 이동속도
character_speed = 0.5

# 적군 캐릭터
enemy = pygame.image.load("D:\\jihoon_python\\python_game\\obstacles.png")
enemy_size = enemy.get_rect().size  # 이미지 크기
enemy_width = enemy_size[0]  # 캐릭터 가로크기
enemy_height = enemy_size[1]  # 캐릭터 세로크기
enemy_x_pos = screen_width / 2 - enemy_width / 2  # 화면 가로의 절반 크기에 캐릭터 위치
enemy_y_pos = (screen_height / 2) - (enemy_height / 2)  # 화면 세로 크기의 가장 아래에 캐릭터 위치


# 폰트 정의
game_font = pygame.font.Font(None, 40)              # 폰트 객체 ( 폰트유형, 크기)

# 총 시간
total_time = 10

# 시간 계산
start_ticks = pygame.time.get_ticks()               # 시간 tick 받아옴


running = True  # 게임 진행중
while running:
    dt = clock.tick(144)  # 게임화면의 초당 프레임 수 설정
    print("fps : {0}".format(clock.get_fps()))

    for event in pygame.event.get():  # 키보드, 마우스 동작(=이벤트) 체크해주는 코드. 그 이벤트에 맞게 프로그램 실행시켜주는 역할
        if event.type == pygame.QUIT:  # 게임 창을 껐을 때
            running = False  # 게임 진행X

        if event.type == pygame.KEYDOWN:  # 키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:  # 캐릭터 왼쪽으로
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:  # 캐릭터 오른쪽으로
                to_x += character_speed
            elif event.key == pygame.K_UP:  # 캐릭터 위쪽으로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:  # 캐릭터 아래쪽으로
                to_y += character_speed

        if event.type == pygame.KEYUP:  # 방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    # 세로 경계값 처리
    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌 !")
        running = False

    screen.blit(background, (0, 0))  # 배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos))  # 캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))  # 적군 그리기


    # 타이머 넣기
    # 경과시간 계산 (초 단위로 표시)
    # 기본 시간 단위: ms
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000

    # 출력할 글자(시간정보) , True(고정), 글자 색상
    timer = game_font.render(str(int(total_time - elapsed_time)), True, (255,0,255))

    screen.blit(timer, (10,10))

    if total_time - elapsed_time < 0:
        print("TIME OVER")
        running = False

    pygame.display.update()  # 배경 채우기

pygame.time.delay(1500)

pygame.quit()  # 게임 종료