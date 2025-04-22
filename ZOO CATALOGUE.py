print("Please enter the requiring details")
print("BE Patient THIS MAY TAKE A WHILE")
zoo={}
land={}
n1=int(input("No.of Land animals:"))
for i in range(n1):
    det1={}
    phy_det1={}
    an_id=input("Animal id:")
    det1['Name']=input("Name:")
    det1['Count']=int(input("Count:"))
    det1['Species']=input("Species:")
    det1['Visitors']=int(input("No.of Visitors:"))
    det1['Type']=input("Type:")
    det1['Continent']=input("Continent:")
    det1['Maintenance']=int(input("Cost of Maintenance:"))
    det1['Ratings']=0
    det1['Comments']="NONE"
    det1['No.of Ratings']=0
    phy_det1['Avg.Lifespan(years)']=int(input("Avg. Lifespan(years):"))
    phy_det1['Avg.Height(feet)']=int(input("Avg.Height(feet):"))
    phy_det1['Avg.Weight(kg)']=int(input('Avg.Weight(kg):'))
    det1['Physical Details']=phy_det1
    land[an_id]=det1
print()
water={}
n2=int(input("No.of Aquatic animals:"))
for i in range(n2):
    det2={}
    phy_det2={}
    an_id=input("Fish id:")
    det2['Name']=input("Name:")
    det2['Count']=int(input("Count:"))
    det2['Species']=input("Species:")
    det2['Visitors']=int(input("No.of Visitors:"))
    det2['Type']=input("Type:")
    det2['Ocean']=input("Ocean:")
    det2['Maintenance']=int(input("Cost of Maintenance:"))
    det2['Ratings']=0
    det2['Comments']="NONE"
    det2['No.of Ratings:']=0
    phy_det2['Avg.Lifespan(years)']=int(input("Avg.Lifespan(years):"))
    phy_det2['Avg.Height(feet)']=int(input("Avg.Height(feet):"))
    phy_det2['Avg.weight(kg)']=int(input('Avg.Weight(kg):'))
    phy_det2["Colour"]=input("Colour:")
    phy_det2['Jaws']=input("Sharpness of Teeth:")
    phy_det2["Water Type"]=input("Water Type:")
    det2['Physical Details']=phy_det2
    water[an_id]=det2
print()
aerial={}
n3=int(input("No.of Aerial animals:"))
for i in range(n2):
    det3={}
    phy_det3={}
    an_id=input("Bird id:")
    det3['Name']=input("Name:")
    det3['Count']=int(input("Count:"))
    det3['Species']=input("Species:")
    det3['Visitors']=int(input("No.of Visitors:"))
    det3['Type']=input("Type:")
    det3['Continent']=input("Continent:")
    det3['Maintenance']=int(input("Cost of Maintenance:"))
    det3['Ratings']=0
    det3['Comments']="NONE"
    det3['No.of Ratings:']=0
    phy_det3['Avg.Lifespan(years)']=int(input("Avg.Lifespan(years):"))
    phy_det3['Avg.Height(feet)']=int(input("Avg.Height(feet):"))
    phy_det3['Avg.Weight(kg)']=int(input('Avg.Weight(kg):'))
    phy_det3["Colour"]=input("Colour:")
    phy_det3['Beak Length(cm)']=input("Beak length(cm):")
    det3['physical details']=phy_det3
    aerial[an_id]=det3
print("\t\tHELLO USER!")
print("\tWELCOME TO  NATIONAL ZOO CATALOGUE")
a=input("Are you a new user or existing user?(New or Existing):")
a1=a.upper()
if(a1=="NEW"):
    print("Hello user please follow the steps for registration")
    ur_name=input("Enter username:")
    new_pass=input("Enter password (Minimum 6 characters):")
    if(len(new_pass)<6):
        print("Password length is too short")
        new_pass=""
        new_pass=input("Enter password (Minimum 6 characters):")
    print("REGISTRATION SUCCESFUL")
    a="Existing"
aa=input("Are you a new user or existing user?(New or Existing):")
a2=aa.upper()
if(a2=="EXISTING"):
    name=input("Enter username:")
    pas=input("Enter your password :")
    if(name==ur_name and pas==new_pass):
        print("Hello ",name)
        print("Welcome to zoo catalogue")
        print("What do u like to do?")
        ch=0
        while(ch!=6):
            print("1.View an animal \n2.Add an animal \n3.General announcement \n4.Visitor ratings \n5.Zoo Timings \n6.Exit")
            ch=int(input("Enter Your choice from the above options:"))
            if(ch==1):
                an=int(input("Enter the option whether the animal is \n1.Land \n2.Water \n3.Aerial \nEnter your choice:"))
                if(an==1):
                    an_id=input("Enter Animal id:")
                    for i in land[an_id]:
                        if(i!="Physical Details"):
                            print(i," : ",land[an_id][i])
                        else:
                            print("PHYSICAL DETAILS:")
                            for j in phy_det1:
                                print(j," : ",phy_det1[j])
                elif(an==2):
                    an_id=input("Enter Animal id:")
                    for i in water[an_id]:
                        if(i!="Physical Details"):
                            print(i," : ",water[an_id][i])
                        else:
                            print("PHYSICAL DETAILS:")
                            for j in phy_det2:
                                print(j,":",phy_det2[j])
                elif(an==3):
                    an_id=input("Enter animal id:")
                    for i in aerial[an_id]:
                        if(i!="Physical Details"):
                            print(i," : ",aerial[an_id][i])
                        else:
                            print("PHYSICAL DETAILS:")
                            for j in phy_det3:
                                print(j," : ",phy_det3[j])
                else:
                    print("Please enter a valid input ")
            elif(ch==2):
                an=int(input("Enter the option whether the animal is \n1.Land \n2.Water \n3.Aerial \nEnter your choice:"))
                if(an==1):
                       det1={}
                       phy_det1={}
                       an_id=input("Animal id:")
                       det1['Name']=input("Name:")
                       det1['Count']=int(input("Count:"))
                       det1['Species']=input("Species:")
                       det1['Visitors']=int(input("No.of Visitors:"))
                       det1['Type']=input("Type:")
                       det1['Continent']=input("Continent:")
                       det1['Maintenance']=int(input("Cost of Maintenance:"))
                       det1['Ratings']=0
                       det1['Comments']="NONE"
                       det1['No.of Ratings']=0
                       phy_det1['Avg.Lifespan(years)']=int(input("Avg. Lifespan(years):"))
                       phy_det1['Avg.Height(feet)']=int(input("Avg.Height(feet):"))
                       phy_det1['Avg.Weight(kg)']=int(input('Avg.Weight(kg):'))
                       det1['Physical Details']=phy_det1
                       land[an_id]=det1
                       print("Animal added successfully")
                elif(an==2):
                      det2={}
                      phy_det2={}
                      an_id=input("Fish id:")
                      det2['Name']=input("Name:")
                      det2['Count']=int(input("Count:"))
                      det2['Species']=input("Species:")
                      det2['Visitors']=int(input("No.of Visitors:"))
                      det2['Type']=input("Type:")
                      det2['Ocean']=input("Ocean:")
                      det2['Maintenance']=int(input("Cost of Maintenance:"))
                      det2['Ratings']=0
                      det2['Comments']="NONE"
                      det2['No.of Ratings:']=0
                      phy_det2['Avg.Lifespan(years)']=int(input("Avg.Lifespan(years):"))
                      phy_det2['Avg.Height(feet)']=int(input("Avg.Height(feet):"))
                      phy_det2['Avg.weight(kg)']=int(input('Avg.Weight(kg):'))
                      phy_det2["Colour"]=input("Colour:")
                      phy_det2['Jaws']=input("Sharpness of Teeth:")
                      phy_det2["Water Type"]=input("Water Type:")
                      det2['Physical Details']=phy_det2
                      water[an_id]=det2
                      print("Animal added successfully")
                elif(an==3):
                      det3={}
                      phy_det3={}
                      an_id=input("Bird id:")
                      det3['Name']=input("Name:")
                      det3['Count']=int(input("Count:"))
                      det3['Species']=input("Species:")
                      det3['Visitors']=int(input("No.of Visitors:"))
                      det3['Type']=input("Type:")
                      det3['Continent']=input("Continent:")
                      det3['Maintenance']=int(input("Cost of Maintenance:"))
                      det3['Ratings']=0
                      det3['Comments']="NONE"
                      det3['No.of Ratings:']=0
                      phy_det3['Avg.Lifespan(years)']=int(input("Avg.Lifespan(years):"))
                      phy_det3['Avg.Height(feet)']=int(input("Avg.Height(feet):"))
                      phy_det3['Avg.Weight(kg)']=int(input('Avg.Weight(kg):'))
                      phy_det3["Colour"]=input("Colour:")
                      phy_det3['Beak Length(cm)']=input("Beak length(cm):")
                      det3['physical details']=phy_det3
                      aerial[an_id]=det3
                      print("Animal added successfully")
            elif(ch==3):
                print("General Announcement!:")
                a=input("Enter the news to be entered:")
                a1=a.upper()
                print("\t",a1)
            elif(ch==4):
                an=int(input("Enter the option whether the animal is \n1.Land \n2.Water \n3.Aerial \nEnter your choice:"))
                if(an==1):
                    an_id=input("Enter Animal id:")
                    for i in land[an_id]:
                        r=float(input('Enter your rathings(out of 5):'))
                        if(i=="Ratings"):
                             if(r<=5):
                                 det1['No.of Ratings:']+=1
                                 det1['Ratings']=(det1['Ratings']+r)/(det1['No.of Ratings:'])
                                 print("Your rating successfully added!")
                                 qn=input("Would you like to give any comments?(Yes/No): ")
                                 qn1=qn.upper()
                                 if(qn1=="YES"):
                                     cm=input("Enter your comment: ")
                                     det1['Comments']+=(cm+"\n")
                                     print("Thank you for your Comments :)  ! ")
                                 else:
                                     print("""\t\tThank You
                                              \n\tHave a good day :)""")
                             else:
                                 print("Please enter the ratings below 5 :(")                  
                elif(an==2):
                    an_id=input("Enter Animal id:")
                    for i in water[an_id]:
                        r=float(input('Enter your ratings(out of 5):'))
                        if(i=="ratings"):
                             if(r<=5):
                                 det2['No.of Ratings:']+=1
                                 det2['Ratings']=(det2['Ratings']+r)/(det2['No.of Ratings:'])
                                 print("Your rating successfully added!")
                                 qn=input("Would you like to give any comments?(Yes/No): ")
                                 qn1=qn.upper()
                                 if(qn1=="YES"):
                                     cm=input("Enter your comment: ")
                                     det2['Comments']+=(cm+"\n")
                                     print("Thank you for your Comments :)  ! ")
                                 else:
                                     print("""\t\tThank You\
                                              \n\tHave a good day :)""")
                             else:
                                 print("Please enter the ratings below 5 :(")
                elif(an==3):
                    an_id=input("Enter Animal id:")
                    for i in aerial[an_id]:
                        r=float(input('Enter your ratings(out of 5):'))
                        if(i=="Ratings"):
                             if(r<=5):
                                 det3['No.of Ratings:']+=1
                                 det3['Ratings']=(det3['Ratings']+r)/(det3['No.of ratings:'])
                                 print("Your rating successfully added!")
                                 qn=input("Would you like to give any comments?(Yes/No): ")
                                 qn1=qn.upper()
                                 if(qn1=="YES"):
                                     cm=input("Enter your comment: ")
                                     det3['Comments']+=(cm+"\n")
                                     print("Thank you for your Comments :)  ! ")
                                 else:
                                     print("""\t\tThank You\
                                              \n\tHave a good day :)""")
                             else:
                                 print("Please enter the ratings below 5 :(")                   
                else:
                    print("Please enter a valid input!!! ")
            elif(ch==5):
                print("ZOO TIMINGS")
                print("""NAME: NATIONAL ZOO
                         VENUE             :G.S.T road,Vandalur,chennai,Tamil nadu.
                         TIMING           : 9 AM to 6.30 PM
                         WORKING DAYS : All the days except TUESDAY
                         TICKET FEE       : Adult(Above 15 yrs)     : 50 Rs per person
                                                children(Above 5 yrs)    : 30 Rs per person
                                                Toddlers                  : FREE!!!!!!""")
            elif(ch==6):
                print("THANK YOU AND HAVE A NICE DAY :<)")
            else:
                print("INVALID CHOICE")
else:
    print("Please register yourself:(")
                            
                         

                        
                
        
        
    
    
    

    
    

