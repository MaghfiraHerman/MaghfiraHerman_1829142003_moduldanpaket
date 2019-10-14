#nama file : import.py

#mengimpor modul BangunRuangDanBangunDatar
import BangunRuangDanBangunDatar

def main():
    #balok
    p = 28   
    l = 10    
    t = 17

    kel = BangunRuangDanBangunDatar.kelilingBalok(p, l, t)
    vol = BangunRuangDanBangunDatar.volumeBalok(p, l, t)
    
    print("BALOK")
    print("Panjang\t: ", p)
    print("Lebar\t: ", l)
    print("tinggi\t: ", t)
    print("Keliling\t= ", kel)
    print("Volume\t= ", vol)


if __name__ == "__main__":
    main()
    
