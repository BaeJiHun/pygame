import pygame
############################################################

# 기본 초기화 ( 반드시 해야 하는 것)
pygame.init()

# 화면 크기 설정
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# 게임 이름 설정
pygame.display.set_caption("지훈`s GAME")

# FPS
clock = pygame.time.Clock()
############################################################

# 1. 사용자 게임 초기화(배경화면, 게임이미지, 좌표, 이동속도, 폰트 등)






# 이벤트 루프
running = True  # 게임 진행중
while running:
    dt = clock.tick(30)  # 게임화면의 초당 프레임 수 설정
    print("fps : {0}".format(clock.get_fps()))

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():  # 키보드, 마우스 동작(=이벤트) 체크해주는 코드. 그 이벤트에 맞게 프로그램 실행시켜주는 역할
        if event.type == pygame.QUIT:  # 게임 창을 껐을 때
            running = False  # 게임 진행X


    # 3. 게임 캐릭터 위치 정의


    # 4. 충돌 처리


    # 5. 화면에 그리기


    pygame.display.update()  # 배경 채우기 (반드시 해야할 것)

pygame.time.delay(1500)

pygame.quit()  # 게임 종료