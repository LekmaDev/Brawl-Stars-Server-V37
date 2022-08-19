from ByteStream.Writer import Writer

class TeamMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24124
        self.player = player

    def encode(self):
        invites = ["BSS", "vanya_dev"]
        modifiers = [1, 4]
        self.writeVInt(1)
        self.writeBoolean(False)
        self.writeVInt(1)
        
        self.writeInt(0)
        self.writeInt(1)
        
        self.writeVInt(0)
        
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(1)

        self.writeDataReference(15, 7)

        self.writeBoolean(False)

        self.writeVInt(1)
        for x in range(1):

            self.writeVInt(1)

            self.writeLong(self.player.ID)

            self.writeDataReference(16, self.player.home_brawler)
            self.writeVint(0)
            self.writeVint(0)

            self.writeVInt(self.player.brawlers_trophies[str(self.player.home_brawler)])
            self.writeVInt(self.player.brawlers_high_trophies[str(self.player.home_brawler)])
            self.writeVInt(self.player.brawlers_level[str(self.player.home_brawler)] + 1)

            self.writeVInt(3)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)

            self.writeString(self.player.name)
            self.writeVInt(100)
            self.writeVInt(28000000)
            self.writeVInt(43000000)
            self.writeNullVInt()

            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)

        self.writeVInt(len(invites))
        for x in invites:
        	self.writeLong(2)
        	self.writeLong(3)
        	self.writeString(x)
        	self.writeVInt(1)
        	self.writeVInt(0)
        #self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeBoolean(False)
        #self.writeVInt(6)
        self.writeVInt(len(modifiers))
        for x in modifiers:
        	self.writeVInt(x)
