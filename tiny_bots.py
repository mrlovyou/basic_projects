class tinyBot:
    
    def __init__(self, name, type, level = 5):
        self.name = name
        self.type = type
        self.level = level
        self.battery = level * 5
        self.max_battery = level * 5
        self.is_out_of_juice = False

    def __repr__(self):
        return "This tinyBro is level {level} and has {battery} battery points. They are a {type} type tinyBro".format(level=self.level, battery = self.battery, type = self.type)
    
    def plug_in(self):
        self.is_out_of_juice = False
        if self.battery == 0:
            self.battery == 1
        print ("{tinyBot} was plugged in. Their battery is at {battery} point".format(tinyBot=self.name, battery = self.battery))
    
    def full_drain(self):
        self.is_out_of_juice = True
        if self.battery != 0:
            self.battery = 0
        print ("{tinyBot} was drained. They are at {battery} battery points".format(tinyBot=self.name, battery = self.battery))
    def drain_battery(self, amount):
        self.battery -= amount
        if self.battery <= 0:
            self.battery = 0
            self.full_drain()
        else:
            print ("{tinyBot} has {battery} battery points remaining".format(tinyBot= self.name, battery = self.battery))

# class for controllers, the PEOPLE who control the tinyBots

class Controller:
    def __init__(self, name, bank, fainted = False):
        self.name = name
        self.BotList = [butlertron]
        self.bank = bank
        self.fainted = fainted
        self.current_bot = 0
        self.tiny_packs = 0
    def __repr__(self):
        print("{trainer} has {botlist} tinyBros. They have {bank} gold. The controller has the following bot(s):".format(trainer = self.name, botlist = len(self.BotList), bank = self.bank))
        for bot in self.BotList:
            print (bot.name)
        return "The current active bot is {active_bot}".format(active_bot = self.BotList[self.current_bot].name)
    
    def switch_active_bot(self, new_active):
        if new_active < len(self.BotList) and new_active >= 0:
            if self.BotList[new_active].is_out_of_juice:
                print ("{bot} is out of battery. You can't make it your active bot".format(bot= self.BotList[new_active].name))
            elif new_active == self.current_bot:
                print ("{bot} is already your active bot".format(bot= self.BotList[new_active].name))
            else: 
                self.current_bot = new_active
                print ("Go {bot}, it's your chance!".format(bot = self.BotList[self.current_bot].name))
    def buy_tiny_pack(self, amount):
        if self.bank >= 20 * amount:
            self.bank -= 20 * amount
            self.tiny_packs += amount
            print ("{name} now has {tinypack} tiny packs".format(name = self.name, tinypack = self.tiny_packs))
        else:
            print ("You only have {bank} gold. Tiny packs cost 20 gold.".format(bank = self.bank))
    def use_tiny_pack(self, bot):
        if self.BotList[bot].battery > 0 and self.BotList[bot].battery < self.BotList[bot].max_battery:
            self.BotList[bot].battery += 20
            if self.BotList[bot].battery > self.BotList[bot].max_battery:
                self.BotList[bot].battery = self.BotList[bot].max_battery
            print ("{bot} is at {battery} battery points".format(bot = self.BotList[bot].name, battery = self.BotList[bot].battery))
        elif self.BotList[bot].battery == 0:
            print ("{bot} is at 0 battery points. They need to be revived first.".format(bot = self.BotList[bot].name))
        else:
            print ("{bot} is at full battery points. The tiny pack was not used".format(bot = self.BotList[bot].name))

        
#        instances of tinyBots

butlertron = tinyBot("Butlertron", "Normal")
hakkuh = tinyBot("Hakkuh", "Dark")

#       instances of controllers

love = Controller("Love",500)
ash = Controller("Ash", 500)

#         "gameplay"

love.buy_tiny_pack(3)

love.use_tiny_pack(0)

kush = Controller("Kush", 500)

kush.BotList[hakkuh]


