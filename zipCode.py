#Hannah Lawson
#In progress
#10/12/2021

from uszipcode import Zipcode, SearchEngine, SimpleZipcode

def zipCode():
    userZip= input("Enter your zipcode: ")
    search = SearchEngine()
    zipcode = search.by_zipcode(userZip)
    city= zipcode.major_city
    #print(city)
    
    if city== "Daniels" or city== "Beckley":
        print("Laurel Mountain Psychological, Inc  \n (304)-894-8930")
    elif city== "Princeton" or city=="Athens":
        print("The Gibson Counseling Center \n (304)-487-9996")
    elif city== "Bluefield":
        print("Brain Matters Therapy \n (276)-970-9747")
    elif city== "Charleston" or city== "Saint Albans":
        print("KPCC Counseling \n (304)-346-9689")
    elif city== "Tazewell" or city== "Cedar Bluff":
        print("Carilion Clinic \n (276)-988-8765")
    elif city== "Bastian" or city== "Pearisburg":
        print("Bland County Medical Clinic \n (276)-688-4331")
    else: 
        print("Try another close city")

    
zipCode()