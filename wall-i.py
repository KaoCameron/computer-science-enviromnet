#Wall-i

def setup():
    size(700,500)

weight = ''
text_x = 350
text_y = 250
text_width = 50
text_height = 50

def keyTyped(): 
     global weight   
     weight += key
     textAlign(CENTER, CENTER)
     text("Insert Weight Of Waste", text_x, text_y)
     text(weight, text_x, text_y+100)


def draw():
    global weight
    background('#231F20')
    noStroke ()
    textSize(32) 
    textAlign(CENTER, CENTER)
    text("Insert Weight Of Waste", text_x, text_y)
    text(weight, text_x, text_y+100)
    if key == ENTER:
        if word <= 100:
            word += 0.2
        if word <=9:
            y = 385
        elif word >=100:
            y =410
        elif word >= 10:
            y = 395
        
        textAlign(CENTER, BOTTOM)
        textSize(40)
        text(int(word), 360, 200)
        text("%", y, 200)
        noFill()
        rect(115, 200,500,75)
        fill(1)
        rect(115, 200, x, 75)
        if x< 500:
            x += 1
        elif x >= 500:
            print("complete")
        print(x)    
