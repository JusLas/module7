from media_biblioteka import *
serial = Serial("Good Father", "1985", "criminal",1,1) 
print(serial)

film = Film ("Santa Clause", 2016, "comedy")
print(film)

media_library = [serial,film] 
for media in media_library:
    print(media)
    

print("Films and serials catalogue")
'''
film1_title="Good father"
film1_publication_date="1985"
film1_type="criminal"
film1_no_plays="1 234 567"
film1_info=f" Film:{film1_title}, wydany {film1_publication_date},gatunek:{film1_type},liczba odtworzen:{film1_no_plays}."


film2_title="No love"
film2_publication_date="2016"
film2_type="drama"
film2_no_plays="234 567"
film2_info=f" Film:{film2_title}, wydany {film2_publication_date},gatunek:{film2_type},liczba odtworzen:{film2_no_plays}."


film3_title="Santa Clause"
film3_publication_date="2015"
film3_type="comedy"
film3_no_plays="567"
film3_info=f" Film:{film3_title}, wydany {film3_publication_date},gatunek:{film3_type},liczba odtworzen:{film3_no_plays}."

film4_title="Foxtrot"
film4_publication_date="1989"
film4_type="criminal"
film4_no_plays="4 567"
film4_info=f" Film:{film4_title}, wydany {film4_publication_date},gatunek:{film4_type},liczba odtworzen:{film4_no_plays}."

film5_title="Summer holidays"
film5_publication_date="2005"
film5_type="criminal"
film5_no_plays="34 567"
film5_info=f" Film:{film5_title}, wydany {film5_publication_date},gatunek:{film5_type},liczba odtworzen:{film5_no_plays}."

serial1_title="Cosmic tales"
serial1_publication_date="1987"
serial1_type="criminal"
serial1_no_plays="77 567"
serial1_epeisode_no=""
serial1_season_no=""
serial1_info=f" Tytuł serialu:{serial1_title},wydany:{serial1_publication_date},gatunek:{serial1_type},liczba odtworzen:{serial1_no_plays},numer odcinka:{serial1_epeisode_no},seria {serial1_season_no}."


serial2_title="move"
serial2_publication_date="2005"
serial2_type="drama"
serial2_no_plays="77 097"
serial2_epeisode_no=""
serial2_season_no=""
serial2_info=f"Tytuł serialu:{serial2_title},wydany:{serial2_publication_date},gatunek:{serial2_type},liczba odtworzen:{serial2_no_plays},numer odcinka:{serial2_epeisode_no},seria {serial2_season_no}."


serial3_title="Dance dance"
serial3_publication_date="1999"
serial3_type="comedy"
serial3_no_plays="34 567"
serial3_epeisode_no=""
serial3_season_no=""
serial3_info=f"Tytuł serialu:{serial3_title},wydany:{serial3_publication_date},gatunek:{serial3_type},liczba odtworzen:{serial3_no_plays},numer odcinka:{serial3_epeisode_no},seria {serial3_season_no}."

serial4_title="Good weather"
serial4_publication_date="1995"
serial4_type="criminal"
serial4_no_plays="55 555"
serial4_epeisode_no=""
serial4_season_no=""
serial4_info=f"Tytuł serialu:{serial4_title},wydany:{serial4_publication_date},gatunek:{serial4_type},liczba odtworzen:{serial4_no_plays},numer odcinka:{serial4_epeisode_no},seria {serial4_season_no}."

serial5_title="War"
serial5_publication_date="1989"
serial5_type="drama"
serial5_no_plays="51 234 "
serial5_epeisode_no=""
serial5_season_no=""
serial5_info=f"Tytuł serialu:{serial5_title},wydany:{serial5_publication_date},gatunek:{serial5_type},liczba odtworzen:{serial5_no_plays},numer odcinka:{serial5_epeisode_no},seria {serial5_season_no}."
# jak jest w jednej linie to się drukuje, a jeśli chce zeby był jeden pod drugim ?? 
Catalogue=f"Films and serial catalogue" 
{film1_info}, 
{film2_info}, 
{film3_info},
{film4_info},
{film5_info}, 
{serial1_info},
{serial2_info},
{serial3_info},
{serial4_info},
#{serial5_info}.
print(Catalogue)
'''
