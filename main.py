#Imports
import RequirmentChecker
import os
# import random
from datetime import datetime # import time
from FirebaseConnector import FirebaseConnector
from datetime import datetime
firebase = FirebaseConnector()
firebase.ServiceKeyChecker()
db = firebase.FirestoreConnector()
#Timer
now = datetime.now()
#for Admin &or Brokers
print("\n")
Auction_Items = db.collection(u'Auction_Items').stream()  # opens 'Auction_Items' collection
for docz in Auction_Items:
    print(f'{docz.id} => {docz.to_dict()}')
print("\n")
Choice = int(input("Which Number from the List of Items above Would You Like to Choose:"))
doc_ref = db.collection(u'Auction_Items').document(str(Choice))
docs = doc_ref.get()
if docs.exists:
    dictionarys = docs.to_dict()
    nAME = dictionarys.get('Name')
    cOST = dictionarys.get('Cost')
else:
    print(u'No such document!')
# itemNAME = input("Enter the Item Name : ")+""
print("The Auction Item is '",nAME,"' .")
print("The Starting Bid is '",cOST,"' .")
itemNAME = nAME
startingBID = cOST
#for the Dealers
count = int(input("Enter How Many Users are Participating in the Bid = "))
os.system("cls")
#StartTimer
start_time = now.strftime("%H:%M:%S")
#for Bidders
db.collection(u'Bid').document(itemNAME).delete()
Item = db.collection(u'Bid').document(itemNAME)  # opens 'Bid' collection
Type = Item.get() #type(collectionStudents.get())
#Create Users
amount = []
counter = 1
while counter <= count:
    Num = 'User'+ str(counter)
    Users = Item.collection(u'Users').document(Num)
    username = input("Enter Your Username = ")+""
    bid = int(input("Enter You Bid = "))
    os.system("cls")
    Users.set({
        'id':username,
        'amount':str(bid)
        })
    amount.append(bid)
    counter += 1
#EndTimer
end_time = now.strftime("%H:%M:%S")
#Query
maximum = max(amount)
docs = Item.collection(u'Users').where(u'amount', u"==", str(maximum)).stream()
for doc in docs:
    personNumber = doc.id
    dictionarys = doc.to_dict()
    identity = doc.get('id')
    # print(f'{doc.id} => {doc.to_dict()}')
#Create Data
Item.set({
    'starTime':str(start_time),
    'endTime':str(end_time),
    'StartPrice': startingBID,
    'WINNER': identity
    })