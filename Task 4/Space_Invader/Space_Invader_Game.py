import tkinter
import random
import math
import os
import turtle
from tkinter import *
from turtle import *
from tkinter import messagebox
from PIL import ImageTk,Image
import winsound
import playsound
window = tkinter.Tk()
window.geometry("600x600")
window.title("Space Invader")

playsound.playsound("spaceinvaders1.mpeg",False)
Player_name = tkinter.Label(text="Player Name : " ,font=("Arial", 15, "bold"))
Player_name.grid(row=0,column=0)
Player_Entry = tkinter.Entry(width=15,font=("Arial", 15, "bold"))
Player_Entry.grid(row=0, column=1)

canvas = Canvas(window, width=600,height=600,bd=1)
canvas.grid(row=3,column=0,columnspan=5)

#set Background Image
back_img = ImageTk.PhotoImage(Image.open("background.jpg"))
turtles = TurtleScreen(canvas)
turtles.register_shape("enemy1.gif")
turtles.register_shape("Player_logo1.gif")
turtles.register_shape("enemylaser.gif")
turtles.tracer(0)
canvas.create_image(-300,-300,anchor=NW, image= back_img)


#Create Player
player = RawTurtle(turtles)
player.shape("Player_logo1.gif")
player.color("red")
player.setheading(90)
player.penup()
player.turtlesize(2)
player.setposition(0,-230)
playerSpeed = 10

#Home Page Text
home_page = turtle.RawTurtle(turtles)
home_page.hideturtle()
home_page.penup()
home_page.color("red")
home_page.speed(0)
home_page.setposition(-200,-50)
home_page.write("Space Invader \n      Game",font=("Times New Roman",48,"bold"))

#this Function To Use When We use To genrate Random enemy
def Random_enemy_position():
    enemies = [enemy1,enemy2,enemy3,enemy4,enemy5]
    for enemy in enemies:
        x = random.randint(-200 ,200)
        y = random.randint(100 ,250)
        enemy.setposition(x ,y)
#create Enemy
enemy1 = turtle.RawTurtle(turtles)
enemy1.shape("enemy1.gif")
enemy1.penup()
enemy1.speed(0)
x = random.randint(-200, 200)
y =  random.randint(100, 250)
enemy1.setposition(x, y)


enemy2 = turtle.RawTurtle(turtles)
enemy2.shape("enemy1.gif")
enemy2.penup()
enemy2.speed(0)
x = random.randint(-200, 200)
y =  random.randint(100, 250)
enemy2.setposition(x, y)

enemy3 = turtle.RawTurtle(turtles)
enemy3.shape("enemy1.gif")
enemy3.penup()
enemy3.speed(0)
x = random.randint(-200, 200)
y =  random.randint(100, 250)
enemy3.setposition(x, y)

enemy4 = turtle.RawTurtle(turtles)
enemy4.shape("enemy1.gif")
enemy4.penup()
enemy4.speed(0)
x = random.randint(-200, 200)
y =  random.randint(100, 250)
enemy4.setposition(x, y)

enemy5 = turtle.RawTurtle(turtles)
enemy5.color("red")
enemy5.shape("enemy1.gif")
enemy5.penup()
enemy5.speed(0)
x = random.randint(-200, 200)
y =  random.randint(100, 250)
enemy5.setposition(x, y)
enemySpeed = 0.4

#Bullets
Bullet = turtle.RawTurtle(turtles)
Bullet.shape("triangle")
Bullet.shapesize(0.2,2)
Bullet.color("orange")
Bullet.penup()
Bullet.speed(0)
Bullet.hideturtle()

#create Enemy Bullets :
enemy_bullet_speed = 0.6
enemy1_bullets = turtle.RawTurtle(turtles)
def eneme1_attack():
    enemy1_bullets.color("red")
    enemy1_bullets.penup()
    enemy1_bullets.shape("triangle")
    enemy1_bullets.shapesize(0.5,1)
    enemy1_bullets.speed(0)
    enemy1_bullets.hideturtle()
    x = enemy1.xcor( )
    y = enemy1.ycor( ) - 10
    enemy1_bullets.setposition(x,y)
    enemy1_bullets.setheading(-90)

enemy2_bullets = turtle.RawTurtle(turtles)
def eneme2_attack():
    enemy2_bullets.color("pink")
    enemy2_bullets.penup()
    enemy2_bullets.shapesize(0.5,1)
    enemy2_bullets.shape("triangle")
    x = enemy2.xcor( )
    y = enemy2.ycor( ) - 10
    enemy2_bullets.setposition(x,y)
    enemy2_bullets.speed(0)
    enemy2_bullets.hideturtle()
    enemy2_bullets.setheading(-90)

enemy3_bullets = turtle.RawTurtle(turtles)
def eneme3_attack():
    enemy3_bullets.color("yellow")
    enemy3_bullets.penup()
    enemy3_bullets.shapesize(0.5,1)
    enemy3_bullets.shape("triangle")
    x = enemy3.xcor( )
    y = enemy3.ycor( ) - 10
    enemy3_bullets.setposition(x,y)
    enemy3_bullets.hideturtle()
    enemy3_bullets.speed(0)
    enemy3_bullets.setheading(-90)

enemy4_bullets = turtle.RawTurtle(turtles)
def eneme4_attack():
    enemy4_bullets.color("orange")
    enemy4_bullets.penup()
    x = enemy4.xcor( )
    y = enemy4.ycor( ) - 10
    enemy4_bullets.shapesize(0.5,1)
    enemy4_bullets.shape("triangle")
    enemy4_bullets.setposition(x,y)
    enemy4_bullets.hideturtle()
    enemy4_bullets.speed(0)
    enemy4_bullets.setheading(-90)

enemy5_bullets = turtle.RawTurtle(turtles)
def eneme5_attack():
    enemy5_bullets.color("blue")
    enemy5_bullets.penup()
    enemy5_bullets.shapesize(0.5,1)
    enemy5_bullets.shape("triangle")
    x = enemy5.xcor( )
    y = enemy5.ycor( ) - 10
    enemy5_bullets.setposition(x,y)
    enemy5_bullets.hideturtle()
    enemy5_bullets.speed(0)
    enemy5_bullets.setheading(-90)

eneme1_attack()
eneme2_attack()
eneme3_attack()
eneme4_attack()
eneme5_attack()

#move Player
def move_left():
    x = player.xcor()
    if x > -290:
        x-=playerSpeed
        player.setx(x)
    else:
        player.setx(x)
def move_right():
    x = player.xcor( )
    if x < 290:
        x += playerSpeed
        player.setx(x)
    else:
        player.setx(x)

#Score Update
Score = 0
ScoreString = "Score : %s" %Score
score = turtle.RawTurtle(turtles)
score.color("white")
score.penup()
score.setposition(-290,275)
score.hideturtle()
score.speed(0)
# score.write(ScoreString,font = ("Arial",15,"bold"))

#lives
player_lives = 5
player_lives_string = "Lives :%s"%player_lives
Lives = turtle.RawTurtle(turtles)
Lives.color("white")
Lives.penup()
Lives.speed(0)
Lives.setposition(220,270)
Lives.hideturtle()
# Lives.write(player_lives_string,font = ("Arial",15,"bold"))

# fire bullets
bulletSpeed = 1.5
bulletState = "ready"
def fire_bullet():
    global bulletState
    if bulletState == "ready":
        bulletState = "fire"
        x = player.xcor( )
        y = player.ycor( ) + 10
        Bullet.setheading(90)
        Bullet.setposition(x ,y)
        Bullet.showturtle()
        Bullet.speed(0)

def isCollision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor( ) - t2.xcor( ) ,2) + math.pow(t1.ycor( ) - t2.ycor( ) ,2))
    if distance < 20 :
        return True
    else:
        return False


#Key Binding
window.bind('<Left>',lambda   a: move_left())
window.bind('<Right>',lambda  a: move_right())
window.bind('<space>',lambda  a: fire_bullet())


#Play Button
global All_Score
All_Score = []
def play_btn():
    global Score
    global player_lives
    home_page.clear()
    Player_Entry.config(state =DISABLED ) #After Enter push Play Button This is Not doing any modification
    global play_btn_state
    play_btn_state = True
    #Player_lives and Score Reset
    player_lives = 5
    Score = 0
    score.clear()
    Lives.clear()
    Lives.write(player_lives_string ,font = ("Arial" ,12 ,"bold"))
    score.write(ScoreString ,font = ("Arial" ,15 ,"bold"))
    Random_enemy_position()
    #here While Loop Funtion Which Run  again if we click play button
    play_btn_while_loop( )
    #print the final score
    global final_score
    Player_name = Player_Entry.get()
    final_score = f"{Player_name} :{Score}"
    tkinter.messagebox.showinfo("Game Over",final_score)
    All_Score.append(final_score)
    Player_Entry.config(state =NORMAL)#eneble entry block so we can change player name

def high_Score():
    #here list convert into string And Showing into msgbox
    Scores = ""
    for i in All_Score:
        Scores +=i
        Scores +="\n"
    tkinter.messagebox._show("High Score" ,Scores)


#if Enemy Crose The X Line Of Player Then Reset
def enemy_player_coloborate():
    global player_lives

    player_lives -= 1
    if player_lives >= 0:
        x = random.randint(-280 ,280)
        y = -230
        player.setposition(x ,y)
        player_lives_string = "Lives :%s" % player_lives
        Lives.clear( )
        Lives.write(player_lives_string ,font = ("Arial" ,12 ,"bold"))


def play_btn_while_loop():
    enemySpeed = 0.5
    global Score
    global play_btn_state
    if play_btn_state == True:
        global player_lives
        while player_lives >0:
            turtles.update( )
            a = enemy1.xcor( )
            a += enemySpeed
            enemy1.setx(a)
            b = enemy1.ycor( )
            if b < -280:
                Random_enemy_position()
            if a > 280 and -280 < b < 800:
                b = enemy1.ycor( )
                b -= 50
                enemy1.sety(b)
                enemySpeed *= -1
            if a < -280 and -280 < b < 800:
                b = enemy1.ycor( )
                b -= 50
                enemy1.sety(b)
                enemySpeed *= -1

            c = enemy2.xcor( )
            c += enemySpeed
            enemy2.setx(c)
            d = enemy2.ycor( )
            if d < -280:
                Random_enemy_position()
            if c > 280 and -280 < d < 800:
                d = enemy2.ycor( )
                d -= 50
                enemy2.sety(d)
                enemySpeed *= -1
            if c < -280 and -280 < d < 800:
                d = enemy2.ycor( )
                d -= 50
                enemy2.sety(d)
                enemySpeed *= -1

            e = enemy3.xcor( )
            e += enemySpeed
            enemy3.setx(e)
            f = enemy3.ycor( )
            if f < -280:
                Random_enemy_position()
            if e > 280 and -280 < f < 800:
                f = enemy3.ycor( )
                f -= 50
                enemy3.sety(f)
                enemySpeed *= -1
            if e < -280 and -280 < f < 800:
                f = enemy3.ycor( )
                f -= 50
                enemy3.sety(f)
                enemySpeed *= -1

            g = enemy4.xcor( )
            g += enemySpeed
            enemy4.setx(g)
            h = enemy4.ycor( )
            if h < -280:
                Random_enemy_position()
            if g > 280 and -280 < h < 800:
                h = enemy4.ycor( )
                h -= 50
                enemy4.sety(h)
                enemySpeed *= -1
            if g < -280 and -280 < h < 800:
                h = enemy4.ycor( )
                h -= 50
                enemy4.sety(g)
                enemySpeed *= -1

            i = enemy5.xcor( )
            i += enemySpeed
            enemy5.setx(i)
            j = enemy5.ycor( )
            if j < -280:
                Random_enemy_position()
            if i > 280 and -280 < j < 800:
                j = enemy5.ycor( )
                j -= 50
                enemy5.sety(j)
                enemySpeed *= -1
            if i < -280 and -280 < j < 800:
                j = enemy5.ycor( )
                j -= 50
                enemy5.sety(j)
                enemySpeed *= -1

            # player Bullets
            global bulletState
            if bulletState == "fire":
                y = Bullet.ycor( )
                y += bulletSpeed
                Bullet.sety(y)

            if Bullet.ycor( ) > 280:
                Bullet.hideturtle( )
                bulletState = "ready"

            # Enemy Atack
            y = enemy1_bullets.ycor( )
            z = enemy1.ycor()
            y -= enemy_bullet_speed
            enemy1_bullets.sety(y)
            if y < -250 and z < 500:
                eneme1_attack( )
                enemy1_bullets.showturtle( )

            y = enemy2_bullets.ycor( )
            z = enemy2.ycor( )
            y -= enemy_bullet_speed
            enemy2_bullets.sety(y)
            if y < -250 and z < 500:
                eneme2_attack( )
                enemy2_bullets.showturtle( )
            if z < -280:
                Random_enemy_position()

            y = enemy3_bullets.ycor( )
            y -= enemy_bullet_speed
            z = enemy3.ycor( )
            enemy3_bullets.sety(y)
            if y < -250 and z < 500:
                eneme3_attack( )
                enemy3_bullets.showturtle()
            if z < -280:
                Random_enemy_position( )

            y = enemy4_bullets.ycor()
            y -= enemy_bullet_speed
            z = enemy4.ycor( )
            enemy4_bullets.sety(y)
            if y < -250 and z < 500:
                eneme4_attack( )
                enemy4_bullets.showturtle( )
            if z < -280:
                Random_enemy_position( )

            y = enemy5_bullets.ycor( )
            y -= enemy_bullet_speed
            z = enemy5.ycor( )
            enemy5_bullets.sety(y)
            if y < -250 and z < 500:
                eneme5_attack( )

            if z < -280:
                Random_enemy_position( )
            
            #collision Between Player Bullets and Enemy :
            enemies = [enemy1,enemy2,enemy3,enemy4,enemy5]
            for enemy in enemies:
                if isCollision(Bullet ,enemy):
                    global Score
                    Bullet.hideturtle( )
                    bulletState = "ready"
                    if enemy == enemy1:
                        Score += 10
                        score.clear( )
                        ScoreString = "Score : %s" % Score
                        score.write(ScoreString,font = ("Arial",15,"bold"))
                        x = random.randint(-200 ,200)
                        y = random.randint(100 ,250)
                        enemy1.setposition(x,y)
                        winsound.PlaySound('shoot.wav' ,winsound.MB_ICONHAND)

                    if enemy == enemy2:
                        Score += 10
                        score.clear( )
                        ScoreString = "Score : %s" % Score
                        score.write(ScoreString,font = ("Arial",15,"bold"))
                        x = random.randint(-200 ,200)
                        y = random.randint(100 ,250)
                        enemy2.setposition(x ,y)
                        winsound.PlaySound('shoot.wav' ,winsound.MB_ICONHAND)

                    if enemy == enemy3:
                        Score += 10
                        score.clear( )
                        ScoreString = "Score : %s" % Score
                        score.write(ScoreString,font = ("Arial",15,"bold"))
                        x = random.randint(-200 ,200)
                        y = random.randint(100 ,250)
                        enemy3.setposition(x ,y)
                        winsound.PlaySound('shoot.wav' ,winsound.MB_ICONHAND)

                    if enemy == enemy4:
                        Score += 10
                        score.clear( )
                        ScoreString = "Score : %s" % Score
                        score.write(ScoreString,font = ("Arial",15,"bold"))
                        x = random.randint(-200 ,200)
                        y = random.randint(100 ,250)
                        enemy4.setposition(x ,y)
                        winsound.PlaySound('shoot.wav' ,winsound.MB_ICONHAND)

                    if enemy == enemy5:
                        Score += 10
                        score.clear( )
                        ScoreString = "Score : %s" % Score
                        score.write(ScoreString,font = ("Arial",15,"bold"))
                        x = random.randint(-200 ,200)
                        y = random.randint(100 ,250)
                        enemy5.setposition(x ,y)
                        winsound.PlaySound('shoot.wav' ,winsound.MB_ICONHAND)


            # #collision between Enemy_Attack And Player
            bulls = [enemy1_bullets , enemy2_bullets , enemy3_bullets ,enemy4_bullets, enemy5_bullets]
            for bullets in bulls:
                if isCollision(bullets,player):
                    player_lives -= 1
                    if player_lives >= 0 :
                        x = random.randint(-280,280)
                        y = -230
                        player.setposition(x,y)
                        player_lives_string = "Lives :%s"%player_lives
                        Lives.clear()
                        Lives.write(player_lives_string,font = ("Arial",12,"bold"))
                        winsound.PlaySound('fastinvader1.wav' ,winsound.MB_ICONHAND)


Play_Button = tkinter.Button(text="Play",font=("Arial", 10, "bold"), command = play_btn)
Play_Button.grid(padx=5, pady=5,row=0, column=4)

High_Score = tkinter.Button(text=" High Score",font=("Arial", 10, "bold"),command = high_Score)
High_Score.grid(padx=10, pady=5,row=0, column=3)


window.mainloop()
