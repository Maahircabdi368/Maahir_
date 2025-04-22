from colorama import Fore,init,Style
import pyfiglet
import requests
from urllib.parse import quote
import time

sites={
'GitHub' : 'https://github.com/{}',
'twitter'  : 'https://twitter.com/{}',
'facebook': 'https://facebook.com/{}',
'tiktok' : 'https://tiktok.com/@{}',
'instagram': 'https://instagram.com/{}',
'pinterest': 'https://pinterest.com/{}',
'linkedin': 'https://www.linkedin.com/in/{}',
'snapchat': 'https://www.snapchat.com/add/{}',
'youtube': 'https://www.youtube.com/{}',
'reddit': 'https://www.reddit.com/user/{}',
'tumblr': 'https://{}.tumblr.com',
'soundcloud': 'https://soundcloud.com/{}',
'vimeo': 'https://vimeo.com/{}',
'twitch': 'https://www.twitch.tv/{}',
'coinmarketcap': 'https://coinmarketcap.com/currencies/{}',
'coingecko': 'https://www.coingecko.com/en/coins/{}',
'opensea': 'https://opensea.io/{}',
'etherscan': 'https://etherscan.io/address/{}',
'binance': 'https://www.binance.com/en/price/{}',
'discord': 'https://discord.com/users/{}' ,
'telegram': 'https://t.me/{}',
'mastodon': 'https://mastodon.social/@{}',
'stackoverflow': 'https://stackoverflow.com/users/{}',
'gitlab': 'https://gitlab.com/{}',
'bitbucket': 'https://bitbucket.org/{}',
'fiverr': 'https://www.fiverr.com/{}',
'upwork': 'https://www.upwork.com/freelancers/~{}' ,
'bandcamp': 'https://bandcamp.com/{}',
'deviantart': 'https://www.deviantart.com/{}',
'behance': 'https://www.behance.net/{}',
 'dribbble': 'https://dribbble.com/{}',
 'replit': 'https://replit.com/@{}',
 'medium': 'https://medium.com/@{}',
 'kaggle': 'https://www.kaggle.com/{}',
 'producthunt': 'https://www.producthunt.com/@{}',
 'codepen': 'https://codepen.io/{}',   'goodreads': 'https://www.goodreads.com/{}',  'aboutme': 'https://about.me/{}',
 'devto': 'https://dev.to/{}',
  'hashnode': 'https://hashnode.com/@{}',
 'buymeacoffee': 'https://www.buymeacoffee.com/{}',
    'patreon': 'https://www.patreon.com/{}',
    'itchio': 'https://{}.itch.io',
    'lastfm': 'https://www.last.fm/user/{}',
    '500px': 'https://500px.com/p/{}',
    'instructables': 'https://www.instructables.com/member/{}',
    'gravatar': 'https://en.gravatar.com/{}',
    'steam': 'https://steamcommunity.com/id/{}',
    'tripadvisor': 'https://www.tripadvisor.com/Profile/{}',
    'myanimelist': 'https://myanimelist.net/profile/{}',
    'roblox': 'https://www.roblox.com/user.aspx?username={}',
   
    'pixiv': 'https://www.pixiv.net/en/users/{}',
    'hackthebox': 'https://app.hackthebox.com/profile/{}',
    'tryhackme': 'https://tryhackme.com/p/{}',
    'letterboxd': 'https://letterboxd.com/{}',
    'namemc': 'https://namemc.com/profile/{}',
    'chess': 'https://www.chess.com/member/{}',
    'lichess': 'https://lichess.org/@/{}',
    'trello': 'https://trello.com/{}',
    'notion': 'https://www.notion.so/{}',
    'sketchfab': 'https://sketchfab.com/{}',
'bluesky': 'https://bsky.app/profile/{}',
'threads': 'https://www.threads.net/@{}',
'clubhouse': 'https://www.clubhouse.com/@{}',
'quora': 'https://www.quora.com/profile/{}',
'venmo': 'https://venmo.com/{}',
'cashapp': 'https://cash.app/{}',
'paypalme': 'https://www.paypal.me/{}',
'duolingo': 'https://www.duolingo.com/profile/{}',
'codementor': 'https://www.codementor.io/@{}',
'freelancer': 'https://www.freelancer.com/u/{}',
'stackexchange': 'https://stackexchange.com/users/{}',
'npm': 'https://www.npmjs.com/~{}',
'pypi': 'https://pypi.org/user/{}',
'runscope': 'https://www.runscope.com/users/{}',
'unsplash': 'https://unsplash.com/@{}',
'canva': 'https://www.canva.com/{}',
'taplink': 'https://taplink.cc/{}',
'carrd': 'https://{}.carrd.co',
'substack': 'https://{}.substack.com',
'loom': 'https://www.loom.com/u/{}',

}

init(autoreset=True)
def check_username(username):
    while True:
        encoded_username = quote(username)
        headers = {'User-Agent': 'Mozilla/5.0'}  # Samee headers u eg browser

        for site, url in sites.items():
            profile_url = url.format(encoded_username)
            try:
                response = requests.get(profile_url,headers=headers, timeout=5)
                if response.status_code == 200:
                    print(f'{Fore.GREEN}[*] {site} {Style.RESET_ALL} : {profile_url}')
                else:
                    print(f'{Fore.RED}[*] {Style.RESET_ALL} {site} : {Fore.RED}not found')
            except requests.RequestException:
                print(f'{Fore.RED}[ERROR] {Style.RESET_ALL} {site}: connection failed')
                time.sleep(0.5)

        doorasho_kale = input(Fore.YELLOW+Style.BRIGHT+'\n. [+] ma doonaysaa username kale baarto (yes/no): ').lower()
        if doorasho_kale == 'no':
            print(Fore.CYAN+'thanks for using user finder')
            break
        elif doorasho_kale=='yes':
        	username = input(Fore.YELLOW + 'gali username: ')
        	continue
        else:
        	print(Fore.RED+'fadlan gali no ama yes')
        	break
    
	


banner= Fore.CYAN+pyfiglet.figlet_format('user finder', font='slant')
print(banner)
print(Fore.BLUE + Style.BRIGHT + " created by: maahir\n")
			
username=input(Fore.YELLOW+Style.BRIGHT+'  gali username:')

	


check_username(username)
