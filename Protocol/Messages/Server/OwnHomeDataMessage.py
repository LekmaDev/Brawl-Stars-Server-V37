import json
from Logic.Quests import Quests
from ByteStream.Writer import Writer
from datetime import datetime
from Files.CsvLogic.Cards import Cards

class OwnHomeDataMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24101
        self.player = player

    def encode(self):
        self.writeVInt(2021122)  # Timestamp (Year * 1000 + DayOfYear)
        self.writeVInt(75735)  # Second Timestamp
        self.writeVInt(self.player.trophies)
        self.writeVInt(self.player.high_trophies)
        self.writeVInt(self.player.high_trophies)

        self.writeVInt(self.player.trophy_reward)
        self.writeVInt(self.player.exp_points)

        self.writeDataReference(28, self.player.profile_icon)
        self.writeDataReference(43, self.player.name_color)

        self.writeVInt(50)
        for x in range(50):
            self.writeVInt(x)

        self.writeVInt(0)
        for x in range(0):
            self.writeVInt(x)

        self.writeVInt(0)
        for x in range(0):
            self.writeVInt(x)

        self.writeVInt(len(self.player.unlocked_skins))
        for x in self.player.unlocked_skins:
            self.writeDataReference(29, x)

        self.writeVInt(0)
        for x in range(0):
            self.writeVInt(x)

        self.writeVInt(0)
        for x in range(0):
            self.writeVInt(x)

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVInt(1)

        self.writeUInt8(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeBoolean(False)
        self.writeBoolean(False)

        self.writeUInt8(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(2)
        self.writeVInt(2)
        self.writeVInt(2)

        self.writeVInt(0)
        for x in range(0):
            self.writeVInt(x)

        self.writeVInt(0)
        for x in range(0):
            self.writeVInt(x)

        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(0)
        for x in range(0):
            self.writeVInt(x)

        self.writeVInt(0)
        self.writeVInt(0)

        self.writeDataReference(16, 0)

        self.writeString(self.player.region)
        self.writeString(self.player.content_creator)

        self.writeVInt(1) # 1
        self.writeInt(4) # что получаем? 4 - кубки, 8 - старпоинты, 10 - очки силовой гонки
        self.writeInt(8) # количество получаемого

        self.writeVInt(0)
        for x in range(0):
            self.writeVInt(x)

        self.writeVInt(2) # бравл пасс 
        for x in range(6, 8):
            self.writeVInt(x) # сезон
            self.writeVInt(-1) # токены
            self.writeUInt8(1) # приобретен ли бп
            self.writeVInt(0) # это вроде собранный уровень
            self.writeUInt8(0)

        self.writeVInt(0)
        for x in range(0):
            self.writeVInt(x)
            
        self.writeByte(1) # QUESTS
        count2 = len(Quests.quests)
        self.writeVint(count2)  # Count
        for i in range(count2): # Count
            item = Quests.quests[i]
            self.writeVint(4) 
            self.writeVint(4)
            self.writeVint(item['MissionID']) # Mission Type
            self.writeVint(item['Reached']) # Current goal achieve
            self.writeVint(item['Max']) # Quest goal
            self.writeVint(item['Reward']) # Tokens reward
            self.writeVint(item['Type']) # Quest Type
            self.writeVint(item['CurrentLVL']) # current level
            self.writeUInt8(item['MaxLVL']) # max level
            self.writeVint(2)

            self.writeVint(item['BrawlPassExclusiveBoolean']) # Brawl Pass Exclusive
            self.writeScId(16, item['BrawlerID']) # csvID and brawlerID

            self.writeVint(item['GamemodeID']) # Gamemode TID
            self.writeVint(1)
            self.writeVint(1)
            
        self.writeBoolean(True)
        self.writeVInt(0)

        self.writeBoolean(True)
        self.writeVInt(0)

        self.writeBoolean(True) # Power League Array
        # Power League Data Array Start #
        self.writeVInt(0) # ?
        self.writeVInt(17) # Rank Solo League
        self.writeVInt(0) # ?
        self.writeVInt(13) # Rank Team League
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        # Power League Data Array End #
        self.writeInt(0)
        
        self.writeVInt(0)

        self.writeVInt(20)
        for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 20, 21, 22, 23, 24]:
            self.writeVInt(x)

        events = json.loads(open("events.json", "r").read())

        self.writeVInt(len(events))

        for event in events:
            self.writeVInt(events.index(event) + 1)
            if x == 30:
                self.writeVInt(15)
            else:
                self.writeVInt(events.index(event) + 1)
            self.writeVInt(event['Ended'])
            self.writeVInt(event['Timer'])
            self.writeVInt(0)
            self.writeDataReference(15, event['ID'])
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeString()
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            if event['Modifier'] > 0:
                self.writeBoolean(True)
                self.writeVInt(event['Modifier'])
            else:
                self.writeBoolean(False)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(1)  # Power League Data Array
        # Power League Data Array Start #
            self.writeVInt(4) # Season
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
        # Power League Data Array End #
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)
            self.writeVInt(0)

        self.writeVInt(0)
        for x in range(0):
            self.writeVInt(x)

        self.writeArrayVint([20, 35, 75, 140, 290, 480, 800, 1250])
        self.writeArrayVint([20, 50, 140, 280])
        self.writeArrayVint([150, 400, 1200, 2600])

        self.writeUInt8(0)

        self.writeVInt(0)
        for x in range(0):
            self.writeVInt(x)

        self.writeVInt(1)
        for x in range(1):
            self.writeInt(1)
            self.writeInt(41000000 + self.player.theme_id)

        self.writeVInt(0)
        for x in range(0):
            self.writeVInt(x)

        self.writeVInt(0)
        for x in range(0):
            self.writeVInt(x)

        self.writeLong(self.player.ID)

        self.writeVInt(3)
        
        self.writeVInt(81) # нотифы
        self.writeInt(3)
        self.writeBoolean(False)
        self.writeInt(3600) # таймер
        self.writeString("GitHub: LekmaDEV")
        self.writeVInt(0)
        
        self.writeVInt(93) # айди нотифа
        self.writeInt(14)
        self.writeBoolean(True)
        self.writeInt(3600)
        self.writeString() # text
        self.writeVInt(0) # xz
        self.writeVInt(16000000 + 51) # Brawler Id
        
        self.writeVInt(94)
        self.writeInt(15)
        self.writeBoolean(True) # прочитано ли
        self.writeInt(3600)
        self.writeString() # text
        self.writeVInt(29000000 + 376) # скин айди
        
        self.writeVInt(0)
        self.writeBoolean(True)

        bool = False
        self.writeBoolean(bool) # UNK
        if bool:
            self.writeVInt(0)
            for x in range(0):
                self.writeDataReference(0, 0)
                self.writeDataReference(0, 0)
                self.writeDataReference(0, 0)
                self.writeDataReference(0, 0)
                self.writeDataReference(0, 0)
                self.writeVInt(0)

        self.writeVInt(0)
        for x in range(0):
            self.writeVInt(x)
            
        for x in range(3):
            self.writeLogicLong(self.player.ID)

        self.writeString(self.player.name)
        self.writeVInt(1)

        self.writeInt(0)

        self.writeVInt(15)

        self.player.brawlers_card_id = []
        for x in self.player.brawlers_unlocked:
            self.player.brawlers_card_id.append(Cards().get_unlock_by_brawler_id(x))

        self.writeVInt(len(self.player.resources) + len(self.player.brawlers_card_id))

        for x in self.player.brawlers_card_id:
            self.writeDataReference(23, x)
            self.writeVInt(1)

        for resource in self.player.resources:
            self.writeDataReference(5, resource['ID'])
            self.writeVInt(resource['Amount'])

        self.writeVInt(len(self.player.brawlers_id))
        for x in self.player.brawlers_id:
            self.writeDataReference(16, x)
            self.writeVInt(self.player.brawlers_trophies[str(x)])

        self.writeVInt(len(self.player.brawlers_id))
        for x in self.player.brawlers_id:
            self.writeDataReference(16, x)
            self.writeVInt(self.player.brawlers_high_trophies[str(x)])

        self.writeVInt(0)
        for x in range(0):
            self.writeDataReference(16, x)
            self.writeVInt(0)

        self.writeVInt(len(self.player.brawlers_unlocked))
        for x in self.player.brawlers_unlocked:
            self.writeDataReference(16, x)
            self.writeVInt(self.player.brawlers_powerpoints[str(x)])

        self.writeVInt(len(self.player.brawlers_id))
        for x in self.player.brawlers_id:
            self.writeDataReference(16, x)
            self.writeVInt(self.player.brawlers_level[str(x)])

        self.writeVInt(len(self.player.brawlers_spg))
        for x in self.player.brawlers_spg:
            self.writeDataReference(23, x)
            self.writeVInt(1)

        self.writeVInt(0)
        for x in range(0):
            self.writeDataReference(16, x)
            self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)


        self.writeVInt(self.player.gems)
        self.writeVInt(self.player.gems)

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(2)