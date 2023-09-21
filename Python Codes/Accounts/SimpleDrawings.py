

def monthdat(month):
    if month=="jan":
        monthn=1
    if month=="feb":
        monthn=2
    if month=="mar":
        monthn=3
    if month=="apr":
        monthn=4
    if month=="may":
        monthn=5
    if month=="jun":
        monthn=6
    if month=="jul":
        monthn=7
    if month=="aug":
        monthn=8
    if month=="sep":
        monthn=9
    if month=="oct":
        monthn=10 
    if month=="nov":
        monthn=11
    if month=="dec":
        monthn=12
    return monthn

def simpledrawings(stype,rate=6):
    
    print("\t\tENTER AMOUNT OF DRAWING: ")    
    si=0
    while True:
        prin=float(input("Enter principal amount: "))
        month=input("Enter the month (first 3 letters) in xxx format: ").lower()
        mtype=int(input("Enter 1 for beginning of month, or 2 for the end of month: "))
        monthn=monthdat(month)
        if mtype==1:
            if monthn==1:
                monthn=12
            else:
                monthn=monthn-1
            
        if monthn==3 and mtype==2:
            q=int(input("Enter 0 to exit or 1 to continue: "))
            if q==0:
                break
            else: 
                continue
            
        if stype==1:
            mleft=12-monthn
        else:
            if monthn<3:
                mleft=3-monthn
            else:
                mleft=12-monthn+3
            
        si+=prin*rate*(mleft)/12/100
        q=int(input("Enter 0 to exit or 1 to continue: "))
        if q==0:
            break
        
    print("Total sum of money is: Rs. ",si)
        
    
stype=int(input("Enter 1 for jan-dec season or 2 for apr-mar season: "))
rate=float(input('Enter the rate: '))

simpledrawings(stype,rate)
        
    
    
    
    
    

    
    
    
    
     