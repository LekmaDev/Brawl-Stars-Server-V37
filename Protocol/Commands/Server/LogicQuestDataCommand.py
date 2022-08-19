from Utils.Writer import Writer


class LogicQuestDataCommand(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24111
        self.player = player

    def encode(self):
        self.writeVint(1) # count ?
        self.writeVint(1) # cum
        self.writeVint(1)
        self.writeVint(1)
        self.writeVint(1)
        self.writeVint(1)