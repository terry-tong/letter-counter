def countLetters(sentence):
    import turtle
    histogram = turtle.Turtle()
    window = turtle.Screen()
    window.screensize(1000, 1000)
    i = 0
    histogram.hideturtle()
    histogram.speed(0)
    histogram.up()
    histogram.goto(-400, -400)
    histogram.down()
    dictionary = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    width = 25
    letter = []
    count = []

    caseSensitivity: bool = False
    while caseSensitivity is False:
        case = input("Case-sensitive? (Y/N) ").upper()
        if case == "Y":
            sentence = list(sentence)
            caseSensitivity: bool = True
        elif case == "N":
            sentence = list(sentence.upper())
            caseSensitivity: bool = True
        else:
            print("Invalid input.")
    for m in range(len(dictionary)):
        x = 0
        for n in range(len(sentence)):
            if sentence[n] == dictionary[m]:
                x += 1
        if x > 0:
            count.append(x)
            letter.append(dictionary[m])
    while i < len(count):
        histogram.left(90)
        histogram.forward(count[i]*10)
        histogram.right(90)
        histogram.forward(width/2)
        histogram.left(90)
        histogram.up()
        histogram.forward(4)
        histogram.write(count[i], align="center")
        histogram.back(4)
        histogram.down()
        histogram.right(90)
        histogram.forward(width/2)
        histogram.right(90)
        histogram.forward(count[i]*10)
        histogram.up()
        histogram.forward(15)
        histogram.right(90)
        histogram.forward(width/2)
        histogram.write(letter[i], align="center")
        histogram.back(width/2)
        histogram.right(90)
        histogram.forward(15)
        histogram.right(90)
        histogram.down()
        i += 1
    histogram.back(len(count)*width)
    turtle.done()

countLetters(input("Please enter your word/phase/sentence here: "))