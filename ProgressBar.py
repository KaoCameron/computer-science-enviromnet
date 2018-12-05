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
    #if key == ENTER:
        #progressbar
