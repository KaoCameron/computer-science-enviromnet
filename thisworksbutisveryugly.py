#Wall-i

weight = ''
text_x = 700/2
text_y = 500/2
text_width = 50
text_height = 50
word = 0
x = 0
y = 290
progress_x = 100
progress_y = 200
t = 10
timer = 0
def setup():
    size(700,500)
    #lr,ud

def keyTyped(): 
     global weight,r 
     weight += key
     r = random(0, int(weight))
     print int(r)

def draw():
    global weight,word,x,y
    background('#231123')
    noStroke ()
    fill('#FFEFFF')
    if key == ENTER:
        if word <= 100:
            word += 0.2
            textAlign(CENTER, BOTTOM)
            text('''Calculating...Beep Boop''', 350, 400)
        if word <=9:
            y = 385
        elif word >=100:
            y =410
        elif word >= 10:
            y = 395
        
        textAlign(CENTER, BOTTOM)
        textSize(40)
        text(int(word), progress_x+500/2, progress_y)
        text("%", y, 200)
        fill(255)
        rect(progress_x, progress_y, 500, 75)
        fill(1)
        rect(progress_x, progress_y, x, 75)
        if x< 500:
            x += 1
        elif x >= 500:
            global t,r,weight
            weight = int(weight)  
            t -= .1
            fill('#FFEFFF')
            textAlign(CENTER, BOTTOM)
            text('Complete! continuing in %s'% (int(t)), 350, 400)
            if t <= 0 and r< weight/2 :
                background('#231123')
                textSize(32) 
                text('The program has found:',350,100)
                textSize(16)
                text("%s kg of valubale waste(gold, platinum etc)" % (int(r)),350,150)
                text("The rest, %s, was safe garbage" % int((weight-r)),350,200)
            if r >= weight/2:
                background('#231123')
                textSize(32)
                text('The program has found:',350,100)
                textSize(16)
                text("%s kg of valubale waste (gold, platinum etc)" % (int(r)) ,350,200)
                text('Since there is still a decent amount (%s) of ' % int((weight-r)), 350, 250)
                text('precious metals inside your garabge, ',350,300)
                text('please send it to an extraction plant',350,340)

    else:
        textSize(32) 
        textAlign(CENTER, CENTER)
        text("Insert Weight Of Waste, in Kg", text_x, text_y)
        text(weight, text_x, text_y+100)

