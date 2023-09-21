

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

def pdtint(stype,freq,rate=6):
    
    print("\t\tENTER AMOUNT OF DRAWING: ")    
    si=0
    
    prin=float(input("Enter principal amount: "))
    fmonth=input("Enter the first drawing month (first 3 letters) in xxx format: ").lower()
    fmtype=int(input("Enter 1 for beginning of month, or 2 for the end of month: "))
    lmonth=input("Enter the last drawing month (first 3 letters) in xxx format: ").lower()
    lmtype=int(input("Enter 1 for beginning of month, or 2 for the end of month: "))
    fmonthn=monthdat(fmonth)
    lmonthn=monthdat(lmonth)

    if fmtype==1:
        if fmonthn==1:
            fmonthn=12
        else:
            fmonthn=fmonthn-1
    if lmtype==1:
        if lmonthn==1:
            lmonthn=12
        else:
            lmonthn=lmonthn-1
         
                
    if fmonthn==3 and fmtype==2:
        print("Not possible!!!") 
    if lmonthn==3 and lmtype==2:
        lmonth=4  
      
           
    if stype==1:
        fmleft=12-fmonthn
        lmleft=12-lmonthn
    else:
        if fmonthn<3:
            fmleft=3-fmonthn
        else:
            fmleft=12-fmonthn+3
        if lmonthn<3:
            lmleft=3-lmonthn
        else:
            lmleft=12-lmonthn+3
        
        
    prin=(lmonthn-fmonthn)/freq*prin   
    si=(fmleft+lmleft)/2/12*prin*rate

    print("Total sum of money is: Rs. ",si)
        
    
stype=int(input("Enter 1 for jan-dec season or 2 for apr-mar season: "))
freq=float(input("Enter frequency of drawings in months: "))
rate=float(input('Enter the rate: '))


pdtint(stype,freq,rate)
        
    
    
    
    
    

    
    
    
    
     