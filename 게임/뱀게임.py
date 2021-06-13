#1. 게임에 필요한 라이브러리를 import
import pygame #파이게임 파일 불러오기[임포트]
from pygame.locals import QUIT, Rect, KEYDOWN, K_UP, K_LEFT, K_RIGHT, K_DOWN
                  #종료, 직각, 키 종료,    위,   왼족,   오른쪽,   아래 방향키
import random #랜덤 파일 불러오기[임포트]
import sys #시스템 파일 불러오기[임포트]

#2. 게임에 필요한 기본설정
pygame.init() #파이게임 초기값
screen = pygame.display.set_mode((1000,1000)) #화면구성
FPS = pygame.time.Clock() #프레임에 파이게임 시간 설정
#FPS(Frame Per Second): 초당 프레임

food = []   #여러개 음식을 저장할 리스트
snake = []  #여러개 뱀 꼬리를 저장할 리스트
(w, h) = (50,50) #가로길이, 세로길이 #튜플선언

    #배경넣기
배경 = pygame.image.load("B2.jpg")

#     #배경 소리 넣기
# pygame.mixer.music.load("M.mp3")
# pygame.mixer.music.play(-1)

#3. 함수 만들기

    #1. 음식함수: 뱀이 음식을 먹었을때 새로운 음식추가, 혹은 게임시작시 음식 추가
def 음식생성(): #임의의 장소에 음식을 배치하는 함수를 선언
    while True: #무한반복
        위치 = (random.randint(0,w-1), random.randint(0,h-1))
                #0~49
        if 위치 in food or 위치 in snake: #해당 위치에 음식이나 뱀이 있으면
            continue #while 다시 실행
        else: #해당위치에 음식이나 뱀이 없으면
            food.append(위치) #음식리스트에 해당위치 추가
            break #while 끝내기

    #2.음식이동 함수: 뱀이 음식을 먹었을때
def 음식이동(위치):
    i = food.index(위치) #해당 위치에 음식찾기
    del food[i] #해당 위치에 음식삭제
    음식생성() #음식생성 함수 호출[새로운 음식 생성]
    #3.그리기 함수
def 그리기(점수판, 게임종료메세지):
    # screen.fill((0,0,0)) #검정색으로 칠하기

    #4. 음식 그리기
    for food2 in food: #리스트내 갯수만큼 반복
        pygame.draw.ellipse(screen, (29, 100, 161),Rect(food2[0]*20, food2[1]*20,20,20))
                #타원 그리기(화면이동, (컬러[RGB]), 타원(x축, y축, 가로크기, 세로크기))
    #5. 뱀 그리기
    for body in snake:
        pygame.draw.rect(screen,(220,168, 85), Rect(body[0]*20,body[1]*20,20,20))
                #사각형 그리기(화면이름, (컬러[RGB]), 사각형(x축, y축, 가로크기, 세로크기))

    # 점수 그리기
    if 점수판 != None:  # 점수에 내용이 있으면
        screen.blit(점수판, (10, 10))  # x좌표, y좌표 표기

    #게임종료 메세지
    if 게임종료메세지 != None: #게임종료메세지가 내용이 있으면
        게임종료메세지 = 긁.render("GAME OVER [Score: " + str(score) + "]", True, (29, 100, 161))
        screen.blit(게임종료메세지, (300, 500))

    pygame.display.update() #화면 업데이트하기

#4. 게임 실행
긁 = pygame.font.SysFont("Cooper Black",30) #글꼴, 글자크기
key = K_DOWN #아래키
gameover = False #게임종료 스위치
snake.append((int(w/2), int(h/2))) #뱀을 화면 가운데 위치
score = 0

for j in range(30): #30개의 음식생성
    음식생성()

while True: #계속 반복하기
    screen.blit(배경,(0,0))
    #키보드 동작하기
    for 동작 in pygame.event.get(): #파이게임 이벤트[동작]가 있을경우
        if 동작.type == QUIT: #이벤트가 종료이면
            pygame.quit() #파이게임 종료
            sys.exit() #시스템[모든코드] 종료
        elif 동작.type == KEYDOWN: #키를 눌렀을때
            key = 동작.key

    #키를 눌렀을때
    if not gameover : #게임종료가 False 이면
        if key == K_LEFT:
            head = (snake[0][0]-1,snake[0][1])
        elif key == K_RIGHT:
            head = (snake[0][0]+1, snake[0][1])
        elif key == K_UP:
            head = (snake[0][0], snake[0][1]-1)
        elif key == K_DOWN:
            head = (snake[0][0], snake[0][1]+1)

        #뱀 몸에 닿았을때 혹은 화면 밖으로 나갔을때 게임 종료
        if head in snake or head[0] < 0 or head[0] >= w or head[1] <0 or head[1] >= h:
            gameover = True

        #뱀 머리 추가
        snake.insert(0,head)

        #음식을 먹었을때 꼬리 추가 아니면 추가 X
        if head in food: #만약 머리가 음식에 닿았을때
            음식이동(head) #새로운 음식추가
            #1점 추가
            score += 1

        else:
            snake.pop() #리스트내 가장 뒤에있는 항목제거
        # 게임종료메세지 = 긁.render(" ", True,(29, 100, 161)) #공백
        점수판 = 긁.render("Score: "+str(score), True,(29, 100, 161))

    그리기(점수판,게임종료메세지)
    k = score // 10
    FPS.tick(5+5*k)
