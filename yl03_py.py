# Regnar 19.11.26

# Ülessanne 3.6 Python Turtle ruut
import turtle

kylje_pikkus = 100
nurk = 90
varv = "red"
edasi = kylje_pikkus

#esimene
turtle.color(varv)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)
#tõstan pliiatsit
turtle.up()
turtle.goto(edasi*1.5,0 )
turtle.down()

#teine
turtle.color(varv)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)
#tõstan pliiatsit
turtle.up()
turtle.goto(edasi*3,0)
turtle.down()

#kolmas
turtle.color(varv)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)
turtle.fd(kylje_pikkus)
turtle.rt(nurk)
#tõstan pliiatsit
turtle.up()
turtle.goto(edasi*4.5,0)
turtle.down()


turtle.done()


# Ülessanne 3.4 Lemmikraamat

raamatu_pealkiri ="Suvi"
raamatuautor ="Oskar Meri"
raamar = raamatu_pealkiri+" "+raamatu_autor
lk = 300
skoor = 10.0
print("Minu lemmikraamat on "+str(raamat)+" , mis on "+str(lk)+" lehekülge pikk ja mille ma hindan "+str(skoor)+" punktiga.")

# Ülessanne 3.2: Ostunimekiri
toode = "juust"
kogus = 50
hind = 15.50

print("Soovin "+toode+" "+str(kogus)+", mille tüki hind on "+str(hind)+" eurot.")
