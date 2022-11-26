#! /usr/bin/env python3

from mastodon import Mastodon
from dotenv import load_dotenv
import sys, os, random

# types of tea we recommend
teas = [
    [ 'Assam', 'a popular black tea from north eastern India' ],
    [ 'Bancha', 'a Japanese green tea, rare outside Japan' ],
    [ 'Ceylon', 'a rich black tea from the island of Sri Lanka' ],
    [ 'Darjeeling', 'a delicate black tea, from northern India' ],
    [ 'Earl Grey', 'a blend of black tea flavoured with bergamot' ],
    [ 'Fukamushi', 'a steamed green tea from Japan' ],
    [ 'Gunpowder' , 'a smoky green tea processed into pellets' ],
    [ 'Hojicha', 'a roasted version of Japanese Bancha green tea' ],
    [ 'Irish Breakfast', 'a blend of black teas, quite popular in...:)' ],
    [ 'Jasmine', 'a green tea flavoured with jasmine flowers' ],
    [ 'Kukicha', 'a Japanese green tea, made from the twigs' ],
    [ 'Lapsang Souchong', 'a strong black tea, flavoured with pinewood smoke' ],
    [ 'Matcha', 'a traditional Japanese ceremonial green tea, ground from the whole leaf' ],
    [ 'Nilgiri', 'a black tea from a lesser known Indian tea region' ],
    [ 'Oolong', 'a floral tea produced in China and Taiwan' ],
    [ 'Puerh', 'a Chinese fermented black tea, very earthy' ],
    [ 'Keemun', 'a fruity black tea produced in the Chinese town of Qimen' ],
    [ 'Rooibos', 'a herbal beverage (not actually a tea) from South Africa' ],
    [ 'Silver Needles', 'a white tea, also known as Bai Hao Yinzhen' ],
    [ 'Tieguanyin', 'a variety of Oolong tea, floral aroma' ],
    [ 'Yellow Tea', 'a variant of green tea, processed to reduce the colour' ],
    [ 'English Breakfast', 'a blend of black teas, the most popular tea in the UK' ],
]

# break reminder phrases
phrases = [
    'Ooh look at the time! Let\'s grab a cuppa eh?',
    'Goodness, I\'m parched, how about a brew?',
    'Anyone fancy a wee break for tea?',
    'Screen break! Whose turn is it to put the kettle on?',
    'Tea up! Who takes sugar again?',
    'Kettle\'s on! Where did you put your mug?',
    'I\'ll pop the kettle on, when did you last wash this mug?',
    'Nearly done here, tea?',
]

# grab access token (or bail)
load_dotenv()
if not 'TEABOT_ACCESS_TOKEN' in os.environ:
    print('Missing TEABOT_ACCESS_TOKEN in environment or .env')
    sys.exit(1)
if not 'TEABOT_BASE_URL' in os.environ:
    os.environ['TEABOT_BASE_URL'] = 'https://botsin.space/'

# create API proxy
mastodon = Mastodon(
    api_base_url = os.environ['TEABOT_BASE_URL'],
    access_token = os.environ['TEABOT_ACCESS_TOKEN']
)

# select a tea and reminder phrase
random.seed()
tea = teas[random.randrange(0,len(teas))]
phrase = phrases[random.randrange(0,len(phrases))]

# toot!
mastodon.status_post(f'{phrase}\n\nHow about some {tea[0]}, {tea[1]}', visibility='unlisted')
if 'TEABOT_VERBOSE' in os.environ:
    print(f'Toot!: {phrase}\n\nHow about {tea[0]}, {tea[1]}')
