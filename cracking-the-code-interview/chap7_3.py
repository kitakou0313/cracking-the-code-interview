import unittest


class Song():
    def __init__(self, name):
        self.__name = name
        self.__playCnt = 0

    def getPlayCnt(self):
        return self.__playCnt

    def getSongName(self):
        return self.__name

    def addPlayCnt(self):
        self.__playCnt += 1


class JukeBox():
    def __init__(self, playList):
        self.__playList = playList

    def play_song(self, songName):
        for song in self.__playList:
            if song.getSongName() == songName:
                song.addPlayCnt()

    def addSong(self, song):
        self.__playList.append(song)

    def getSongList(self):
        return self.__playList


class Test(unittest.TestCase):
    def test_jukebox(self):
        song1 = Song("Grenge")
        song2 = Song("Inotini kirawareteiru")
        jukebox = JukeBox([song1, song2])

        song3 = Song("Zenzenzense")

        jukebox.play_song("Inotini kirawareteiru")
        jukebox.addSong(song3)
        self.assertEqual(len(jukebox.getSongList()), 3)
        self.assertEqual(song2.getPlayCnt(), 1)


if __name__ == "__main__":
    unittest.main()
