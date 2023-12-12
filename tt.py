import matplotlib.pyplot as plt
import streamlit as st

fig, ax = plt.subplots()
c1 = st.sidebar.radio,('선의 색을 선택하시오',['red','green','blue'])
s1 = st.sidebar.radio,('선의 형태를 선택하시오',['-','--','-.'])
m1 = st.sidebar.radio,('마커의 형태를 선택하시오',['o','^',"s"])





a = st.number_input('a의 값을 입력하시오',value=2.0,step=1.0)
b = st.number_input('b의 값을 입력하시오',value=-1.0,step=1.0)
c = st.number_input('c의 값을 입력하시오',value=15.0,step=1.0)
d = st.number_input('d의 값을 입력하시오',value=2000.0,step=100.0)

x=[]
y=[]
y2=[]
for i in range(-29,30,3):
    x.append(i)
    y.append(a^ + b +c)
    y2.append(d/x)







plt.plot(x , y, y2, color = c1, linestyle = s1, marker = m1)


st.pyplot(fig)


import sys
sys.exit()









# import random as r 

# import matplotlib.pyplot as plt

# fig, ax = plt.subplots()

# x = []
# for i in range(-100,100):
#     x.append(i/10.0)

# col = st.columns(3)
# with col[0]:
#     a = st.number_input('insert a',step = 1)
# with col[1]:
#     with col[0]:
#      b = st.number_input('insert b',step = 1)
# with col[1]:
#     with col[0]:
#      c = st.number_input('insert c',step = 1)

# y = []
# for i in x:
#    y.append(a*i**2 + b*i + c)

# plt.plot(x, y)

# st.pyplot(fig)     











































# s=[3, 7, 1, 9, -3, 3, 10]
# s







# for i in s:
#     t = t + i
# t 


# s1 = 1
# s2 = 2
# s3 = 3 
# s4 = 4
# s5 = 5
# s1, s2 ,s3 ,s4, s5
# s= ['a','b','c','d','e']


# s.append('사과')
# s.remove('c')
# s
# i = s.index('d')
# i






# t.speed(0)




# t.pensize(5)

# def shape(sh):
#    for j in range(sh):
#             t.fd(1+5*i)
#             t.left(360/sh)








# sh = 7
# while True:
#     for i in range(30):
#         if i < 10:
#              shape(3)
#         elif i < 20:
#              shape(4)
#         elif i < 30:
#              shape(5)



#         t.color((r.random(), r.random(), r.random()))
#         t.goto(i*20, 0)
        

# turtle.done()








# screen = turtle.Screen()

# iml= 'rabbit.gif'
# screen.addshape(iml)

# iml = 'rabbit.gif'
# im2 = 'rabbit.gif'



# t1 = turtle. Turtle()
# t2=  turtle.Turtle()

# screen.addshape(iml)
# t1.shape(iml)
# t2.shape("turtle")

# t1.penup()
# t1.shapesize(3)
# t1.goto(-300,100)

# t2.penup()
# t2.shapesize(3)
# t2.goto(-300,-100)

# t1.pendown()
# t2.pendown()
# t1.speed(1)
# t2.speed(1)





# for i in range(50):
#     d1=random.randint(1,30)
#     t1.fd(d1)
#     d2=random.randint(1,30)
#     t2.fd(d2)








# for _ in range(6):
#     a1=r.randint(1,45)
#     a1
#     a2 = r. random()
#     a1,a2

# a=0
# a=10
# for i in range(n):
#     c= r.choice('abcedf')
#     if c == "a":
#             a=a + 1


# a/n, "%"






# a1 = random.randint(1, 45)
# a1


























# import turtle 



# t = turtle.Turtle()
# t.shape('turtle')
# t.speed(1)

# def rec(x, y, lx, ly):
#     t.up()
#     t.goto(x,y)
#     t.down()   
 
#     for i in range(2):       
#        t.fd(lx)
#        t.left(90)
#        t.fd(ly)       
#        t.left(90)

# rec(-200, 0 ,100, 50)
# rec(0, 0, 100, 150)
# rec(200, 0, 100, 50)


# turtle.done() 








# a = 3
# b = '1'
# c = '1'


# print('a=',a)
# 'a=', a
# b
# c




# s= 95
# if s >= 90:
#     st.write('귀하의 점수는'+ str(s) + '점으로 :red[A등급]입니다')
# elif s >= 80:
#     '# 귀하의 점수는'+ str(s) +'점으로 :red[B등급]입니다'
# elif s >= 70:
#     '# 귀하의 점수는'+ str(s) +'점으로 :red[C등급]입니다'
# elif s >= 60:
#     '# 귀하의 점수는'+ str(s) +'점으로 :red[D등급]입니다'
# else:
#     '# 귀하의 점수는'+ str(s) +'점으로 :red[f등급]입니다'





# for i in range(1, 100, 5):
#     if i%3 == 1:   
#         i  



# import turtle



# # n = 40
# # ang = 360/n
# t = turtle.Turtle()
# t.shape('turtle')
# t.speed(0)
# t.width(2)
# #colors = ('blue','purple','red','yellow','orange','green')


# # for i in range(3):
# #     t.fd(80)
# #     t.left(120)

# length = 5

# for i in range(100): 
#     t.fd(length)
#     t.right(80)
#     length += 5
#     #t.pencolors(colors[length%6])


# turtle.done()





























# st.latex(r'''
#     a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
#     \sum_{k=0}^{n-1} ar^k =
#     a \left(\frac{1-r^{n}}{1-r}\right)
#     ''')














#s = 0
#for i in range(1, 101, 2):
    #'s=' ', s, ' 'i = ', i
   # s = s + i
   #s += i
    #'s + i =', s
#s   






# '7과 4의 연산'


# '덧셈',   7 + 4
# '뺄셈',   7 - 4
# '곱셈',   7 * 4
# '나눗셈',   7 / 4
# '몫' ,  7 // 4
# '나머지', 7 % 4
# '거듭제곱', 2 ** 4












# r = 100


# t.left(60)
# t.fd(r)
# t.right(120)
# t.fd(r)

# t.right(30)
# t.fd(r)
# t.right(90)
# t.fd(r)
# t.right(90)
# t.fd(r)
# t.right(90)
# t.fd(r)


# turtle.done()















#  