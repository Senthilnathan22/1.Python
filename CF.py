class Functions():
    def Subfields():
        print("Sub-Fieldsin AI are:");
        print("Machine Learning")
        print("Neural networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing")

    def oddEven():
        num=int(input("Enter the Number:"))
        if((num%2)==1):
                print(num,"is Odd number")
                mes="Odd Number"
        else:
                print(num,"is Even Number")
                mes="Even number"
        return mes

    def eligible():
        Gender=input("Your Gender:")
        Age=int(input("Your Age:"))
        if(Gender.lower()=="male" and Age>=21):
            print("Eligible")
            sel="Eligible"
        elif(Gender.lower()=="female" and Age>=18):
            print("Eligible")
            sel="Eligible"
        else:
            print("Not Eligible")
            sel="Not Eligible"
        return sel

    def Percentage():
        S1=98
        S2=87
        S3=95
        S4=95
        S5=93
        T= S1+S2+S3+S4+S5
        Per= (T/500)*100
        print("Subject1=", S1)
        print("Subject2=", S2)
        print("Subject3=", S3)
        print("Subject4=", S4)
        print("Subject5=", S5)
        print("Total:", T)
        print("Percentage:", Per)
        percent=Per
        return percent

    def triangle():
        H=32
        B=34
        H1=2
        H2=4
        B1=4
        AOT=(H*B)/2
        PF=H1+H2+B1
        print("Height:", H)
        print("Breath:", B)
        print("Area of Triangle:", AOT)
        tri=AOT,PF
        print("Height1:", H1)
        print("Height2:", H2)
        print("Breadth:", B1)
        print("Perimeter of Triangle:", PF)
        tri=AOT,PF
        return tri