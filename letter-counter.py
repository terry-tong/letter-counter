import turtle
histogram = turtle.Turtle()
window = turtle.Screen()
window.screensize(1000,1000)
i = 0
histogram.hideturtle()
histogram.speed(0)
histogram.up()
histogram.goto(-400,-400)
histogram.down()
dictionary = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

letter = []
count = []

def countLetters(sentence):
    sentence = list(sentence)
    for m in range(len(dictionary)):
        x = 0
        for n in range(len(sentence)):
            if sentence[n] == dictionary[m]:
                x += 1
        if x > 0:
            count.append(x)
            letter.append(dictionary[m])

countLetters(input("Please enter your word/phase/sentence here: "))

while i < len(count):
    histogram.left(90)
    histogram.forward(count[i]*10)
    histogram.right(90)
    histogram.forward(0.4*25)
    histogram.left(90)
    histogram.up()
    histogram.forward(5)
    histogram.write(count[i])
    histogram.back(5)
    histogram.down()
    histogram.right(90)
    histogram.forward(0.6*25)
    histogram.right(90)
    histogram.forward(count[i]*10)
    histogram.up()
    histogram.forward(15)
    histogram.right(90)
    histogram.forward(0.6*25)
    histogram.write(letter[i])
    histogram.back(0.6*25)
    histogram.right(90)
    histogram.forward(15)
    histogram.right(90)
    histogram.down()
    i += 1
histogram.back(len(count)*25)
turtle.done()