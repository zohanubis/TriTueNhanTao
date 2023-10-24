#Viết chương trình tính tiền thuê Taxi. 
# Biết rằng, mỗi khách hàng tính 2£ và 1.5£ cho 1km.
def taxi():
    passengers = (int) (input("\nNhập vào số người :"))
    distance = (float)(input("\nNhập vào số km : "))
    total = 2* passengers + 1.5 * distance
    print("\nTotal : ", total)
    
taxi()