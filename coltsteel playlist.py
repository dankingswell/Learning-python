

class playlist ():

    songs =  []


    def __init__(self,Author):
        self.author = Author
        

    def addSong(self,song_title,Song_artists,song_duration):
        Song_artists = list(Song_artists)
        songinfo = {
            "title" : song_title.lower(),
            "artists" : Song_artists[0] if len(Song_artists) == 1 else Song_artists,
            "duration" : song_duration
        }

        self.songs.append(songinfo)
    
    def orderSongs(self):

        SongOrderStorage = {}
        index = 0
        for song in self.songs:
            print(song["title"])
            SongOrderStorage[song["title"]] = index
            index +=1


        
        print("\n\n")
        while True:
            change = input("would you like to change the order? (Y/N) \t\t")
            if change.upper() == "Y":
                info  =  input("please enter song title you would like to change or enter quit to cancel \t").lower()
                if info == "quit":
                    break
                if  SongOrderStorage.get(info) is None :
                    print("i couldn't find that song, did you spell it correctly?")
                    continue
                position = int(input("what number would you list to move the song to (1,2,3 etc) \t"))

                self.songs[position],self.songs[SongOrderStorage.get(info)] = self.songs[SongOrderStorage.get(info)] , self.songs[position]
                self.printsongs()
                break
            elif change.upper() == "N":
                break
            else:
                print("please confirm yes or no with a Y or N") 
                continue
                
    

    def printsongs(self):
        for song in self.songs:
            print(song["title"])

            
        

playit = playlist("Dan")
playit.addSong("song1",["artist1","artist2"],"2mins")
playit.addSong("song2",["artist1","artist2"],"2mins")
playit.addSong("song3",["artist1","artist2"],"2mins")
print(playit.songs)

playit.orderSongs()

print("\n\n")
playit.printsongs()