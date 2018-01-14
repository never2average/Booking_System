    
def login():
    login_page=Tk()
    menucreator()
    def back():
        login_page.destroy()
    eback=Button(login_page,text='<=Back',command=back)
    eback.grid(row=0,column=0)

    
    username_label=Label(login_page,text='Username:')
    username_label.grid(row=1,column=1,sticky='E')
    username_entry=Entry(login_page)
    username_entry.grid(row=1,column=2)

    password_label=Label(login_page,text='Password:')
    password_label.grid(row=2,column=1,sticky='E')
    password_entry=Entry(login_page,show='*')
    password_entry.grid(row=2,column=2)

    def helpline():
        password_entry.config(state='DISABLED')
        username_entry.config(state='DISABLED')

        rec_emailid_label=Label(login_page,text='enter recovery email address:')
        rec_emailid_label.grid(row=4,column=1,sticky='E')
        rec_emailid_entry=Entry(login_page)
        rec_emailid_entry.grid(row=4,column=2)

        def recovery_help():
            showinfo('','The one time password will be emailed to you.Enter it here and the reset password option will appear.')
        i_button=Button(login_page,text='i',command=recovery_help)
        i_button.grid(row=4,column=3)

        
        def emailsender():
            try:
                part2=["1234","asd1","qwe1","qe1q"]
                server=smtplib.SMTP("smtp.gmail.com",587)
                server.starttls()
                server.login("bondpriyesh@gmail.com","viratkohli")
                global main
                main=part2[random.randint(0,3)]
                msg="YOUR CONFIRMATION CODE IS"+part2[random.randint(0,3)]
                server.sendmail("bondpriyesh@gmail.com",rec_emailid_entry.get())

                otp_label=Label(login_page,text='enter otp:')
                otp_label.grid(row=6,column=1,sticky='E')
                otp_entry=Entry(login_page)
                otp_entry.grid(row=6,column=2)
                def verify_otp():
                    if main==otp_entry.get():
                        comp_fin='update masteruser set password=Default*1 where emailid='+'"'+rec_emailid_entry.get()+'";'
                        cursor.execute(comp_fin)
                        conn.commit()
                otp_verify_button=Button(login_page,text='verify',command=verify_otp)
                otp_verify_button.grid(row=7,column=1)
            except:
                showinfo('','System has encountered an unknown error.')
                login_page.destroy()



        otp_button=Button(login_page,text='send otp',command=emailsender)
        otp_button.grid(row=5,column=2)

        
    forgotpassword_button=Button(login_page,text='Forgot password',command=emailsender)
    forgotpassword_button.grid(row=3,column=1,columnspan=2)

    def logging_in():
        cursor.execute('select * from masteruser;')
        final_checkup=cursor.fetchall()
        for i in final_checkup:
            if i[0]==username_entry.get() and i[1]==password_entry.get():
                global current_table_for_user                     #active users table reference
                current_table_for_user=username_entry.get()
                login_page.destroy()
                airline.config(state='ENABLED')
                train.config(state='ENABLED')
                bus.config(state='ENABLED')
                visa.config(state='ENABLED')
                rentals.config(state='ENABLED')
                holiday.config(state='ENABLED')
                hotels.config(state='ENABLED')

                signup.grid_forget()
                login.grid_forget()

                myaccount_button=Button(root,text='My Account',command=Myaccount_constructor)
                myaccount_button.grid(row=1,column=9,columnspan=2)
                f = font.Font(pref, pref.cget("font"))
                f.configure(underline=True)
                myaccount_button.configure(font=f)

                def myaccount_constructor():
                    account_page=Tk()
                    menucreator()
                    def back():
                        account_page.destroy()
                    mback=Button(account_page,text='<=Back',command=back)
                    mback.grid(row=0,column=0)
                    cursor.execute('select * from '+current_table_for_user+';')
                    myaccount_designer=cursor.fetchall()
                    
                    myusername_label=Label(account_page,text='Username:')
                    myusername_label.grid(row=1,column=1,sticky='E')
                    myusername_data_label=Label(account_page,text=myaccount_designer[0][0])
                    myusername_data_label.grid(row=1,column=2)

                    mypassword_label=Label(login_page,text='Password:')
                    mypassword_label.grid(row=2,column=1,sticky='E')
                    mypassword_entry=Label(account_page,text=myaccount_designer[0][0])
                    mypassword_entry.grid(row=2,column=2)
                    
                    


                    
                    account_page.mainloop()
                
                break
        else:
            showinfo('','The username and password you mentioned do not match please try again.')
                
    go_button=Button(login_page,text='Go',command=logging_in)
    go_button.grid(row=8,column=1)


    
