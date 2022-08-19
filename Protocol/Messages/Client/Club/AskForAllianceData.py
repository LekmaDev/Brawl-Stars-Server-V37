from ByteStream.Reader import Reader
from Utils.Helpers import Helpers
from Protocol.Messages.Server.Club.AllianceData import AllianceData

class AskForAllianceData(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        self.helpers = Helpers()

    def decode(self):
        pass

    def process(self, db):
        AllianceData(self.client, self.player).send()



