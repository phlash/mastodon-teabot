#! /usr/bin/env python3

from mastodon import Mastodon
from dotenv import load_dotenv
import sys, os, random

# types of tea we recommend
teas = [
    [ 'Assam', 'a popular black tea from north eastern India' ],
    [ 'Bancha', 'a Japanese green tea, rare outside Japan' ],
    [ 'Ceylon', 'a rich black tea from the island of Sri Lanka' ],
]

# break reminder phrases
phrases = [
    'Ooh look at the time! Let\'s grab a cuppa eh?',
    'Goodness, I\'m parched, how about a brew?',
    'Anyone fancy a wee break for tea?',
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
