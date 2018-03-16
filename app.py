from lib import SubsceneDownload

download = SubsceneDownload()
URL = raw_input("Masukkan URL Subscene : ")

print ("Downloading file...")
download.fetchUrlSubs(URL)
print ("Download file successfull!")