class MediaLibrary:
    def __init__(self, title, publication_date, genre):
        self.title = title
        self.publication_date = publication_date
        self.genre = genre
        self.no_plays = 0
    
    def play (self):
        self.no_plays += 1


class Film(MediaLibrary):
    def __init__(self, title, publication_date, genre):
        super().__init__(title, publication_date, genre)
    def __str__(self):
        return f'"{self.title}" ({self.publication_date})'

class Serial(MediaLibrary):
    def __init__(self, title, publication_date, genre, epeisode_no, season_no):
        super().__init__(title, publication_date, genre)
        self.epeisode_no = epeisode_no
        self.season_no = season_no
    
    def __str__(self):
        return f"Tytuł serialu:{self.title},wydany:{self.publication_date},gatunek:{self.genre},liczba odtworzen:{self.no_plays},numer odcinka:{self.epeisode_no},seria {self.season_no}."

    




