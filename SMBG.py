from datetime import datetime

name= input("Enter your name:")
#Lists of Items
lists='''

Rice    $ 2/Kg
Sugar   $ 3/kg
Salt    $ 2kg
Oil     $ 8/litre
Paneer  $ 11Kg
Maggi   $ 5/Kg
Boost   $ 9/Each
Colgate $ 4/Each

'''
#Declaration
Price=0
Pricelist=[]
Totalprice=0
Finalprice=0
ilist=[]
qlist=[]
plist=[]
#Rates for items
items={'Rice':2,'Salt':2,'Sugar':3,'Oil':8,'Paneer':11,'Maggi':5,'Boost':9,'Colgate':4}
option=int(input("For list of items press 1"))
if option==1:
    print(lists)
#elif option!=1:
    #exit()
for i in range(len(items)):
    inp1=int(input("If you want to buy press1 or 2 for exit"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items")
        quantity=int(input("Enter quantity"))
        if item in items.keys():
                Price=quantity*(items[item])
                Pricelist.append((item,quantity,items,Price))
                Totalprice+=Price
                ilist.append(item)
                qlist.append(quantity)
                plist.append(Price)
                gst=(Totalprice*5)/100
                Finalprice=gst+Totalprice
        else:
         print("You entered item is not available")
    else:
        print("You entered wrong number")


    inp=input("Can i bill the itesms yes or no:")
    if inp=='yes':
        pass
        if Finalprice!=0:
            print(25*"=","Santosh Supermarket",25*"=")
            print(28*"=","Hyderabad",30*"=")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"_")

            print("sno",1,10*" ",'items',item,10*" ",'quantity',quantity,10*" ",'Price  $',Price)
           # print("sno",10*" ",'items',10*" ",'quantity',10*" ",'Price')





            for i in range(len(Pricelist)):
                #print(i,8*' ',8*' ',ilist[i],3*' ',qlist[i],plist[i])
                print(75*"_")
                print(50*" ",'Totalprice:','$',Totalprice)
                print(50*" ",'gst amount:','$',gst)

                print(75*"_")
                print(50*" ",'finalprice:','$',Finalprice)
                print(75*" ")
print(50*" ","Thanks for visiting")
print(75*"_")
