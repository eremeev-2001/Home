from graphics import*
win = GraphWin("MyWin", 700, 1000)


r = Rectangle(Point(93,355), Point(555, 663))# первый этаж
r.setWidth(3)
r.setFill("#efe3af")


p=Polygon(Point(67,355),Point(327,55),Point(587,355))# крыша
p.setWidth(3)
p.setFill("#efe3af")


k=Polygon(Point(252,200),Point(327,122),Point(397,201),Point(327,278))# оконтовка верхнего окна
k.setWidth(3)
k.setFill("#b77a5d")

o=Circle(Point(440,410),26)# фонарь
o.setWidth(3)
o.setFill("yellow")

g=Polygon(Point(273,200),Point(327,148),Point(378,199),Point(327,251), Point(327,148), Point(327,251))#верхнее окно
z=Line(Point(273,200),Point(378,199))
z.setWidth(3)
g.setWidth(3)
g.setFill("#98daea")


q = Rectangle(Point(145,389), Point(321, 404))#
q.setWidth(3)
q.setFill("#b77a5d")
w = Rectangle(Point(157,404), Point(310, 578))#
w.setWidth(3)
w.setFill("#98daea")
e = Rectangle(Point(145,579), Point(321, 593))#
e.setWidth(3)
e.setFill("#b77a5d")
t=Line(Point(158,453), Point(311, 453))#
t.setWidth(3)
y=Line(Point(235,453), Point(235, 579))#нижнее окно
y.setWidth(3)



u = Rectangle(Point(354,444), Point(517, 457))#
u.setWidth(3)
u.setFill("#b77a5d")
i = Rectangle(Point(365,459), Point(505, 662))#
i.setWidth(3)
i.setFill("#880016")
a = Rectangle(Point(474,532), Point(483, 580))#дверь
a.setFill("#b77a5d")
a.setWidth(3)


s = Rectangle(Point(145,40), Point(255, 69))#
s.setWidth(3)
s.setFill("#7f7f7f")
d=Polygon(Point(171,232),Point(171,70),Point(233,70), Point(233,160))# труба
d.setWidth(3)
d.setFill("#da4800")





r.draw(win)
p.draw(win)
k.draw(win)
o.draw(win)
g.draw(win)
z.draw(win)
q.draw(win)
w.draw(win)
e.draw(win)
t.draw(win)
y.draw(win)
u.draw(win)
i.draw(win)
a.draw(win)
s.draw(win)
d.draw(win)


win.getMouse()
win.close()

