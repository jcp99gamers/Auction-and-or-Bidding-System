#Imports
import RequirmentChecker
from FirebaseConnector import FirebaseConnector
from datetime import datetime
firebase = FirebaseConnector()
firebase.ServiceKeyChecker()
db = firebase.FirestoreConnector()
#Item = db.collection(u'Bid').document(u'Items')  # opens 'Bid' collection
Auction_Items = db.collection(u'Auction_Items').stream()  # opens 'Bid' collection
for docz in Auction_Items:
    print(f'{docz.id} => {docz.to_dict()}')
Choice = int(input("Which Number from the List of Items above Would You Like to Choose:"))
doc_ref = db.collection(u'Auction_Items').document(str(Choice))
docs = doc_ref.get()
if docs.exists:
    dictionarys = docs.to_dict()
    nAME = dictionarys.get('Name')
    cOST = dictionarys.get('Cost')
else:
    print(u'No such document!')
print("The Auction Item is '",nAME,"' .")
print("The Starting Bid is '",cOST,"' .")


# https://firebase.google.com/docs/firestore/query-data/queries?hl=en&authuser=0 

'''
class City(object):
    def __init__(self, name, state, country, capital=False, population=0,
                 regions=[]):
        self.name = name
        self.state = state
        self.country = country
        self.capital = capital
        self.population = population
        self.regions = regions

    @staticmethod
    def from_dict(source):
        # [START_EXCLUDE]
        city = City(source[u'name'], source[u'state'], source[u'country'])

        if u'capital' in source:
            city.capital = source[u'capital']

        if u'population' in source:
            city.population = source[u'population']

        if u'regions' in source:
            city.regions = source[u'regions']

        return city
        # [END_EXCLUDE]

    def to_dict(self):
        # [START_EXCLUDE]
        dest = {
            u'name': self.name,
            u'state': self.state,
            u'country': self.country
        }

        if self.capital:
            dest[u'capital'] = self.capital

        if self.population:
            dest[u'population'] = self.population

        if self.regions:
            dest[u'regions'] = self.regions

        return dest
        # [END_EXCLUDE]

    def __repr__(self):
        return (
            f'City(\
                name={self.name}, \
                country={self.country}, \
                population={self.population}, \
                capital={self.capital}, \
                regions={self.regions}\
            )'
        )
# [END firestore_data_custom_type_definition]
# [END custom_class_def]
cities_ref = db.collection(u'cities')
cities_ref.document(u'BJ').set(City(u'Beijing', None, u'China', True, 21500000, [u'hebei']).to_dict())
cities_ref.document(u'SF').set(City(u'San Francisco', u'CA', u'USA', False, 860000,[u'west_coast', u'norcal']).to_dict())
cities_ref.document(u'LA').set(City(u'Los Angeles', u'CA', u'USA', False, 3900000,[u'west_coast', u'socal']).to_dict())
cities_ref.document(u'DC').set(City(u'Washington D.C.', None, u'USA', True, 680000,[u'east_coast']).to_dict())
cities_ref.document(u'TOK').set(City(u'Tokyo', None, u'Japan', True, 9000000,[u'kanto', u'honshu']).to_dict())
'''