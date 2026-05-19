client_ident =[]
client_fullname=[]
client_adress=[]
client_mobile=[]
client_email=[]
client_gender=[]
client_age=[]


product_code=[]
product_name=[]
product_quantity=[]
product_unit_val=[]


def mainmenu():
 print(":::market main menu:::")
 print(
    "[1]. register client \n"\
    "[2]. register product \n"\
    "[3]. list client \n"\
    "[4]. list products \n"\
    "[5]. search client by ident \n"\
    "[6]. search product by code \n"\
    "[7]. update client  \n"\
    "[8]. update product \n"\
    "[9]. delete client \n"\
    "[10]. delete product \n"\
    "[11]. exit \n"
    ".::press any option::.")
 

# MAIN
menu_status=True
while menu_status:
    mainmenu()
    opt= input()
    if opt == 1:
       os.system('cls')
       print("::::::::::::::::::::::::::")
       print(":::new client::")
       print("::::::::::::::::::::::::::")

       i = 0
       while i < len(client_fullname[1]}   l    client_fullname}):
          if client_ident[i] == ident:
             print("client already exist. try again")
             break
          i += 1
       ident = input("enter client ident: ")
       fullname = input("enter client fullname: ")
       print("enter client adress: ")
    
    key = input("press any key to back main menu.")
    if opt ==11:
        print("bye bye")
        break
    if opt < 1 and opt > 11:
        print('invalid option. try again '\n
        os.system('pause')
