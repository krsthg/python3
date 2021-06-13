import pygame #파이게임 파일 불러오기
from pygame.locals import QUIT, Rect, KEYDOWN, K_UP, K_LEFT, K_RIGHT, K_DOWN
                        # 종료, 직각, 키 종료,    위,   왼족,   오른쪽,   아래 방향키
import random #랜덤 파일 불러오기
import sys #시스템 파일 불러오기

pygame.init()   #파이게임 초기값
screen = pygame.display.set_mode((700,700)) #화면 크기 설정
FPS = pygame.time.Clock() #화면 프레임 설정
score = 0 #점수 변수
food = [] #음식 리스트 선언
snake = [] #뱀 고리 리스트 선언
(w,h) = (35,35) #가로길이, 세로길이 => 튜플 선언
gomessage = 0
def fp(): #음식생성 함수 선언
    while True: #무한반복
        l = (random.randint(0,w-1), random.randint(0,h-1)) #음식이 생성되는 위치 랜덤으로 설정
        if l in food or l in snake: #만약 위치에 음식이나 뱀이 있으면
            continue #while 다시 실행
        else: #위치에 음식이나 뱀이 없으면
            food.append(l) #음식리스트에 해당위치 추가
            break #while 끝내기

def fm(l): #음식이동 함수 선언
    i = food.index(l) #해당 위치에 음식찾기
    del food[i] #해당 위치 음식 삭제
    fp() #음식생성함수 호출(새로운 음식 생성)

def draw(scorep, gomessage): #그리기 함수 선언
    screen.fill((255,255,255)) #화면 색

    for food2 in food: # 음식2에 음식이 있는만큼 반복
        pygame.draw.ellipse(screen,(0,0,255), Rect(food2[0]*20, food2[1]*20,20,20))
        # 타원 그리기(화면이동, (컬러[RGB]), 타원(x축, y축, 가로크기, 세로크기))

    for body in snake: #뱀이 몸에 닿으면
        pygame.draw.rect(screen,(0,0,0), Rect(body[0]*20, body[1]*20,20,20))
        # 사각형 그리기(화면이름, (컬러[RGB]), 사각형(x축, y축, 가로크기, 세로크기))

    if scorep != None: #점수판에 내용이 있으면
        screen.blit(scorep,(10,10)) #x,y 좌표 표기

    if gomessage: #게임종료메세지에 내용이 있으면
        gomessage = font.render("Game Over [Score:"+str(score)+"]", True,(0,0,0))
        screen.blit(gomessage, (250, 350))  # 화면에 게임종료메세지 띄우기

    pygame.display.update() #화면 업데이트

font = pygame.font.SysFont("Droid Sans Mono", 30) #글골 ,글자크기
key = K_UP #아래키
gameover = False #게임종료 스위치
snake.append((int(w/2), int(h/2))) #뱀을 화면 가운데에서 시작


for j in range(40): #30개의 음식 생성
    fp() #음식생성 함수 호출

while True: #계속 반복하기
    for move in pygame.event.get(): #파이게임에 이벤트가 있다면
        if move.type ==QUIT: #이벤트가 나가는 거면
            pygame.quit() #파이게임 나가기
            sys.exit() #시스템 종료
        elif move.type == KEYDOWN: #키를 눌렀다면
            key = move.key

    if not gameover:
        if key == K_LEFT: #만약 왼쪽 키를 눌렀으면
            head = (snake[0][0]-1, snake[0][1])
        elif key == K_RIGHT: #만약 오른쪽 키를 눌렀으면
            head = (snake[0][0]+1, snake[0][1])
        elif key == K_UP: #만약 위쪽 키를 눌렀으면
            head = (snake[0][0],snake[0][1]-1)
        elif key == K_DOWN: #만약 아래쪽 키를 눌렀으면
            head = (snake[0][0], snake[0][1]+1)

        if head in snake or head[0] < 0 or head[0] >= h or head[1] <0 or head[1] >=w: #뱀 몸에 닿았거나 화면 밖으로 나가면
            gameover = True #게임 종료

        snake.insert(0,head) #뱀 머리 추가

        if head in food: #만약 머리가 음식에 닿았다면
            fm(head) #새로운 음식 추가
            score+=1 #1점 추가

        else: #아니면
            snake.pop() #리스트내 가장 뒤에있는 항목 제거
        scorep = font.render("Score:" + str(score), True, (0, 0, 0))

    draw(scorep,gomessage) #그리기 함수 호출
    k = score // 10 #점수를 10으로 나눈 몫 = k
    FPS.tick(5+5*k) #프레임이 증가 => 속도 증가
