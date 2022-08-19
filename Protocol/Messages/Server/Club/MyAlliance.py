from ByteStream.Writer import Writer


class MyAlliance(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.id = 24399

    def encode(self):
        self.writeVInt(1) #Members
        self.writeBoolean(True)
        
        self.writeScId(25, 1)
        
        self.writeInt(0)
        self.writeInt(self.player.ID)
        
        self.writeString("Club Beta")
        self.writeScId(8, 0)
        self.writeVInt(1)
        self.writeVInt(1)
        self.writeVInt(self.player.trophies)
        self.writeVInt(0)
        self.writeVint(0)
        self.writeBoolean(False)
        
        