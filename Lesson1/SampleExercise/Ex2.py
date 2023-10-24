#Viết chương trình tính tiền thuê Taxi. 
# Biết rằng, mỗi khách hàng tính 2£ và 1.5£ cho 1km.
def taxi():
    passengers = (int) (input("\nNhap vao so nguoi :"))
    distance = (float)(input("\nNhap vao so km : "))
    total = 2* passengers + 1.5 * distance
    print("\nTotal : ", total)
    
taxi()