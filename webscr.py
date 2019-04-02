from bs4 import BeautifulSoup
import requests
import mysql.connector
import inspect
import unittest

mydb = mysql.connector.connect(
  host="localhost",
  user="dinesh",
  passwd="Dinesh21",
 database="python"
)
mycursor=mydb.cursor()


def deco(func):
    def wrapper(name):
        mycursor.execute('SELECT * FROM user where username="%s"'%name)
        count=0
        for x in mycursor:
            count+=1
        if(count>0):
            func(name)
        else:
           return 0
    return wrapper

@deco        
def check(name):
      print('present')
      return 1
         
class person:
    def __init__(self):
        self.city="Roorkee"
    def initiate(self,p_name,*argv):
        self.name=p_name
        self.favourite={}
        for arg in argv:
            if(type(arg)==type([])):
                self.work = arg
            elif(type(arg)==type({})):
               self.favourite=arg
            else:
              self.city=arg



def scrap(username):
   name=soup.find_all('a',attrs={'class':'_2nlw _2nlv'})
   for data in name:
     name_a=data.text
    # print("name",data.text)
  
   work1 =soup.find_all('div',attrs={'class':'_4qm1'})
   for data in work1:
      work2=data
      break
  
  #  print("\nWorks:")
   work3=work2.find_all('div',attrs={'class':'_6a _6b'})
   for data in work3:
      work5=data.find_all('div',attrs={'class':'_2lzr _50f5 _50f7'})
      for data2 in work5:
        work_a.append(data.a.text)
        # print(data.a.text)
  
   city=soup.find_all('span',attrs={'class':'_2iel _50f7'})
   for data in city:
     city_a=data.text
    #  print("city",data.text)
     break
  
   value_f = soup.find_all('div',attrs={'class':'mediaPageName'})
   key_f=soup.find_all('th',attrs={'class':'label'})
  
   for i in range(len(value_f)):
     key=key_f[i].text
     favourites[key]=value_f[i].text
  
   if(work_a!=[] and city_a!=''):
     p[username].initiate(name_a,work_a,city_a,favourites)
   elif(work_a!=[] and city_a==''):
     p[username].initiate(name_a,work_a,favourites)
   elif(work_a==[] and city_a!=''):
     p[username].initiate(name_a,city_a,favourites)
   else:
     p[username].initiate(name_a,favourites)
  
p={}
checked={}

n=int(input("Enter number of usernames\n"))
for i in range(n):
  username=input("Enter the username\n")
  flag=check(username)
  if(flag==0):
    raise Exception("Username not Present")
    print("username not present")
  else:
    flag2=0
    if(username in checked):
      flag2=1
    if(flag2==0):
      page_link="https://en-gb.facebook.com/%s"%username
      page_response=requests.get(page_link)
      soup=BeautifulSoup(page_response.content,"html.parser")
      name_a=''
      work_a=[]
      city_a=''
      favourites={}
      checked[username]=1
      p[username]=person()
      scrap(username)
      
    print("name : ",p[username].name)
    print("\n")

    print("city:",p[username].city)
    print("\n")

    attr=[i for i in dir(p[username])]
    if('work' in attr):
      if(p[username].work!=[]):
        print("work:",end=" ")
        print(p[username].work)
        print("\n")
    
    print("Favourites :",end=" ")
    if(p[username].favourite!={}):
      print(p[username].favourite)
      print("\n")
    else:
      print("No Favourites\n")

  
class test1(unittest.TestCase):
  
  def test_decorator(self):
     flag3=check("k4ni5h")
     if(flag3!=0):
       flag3=1
   
     flag2=0
     mycursor.execute('SELECT * FROM user where username="k4ni5h"')
     count2=0
     flag2=0
     for x in mycursor:
       count2+=1
     if(count2>0):
       flag2=1
     self.assertEqual(flag2,flag3)
     self.assertRaises(Exception,"Username existence",check,"k4ni5h")

  def test_class_name(self):
      s=person()
      s.initiate("swapnil")
      self.assertEqual("swapnil",s.name)
      self.assertEqual(s.city,"Roorkee") 
      self.assertRaises(Exception,"city name should be Roorkee by default")

      flag4=0
      attr=[i for i in dir(s)]
      if('work' in attr):
        flag4=1
  
      self.assertEqual(flag4,0)
      self.assertRaises(Exception,"work should not initialized",s.initiate,"swapnil")


      self.assertEqual(s.favourite,{})

      s.initiate("djs","kdnf",["fg","dfd"])
      self.assertEqual("kdnf",s.city)
      self.assertRaises(Exception,"city name should be updated")

      self.assertEqual(s.work,["fg","dfd"])
      

      

if __name__ == '__main__':
    unittest.main()

  
  


  



   