import tkinter
import pygame

#音楽再生
def main():
    # 音楽用のモジュールを初期化
    pygame.mixer.init()
    # 音声ファイルの読み込み
    pygame.mixer.music.load("sound/kokorozasi.mp3")
    # 音声ファイルの再生（無限ループ）
    pygame.mixer.music.play(-1)
main()

# 解読関数
def decole_line(event):
    global current_line, bgimg, lcharimg, ccharimg, rcharimg
    if current_line >= len(scenario):
        return
    # 1行読み込む
    line = scenario[current_line]
    current_line = current_line + 1
    line = line.replace("\\n", "\n").strip()
    params = line.split(" ")
    se1 = pygame.mixer.Sound("sound/kendekiru.wav")
    se2 = pygame.mixer.Sound("sound/tume.wav")
    se3 = pygame.mixer.Sound("sound/taoreru.wav")
    se4 = pygame.mixer.Sound("sound/wareru.wav")
    # 分岐
    if line[0] != "#":
        message["text"] = line
        return
    elif params[0] == "#back":
        canvas.delete("all")
        bgimg = tkinter.PhotoImage(file=params[1])
        canvas.create_image(450, 230, image=bgimg)
    elif params[0] == "#putChar":
        if params[2] == "L":
            canvas.delete("left")
            lcharimg = tkinter.PhotoImage(file=params[1])
            lcharimg = lcharimg.subsample(2, 2)
            canvas.create_image(200, 160, image=lcharimg, tag="left")
        elif params[2] == "R":
            canvas.delete("right")
            rcharimg = tkinter.PhotoImage(file=params[1])
            rcharimg = rcharimg.subsample(2, 2)
            canvas.create_image(700, 160, image=rcharimg, tag="right") 
        else:
            canvas.delete("center")
            ccharimg = tkinter.PhotoImage(file=params[1])
            ccharimg = ccharimg.subsample(2, 2)
            canvas.create_image(450, 160, image=ccharimg, tag="center") 

    elif params[0] == "#music1":    #志は死なない：ベース常音楽
            pygame.mixer.music.load("sound/kokorozasi.mp3")
            pygame.mixer.music.play(-1)
    elif params[0] == "#music2":    #剣の舞：戦闘時音楽
            pygame.mixer.music.load("sound/turuginomai.mp3")
            pygame.mixer.music.play(-1)
    elif params[0] == "#music3":    #透き通る風の中で：エンディング音楽
            pygame.mixer.music.load("sound/sukitooru.mp3")
            pygame.mixer.music.play(-1)
    elif params[0] == "#music4":    #Night_Shade_Story：緊迫感のある音楽
            pygame.mixer.music.load("sound/nightshadestory.mp3")
            pygame.mixer.music.play(-1)
    elif params[0] == "#music5":    #茶屋にて：日常シーン（家）
            pygame.mixer.music.load("sound/tyayanite.mp3")
            pygame.mixer.music.play(-1)
    elif params[0] == "#music6":    #花よ川よこの大地よ：昔話
            pygame.mixer.music.load("sound/hanayokawayo.mp3")
            pygame.mixer.music.play(-1)
    elif params[0] == "#music7":    #todays_progress：日常シーン（学校）
            pygame.mixer.music.load("sound/todaysprogress.mp3")
            pygame.mixer.music.play(-1)
    elif params[0] == "#music8":    #Vague_Anxiety：不穏なシーン
            pygame.mixer.music.load("sound/vagueanxiety.mp3")
            pygame.mixer.music.play(-1)
    elif params[0] == "#music9":    #流星群の夜：物悲しいシーン
            pygame.mixer.music.load("sound/ryuseigun.mp3")
            pygame.mixer.music.play(-1)
    elif params[0] == "#music10":    #天地に咲く花：静子のシーン
            pygame.mixer.music.load("sound/tentinisakuhana.mp3")
            pygame.mixer.music.play(-1)
    elif params[0] == "#music11":    #moment：育江のシーン
            pygame.mixer.music.load("sound/moment.mp3")
            pygame.mixer.music.play(-1) 
    elif params[0] == "#music12":    #効果音：剣で斬る
            se1.play(0)
    elif params[0] == "#music13":    #効果音：爪で刺す
            se2.play(0)
    elif params[0] == "#music14":    #効果音：倒れる
            se3.play(0)
    elif params[0] == "#music15":    #効果音：割れる
            se4.play(0)

    elif params[0] == "#branch":
        message.unbind("<Button-1>")
        btn = tkinter.Button(text=params[2], width=20)
        branch.append(btn)
        btn["command"] = lambda : jump_to_line(int(params[1])-1)
        btn.place(x=300, y=60+int(params[1])*60)
        jumplabel.append(params[3])
        if params[4] == "n":
            return
    elif params[0] == "#jump":
        label = params[1].strip()
        # ジャンプ先を探す
        for l in range(len(scenario)):
            if scenario[l].strip() == "## " + label:
                current_line = l
                decole_line(None)
                return                  
    elif params[0].strip() == "#end":
        message["text"] = "おしまい"
        message.unbind("<Button-1>")
        current_line = 999999999
    # 再帰呼び出し
    decole_line(None)

# ジャンプ関数
def jump_to_line(branchID):
    global current_line
    # ボタンを消す
    for btn in branch:
        btn.place_forget()
        btn.destroy()
    branch.clear()
    label = jumplabel[branchID]
    jumplabel.clear()
    message.bind("<Button-1>", decole_line)
    # ジャンプ先を探す
    for l in range(len(scenario)):
        if scenario[l].strip() == "## " + label:
            current_line = l
            decole_line(None)
            return
    decole_line(None)  
 
# ウィンドウ作成
root = tkinter.Tk()
root.title("面影の君は")
root.minsize(900, 460)
root.option_add("*font", ["メイリオ", 14])
# キャンバス作成
canvas = tkinter.Canvas(width=900, height=460)
canvas.place(x=0, y=0)


# メッセージエリア
message = tkinter.Label(width=70, height=5, wraplength=840,
    bg="white", justify="left", anchor="nw")
message.place(x=28, y=297)
message["text"]= "クリックしてスタートしてください"

# ファイル読み込み
scenario = []
file = open("img/scenario.txt", "r", encoding="utf-8")
while True:
    line = file.readline()
    scenario.append(line)
    if not line:
        file.close()
        break

# 現在の行数
current_line = 0
# イベント設定
message.bind("<Button-1>", decole_line)
# 画像
bgimg = tkinter.PhotoImage(file="img/back0-title.png")
canvas.create_image(450, 280, image=bgimg)
lcharimg = None
ccharimg = None
rcharimg = None
# 選択肢
branch = []
jumplabel = []

root.mainloop()