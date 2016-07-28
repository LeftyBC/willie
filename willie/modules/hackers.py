# coding=utf8
from __future__ import unicode_literals
"""
hackers.py - Random quote from Hackers
"""

import random

from willie.module import commands, example, rule

quotes = [
        "ACID BURN SEZ LEAVE B 4 U R EXPUNGED",
        "A million psychedelic colors.",
        "Angelheaded hipsters burning for the ancient heavenly connection to the starry dynamo in the machinery of night.",
        "Animal.",
        "Anything else, mom? You want me to mow the lawn? Oops! I forgot, New York, No grass.",
        "Are you nuts? Come at me!",
        "'Blow me.' 'Thank you.'",
        "But you've created a virus that's going to cause a worldwide ecological disaster, just to arrest some hacker kid?",
        "Can't get this in stores, man!",
        "Can this wait until both my eyes are open, please?",
        "Check it, Friday.",
        "Congratulations, you just made an enemy for life.",
        "Cool? It's commie bullshit!",
        "Fifteen hundred and SEVEN.",
        "FYI man, alright. You could sit at home, and do like absolutely nothing, and your name goes through like 17 computers a day. 1984? Yeah right, man. That's a typo. Orwell is here now. He's livin' large. We have no names, man. No names. We are nameless!",
        "Get the file.  Otherwise you'll lose all your toys.",
        "'God gave men brains larger than dogs so they wouldn't hump women's legs at cocktail parties.' - Ruth Libby.",
        "God wouldn't be up this late.",
        "Hackers ravage and penetrate delicate public and privately owned computers, infecting them with viruses, and stealing materials for their own ends.  These people, they are terrorists.",
        "HACK THE PLANET!!",
        "His computer virus crashed one thousand five hundred and seven computer systems, including Wall Street trading systems, single handedly causing a seven point drop in the New York Stock Market.",
        "I don't DO dates. But I don't lose either, so you're on!",
        "I don't play well with others.",
        "If it isn't Leopard Boy. And the Decepticons.",
        "I hope you don't screw like you type.",
        "I kinda feel like God.",
        "I know some of you kids got computers at home. But these are school property, people, and I don't want to see any gum stuck to 'em.",
        "It's a little boxy thing, Norm, with switches on it... lets my computer talk to the one there...",
        "It's got a 28 point 8 BPS modem!",
        "It's in that place where I put that thing that time.",
        "It's root slash period workspace slash period garbage period.",
        "JOEY?!",
        "Jolt Cola.  THE soft drink of the elite hacker.",
        "Kid, don't threaten me. There are worse things than death, and uh, I can do all of them.",
        "Listen you guys, help yourself to anything in the fridge... Cereal has.",
        "Love, sex, secret and... God.",
        "Meet Cereal Killer. As in Froot Loops? But he does know things.",
        "Mess with the best, die like the rest.",
        "Never fear, I is here.",
        "Never send a boy to do a woman's job.",
        "Of all the things I've lost, I miss my mind the most.  - Ozzie Osborne",
        "One more dude outta you and I'mma slap the shit outta you!",
        "Pool on the roof must have a leak.",
        "Razor and Blade? They're flakes!",
        "Remember, hacking is more than just a crime. It's a survival trait.",
        "Right, well my BLT drive on my computer just went AWOL, and I've got this big project due tomorrow for Mr. Kawasaki, and if I don't get it in, he's gonna ask me to commit Hari Kari...",
        "Security, uh... Norm...",
        "Someone didn't bother reading my carefully prepared memo on commonly-used passwords. Now, then, as I so meticulously pointed out, the four most-used passwords are: love, sex, secret, and... God.",
        "Spandex: it's a privilege, not a right.",
        "Technicolor rainbow.",
        "That's why they call me Stallion.",
        "The defendant, Dade Murphy, who calls himself \"Zero Cool\", has repeatedly committed criminal acts of a malicious nature.",
        "There is no right and wrong. There's only fun and boring.",
        "This defendant possesses a superior intelligence, which he uses to a destructive and antisocial end.",
        "This is the end, my friend. Thank you for calling.",
        "Type \"cookie\", you idiot.",
        "Ugh. Hard copy.",
        "Unbelievable.  A hacker!",
        "We have just gotten a wake-up call from the Nintendo Generation.",
        "What are you, stoned or stupid? You don't hack a bank across state lines from your house, you'll get nailed by the FBI.",
        "What, did your 'ma buy you a 'puter for Christmas?",
        "What is it, you hapless techno-weenie?",
        "When I was a child, I spoke as a child, I understood as a child, I thought as a child, but when I became a man, I put away childish things. What? It's Corinthians one, chapter thirteen verse eleven. No duh!",
        "Whoa! This isn't woodshop class?",
        "Why of course, Jennifer...",
        "Yak yak yak.  Get a job!",
        "Yeah.  RISC is good.",
        "Yo, Joey's gettin' STUPID busy!",
        "'You look good in a dress.' 'You would have looked better.'",
        "You're in the butter zone now, baby.",
        "You wanted to know who I am, Zero Cool? Well, let me explain the New World Order. Governments and corporations need people like you and me. We are Samurai... the Keyboard Cowboys... and all those other people who have no idea what's going on are the cattle. Moooo.",
        "Zero Cool? Crashed fifteen hundred and seven computers in one day? Biggest crash in history, front page New York Times August 10th, 1988. I thought you was black man. YO THIS IS ZERO COOL!",
]

@commands('hackers','dade')
@rule(r'(hack|dade|joey|jennifer|burn|cereal|nikon|phreak|phantom|nynex|plague)')
@example('hackers - random quote from our favourite movie')
def random_hackers_quote(bot, trigger):
        bot.say(random.choice(quotes))

