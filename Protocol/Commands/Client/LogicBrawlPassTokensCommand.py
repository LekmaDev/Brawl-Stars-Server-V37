from Database.DatabaseManager import DataBase

from Utils.Reader import BSMessageReader

class LogicBrawlPassTokensCommand(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass


    def process(self):
        if 0 <= self.player.brawl_pass_tokens <= 75:
            newtokenone =  75
            DataBase.replaceValue(self, 'BrawlPassTokens', newtokenone)
        elif 75 <= self.player.brawl_pass_tokens <= 150:
            newtokentwo = 150
            DataBase.replaceValue(self, 'BrawlPassTokens', newtokentwo)
        elif 150 <= self.player.brawl_pass_tokens <= 250:
            newtokenthree = 250
            DataBase.replaceValue(self, 'BrawlPassTokens', newtokenthree)
        elif 250 <= self.player.brawl_pass_tokens <= 400:
            newtokenfour = 400
            DataBase.replaceValue(self, 'BrawlPassTokens', newtokenfour)
