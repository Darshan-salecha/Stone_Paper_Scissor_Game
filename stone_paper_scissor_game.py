import numpy as np
import random
import threading
import cv2

list=[]
def generator():
    Dic={0:"Stone",1:"Paper",2:"Scissor"}
    x=random.randint(0,2)
    threading.Timer(2,generator).start()
    list.append(Dic[x])

generator()

stone_cascade=cv2.CascadeClassifier("fist.xml")
paper_cascade=cv2.CascadeClassifier("palm.xml")
scissor_cascade=cv2.CascadeClassifier("fingers.xml")
none_cascade=cv2.CascadeClassifier("none.xml")

cap=cv2.VideoCapture(0)
count_s=0
count_p=0
count_sc=0
count_n=0
c_win=0
c_lose=0
c_tie=0

while (True):
    ret,img=cap.read()
    img =img[100:350,100:350]
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    stone=stone_cascade.detectMultiScale(gray,1.1,5)
    paper=paper_cascade.detectMultiScale(gray,1.3,5)
    scissor=scissor_cascade.detectMultiScale(gray,1.15,50)
    none=none_cascade.detectMultiScale(gray,1.1,5)

    for (x, y, w, h) in stone:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)

        count_s += 1
        if (count_s == 1):
            # print("stone-user")
            count_p = 0
            count_n = 0
            count_sc = 0
            cv2.destroyWindow('none')
            if (list[len(list) - 1] == "Scissor"):
                img1 = cv2.imread("Scissors.jpg")
                cv2.imshow('S_P', img1)
                print("You Win!")
                c_win += 1
            elif (list[len(list) - 1] == "Paper"):
                img1 = cv2.imread("paper.jpg")
                cv2.imshow('S_P', img1)
                print("You Lose!")
                c_lose += 1
                # cv2.destroyWindow('S_P')
            else:
                img1 = cv2.imread("stone.jpg")
                cv2.imshow('S_P', img1)
                print("It is a tie!")
                c_tie += 1
    if len(stone) == 0:
        for (x, y, w, h) in paper:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

            count_p += 1
            if (count_p == 1):
                # print("paper-user")
                count_s = 0
                count_n = 0
                count_sc = 0
                cv2.destroyWindow('none')
                if (list[len(list) - 1] == "Stone"):
                    img1 = cv2.imread("stone.jpg")
                    cv2.imshow('S_P', img1)
                    print("You Win!")
                    c_win += 1
                elif (list[len(list) - 1] == "Scissor"):
                    img1 = cv2.imread("scissors.jpg")
                    cv2.imshow('S_P', img1)
                    print("You Lose!")
                    c_lose += 1
                    # cv2.destroyWindow('S_P')
                else:
                    img1 = cv2.imread("paper.jpg")
                    cv2.imshow('S_P', img1)
                    print("It is a tie!")
                    c_tie += 1

    if len(stone) == 0 and len(paper) == 0:
        for (x, y, w, h) in scissor:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            count_sc += 1
            if (count_sc == 1):
                cv2.destroyWindow('none')
                # print("paper-user")
                count_s = 0
                count_n = 0
                count_p = 0
                if (list[len(list) - 1] == "Paper"):
                    img1 = cv2.imread("paper.jpg")
                    cv2.imshow('S_P', img1)
                    print("You Win!")
                    c_win += 1
                elif (list[len(list) - 1] == "Stone"):
                    img1 = cv2.imread("stone.jpg")
                    cv2.imshow('S_P', img1)
                    print("You Lose!")
                    c_lose += 1
                else:
                    img1 = cv2.imread("scissors.jpg")
                    cv2.imshow('S_P', img1)
                    print("It is a tie!")
                    c_tie += 1

    if len(stone) == 0 and len(paper) == 0 and len(scissor) == 0:
        for (x, y, w, h) in none:
            img1 = cv2.imread("none.jpg")
            cv2.imshow('none', img1)
            count_n += 1
            if (count_n == 1):
                # print("None")
                count_p = 0
                count_s = 0
                count_sc = 0
                cv2.destroyWindow('S_P')

    cv2.imshow('img', img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break



print("Final Scores:-")
print("Player:", c_win, "Computer:", c_lose, "Tied:", c_tie)
cap.release()
cv2.destroyAllWindows()
