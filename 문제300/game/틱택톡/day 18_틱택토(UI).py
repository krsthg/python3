from tkinter import * #tkinter: 파이썬 UI
from tkinter import messagebox #메시지 창 제공
import random as r    #난수 생성 함수 제공

#2. 버튼 만들기
def b(screen):
    b = Button(screen, padx=1, bg="whitesmoke", width=3, text="   ", font=("arial", 60, "bold"), relief="sunken", bd=10)
    return b

#6.리셋하기
def reset():    #Resets the game
    global r
    for i in range(3):
        for j in range(3):
            gb[i][j]["text"]=" "
            gb[i][j]["state"]=NORMAL
    a = r.choice(["o","x"])
#5. 이기는 수 함수 만들기
def win():
    for i in range(3): #i는 0부터 2까지 1씩 증가 반복
#가로로 이기는 수
        if gb[i][0]["text"] == gb[i][1]["text"] == gb[i][2]["text"] == r:
            messagebox.showinfo("게임종료", r+" 플레이어 승리")
            reset()
#세로로 이기는 수
        if gb[0][i]["text"] == gb[1][i]["text"] == gb[2][i]["text"] == r:
            messagebox.showinfo("게임종료", r + " 플레이어 승리")
            reset()
#대각선으로 이기는 수
    #0 4 8
    if gb[0][0]["text"] == gb[1][1]["text"] == gb[2][2]["text"] == r:
        messagebox.showinfo("게임종료", r + " 플레이어 승리")
        reset()
    #2 4 6
    if gb[0][2]["text"] == gb[1][1]["text"] == gb[2][0]["text"] == r:
        messagebox.showinfo("게임종료", r + " 플레이어 승리")
        reset()
#4. 알 교체 함수 만들기
def c():
    global r
    for i in ["o","x"]: #o혹은 x를 i에 대입
        if not(i==r): #현재 알이 i와 같지 않으면
            r=i #교체
            break #반복문 종료

# 3. 클릭 함수 만들기
def click(w, h):  # 클릭한 위치를 가져오기
    gb[w][h].config(text=r, state=DISABLED, disabledforeground=colour[r])
    win() #이기는수 함수 불러내기
    c() #알교체 함수 불러내기
    lable.config(text=r+ "님 플레이어 순서입니다.")

#게임 화면 설정
screen = Tk() #window 화면 만들기
screen.title("틱택토 게임기") #화면 이름

#알 만들기
r=r.choice( ["o","x"])
colour = {"o":"DodgerBlue4", "x":"indian red"} #tkinter colour 색상 설정 #RoyalBlue4 DodgerBlue4

gb= [[],[],[]] #2차원 배열

#2. 2차원 배열에 버튼 넣기
for i in range(3): #가로단위
    for j in range(3): #세로단우;
        gb[i].append(b(screen))
        gb[i][j].config(command=lambda row=i, col=j:click(row,col))
        gb[i][j].grid(row=i, column=j)

#텍스트 만들기
lable = Label(text=r+"님 플레이어 순서입니다.", font = ("arial",15,"bold"))
             #text="(내용입력)"           , font=("(글꼴명)",글자크기, "(굵기)")

#텍스트[레이블] 배치하기[4번째 행[가로]에 1번째 열[세로], 세로 3칸을 병합[합치기]]
lable.grid(row=3, column=0, columnspan=3)

screen.mainloop()
