from lib import SubsceneDownload

download = SubsceneDownload()
URL = raw_input("Masukkan URL Subscene : ")
#https://subscene.com/subtitles/longing-heart-my-first-love-aeganjang

print ("Downloading file...")
download.fetchUrlSubs(URL)
print ("Download file successfull!")
