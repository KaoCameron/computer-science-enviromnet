def draw():
    global x, word, y
    background(255)
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
    noFill()# computer-science-enviromnet
thingy
Class collaboration on hangman.
 Python  50 Updated on Oct 5
￼Star

    rect(115, 200,500,75)
    fill(1)
    rect(115, 200, x, 75)
    if x< 500:
        x += 1
    elif x >= 500:
        print("complete")
    print(x)
