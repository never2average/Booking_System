from tkinter import *
from tkinter.messagebox import *
import os
import smtplib
root=Tk()
import mysql.connector
root.configure(background='green yellow')
conn=mysql.connector.connect(user='root',password='developer17',host='localhost',database='Users')
cursor=conn.cursor()


#________________________MENU BAR____________________________________________________________________
def menucreator():
    file=Menu(root)
    def exiter():
        root.destroy()
    root.config(menu=file)
    submenu1=Menu(file)
    file.add_cascade(label="File",menu=submenu1)
    submenu1.add_command(label="New tab")
    submenu1.add_command(label="New Window")
    submenu1.add_command(label="Private window")
    submenu1.add_separator()
    submenu1.add_command(label="Settings")
    submenu1.add_command(label="Print")
    submenu1.add_command(label="Help")
    submenu1.add_command(label="Exit",command=exiter)

    submenu2=Menu(file)
    file.add_cascade(label="History",menu=submenu2)
    submenu2.add_command(label="Download History")
    submenu2.add_command(label="Browser History")
    submenu2.add_command(label="Offline pages")
    submenu2.add_command(label="Cookies")



    submenu3=Menu(file)
    file.add_cascade(label="Edit",menu=submenu3)
    submenu3.add_command(label="Zoom In")
    submenu3.add_command(label="Zoom Out")
    submenu3.add_command(label="Font")
    submenu3.add_command(label="Reload")
    submenu3.add_command(label="Cancel")


    submenu4=Menu(file)
    file.add_cascade(label="Bookmarks",menu=submenu4)
    submenu4.add_command(label="Bookmarks folder")
    submenu4.add_command(label="Browser bookmarks")
    submenu4.add_command(label="Import bookmarks")

menucreator()
#______________________________________________________________________________________________________
def airlinebooking():
    airline_main_display=Tk()
    menucreator()

    def back():
        airline_main_display.destroy()
    eback=Button(airline_main_display,text='<=Back',command=back)
    eback.grid(row=0,column=0)


    mainheading=Label(airline_main_display,text='AIRLINE BOOKING SYSTEM',bg='red',fg='white',font=('Copperplate Gothic Bold',35),height=2)
    mainheading.grid(row=1,column=0)


    bookticket=Button(airline_main_display,text='BOOK \n NOW',fg='GREEN',font=('ARIAL BLACK',20))
    bookticket.grid(row=2,column=0)

    photo1=PhotoImage(master=airline_main_display,file='airplane.png')
    mainpic=Label(airline_main_display,image=photo1)
    mainpic.grid(row=2,column=1)

    photo2=PhotoImage(master=airline_main_display,file='WORLDTRAVELAIRLINES.png')
    supportpic=Label(airline_main_display,image=photo2)
    supportpic.grid(row=3,column=2)


    extra=Label(airline_main_display,text='                                                                                              CONTACT US |  F.A.Q',bg='BLUE',fg='YELLOW',width=10)
    extra.grid(row=4,column=0)



    
photo=PhotoImage(file='main.png')
label1=Label(root,image=photo)
label1.grid(row=2,column=2,rowspan=7,columnspan=9)


def suggestion():
    suggest_root=Tk()#dealing with tkinter
    image2=PhotoImage(master=suggest_root,file='help.png')
    helper=Label(suggest_root,image=image2)
    helper.grid(row=1,column=0,columnspan=5)

    def b():
        showinfo('help','choose the required option from drop down menu,click go and click on the pic for more info about the package') 
    info=Button(suggest_root,text="i",command=b)
    info.grid(row=0,column=7)

    choice=StringVar()
    choices=OptionMenu(suggest_root,choice,'"FAMILY"','"CRUISE"','"PILIGRIMAGE"','"INDIVIDUAL"','"NEWLY MARRIED"')
    choices.grid(row=2,column=2)


    def getter_function():
        conn1=mysql.connector.connect(user='root',password='developer17',host='localhost',database='holidays')   #dealing with data
        cursor=conn1.cursor()
        c=choice.get()
        d='select * from suggestion where status='+c+';'
        cursor.execute(d)
        e=cursor.fetchall()
        final=e[0][4]
        extrawin=Tk()
        image3=PhotoImage(master=extrawin,file=final)
        def itinereries():
            os.startfile(e[0][5])
        def back():
            extrawin.destroy()
        eback=Button(extrawin,text='<=Back',command=back)
        eback.grid(row=0,column=0)
        b=Button(extrawin,image=image3,command=itinereries)
        b.grid(row=2,column=0,columnspan=3)
        extrawin.mainloop()

    go=Button(suggest_root,text='go',command=getter_function)
    go.grid(row=2,column=4)
    def rubbish():
        suggest_root.destroy()
    back=Button(suggest_root,text='<=Back',command=rubbish)
    back.grid(row=0,column=0)
    suggest_root.mainloop()
def a():
    pass
airline=Button(root,text='AIRLINE BOOKING',bg='orange',fg='black',width=30,height=5,command=a,state='disabled')
airline.grid(row=2,column=0)


train=Button(root,text='TRAIN\nRESERVATION',fg='white',bg='black',width=30,height=5,state='disabled',command=a)
train.grid(row=3,column=0)

bus=Button(root,text='BUS TICKETS',bg='orange',fg='black',width=30,state='disabled',height=5,command=a)
bus.grid(row=4,column=0)

visa=Button(root,text='VISA PROCESSING',fg='white',bg='black',width=30,height=5,state='disabled',command=a)
visa.grid(row=5,column=0)

rental=Button(root,text='RENT A CAR',bg='orange',fg='black',width=30,height=5,state='disabled',command=a)
rental.grid(row=6,column=0)

holiday=Button(root,text='HOLIDAY PACKAGE',fg='white',bg='black',height=5,width=30,state='disabled',command=a)
holiday.grid(row=7,column=0)

hotels=Button(root,text='HOTELS NEAR ME',bg='orange',fg='black',height=5,width=30,state='disabled',command=a)
hotels.grid(row=8,column=0)

suggest=Button(root,text='S\nU\nG\nG\nE\nS\nT\n\nM\nE\n\nA\n\nH\nO\nL\nI\nD\nA\nY',bg='black',fg='white',width=2,height=45,command=suggestion)
suggest.grid(row=1,rowspan=8,column=11)



#to be continued
def signup():
    signup_page=Tk()
    def execute():
        signup_page.destroy()
    backbutton=Button(signup_page,text="<=Back",command=execute)
    
    
    username_label=Label(signup_page,text='Username:')
    username_label.grid(row=1,column=0,sticky='E')
    username_entry=Entry(signup_page,show='*')
    username_entry.grid(row=1,column=1)

    password_label=Label(signup_page,text='Password:')
    password_label.grid(row=2,column=0,sticky='E')
    password_entry=Entry(signup_page,show='*')
    password_entry.grid(row=2,column=1)
    def passreq():
        showinfo("password requirements","The password must contain atleast 1 number,1\nspecial character and 1 capital letter.")
    info=Button(signup_page,text='info',command=passreq)
    info.grid(row=2,column=2)
    
    confirmpassword_label=Label(signup_page,text='Confirm Password:')
    confirmpassword_label.grid(row=3,column=0,sticky='E')
    confirmpassword_entry=Entry(signup_page,show='*')
    confirmpassword_entry.grid(row=3,column=1)

    emailid_label=Label(signup_page,text='Email id:')
    emailid_label.grid(row=4,column=0,sticky='E')
    emailid_entry=Entry(signup_page)
    emailid_entry.grid(row=4,column=1)


    date_of_birth_label=Label(signup_page,text='Date of Birth:')
    date_of_birth_label.grid(row=5,column=0,sticky='E')

    month_choice=StringVar()
    month=OptionMenu(signup_page,month_choice,'January','Febraury','March','April','May','June','July','August','September','October','November','December')
    month.grid(row=5,column=2)


    date_choice=StringVar()
    date=OptionMenu(signup_page,date_choice,'01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28')
    date.grid(row=5,column=1)


    year_choice=StringVar()
    year=OptionMenu(signup_page,year_choice,'1920','1921','1922','1923','1924','1925','1926','1927','1928','1929','1930','1931','1932','1933','1934','1935','1936','1937','1938','1939','1940','1941','1942','1943','1944','1945','1946','1947','1948','1949','1950','1951','1952','1953','1954','1955','1956','1957','1958','1959','1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999')
    year.grid(row=5,column=3)

    gender_label=Label(signup_page,text='Gender:')
    gender_label.grid(row=6,column=0,sticky='E')
    gender_choice=IntVar()
    male= Radiobutton(signup_page, text="Male",variable=gender_choice,value=1)
    male.grid(row=6,column=1)
    female= Radiobutton(signup_page, text="Female",variable=gender_choice,value=2)
    female.grid(row=6,column=2)

    
    securityquestion_label=Label(signup_page,text="choose a security question:")
    securityquestion_label.grid(row=7,column=0,sticky="E")
    sec_choice=StringVar()
    securityquestion_option=OptionMenu(signup_page,sec_choice,'"What is the name of your elementary school?"','"What is the name of the first book you read?"','"Where did you hide after bunking school?"','"What was your favorite animated film?"','"What was your favorite sport in school?"')
    securityquestion_option.grid(row=7,column=1)
    
    securityanswer_label=Label(signup_page,text="Answer:")
    securityanswer_label.grid(row=8,column=0,sticky="E")
    securityanswer_entry=Entry(signup_page)
    securityanswer_entry.grid(row=8,column=1)
    def message():
        showinfo('',"The answer must not exceed 20 charcters")
    securityanswer_button=Button(signup_page,text="(i)",command=message)
    securityanswer_button.grid(row=8,column=2)



    mobile_label=Label(signup_page,text='Mobile No:')
    mobile_label.grid(row=9,column=0,sticky='E')
    mobile_entry=Entry(signup_page)
    mobile_entry.grid(row=9,column=1)

    nationality_label=Label(signup_page,text='Nationality:')
    nationality_label.grid(row=10,column=0,sticky='E')
    nationality_entry=Entry(signup_page)
    nationality_entry.grid(row=10,column=1)

    permaddress_label=Label(signup_page,text='Permanent Address:')
    permaddress_label.grid(row=11,column=0)
    permaddress_entry=Entry(signup_page)
    permaddress_entry.grid(row=11,column=1)
    




    
    cardno_label=Label(signup_page,text="enter your 12 digit credit card no:")
    cardno_label.grid(row=12,column=0)
    cardno_entry=Entry(signup_page)
    cardno_entry.grid(row=12,column=1)
    def cardnomessage():
        showinfo('',"We ask credit card numbers only to save your time \n during payment and to protect our site from bots .\nDo note that your data is safe and we do not share these sensitive information with third parties.\nRegards,\n Priyesh Srivastava.")
    cardno_message=Button(signup_page,text='i')
    cardno_message.grid(row=12,column=2)

    tandcvar=IntVar()
    tandc=Checkbutton(signup_page,variable=tandcvar,onvalue=1,offvalue=0)
    tandc.grid(row=13,column=0)
    def tandcfunction():
        os.startfile('terms_and_conditions.pdf')
    tandc_button=Button(signup_page,text='I agree to the terms and conditions',command=tandcfunction)
    tandc_button.grid(row=13,column=1)

    global final
    final=False
    

    
    def securitycode():
        username_entry.config(state='DISABLED')
        password_entry.config(state='DISABLED')
        emailid_entry.config(state='DISABLED')
        confirmpassword_entry.config(state='DISABLED')
        securityquestion_option.config(state='DISABLED')
        securityanswer_entry.config(state='DISABLED')
        cardno_entry.config(state='DISABLED')
        mobile_entry.config(state='DISABLED')
        nationality_entry.config(state='DISABLED')
        permaddress_entry.config(state='DISABLED')
        
        try:
            part2=["1234","asd1","qwe1","qe1q"]
            server=smtplib.SMTP("smtp.gmail.com",587)
            server.starttls()
            server.login("bondpriyesh@gmail.com","viratkohli")
            main=part2[random.randint(0,3)]
            msg="YOUR CONFIRMATION CODE IS"+part2[random.randint(0,3)]
            server.sendmail("bondpriyesh@gmail.com",emailid_entry.get())
        except:
            showinfo('','registration not completed as emailid was incorrect')
            execute()

        

        confirmation_label=Label(signup_page,text='confirmation code:')
        confirmation_label.grid(row=14,column=0,sticky='E')
        confirmation_entry=Entry(signup_page)
        confirmation_entry.grid(row=14,column=1)

        def registration():
            mishmash='"'+username_entry.get()+'","'+password_entry.get()+'","'+emailid_entry.get()+'","'+date_choice.get()+'-'+month_choice.get()+'-'+year_choice.get()+'-'+'","'+mobile_entry.get()+'","'+nationality_entry.get()+'","'+permaddress_entry.get()+'","'+sec_choice.get()+'","'+securityanswer_entry.get()+'","'+cardno_entry.get()+'","'
            mishmash_final='insert into masteruser values('+mishmash+');'

            cursor.execute(mishmash_final)
            conn.commit()

            personal_table='create table '+username_entry.get()+'(tickettype varchar(10),modeno varchar(10),bookingnumber varchar(7),ticketnumber varchar(8),seattype varchar(12),addons varchar(80),passengername varchar(30),passengerage numeric(3),passportno varchar(8),concession varchar(30),departuredate varchar(10),departuetime varchar(4),seatnumber varchar(3) ;' 
            cursor.execute(personal_table)
            conn.commit()
            showinfo('','Congratulations on creating your account try logging in to your account.')
            execute()
            
        register_button=Button(signup_page,text="Register Now",command=registration)
        register_button.grid(row=15,column=1)

        

    def check_emailid():
        if emailid_entry.get()==' ':
            showinfo('','invalid emailid')
            final=False
        else:
            check_nonsense=list(emailid_entry.get())
            if '@' in check_nonsense:
                cursor.execute('select * from masteruser;')
                mail_exists=cursor.fetchall()
                for i in mail_exists:
                    if i[2]==emailid_entry.get():
                        showinfo('','The email id already exists.Try logging into your account')
                        final=False
                        break
                    else:
                        pass
                else:
                    final=True
            else:
                showinfo('','invalid emailid')
                final=False
            if final==True:
                securitycode()
                
        
                


        
    def check_password():
        if password_entry.get()!=confirmpassword_entry.get():
            showinfo('','Passwords do not match')
        else:
            if len(password_entry.get())<8:
                showinfo('','Password does not meet requirements')
            else:
                spl_char=num_char=caps_char=0
                pass_split=list(password_entry.get())
                for i in pass_split:
                    if i.isdigit():
                        num_char+=1
                    elif i.isupper():
                        caps_char+=1
                    elif i.isalpha():
                        pass
                    else:
                        spl_char+=1
                if spl_char<1 or num_char<1 or caps_char<1:
                    showinfo('','Password does not meet requirements')
                    final=False
                else:
                    final=True
                if final==True:
                    check_emailid()
                else:
                    pass



    
    def check_username():        
        cursor.execute('select * from masteruser;')
        user_exists=cursor.fetchall()
        for i in user_exists:
            if i[0]==username_entry.get():
                showinfo('','The username you have chosen already \n exists.Please choose another one or login to your account.')
                final=False
                break
        else:
            final=True
        if final==True:
            check_password()
    continue_button=Button(signup_page,text="Continue",command=check_username)
    continue_button.grid(row=14,column=0)
    signup_page.mainloop()


signup=Button(root,text='SIGN UP',bg='blue',fg='white',width=20,height=4,command=signup)
signup.grid(row=1,column=9)

login=Button(root,text='LOGIN',bg='red',fg='black',width=20,command=a,height=4)
login.grid(row=1,column=10)

blank=Label(root,text='                                                                                                                                                                                                                                     ',bg='grey')
blank.grid(row=10,column=0,columnspan=8)

def contactus():
        showinfo("contact details","Ph: +91 7043098705 \n Email: kmatravels@gmail.com")
contact=Button(root,text='CONTACT US',command=contactus,width=20)
contact.grid(row=10,column=9)

def faq1():
    os.startfile('FAQ.pdf')
    
faq=Button(root,text='FAQ',command=faq1,width=20)
faq.grid(row=10,column=10)


root.mainloop()
