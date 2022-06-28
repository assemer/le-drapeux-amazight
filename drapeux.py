#!/usr/bin/python3

#####################################
# voisi un petits scripts en python #
#  qui uttilise le module turtle    #
# pour designer Le drapeux Amaziht  #
#####################################
#	 AUTHORS : Assemer LAYAS        #
#####################################

import turtle

pen = turtle.Turtle()
pen.up()

def bgs():
	pen.setpos(0,0)
	pen.up();
	pen.left(90)
	pen.color("#007BE3")
	pen.forward(200 * C)
	pen.left(90)
	pen.down()
	pen.forward(200 * C)
	pen.left(90)
	pen.forward(400 * C)
	pen.left(90)
	pen.forward(200 * C)
	pen.left(90)
	pen.up()
	pen.forward(400 * C)
	pen.color('#E3B500')
	pen.right(90)
	pen.down()
	pen.forward(200 * C)
	pen.right(90)
	pen.forward(400 * C)
	pen.right(90)
	pen.forward(200 * C)
	pen.right(90)
	pen.up()
	pen.forward(400 * C)
	pen.right(90)


	return 0

def logos():
	pen.setpos(40,0)
	pen.color("#96192C")
	pen.up()
	pen.back(60)
	pen.left(90)
	pen.down()
	pen.forward(V*100)
	pen.left(90)
	pen.forward(V*100*distance)
	pen.left(-90)
	pen.forward(V*100)
	pen.left(-90)
	pen.forward(V*40)
	pen.left(-90)
	pen.forward(V*70)
	pen.left(90)
	pen.forward((V*100*distance)-40)
	pen.left(90)
	pen.forward(V*100)
	pen.left(-90)
	pen.forward(V*40)
	pen.left(-90)
	pen.forward(V*100)
	pen.left(90)
	pen.forward(V*(100-28)*distance)
	pen.left(90)
	pen.forward(V*70)
	pen.left(-90)
	pen.forward(V*40)
	pen.left(-90)
	pen.forward(V*100)
	pen.left(-90)
	pen.forward((V*100*distance))
	pen.left(90)
	pen.forward(V*100)
	pen.forward(V*100)



	pen.left(90)
	pen.forward(V*100*distance)
	pen.left(-90)
	pen.forward(V*100)
	pen.left(-90)	
	pen.forward(V*40)
	pen.left(-90)
	pen.forward(V*70)
	pen.left(90)
	pen.forward((V*100*distance)-40)
	pen.left(90)
	pen.forward(V*100)
	pen.left(-90)
	pen.forward(V*40)
	pen.left(-90)
	pen.forward(V*100)
	pen.left(90)
	pen.forward(V*70 *distance)
	pen.left(90)
	pen.forward(V*70)
	pen.left(-90)
	pen.forward(V*40)
	pen.left(-90)
	pen.forward(V*100)
	pen.left(-90)
	pen.forward((V*100*distance)-pen.pensize()/2)
	pen.left(90)
	pen.forward(V*100)
	pen.hideturtle()





bg  = turtle.Screen()
bg.bgcolor("#fff")

C = 1.3  # Pour Modifie La Taille Du backGround
V = 1    # Pour Modifie La Taille Du Logo
distance = 1.2 # la distance des main
pen.speed(3)    # la vitese du movement du desin


pen.pensize(10) # la taille du crayon
bgs()

pen.pensize(4) # la taille du crayon
logos()





s = input()     # Cest Just Pour Que La Fenter se ferme pas Lorce quille a fini 