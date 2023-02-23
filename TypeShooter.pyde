 
def setup(): 
    global stageNum 
    global space, pos, speed, StartButton, HowToPlay, title
    
    stageNum = 0 
    
    StartButton = loadImage("startbutton.png") 
    HowToPlay = loadImage("howtoplay.png") 
    title = loadImage("title.png") 
    
    global player1, player1w, player1h, space, pos, speed
    global totalNum, x, y, w, h, dx, dy, img, data
    global alive 
    global letterCnt, wordIdx
    global textcolor
    global rand_index #data 
    global score 
    global lives 
    global f #font 
    global wordList    
    global gameoverimg, retryimg, yesimg, noimg
    
    #gameover 
    gameoverimg = loadImage("gameover.png") 
    retryimg = loadImage("retry.png") 
    yesimg = loadImage("yesbutton.png") 
    noimg = loadImage("nobutton.png") 
    
    f = loadFont("font.vlw") 

    
    score = 0 
    lives = 3 
    
    #variables for keyPressed
    letterCnt = 0 
    wordIdx = ''

    #variables for GAMEPLAY
    size(800, 850) 
    space = loadImage("space.png") 
    pos = 0 
    speed = 3
    
    player1 = loadImage("player_1.png")
    player1w = 200*1.2
    player1h = 90*1.2
    

    #wordIdx 
    wordList = ['asteroid', 'battleship', 'coffee', 'dynamite', 'earbobs', 'fighter', 'garden', 'hungry', 'instrumental', 'jet', 'keyboard', 'listen', 'minecraft', 'nougat', 'optimal', 'practice', 'quest', 'rocket', 'space', 'tracking', 'universe', 'victory', 'weapon', 'xerox', 'yahoo', 'zombies']
    data = []

    
    totalNum = 10 
    
    alive = [] 
    img   = [] 
    x     = [] 
    y     = [] 
    w     = [] 
    h     = [] 
    dx    = [] 
    dy    = [] 
    
    for i in range(totalNum): 
        scale = random(0.15, 0.25) 
        img.append(loadImage("Enemy.png")) 
        w.append(img[i].width * scale) 
        h.append(img[i].height * scale)  
        x.append(random(0, width - w[i])) 
        y.append(random(-200, -50)) 
        dx.append(random(0.1, 1)) 
        dy.append(random(0.5, 0.7)) 
        alive.append(True) 
        data.append(wordList[int(random(26))])

                    

def draw(): 
    global pos, space, speed, lives, stageNum 
    
    image(space, 0, pos , width*1.15, height)
    image(space, 0, pos-height, width*1.15, height)
    
       
    pos = pos + speed
    if (pos >= height):
        pos = 0

    if stageNum == 0: 
        drawStartScreen()
    elif stageNum == 1 and lives != 0: 
        drawGamePlay()
    else: 
        stageNum = 2 
    
    if stageNum == 2: 
        drawGameOver()
        
    
def drawGamePlay(): 
    global textcolor, lives, score, wordIdx 
    
    #DISPLAY ENEMY SHIPS     
    for i in range(totalNum): 
        if (alive[i] == True): 
            image(img[i], x[i], y[i], w[i], h[i])
            y[i] += dy[i] 
            
            if y[i] > height: 
                lives = lives - 1 
                y[i] = -100 
                alive[i] = False 
        
            #display text on enemy ships#USE TextWidth()
            # battleship --> batt l eship 
            #     ^
            # if i == wordIdx: 
                #[0:LetterCnt] 
                #textcolor 
                #text statement 
                #text width
                #[letterCnt:] 
                #textcolor 
                #text statement 
                #text width 

            #if letterCnt == 0     
            textcolor = fill(0, 255, 0)
            textAlign(CENTER) 
            textFont(f) 
            textSize(22) 
            text(str(data[i]), x[i] + w[i]/2, y[i] + h[i]/2)
 
            
            #DISPLY SCORE 
            fill(255) 
            textSize(18) 
            text("Score: " + str(int(score)), 600, 790)

            #Display Lives 
            fill (255) 
            textSize(18) 
            text("Lives: " + str(int(lives)), 100, 790)
            

            

    
    #display player1 
    image(player1, width/2 - player1h, height - player1h, player1w, player1h) 

    
def drawGameOver(): 
    global gameoverimg, score
    image(gameoverimg, (gameoverimg.width*1.25)/8, height/9, 600, 600) 
    image(retryimg, retryimg.width - width/2, 300, 350, 350) 
    image(yesimg, 225, 400, 250, 250) 
    image(noimg, 350, 400, 250, 250)
    
    textcolor = fill(255)
    textAlign(CENTER) 
    textFont(f) 
    textSize(22) 
    text("Total Score: " + str(int(score)), width/2, height/4) 
    
def drawStartScreen(): 
    global pos
    #startbutton 
    image(StartButton, width/5, height/2.5, 500, 200) 
    #title 
    image(title, width - 750, -100, 700, 700) 
    image(HowToPlay, 100, 400, 600, 600) 
    
    textcolor = fill(255)
    textAlign(CENTER) 
    textFont(f) 
    textSize(11) 
    text("Hint: Words are repetitive so you might have to type the same words twice or even three times!", width/2, 800) 
    
    textcolor = fill(255)
    textAlign(CENTER) 
    textFont(f) 
    textSize(14) 
    text("You have 3 Lives, Make it Count!", width/2, 820) 
    
    textcolor = fill(255)
    textAlign(CENTER) 
    textFont(f) 
    textSize(14) 
    text("Click the Start button to begin.", width/2, 550) 
    
    textcolor = fill(255)
    textAlign(CENTER) 
    textFont(f) 
    textSize(14) 
    text("If you mistype, you'll have to type the whole word again!", width/2, 770) 
    
    
    
def keyPressed(): 
    global letterCnt, data, wordIdx, rand_index, y, h, score, lives, stageNum 
     
    if letterCnt == 0: 
        for j in range(len(data)):
            if key == data[j][0:1]: 
                letterCnt = 1
                wordIdx = j
                print "New word:", letterCnt, wordIdx, data[j]
                textcolor = fill(255)
                textAlign(CENTER) 
                textFont(f) 
                textSize(22) 
                text(((data[j])), width/2 - player1h, 800) 

    
    else:
        if key == data[wordIdx][letterCnt:letterCnt + 1]: 
            letterCnt = letterCnt + 1 
            textcolor = fill(255)
            textAlign(CENTER) 
            textFont(f) 
            textSize(22) 
            text(((data[wordIdx])), width/2 - player1h,800) 
            
            if key == data[wordIdx][len(data[wordIdx]) - 1:len(data[wordIdx])]: 
                letterCnt = 0 
                y[wordIdx] = -500
                x[wordIdx] = (random(0, width - w[wordIdx]))
                dy[wordIdx] += 0.5
                data[wordIdx] = wordList[int(random(len(wordList)))]
                score = score + w[wordIdx]*len(data[wordIdx]) * 0.01

                                
        
        else: 
            letterCnt = 0 
            
    print (str(letterCnt) , (str(wordIdx))) 


    
    
def mousePressed(): 
    global stageNum 
    if stageNum == 0 and mouseX >= width/5 and mouseX < width/5 + 500 and mouseY >= height/2.5 and mouseY < height/2.5 + 200:
        stageNum = 1  
           
    elif stageNum == 2 and mouseX >= (225) and mouseX < (475) and mouseY >= (400) and mouseY < (650):
        setup()
    
    elif stageNum == 2 and mouseX >= (350) and mouseX < (600) and mouseY >= (400) and mouseY < (650): 
        exit()

    
    
