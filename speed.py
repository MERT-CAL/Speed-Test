import speedtest
import time

s = speedtest.Speedtest()

no = 1000000

print(f"dowland hız ölçülüyor")
dws = round(s.download()/no,2)
print(f"{dws} download hızınız")

print("upload hızınız ölçülüyor")
ups = round(s.upload()/no,2)
print(f"{ups} upload hızınız")

sonuc = round(dws/8,2)
print(f"ortalama dosya indirme hızınız : {sonuc}MB/s")

time.sleep(20)




