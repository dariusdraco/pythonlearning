import time as t
from pydub import AudioSegment
from pydub.playback import play


class Animal():
    def __init__(self,name,species,sound) -> None:
        self.name=name
        self.species=species
        self.sound=sound

    def animal_sound():
        sound = AudioSegment.from_mp3('')
        sound = sound.speedup(6)
        play(sound)

    def animal_info(self):
        print(f'''
name : {self.name},
species : {self.species},
sound : {self.sound},''')


class Mammals(Animal):
    def __init__(self, name, species, sound,legs) -> None:
        super().__init__(name, species, sound)
        self.legs=legs
    def animal_sound(self):
        sound = AudioSegment.from_mp3('/Users/darius/Library/Mobile Documents/com~apple~CloudDocs/Gamingoh/mp3_sound/Lowe.mp3')
        sound = sound.speedup(6)
        play(sound)
    def animal_info(self):
        super().animal_info()
        print(f'''
legs : {self.legs}
''')

class Reptiles(Animal):
    def __init__(self, name, species, sound) -> None:
        super().__init__(name, species, sound)
    def animal_sound(self):
        sound = AudioSegment.from_mp3('/Users/darius/Library/Mobile Documents/com~apple~CloudDocs/Gamingoh/mp3_sound/rattlesnake.mp3')
        sound = sound.speedup(6)
        play(sound)
    def animal_info(self):
        super().animal_info()


class Birds(Animal):
    def __init__(self, name, species, sound,wingspan) -> None:
        super().__init__(name, species, sound)
        self.wingspan=wingspan
    def animal_sound(self):
        sound = AudioSegment.from_mp3('/Users/darius/Library/Mobile Documents/com~apple~CloudDocs/Gamingoh/mp3_sound/rattlesnake.mp3')
        sound = sound.speedup(6)
        play(sound)
    def animal_info(self):
        super().animal_info()
        print(f'''
wingspan : {self.wingspan} cm
''')
    
def main():
    mammals=Mammals('simba','lion','roar',4)
    mammals.animal_sound()
    mammals.animal_info()
    t.sleep(5)
    reptiles=Reptiles('slithername','rattlesnake','rattle')
    reptiles.animal_sound()
    reptiles.animal_info()
    t.sleep(5)
    birds=Birds('tweety','canary','tweet',10)
    birds.animal_sound()
    birds.animal_info()
    t.sleep(5)
    
if __name__ == "__main__":
    main()