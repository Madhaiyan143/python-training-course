"""my_name="i am enter in the world is very good"
#print(my_name[:-1])
#print(my_name[1:7])
print(my_name[:20:2])"""


#concoditionation

"""friend1="tamilarsan"
friend2="aswak"
# number does not add
madhaiyan=friend1+" "+friend2
print(madhaiyan)"""


# string modification

"""my_name="i am enter in the world is very good"
print(my_name.lower())
print(my_name.upper())
"""


#strip first free space is removed

"""my_name="  i am enter in the world is very good   "
print(my_name)
print(my_name.strip())
"""

#replace in the letters

"""my_name="i am enter in the world is very good"
madhan="earth is very beatiful,earth is very storg"
print(madhan.replace("earth","moon",1))    # two comind two times 1 one time coming
print(my_name.replace("enter","going"))"""


#spilt in th paraa

"""my_name="i am enter in the world is very good"
print(my_name.split())
print(my_name.split("is"))
print(my_name.split(" ",5))"""


"""name="i love in the infreena"
print("infreena" in name)
print("Abi"not in name)"""


                     #some comedy game
"""name1=input("enter your name")
name2=input("enter in the secomd name")
last=name1[0:3]+name2[0:3]
print(last)"""

"""madhaiyan_love="infreena"

if madhaiyan_love==input("enter lover;"):
    print("madhaiyan lover")
else:
    print("madhaiyan is also sinle")"""

"""rain=True

if rain==False:
    print("jolly enjoy the day")
else:
    print("sorry goes to school")"""

      # coditional statement

"""mark=int(input("enter your mark"))

if mark>90:
    print("A grade in the exam")
if mark>80:
    print("B grade in the exam")
if mark>70:
    print("C grade in the exam")
if mark>60:
    print("D grade in the exam")
if mark<50:
    print("fail in the exam")"""


"""name="madhaiyan"
age=10
continue_travelling=True
if age<18:
    if continue_travelling:
        print("go enjoy the day live long")
    else:
        print("your not allowed")
elif age>=60:
    if continue_travelling:
        print("enjoy the days") 
    else:
        print("dont allowas")
else:
    print("sorrry discount finishd")"""

"""name=input("enter in the name")
for i in name:
    print(i)"""


"""for i in range(3):
    for j in range(2):
        print(f"i={i} j={j}")"""


#while loop condition
"""
a=1
while a<10:
    print(a)
    a+=1
"""

"""tourist=["tamil","aswak","praveenkumar","madhaiyan","manoj","senthil"]
for item in tourist:
    if item=="madhaiyan":
     break
    print(item)
                  """  

"""tourist=["tamil","aswak","praveenkumar","madhaiyan","manoj","senthil"]
for item in tourist:
    if item=="madhaiyan":
        break
    print(item)"""


"""v=1
while v<=20:
    if v==10:
        break
    print(v)
    v+=1"""


"""tourist=["tamil","aswak","praveenkumar","madhaiyan","manoj","senthil"]
for item in tourist:
    if item=="madhaiyan":
        continue
    print(item)
"""

                                                  # Even number prnting

"""o=1
while o<=20:
    o+=1
    if o%2==0:
        continue
    print(o)
        """


"""i=0

while i<=20:
    if i==3:
        pass
    else:
        print(i)
        i+=1

    
    """
                       #pizza order booking wizard

"""small_pizza=15
medium_pizza=20
large_pizza=25


add_papper_small_pizza=2
add_papper_large_or_medium_size=3
add_cheese_any_size=1

size=input("enna size vanum chellanm pizza[S/M/L]")
add_papper=input("do want paper[Y/N]")
add_wxtra_chees=input("do you want chees[Y/N]")
bill=0

if size=="S":
    bill+=small_pizza
elif size=="M":
    bill+=medium_pizza

elif size=="L":
    bill+=large_pizza

else:
    bill+=add_papper_large_or_medium_size

if add_wxtra_chees=="Y":
    bill+=add_cheese_any_size

print("finiall bill ,",bill)"""


"""spelling=list(("ee","er","errt","err","er","ty"))
print(spelling)
print(type(spelling))
print(spelling[2])"""

                 #conditional statement
"""spelling=["m","t","h","f","p"]
print(spelling)
spelling[-1]="s"
print(spelling)
print(spelling[-3:-1])
"""
"""
name=["thala","mass","kancha","boss","sri","ram"]
print("thala"in name)"""
                            
                            
                            
                              #list statment



"""name=["thala","mass","kancha","boss","sri","ram"]
       #0       1      2        3      4     5
name[-1]="counter"
print(name)
#name[1:3]="madhra","kail"
name[1:4]="madhra","kkk"                 # that letter was missed nanba
print(name)
"""
                 
                 # insert in the list
"""name=["thala","mass","kancha","boss","sri","ram"]
name.insert(0,"masskara")
print(name)"""

                    # append
"""name=["thala","mass","kancha","boss","sri","ram"]
name.append("kotha")
name.append(600)
name.append(["kk","cc","mala"])
print(name)"""
                             # list using extend

"""name=["thala","mass","kancha","boss","sri","ram"]
name.extend(["latu","kuthal","kuttan","saraku"])
payar=["latu, kuthal saraku soapu"]
name.extend(payar)
print(name)"""

                   #  list removing item
"""name=["thala","mass","kancha","boss","sri","ram"]
name.remove("kancha")
print(name)"""
                            # list pop
"""name=["thala","mass","kancha","boss","sri","ram"]
name.pop(1)
name.pop()
print(name)"""
                   # list del
"""name=["thala","mass","kancha","boss","sri","ram"]
del name [1:4 ]
print(name)"""

"""name=["thala","mass","kancha","boss","sri","ram"]
name.clear()
print(name)"""
                             #list comparsion
"""name=["thala","mass","kancha","boss","sri","ram"]
empty=[]
for item in name:
    if "t" in item:
     
     empty.append(item)

     print(name)"""

"""name=["thala","mass","kancha","boss","sri","ram"]
empty=[ item for item in name if "k" in item]
print(empty)"""

"""name=["thala","mass","kancha","boss","sri","ram"]
empty=[i for i in name if "m" not in i]
print(empty)"""
                                      # list comparsion
"""thala="hero is the my world forming"
sentence=thala.split()
mass=[item for item in sentence if len(item)>4]
print(mass)"""
     
"""name=["thala","mass","kancha","boss","sri","ram"]
empty=[ item for item in name if"k" in item]
print(empty)

kulla="poorni is also is kullai"
sentence=kulla.split()
entery=[item for item in sentence if len(item)>2]
print(entery)"""                               
                                  #tuple start scartch
"""name=("thala","mass","kancha","boss","sri","ram")
print(type(name))"""
                                 # another tuole
"""name="thala","mass","kancha","boss","sri","ram"
print(name)
print(type(name))"""

#print(name[0:4])

  #condation
  #repation
  #membership

                            
                         # condation 

"""name=("thala","mass","kancha","boss","sri",)
mass=("jaga","madhan","mulai")
preparatiom=name+mass
print(preparatiom)"""

                   #reptation
"""name=("madhan","infreena")
repeated=name*2
print(repeated)
print("madhan"in repeated)
"""
                           #packing
"""name=("naruto","sasukey","sakura","devil")
uzumaking,*uchiya,kupai=name
print(uzumaking)
print(uchiya)
print(kupai)"""
                          #set
"""m={"madhaiyan","tamil",'tamil',"devil","kanchana"}
print(m)"""

"""m=set(("mahaiyan","infreena","mass","loose"))
print(type(m))

name={"madahaiyan","devil",True,1,0,"madhaiyan",False}
print(name)"""
            #Adding and removing item


"""movie={"kanchana","devil","sasukey","devil"}
movie.add("madhaiyan")
print(movie)"""
                    # disccard topic
"""college_name={"Adswak","tamilarsan","praveen","santhosh","poovrsan"}
college_name.discard("soundarya")
print(college_name)"""

                          # clear off
 
"""college_name={"Adswak","tamilarsan","praveen","santhosh","poovrsan"}
college_name.clear()
print(college_name)"""

               #union
 
"""college_name={"Adswak","tamilarsan","praveen","santhosh","poovrsan"}
master={"master","killi","velu"}
#c=college_name.union(master)
c=college_name|(master)
print(c)"""
                       
                       #intersection
 
"""college_name={"Adswak","tamilarsan","praveen","santhosh","poovrsan"}
name={"tamilarsan","praveen"}
c=college_name & name
print(c)""" 
                    
                     # difference A B same ellatha number print agum
 
"""college_name={"Adswak","tamilarsan","praveen","santhosh","poovrsan"}
name={"samey","tamilarsan","praveen"}
c=college_name-name
print(c)"""
                      

                      #dictionary key constator

"""name=dict(bread=23,jam=12,pizza=14,mango_juice=30)
print(name)"""

                #adding in the items
 
"""name=dict(bread=23,jam=12,pizza=14,mango_juice=30)
namee =name["senthil"]=35
print(namee)"""

"""name={"madhaiyan":23,"tamil":21,"praveen":19,}
c=name.get("madhaiyan")
print(c)

"""
                           #remove dictionary item
"""name={"madhaiyan":23,"tamil":21,"praveen":19,}
#name.pop("tamil")
#ame.popitem()
name.clear()
print(name)"""
                       #key values,values
"""name={"madhaiyan":23,"tamil":21,"praveen":19,}
#product=name.keys()
#product=name.values()
print(name.items())"""
                     
                     #nested dictionary
                     
"""name={"madhaiyan":23}
tamil={"tamil":21,}
praveen={"praveen":19,}

madhaiyan={"p1":name,"p2":tamil,"p3":praveen}
print(madhaiyan["p1"],["tamil"])
"""
                                  #function
"""def marriage():
    print("madhaiyan love infreena")
marriage()"""
  
"""def additing():
    a=20
    b=20
    c=a+b
    print(c)
def subraction(a,b):
    c=a+b
    print(c)
additing()
subraction(10,2)"""

 
"""def marriage(ponnu,mapalli):

    print(f"{ponnu} weds {mapalli}")
marriage("infreena","madhaiyan")
"""
    # without argument

"""def adding():
    a=10
    b=20
    c=a+b
    return c
print(adding())
                          # within argument
def addition(a,b):
    c=a+b
    return c
a=int(input("enter in the number"))
b=int(input("enter in the second number"))
print(addition(a,b))

 # three types modules
 1-build in modules
2-extrnal modules
3-user defined modules"""

                        #import module1 as mm

"""from module1 import*

print(name)
mass()
"""
                         #random is automative number create
import random
"""randaom_float=random.random()

print(randaom_float)"""
                                         # randint particular number(1,10)
"""randon_float=random.randint(1,10)
print(randon_float)"""
                                     
                                     #randite.uniform
#print(random.uniform(5,10))
                                    # choiec\
#print(random.choice([1,2,3,4,5,6]))

#8:21
                      #shuffle
"""name=["madhaiyan","tamil","aswak","praveen"]
random.shuffle(name)
print(name"""
                      
                       #sample
"""name=["madhaiyan","tamil","aswak","praveen"]
sampule=random.sample(name,2)
print(sampule)"""
                         #stone papper scessior
rock="""
    
----'_________
     _________)
    (_________)
    (__________)
 _  (__________)  
 | """
papper="""

     ____________
     ____________)
     ______________)
     _____________)
    ____________)
    __________)
"""
scessior="""

    ______
   _______)_______
   _______________)
   _______________)
   _________)
   ______)

"""

"""  
0-rock
1-papper
2-scessior
"""
import random
game=[rock,papper,scessior]

madhaiyan=int(input("enter in the values"))
print("madhaiyan choose",game[madhaiyan])
computer=random.randint(0,2)
print("computer choose",game[computer])

if madhaiyan==0 and computer==2:
    print("madhaiyan you win") 
elif madhaiyan==2 and computer==0:
    print("computer win!,you looser")
elif computer>madhaiyan:
    print("computer win you loose!")
elif madhaiyan>computer:
    print("madhaiyan win ")
elif madhaiyan==computer:
    print("tie in the match")































