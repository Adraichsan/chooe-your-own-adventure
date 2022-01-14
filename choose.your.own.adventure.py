name = input("ketik nama kamu: ")
print("welcome", name, "mulai pertualangan anda!")

answer = input(
    "kamu tersesat di gunung, dan kamu menemukan dua jalur di pendakian tersebut, pilih arah nya (kanan/kiri) ? ") 

if answer == "kiri":
    answer = input(
         "kamu akan menemukan dua pilihan? ketik meloncati pohon tumbang yang menghalangi jalan atau bertemu kawanan harimau(meloncati/kawanan harimau/tidak ada pilihan) : ")
    
    if answer == "meloncati":
        print("kamu meloncati dan jatuh terpleset. ")
    elif answer == "kawanan harimau":
        print("kamu berjalan melewati kawanan harimau dan di makan ")
    else:
        print('tidak ada pilihan yang valid. kamu kalah. ')

elif answer == "kanan":
    answer = input(
        "kamu akan bertemu dengan dua rombongan, rombongan bendera putih dan kuning (putih/kuning)? ")
    
    if answer == "putih":
        print("kamu bertemu dengan rombongan hantu. ")
    elif answer == "kuning":
        answer = input(
            "kamu bertemu dengan rombongan anak UI, dan kamu di ajak berbicara (iya/tidak)? ")
        
        if answer == "iya":
            print("kamu berbicara dengan anak UI tersebut dan dia memberi mu makanan. kamu MENANG!")
        elif answer == "tidak":
            print("kamu abaikan anak UI itu dan dia pergi dan kamu kalah.")
        else:
            print('tidak ada pilihan yang valid. kamu kalah')
    else:
        print('tidak ada pilihan yang valid, kamu kalah, ')

else:
    print('tidak ada pilihan yang valid')

print("terima kasih telah mencoba petualangan tersebut", name)




        
       

