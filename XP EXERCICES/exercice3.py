class Song:
    def __init__(self):
        self.lyrics =[]
        
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)