from cards import *

business_cards = []
card1 = BusinessCard( "Anna Kowalska"," PKP","acountant","business_phone 1235","email ak@wp.pl","priv_phone 5434")
card2 = BusinessCard( "Jan Nowak","LOT","pilot","business_phone 2143", "email jn@plot.pl","priv_phone 6634")
card3 = BusinessCard( "Franek Dolas", "Gazownia", "analyst","business_phone 1324","email fd@gazownia.pl","priv_phone 1984")
card4 = BusinessCard( "Edmund Foks",   "elektryka","manager", "business_phone 7234", "email ef@elektryka.pl","priv_phone 1004")
card5 = BusinessCard( "Kot Luslaw",  "Lux materace","tester", "business_phone 1634", "email kl@lmaterace.pl","priv_phone 1504")
business_cards.append(card1)
business_cards.append(card2)
business_cards.append(card3)
business_cards.append(card4)
business_cards.append(card5)

for card in business_cards:
    print (card)


sorted_cards = sorted(business_cards, key= lambda x: x.name)    
for card in sorted_cards:
    print(card)

sorted_cards = sorted (business_cards, key=lambda x: x.email )
for card in sorted_cards:
    print(card)
card1.contact()
card5.contact()

print (card1.lenght)

# Zadanie do zaliczenia - 7.3 dziedziczenie- wizytówki
card1 = BaseContact( "Anna Kowalska","email ak@wp.pl","priv_phone 5434")
card2 = BusinessContact("Anna Kowalska"," PKP","acountant","business_phone 1235","email ak@wp.pl","priv_phone 5434")
card1.contact()
card2.contact()

print(card1.lenght)
print(card2.lenght)

from faker import Faker
def create_contacts(type, number):
    contacts = []
    faker = Faker ()
    if type == "business":
        for i in range(number):
            contacts.append(BusinessContact(faker.name(), faker.company(), "position",faker.phone_number(),faker.address(), faker.phone_number()))
    if type == "private":
        for i in range(number):
            contacts.append(BaseContact(faker.name(),faker.email(),faker.phone_number()))
    return contacts
private = create_contacts("private",5)
business = create_contacts("business",5)

for card in private:
    card.contact()



