#!/usr/bin/python3
'''
ping.py - Phenny Ping Module
Author: Sean B. Palmer, inamidst.com
About: http://inamidst.com/phenny/

Modified from ping.py by Amos

Modified by Jordan Kinsley <jordan@jordantkinsley.org>
'''

import random

saucyreplies = ('Kinsley','MalevolentSpoon','Aurora','Cocoa','TiredFoal','Lapsus')

def hello(phenny, input): 
    greeting = random.choice(('Hi', 'Hey', 'Hello'))
    punctuation = random.choice(('.', '!'))
hello.rule = r'(?i)(hi|hello|hey) (I|Bli|Pi)nkie(Pie)?(Bot)?\b'

def sniff(phenny, input): 
    sniffresponse = random.choice(('Hey! Do I know you?', 'Umm...', 'Do I smell funny - like \'haha\' funny or \'funny\' funny?', 'EEP!', '\x01ACTION prods ' + input.nick + '\'s nose.\x01'))
sniff.rule = r'(?i)(\x01ACTION sniffs (I|Bli|Pi)nkie(Pie)?(Bot)?)'

def grope(phenny, input): 
    groperesponse = random.choice(('I love hugs!', '\x01ACTION hugs ' + input.nick + ' SUPER hard.\x01', 'ACK!', 'Hahaha, you suprised me, ' + input.nick + '!', 'Gasp!'))
grope.rule = r'(?i)(\x01ACTION runs over and squeezes (I|Bli|Pi)nkie(Pie)?(Bot)?)'

def flirt(phenny, input): 
    attractresponse = '.'
    if input.nick in saucyreplies:
        attractresponse = random.choice(('Well, hey there, cutie. ;)','Such a flirt!','\x01ACTION pounces ' + input.nick + '.\x01','\x01ACTION winks at ' + input.nick + '.\x01'))
    else: 
        attractresponse = random.choice(('I don\'t like you that way...', 'Sorry, I\'m not like that.', 'Flattering, but no.', 'Are you trying to flirt with me?', 'I\'d rather just be friends.', '...'))
flirt.rule = r'(?i)(\x01ACTION winks at (I|Bli|Pi)nkie(Pie)?(Bot)?)'

def lick(phenny, input): 
    lickresponse = '.'
    if input.nick in saucyreplies:
        lickresponse = random.choice(('\x01ACTION blushes.\x01', '\x01ACTION pounces ' + input.nick + '.\x01', '\x01ACTION steals ' + input.nick + '\'s virginity.\x01', 'Hee... We better take this elsewhere...','Ooooh!'))
    else:
        lickresponse = random.choice(('...', 'What do I taste like? I want to know!', 'Ah!', 'Eep!', 'That tickles!', '\x01ACTION licks ' + input.nick + ' right back.\x01', 'I don\'t like you that way...', 'Eww...','Waugh...', 'Ah!', '!', '\x01ACTION blushes.\x01', '\x01ACTION pounces ' + input.nick + '.\x01', '\x01ACTION steals ' + input.nick + '\'s virginity.\x01', 'Hehe...'))
lick.rule = r'(?i)(\x01ACTION licks (I|Bli|Pi)nkie(Pie)?(Bot)?)'

def growl(phenny, input): 
    # TODO: add more responses
    growlresponse = random.choice(('Silly puppy!', '\x01ACTION gives ' + input.nick + ' a slice of cake.\x01', 'What did I do?', '\x01ACTION growls back.\x01', 'Something wrong?'))
growl.rule = r'(?i)(\x01ACTION growls at (I|Bli|Pi)nkie(Pie)?(Bot)?)'

def kiss(phenny, input):
    kissresponse = '.'
    if input.nick in saucyreplies:
        kissresponse = random.choice(('\x01ACTION blushes.\x01', '\x01ACTION pounces ' + input.nick + '.\x01', '\x01ACTION steals ' + input.nick + '\'s virginity.\x01', 'Hee... We better take this elsewhere...','Ooooh!','\x01ACTION kisses ' + input.nick + ' back.\x01','\x01ACTION pushes ' + input.nick + ' to the ground and ravishes them.\x01'))
    else:
        kissresponse = random.choice(('\x01ACTION blushes\x01','What was that for?','\x01ACTION leaps into the air in suprise.\x01', '\x01ACTION pushes ' + input.nick + ' away.\x01', '\x01ACTION bucks ' + input.nick + ' in the chest. Hard.\x01', '\x01ACTION giggles.\x01'))
kiss.rule = r'(?i)(\x01ACTION kisses (I|Bli|Pi)nkie(Pie)?(Bot)?)'

def interjection(phenny, input): 
    phenny.say(input.nick + '!')
interjection.rule = r'(I|Bli|Pi)nkie(Pie)?(Bot)?!'
interjection.priority = 'high'
interjection.thread = False

def hugs(phenny, input):
    hugresponse = random.choice(('\x01ACTION hugs ' + input.nick + ' back.\x01', '\x01ACTION giggles.\x01', 'Thanks, ' + input.nick + ', that felt really good!', 'Hugs for everypony!'))
hugs.rule = r'(\x01ACTION)? (?i)(hugs) (?i)(I|Bli|Pi)nkie(Pie)?(Bot)?'

def tickles(phenny, input):
    tickleresponse = '.'
    if input.nick in saucyreplies:
        tickleresponse = random.choice(('Hehehe! That tickles!', '\x01ACTION rolls on the floor, laughing.\x01','EEP!','\x01ACTION gigglesnorts\x01','\x01ACTION rolls ' + input.nick + ' over and tickles them back!\x01','\x01ACTION declares a tickle war!\x01','\x01ACTION giggles and pushes ' + input.nick + ' to the floor and kisses them.\x01', '\x01ACTION giggles and takes ' + input.nick + '\'s hoof, and leads them to private room.\x01'))
    else:
        tickleresponse = random.choice(('Hehehe! That tickles!', '\x01ACTION rolls on the floor, laughing.\x01','EEP!','\x01ACTION gigglesnorts\x01','\x01ACTION rolls ' + input.nick + ' over and tickles them back!\x01','\x01ACTION declares a tickle war!\x01'))
tickles.rule = r'(\x01ACTION)? (?i)(tickles) (?i)(I|Bli|Pi)nkie(Pie)?(Bot)?'

def parties(phenny, input):
    # TODO: add more responses
    partyresponse = random.choice(('Woo! A party!', '\x01ACTION invites the whole town to party!\x01', '\x01ACTION grabs her emergency party supplies!\x01', '\x01ACTION puts on some sweet jams!\x01'))
parties.rule = r'(\x01ACTION)? (?i)(parties with) (?i)(I|Bli|Pi)nkie(Pie)?(Bot)?'

def smiles(phenny, input):
    # \x01ACTION smiles back!\x01 gets extra "weight" because it's a good response
    smilesresponse = random.choice(('Aww, I love to see my friends smile!','\x01ACTION smiles back!\x01','#youtubelink','\x01ACTION grins!\x01','\x01ACTION claps her hooves together!\x01','\x01ACTION smiles back!\x01'))
smiles.rule = r'(\x01ACTION)? (?i)smiles (?i)(at|with|to|because of) (?i)(I|Bli|Pi)nkie(Pie)?(Bot)?'

#TODO: create a "frowns" function with rule for "frownie" smilies and /me frowns.
def frowns(phenny, input):
    # we're going to have a one-in-ten chance of Pinkie trying to cheer you up
    if random.randint(1,10) == 10:
        frownsresponse = random.choice(('Aww, don\'t be sad, ' + input.nick + ', I\'m here!','\x01ACTION hugs ' + input.nick + '\x01', 'Cheer up, ' + input.nick + ', all of your friends are here!'))
frowns.rule = r'(:<|:C|D:)|(\x01ACTION (?i)frowns(.*))|:\('

def thanks(phenny, input):
    thanksresponse = random.choice(('No problemo', 'My pleasure', 'Hahah, you\'re welcome','I\'m always there for my friends'))
    thankspuncuation = random.choice(('!', '.'))
thanks.rule = r'(?i)(Thank( you|s)?(,)? (I|Bli|Pi)nkie(Pie)?(Bot)?)'

# TODO: add these actions and appropriate responses
'''
Actions to add: 
(first to four stars get written, and any action with three or more at that time will be written as well)
* pokes ****
* cupcakes *
* kicks *
* good night *
* pets **
* hoofshake **
* flank-smack *
* how are you *
* gives a massage to *
* fondles/molests/gropes **
'''

# action string '\x01ACTION\x01'

if __name__ == '__main__': 
	print(__doc__.strip())
