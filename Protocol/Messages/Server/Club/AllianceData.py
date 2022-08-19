from ByteStream.Writer import Writer
import random

class AllianceData(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.id = 24301

    def encode(self):
        self.writeBoolean(True)
        self.writeLong2(0, 0) #hlid
        self.writeString("Brawl Stars v35") #name
        self.writeDataReference(8, 1) #badge
        self.writeVInt(1) # Type
        self.writeVInt(1)  # Total Members
        self.writeVInt(99999)  # Total Trophies
        self.writeVInt(200)  # Trophies Required
        self.writeDataReference(0)
        self.writeString("RU")  # Region
        self.writeVInt(0)
        self.writeBoolean(False)  # Family Friendly

        self.writeString("TESTER CLUBS V35") # Description
        self.writeVInt(2) # Members Count
        
        self.writeLong2(0, 1)
        self.writeVInt(2)
        self.writeVInt(self.player.trophies) # Trophies
        self.writeVInt(2)
        self.writeVInt(6974) # State Timer
        self.writeVInt(0)
        self.writeBoolean(False) #DND
        self.writeString(self.player.name)
        self.writeVInt(100)
        self.writeVInt(28000000) # Player Thumbnail
        self.writeVInt(43000000) # Player Name Color
        self.writeVInt(42000000) # Color Gradients
        
        self.writeLong2(0, 0)
        self.writeVInt(2)
        self.writeVInt(6666) # Trophies
        self.writeVInt(1)
        self.writeVInt(6974) # State Timer
        self.writeVInt(0)
        self.writeBoolean(False) #DND
        self.writeString("t.me/artemBSmods")
        self.writeVInt(100)
        self.writeVInt(28000001) # Player Thumbnail
        self.writeVInt(43000006) # Player Name Color
        self.writeVInt(42000000) # Color Gradients

        self.writeVInt(0)
        
        