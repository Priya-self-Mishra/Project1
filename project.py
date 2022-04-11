x=True
while x==True :
    print("""

                                ************** WELCOME TO MISSION DEVELOPMENT PROJECT ***************


                                """)
    #creating database connectivity
    import mysql.connector
    passwd=str(input("enter your database password :"))
    sql=mysql.connector.connect(host="localhost",user="root",password=passwd)
    cursor=sql.cursor()
    #creating database
    cursor.execute("create database if not exists Mission_Development")
    cursor.execute("use Mission_Development")
    #creating needed tables
    cursor.execute("create table if not exists Project_Details(Project_id int(8)Primary key auto_increment,Position int(3)Not Null unique,Name varchar(20)Not Null,Outlay double(10,2)Not Null,Address varchar(50)Not Null,expected_time varchar(15)Not Null,covered_Area varchar(15)Not Null,Status varchar(10))")
    cursor.execute("create table if not exists Contractor_Details(Company_id int(8)Primary key auto_increment,Position int(3)Not Null unique,Company_Name varchar(25)Not Null,Contact_No int(12)Not Null,Incharge_Name varchar(15)Not Null,incharge_contact_no int(12)Not Null,Total_Workers int(3)Not Null,Status varchar(10))")
    cursor.execute("create table if not exists source_of_money(Project_id int(8)Primary key auto_increment,Position int(3)Not Null unique,State_govt double(10,2)Not Null,Central_govt double(10,2)Not Null,Local_bodies double(10,2)Not Null,Private_companies double(10,2)Not Null,Status varchar(10))")
    cursor.execute("create table if not exists Feedback(Project_id int(8)Primary Key auto_increment,Position int(3)Not Null unique,Ongoing varchar(10)Not Null,Issue varchar(70)Not Null,Status varchar(10))")
    #creating table for sorting the user name and password
    cursor.execute("create table if not exists user_Details(User_Name varchar(15),User_Password varchar(8))")
    def delete(f):
        #Deleting Selected Record from all the tables
        cursor.execute("Delete from Project_Details where Position='"+str(f)+"'")
        cursor.execute("Delete from Contractor_Details where Position='"+str(f)+"'")
        cursor.execute("Delete from Feedback where Position='"+str(f)+"'")
        cursor.execute("Delete from Source_of_Money where Position='"+str(f)+"'")
        sql.commit()
        print("Deleted Successfully")
    while x==True:
        print("""
                                                                                1. Sign in 
                                                                                2. Sign up
                                                                                """)
    
        r=int(input("enter your choice:"))
    
    
    
        # if user wants to register
        if r==2:
            print("""

                                                   .................Register yourself.................

                                                   
                                                    """)
            u=input("Enter your username:")
            p=input("Enter your password:")
            #inserting the entered details in user detail table
            cursor.execute("insert into user_details values('"+u+"','"+p+"')")
            sql.commit()
    
    
            print("""
                                                  ...................Registered successfully..................
                                     
                                     
                                                    """)
            
        #if user wants to sign in
        elif r==1:

            print("""
                                                       .....................Sign in......................

                                                       
                                                        """)
            un=input("Enter your Username:")
            ps=input("Enter your password:")
            print("""

                                 ...............Signing you in ................

                                 """)
                
            cursor.execute("select User_Password from user_details where User_name='"+un+"'")
            row=cursor.fetchall()
            for i in row:
                a=list(i)
                if a[0]==str(ps):
                    while x==True:
                        #displaying various tables on which user can perform 
                        print("""
                                                  1 .Details of projects
                                                  2 .Details of contractors
                                                  3 .Finance
                                                  4 .Feedback
                                                  5 .Sign Out

                                                  """)
                        ch=int(input("Enter your choice: "))
                        if ch==1:
                            #displaying the tasks that user can perform
                            print("""
                                                        1 .Show Record
                                                        2 .Add New Record
                                                        3 .Delete Existing record
                                                        4 .Update
                                                        5 .Previous
                                                 """)
                            b=int(input("Enter your choice: "))
                            if b==1:
                                print("""
       
                                                       1. All records
                                                       2. Pariticular Record

                                             """)
                                c=int(input("Enter your choice: "))
                                if c==1:
                                    # Displaying all record which are in this table
                                    cursor.execute("select Position,Name,Outlay,Address,expected_time,covered_Area,Status from Project_Details")
                                    row=cursor.fetchall()
                                    for i in row:
                                        v=list(i)
                                        k=["Position","Name ","Outlay","Address","expected_time","covered_Area ","Status"]
                                        d=dict(zip(k,v))
                                        print(d)
                                else:
                                    #To show particular record
                                    f=int(input("what is the Position of that project which you want to see: "))
                                    cursor.execute("select Position,Name,Outlay,Address,expected_time,covered_Area,Status from Project_Details where Position ='"+str(f)+"'")
                                    row=cursor.fetchall()
                                    for i in row:
                                        v=list(i)
                                        k=["Position","Name ","Outlay","Address","expected_time","covered_Area ","Status"]
                                        d=dict(zip(k,v))
                                        print(d)
                            elif b==2:
                                q=int(input("How many Records you want to add:"))
                                for q in range(0,q):
                                    try:
                                        #Asking the details
                                        name=input("Enter Name of the Project:")
                                        Outlay=int(input("Enter Expected Money:"))
                                        address=input("Enter Name of the locality:")
                                        time=int(input("Enter expected time(in months only):"))
                                        area=int(input("Enter its covered Area(in metre square):"))
                                        Position=int(input("Enter position:"))
                                        statusrecord="Active"
                                        #inserting the details in table
                                        cursor.execute("insert into Project_Details (Position,Name,Outlay,Address,expected_time,covered_Area,Status) values('"+str(Position)+"','"+name+"','"+str(Outlay)+"','"+address+"','"+str(time)+"','"+str(area)+"','"+statusrecord+"')")
                                        sql.commit()
                                        print("""
                                             ...........Added your record successfully........
                                                """)
                                    except:
                                        print("""
                                                      .....Please Check "Position".....
                                                      """)
                            elif b==3:
                                # To know whether user really wanted to loose his record
                                p=input("Do you really want to delete(Y/N): ")
                                if p=="Y":
                                    f=int(input("Enter the Position of that project which you want to delete:"))
                                    #Deleting Selected Record
                                    delete(f)
                                else:
                                    pass
                            elif b==4:
                                print("""
                                                     1 Name
                                                     2 Outlay
                                                     3 Address
                                                     4 expected time
                                                     5 Area
                                                     6 Position
                                                     7 Status

                                           """)
                                row=cursor.execute("SELECT ALL position FROM  Project_Details")
                                print("""
                                          ..................These all are various Position...................
                                                            """)
                                #Here, We are showing that what ids User have
                                row=cursor.fetchall()
                                for i in row:
                                    v=list(i)
                                    k=["Position"]
                                    d=dict(zip(k,v))
                                    print(d)
                                q=int(input("how many items you want to update: "))
                                # Here, We are updating the existing Records
                                for a in range(0,q):
                                    p=int(input("What you want to change: "))
                                    if p==1:
                                        n=int(input("Enter Position  of that Project: "))
                                        f=input("Enter new name: ")
                                        cursor.execute("update Project_Details set Name='"+f+"' where Position='"+str(n)+"'")
                                        print("""
                                                      ......Data Updated sucessfully......
                                          """)
                                    elif p==2:
                                        n=int(input("Enter Position  of that Project: "))
                                        f=int(input("Enter new Outlay: "))
                                        cursor.execute("update Project_Details set Outlay='"+str(f)+"' where Position='"+str(n)+"'")
                                        print("""
                                                      ......Data Updated sucessfully......
                                          """)
                                    elif p==3:
                                        n=int(input("Enter Position  of that Project: "))
                                        f=input("Enter new Address: ")
                                        cursor.execute("update Project_Details set Address='"+f+"' where Position='"+str(n)+"'")
                                        print("""
                                                              ......Data Updated sucessfully......
                                          """)
                                    elif p==4:
                                        n=int(input("Enter Position of that Project: "))
                                        f=int(input("Enter new  expected time(in months): "))
                                        cursor.execute("update Project_Details set expected_time='"+str(f)+"' where Position='"+str(n)+"'")
                                        print("""
                                                     ......Data Updated sucessfully......
                                                   """)
                                    elif p==5:
                                        n=int(input("Enter Position of that Project: "))
                                        f=int(input("Enter new Area(in metre square): "))
                                        cursor.execute("update Project_Details set covered_Area='"+str(f)+"' where Position='"+str(n)+"'")
                                        print("""
                                                 ......Data Updated sucessfully......
                                                   """)
                                    elif p==6:
                                        n=int(input("Enter Position of that Project: "))
                                        f=int(input("Enter new Position: "))
                                        cursor.execute("update Project_Details set Position ='"+str(f)+"' where Position='"+str(n)+"'")
                                        print("""
                                                    ......Data Updated sucessfully......
                                                    """)
                                    elif p==7:
                                        n=int(input("Enter Position of that Project: "))
                                        f=input("Enter new Status: ")
                                        cursor.execute("update Project_Details set Status ='"+f+"' where Position='"+str(n)+"'")
                                        print("""
                                                    ......Data Updated sucessfully......
                                                    """)
                                    else:
                                        print("Enter correct choice")
                            elif b==5:
                                pass
                            else:
                                print("""
                                          Enter correct choice
                                            
                                                 """)
                        elif ch==2:
                            print("""
    
                                                        1 .Show Record
                                                        2 .Add New Record
                                                        3 .Delete Existing record
                                                        4 .Update
                                                        5 .Previous

                                                  """)
                            b=int(input("Enter your choice: "))
                            if b==1:
                                print("""

                                                              1. All records
                                                              2. Pariticular Record

                                             """)
                                c=int(input("Enter your choice: "))
                                if c==1:
                                    # Displaying all record which are in this table
                                    cursor.execute("select Position,Company_Name,Contact_No,Incharge_Name,incharge_contact_no,Total_Workers,Status from  Contractor_Details")
                                    row=cursor.fetchall()
                                    for i in row:
                                        v=list(i)
                                        k=["Position","name","Contact_No" ,"Incharge_Name","incharge_contact_no" ,"Total_Workers\n","Status/n"]
                                        d=dict(zip(k,v))
                                        print(d)
                                else:
                                    #To display particular record
                                    f=int(input("what is the Position of that project which you want to see: "))
                                    cursor.execute("select Position,Company_Name,Contact_No,Incharge_Name,incharge_contact_no,Total_Workers,Status  from Contractor_Details where Position ='"+str(f)+"'")
                                    row=cursor.fetchall()
                                    for i in row:
                                        v=list(i)
                                        k=["Position","name","Contact_No" ,"Incharge_Name","incharge_contact_no" ,"Total_Workers","status"]
                                        d=dict(zip(k,v))
                                        print(d)
                            elif b==2:
                                q=int(input("How many Records you want to add:"))
                                for q in range(0,q):
                                    try:
                                        #Asking the details
                                        Position=int(input("Enter Position of the Project:"))
                                        Company_name=input("Enter Name of the Company name:")
                                        Contact_no=int(input("Enter Contact no:"))
                                        Incharge_name=input("Enter Name of Incharge:")
                                        Contact_no=int(input("Enter Contact No :"))
                                        Total_Worker=int(input("Enter total no workers:"))
                                        Statusrecord="Active"
                                        #inserting the details in table
                                        cursor.execute("insert into Contractor_Details (Position,Company_Name,Contact_No,Incharge_Name,incharge_contact_no,Total_Workers,Status)values('"+str(Position)+"','"+Company_name+"','"+str(Contact_no)+"','"+Incharge_name+"','"+str(Contact_no)+"','"+str(Total_Worker)+"','"+Statusrecord+"')")
                                        sql.commit()
                                        print("""
                                                        ................Added your record successfully............
                                                        """)
                                    except:
                                        print("""
                                                      .....Please check Position......
                                                      """)
                            elif b==3:
                                # To know whether user really wanted to loose his record
                                p=input("Do you really want to delete(Y/N): ")
                                if p=="Y":
                                    f=int(input("Enter the Position of that project which you want to delete:"))
                                    #Deleting Selected Record
                                    delete(f)
                                else:
                                    pass
                            elif b==4:
                                print("""
                                                     1 Position
                                                     2 Company_Name
                                                     3 Contact_No
                                                     4 Incharge_Name
                                                     5 incharge_contact_no
                                                     6 Total_Workers
                                                     7 Status

                                           """)
                                row=cursor.execute("SELECT ALL Position FROM  Contractor_Details")
                                print("""
                                          ..................These all are various Positions ...................
                                                            """)
                                #Here, We are showing that what ids User have
                                row=cursor.fetchall()
                                for i in row:
                                    v=list(i)
                                    k=["Position"]
                                    d=dict(zip(k,v))
                                    print(d)
                                q=int(input("how many things you want to update: "))
                                # Here, We are updating the existing Records
                                for a in range(0,q):
                                    p=int(input("What you want to change: "))
                                    if p==1:
                                        n=int(input("Enter Position of that Project: "))
                                        f=int(input("Enter new Position: "))
                                        cursor.execute("update Contractor_Details set Position='"+str(f)+"' where Position='"+str(n)+"'")
                                        print("""
                                                      ......Data Updated sucessfully......
                                                        """)
                                    elif p==2:
                                        n=int(input("Enter Position  of that Project: "))
                                        f=input("Enter new Name: ")
                                        cursor.execute("update Contractor_Details set Company_Name='"+f+"' where Position='"+str(n)+"'")
                                        print("""
                                                      ......Data Updated sucessfully......
                                                        """)
                                    elif p==3:
                                        n=int(input("Enter Position of that Project: "))
                                        f=int(input("Enter new contact no: "))
                                        cursor.execute("update Contractor_Details set Contact_No ='"+str(f)+"' where Position='"+str(n)+"'")
                                        print("""
                                                      ......Data Updated sucessfully......
                                                        """)
                                    elif p==4:
                                        n=int(input("Enter Position of that Project: "))
                                        f=input("Enter new Incharge Name: ")
                                        cursor.execute("update Contractor_Details set Incharge_Name='"+f+"' where Position='"+str(n)+"'")
                                        print("""
                                                      ......Data Updated sucessfully......
                                                        """)
                                    elif p==5:
                                        n=int(input("Enter Position of that Project: "))
                                        f=int(input("Enter new  Contact no of Incharge: "))
                                        cursor.execute("update Contractor_Details set Incharge_contact_no ='"+str(f)+"' where Position='"+str(n)+"'")
                                        print("""
                                                      ......Data Updated sucessfully......
                                                        """)
                                    elif p==6:
                                        n=int(input("Enter Position of that Project: "))
                                        f=int(input("Enter new no of workers: "))
                                        cursor.execute("update Contractor_Details set Total_Workers='"+str(f)+"' where Position='"+str(n)+"'")
                                        print("""
                                                      ......Data Updated sucessfully......
                                                        """)
                                    elif p==7:
                                        n=int(input("Enter Position of that Project: "))
                                        f=input("Enter new status: ")
                                        cursor.execute("update Contractor_Details set Status='"+f+"' where Position='"+str(n)+"'")
                                        print("""
                                                      ......Data Updated sucessfully......
                                                        """)
                                    else:
                                        print("Enter correct choice")
                            elif b==5:
                                    pass
                            else:
                                print("""
                                          Enter correct choice
                                            
                                                 """)
                        elif ch==3:
                            print("""
                                                      1 .Show Record
                                                      2 .Add New Record
                                                      3 .Delete Existing record
                                                      4 .Update
                                                      5 .Previous
                                                      
                                                 """)
                            b=int(input("Enter your choice: "))
                            if b==1:
                                print("""

                                                     1. All records
                                                     2. Pariticular Record

                                             """)
                                c=int(input("Enter your choice: "))
                                # Displaying all record which are in this table
                                if c==1:
                                    cursor.execute("select Position,State_govt,Central_govt,Local_bodies,Private_companies,Status from  Source_of_Money")
                                    row=cursor.fetchall()
                                    for i in row:
                                        v=list(i)
                                        k=["Position","State_govt"," Central_govt"," Local_bodies","Private_companies","status"]
                                        d=dict(zip(k,v))
                                        print(d)
                                else:
                                    #To show particular record
                                    f=int(input("what is the Position of that project which you want to see: "))
                                    cursor.execute("select Position,State_govt,Central_govt,Local_bodies,Private_companies,Status from Source_of_Money where Position='"+str(f)+"'")
                                    row=cursor.fetchall()
                                    for i in row:
                                        v=list(i)
                                        k=["Position","State_govt"," Central_govt"," Local_bodies","Private_companies","status"]
                                        d=dict(zip(k,v))
                                        print(d)
                            elif b==2:
                                q=int(input("How many Records you want to add:"))
                                for q in range(0,q):
                                    #Asking the details
                                    try:
                                        Position=int(input("Enter Position of the Project:"))
                                        state=int(input("Enter the amount of money given by state govt:"))
                                        central=int(input("Enter the amount of money given by central govt:"))
                                        local=int(input("Enter the amount of money taken from Local people:"))
                                        Private=int(input("Enter the amount of money given by Private Companies:"))
                                        statusrecord="Active"
                                        #inserting the details in table
                                        cursor.execute("insert into Source_of_Money (Position,State_govt,Central_govt,Local_bodies,Private_companies,Status) values('"+str(Position)+"','"+str(state)+"','"+str(central)+"','"+str(local)+"','"+str(Private)+"','"+statusrecord+"')")
                                        sql.commit()
                                        print("""
                                                      ...............Added your record successfully.................
                                                      """)
                                    except:
                                        print("""
                                                   ......Please Check Position ......""")
                            elif b==3 :
                                # To know whether user really wanted to loose his record
                                p=input("Do you really want to delete(Y/N): ")
                                if p=="Y":
                                    f=int(input("Enter the Position of that project which you want to delete:"))
                                    #Deleting Selected Record
                                    delete(f)
                                else:
                                    pass
                            elif b==4:
                                print("""
                                                     1 Position 
                                                     2 State govt
                                                     3 Central govt
                                                     4 Local bodies
                                                     5 Private companies
                                                     6 status

                                           """)
                                cursor.execute("SELECT ALL Position FROM Source_of_Money")
                                print("""
                                          ..................These all are various Positions...................
                                                            """)
                                #Here, We are showing that what ids User have
                                row=cursor.fetchall()
                                for i in row:
                                    v=list(i)
                                    k=["Position"]
                                    d=dict(zip(k,v))
                                    print(d)
                                q=int(input("how many things you want to update: "))
                                # Here, We are updating the existing Records
                                for a in range(0,q):
                                    p=int(input("What you want to change: "))
                                    if p==1:
                                        n=int(input("Enter Position of that Project: "))
                                        f=int(input("Enter new  Position: "))
                                        cursor.execute("update Source_of_Money set Position ='"+str(f)+"' where Position='"+str(n)+"'")
                                        print("""
                                                      ......Data Updated sucessfully......
                                                        """)
                                    elif p==2:
                                        n=int(input("Enter Position of that Project: "))
                                        f=int(input("Enter new amount given by state govt: "))
                                        cursor.execute("update Source_of_Money set State_govt ='"+str(f)+"' where Position='"+str(n)+"'")
                                        print("""
                                                      ......Data Updated sucessfully......
                                                        """)
                                    elif p==3:
                                        n=int(input("Enter Position of that Project: "))
                                        f=int(input("Enter new amount given by central govt: "))
                                        cursor.execute("update Source_of_Money set central_govt ='"+str(f)+"' where Position='"+str(n)+"'")
                                        print("""
                                                     ......Data Updated sucessfully.....
                                                     """)
                                    elif p==4:
                                        n=int(input("Enter Position of that Project: "))
                                        f=int(input("Enter new amount taken from Local Bodies: "))
                                        cursor.execute("update Source_of_Money set Local_bodies ='"+str(f)+"' where Position='"+str(n)+"'")
                                        print("""
                                                      ......Data Updated sucessfully......
                                                        """)
                                    elif p==5:
                                        n=int(input("Enter Position of that Project: "))
                                        f=int(input("Enter new amount of fund given by Private companies: "))
                                        cursor.execute("update Source_of_Money set Private_Companies ='"+str(f)+"' where Position='"+str(n)+"'")
                                        print("""
                                                      ......Data Updated sucessfully......
                                                        """)
                                    elif p==6:
                                        n=int(input("Enter Position of that Project: "))
                                        f=input("Enter new status: ")
                                        cursor.execute("update Source_of_Money set Status ='"+f+"' where Position='"+str(n)+"'")
                                        print("""
                                                      ......Data Updated sucessfully......
                                                        """)
                                    else:
                                        print("Enter correct choice")
                            elif b==5:
                                    pass
                            else:
                                print("""
                                          Enter correct choice
                                            
                                                 """)
                        elif ch==4:
                            print("""
        
                                                        1 .Show Record
                                                        2 .Add New Record
                                                        3 .Delete Existing record
                                                        4 .Update
                                                        5 .Previous

                                              """)
                            b=int(input("Enter your choice:"))
                            if b==1:
                                print("""

                                                     1. All records
                                                     2. Pariticular Record

                                             """)
                                c=int(input("Enter your choice: "))
                                # Displaying all record which are in this table
                                if c==1:
                                    cursor.execute("select Position,Ongoing,Issue,Status from  Feedback")
                                    row=cursor.fetchall()
                                    for i in row:
                                        v=list(i)
                                        k=["Position","Ongoing","Issue","Status"]
                                        d=dict(zip(k,v))
                                        print(d)
                                else:
                                    #To display particular record
                                    f=int(input("what is the Position of that project which you want to see: "))
                                    cursor.execute("select Position,Ongoing,Issue,Status from Feedback where Position='"+str(f)+"'")
                                    row=cursor.fetchall()
                                    for i in row:
                                        v=list(i)
                                        k=["Position","Ongoing","Issue","status"]
                                        d=dict(zip(k,v))
                                        print(d)
                            elif b==2:
                                q=int(input("How many Records you want to add:"))
                                for q in range(0,q):
                                    try:
                                        #Asking the details
                                        Position=int(input("Enter Position of the Project:"))
                                        Ongoing=input("Enter whether work is in Progress or not :")
                                        Issue=input("Enter issue if there otherwise write No:")
                                        Statusrecord="Active"
                                        #inserting the details in table
                                        cursor.execute("insert into Feedback (Position,Ongoing,Issue,Status) values('"+str(Position)+"','"+Ongoing+"','"+Issue+"','"+Statusrecord+"')")
                                        sql.commit()
                                        print("""
                                                 ............Added your record successfully............
                                                 """)
                                    except:
                                        print("""
                                                          ....Check Position.....
                                                   """)
                            elif b==3 :
                                # To know whether user really wanted to loose his record
                                p=input("Do you really want to delete(Y/N): ")
                                if p=="Y":
                                    f=int(input("Enter the Position of that project which you want to delete:"))
                                    #Deleting Selected Record
                                    delete(f)
                                else:
                                    pass
                            elif b==4:
                                print("""
                                                     1 Position
                                                     2 Ongoing
                                                     3 Issue
                                                     4 Status

                                           """)
                                row=cursor.execute("SELECT Position FROM  Feedback")
                                print("""
                                          .................. Position ...................
                                                            """)
                                #Here, We are displaying that what Positions User have
                                row=cursor.fetchall()
                                for i in row:
                                    v=list(i)
                                    k=["Position"]
                                    d=dict(zip(k,v))
                                    print(d)
                                q=int(input("how many things you want to update: "))
                                # Here, We are updating the existing Records
                                for a in range(0,q):
                                    p=int(input("What you want to change: "))
                                    if p==1:
                                        n=int(input("Enter Position of that Project: "))
                                        f=int(input("Enter new Position : "))
                                        cursor.execute("update Feedback set Position='"+str(f)+"' where Position='"+str(n)+"'")
                                        print("""
                                                      ......Data Updated sucessfully......
                                                        """)
                                    elif p==2:
                                        n=int(input("Enter Position of that Project: "))
                                        f=input("Enter Ongoing or not(Yes /No): ")
                                        cursor.execute("update Feedback set Ongoing='"+f+"' where Position='"+str(n)+"'")
                                        print("""
                                                      ......Data Updated sucessfully......
                                                        """)
                                    elif p==3:
                                        n=int(input("Enter Position of that Project: "))
                                        f=input("Enter new Issue: ")
                                        cursor.execute("update Feedback set Issue='"+f+"' where Position='"+str(n)+"'")
                                        print("""
                                                      ......Data Updated sucessfully......
                                                        """)
                                    elif p==4:
                                        n=int(input("Enter Position of that Project: "))
                                        f=input("Enter new status: ")
                                        cursor.execute("update Feedback set Status='"+f+"' where Position='"+str(n)+"'")
                                        print("""
                                                      ......Data Updated sucessfully......
                                                        """)
                                
                                    else:
                                        print("Enter correct choice")
                            elif b==5:
                                    pass
                            else:
                                print("""
                                          Enter correct choice
                                            
                                                 """)
                        elif ch==5:
                             print("""

                                ............................ THANK YOU ..............................



                                         """)
                             x=False
                        else:
                            print("""

                                                     ..... Enter your correct choice .....

                                                     """)
                                                     
