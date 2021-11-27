import os
os.system("pip install phonenumbers")
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
os.system("figlet phoneprinting")
print("by pratv3")
class Phone:
    def __init__(self,num):
        try:
            self.num=num
            st=phonenumbers.parse(self.num)
            va=phonenumbers.is_valid_number(st)
            loc=geocoder.description_for_number(st,"en")
            ser=carrier.name_for_number(st,"en")
            timz=timezone.time_zones_for_number(st)
            print(f"[#] number for test is {self.num}")
            print(f"[#] phone number activation is {va}")
            print(f"[#] location country is {loc}")
            print(f"[#] ISP for the number is {ser}")
            print(f"[#] Timezone of the located number {timz}")
        except:
            print("[!] may be there is some mistake")
            print(f"[i] phonenumber validation maybe false")
i=input("[+] Enter the phonenumber with country code:")
service=Phone(i)
print(service.num)
