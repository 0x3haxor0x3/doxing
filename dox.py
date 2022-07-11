#! /usr/bin/python3
from requests import get,exceptions
from os import system
from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument("username",type=str,nargs='?')
args = parser.parse_args()
r = "\033[31m"
g = "\033[32m"
y = "\033[33m"
b='\33[36m'
p = "\033[35m"
banner=f"""{y}

*********************************************************************************
*                         Cyber Security Researcher                             *                                                
*********************************************************************************
*                                                                               *
* ██████╗  ██████╗ ██╗  ██╗██╗███╗   ██╗ ██████╗     ██╗   ██╗ ██╗    ██████╗   *
* ██╔══██╗██╔═══██╗╚██╗██╔╝██║████╗  ██║██╔════╝     ██║   ██║███║   ██╔═████╗  *
* ██║  ██║██║   ██║ ╚███╔╝ ██║██╔██╗ ██║██║  ███╗    ██║   ██║╚██║   ██║██╔██║  *
* ██║  ██║██║   ██║ ██╔██╗ ██║██║╚██╗██║██║   ██║    ╚██╗ ██╔╝ ██║   ████╔╝██║  *
* ██████╔╝╚██████╔╝██╔╝ ██╗██║██║ ╚████║╚██████╔╝     ╚████╔╝  ██║██╗╚██████╔╝  *
* ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝ ╚═════╝       ╚═══╝   ╚═╝╚═╝ ╚═════╝   *
*                                                                               *                                                                            
*********************************************************************************
*       Kaizen - X-m3n - Yhuricka - MangKepweng - Oracle - Luca Hanabi          *                                                
********************s************************************************************  


{g}This Tool for only Doxing of Social Media Accounts.

{g}Developed By: {y}X-m3n
"""
def scanner(u):
 social={
 "facebook":f"https://facebook.com/{u}",
 "twitter":f"https://twitter.com/{u}",
 "telegram":f"https://t.me/{u}",
 "youtube":f"https://youtube.com/{u}",
 "pornhub":f"https://www.pornhub.com/model/{u}",
 "instagram":f"https://instagram.com/{u}",
 "tiktok":f"https://www.tiktok.com/{u}",
 "github":f"https://github.com/{u}",
 "linkedin":f"https://www.linkedin.com/in/{u}",
 "plus":f"https://plus.google.com/{u}",
 "pinterest":f"https://pinterest.com/{u}",
 "flickr":f"https://flickr.com/people/{u}",
 "hashnode":f"https://hashnode.com/@{u}",
 "twitter":f"https://twitter.com/{u}",
 "medium":f"https://medium.com/@{u}",
 "hackerone":f"https://hackerone.com/{u}",
 "imgur":f"https://imgur.com/user/{u}",
 "spotify":f"https://open.spotify.com/user/{u}",
 "pastebin":f"https://pastebin.com/u/{u}",
 "wattpad":f"https://wattpad.com/user/{u}",
 "codecademy":f"https://codecademy.com/{u}",
 "wikipedia":f"https://www.wikipedia.org/wiki/User:{u}",
 "blogspot":f"https://{u}.blogspot.com/",
 "tumblr":f"https://{u}.tumblr.com/",
 "wordpress":f"https://{u}.wordpress.com/",
 "steamcommunity":f"https://steamcommunity.com/id/{u}",
 "zone-h":f"http://www.zone-h.org/archive/notifier={u}"
 }
 print(f"\n{p}starting:\n")
 spece=" "*20
 print(f"{g}#"*126)
 print(f"{g}# {r}SOCIAL MEDIA   {g}|        {r}USER {g}        | {r}STATUS CODE{g} | {r}                   URL   {g}      {spece}                   #")
 for i,j in social.items():
  try:
   req = get(j)
   code=req.status_code
  except exceptions.TooManyRedirects:
   print("TooManyRedirects")
   break
  except exceptions.ConnectionError:
   print("\n\nConnectionError!\n\ncheck your internet connection!\n\n")
   break
  except exceptions.Timeout: 
   continue
  print(f"{g}#"+f"{p}-"*124+f"{g}#")
  if code==200:
   user=f"{g}|{y}        Found        "
  elif code==404:
   user=f"{g}|{r}      Not Found      "
  else:
   user=f"{g}|{b}undefined status code"
   j="none"
  media=f"{g}# {y}"+i+" "*(15-len(i))
  code=f"{g}|     {y}"+str(code)+" "*5
  url=f"{g}|{y} "+j+" "*(70-len(j))+f"{g}#"
  print(media+user+code+url)
 print("#"*126)
 print(f"\n{r}vist {g}https://en.wikipedia.org/wiki/List_of_HTTP_status_codes{r} to know more about status codes!\n")
 print(f"{b}Thank you\n")
 print(f"{y}follow gmail:{g}@xmenhaxor\n")
def main(username):
 system("clear")
 print(banner)
 print(f"{r}Read Team: {y}Kaizen - X-m3n - Yhuricka - MangKepweng\n")
 print(f"{b}Blue Team: {y}Oracle - Luca Hanabi\n")
 if username == None:
  u=input(f"{y}Enter the username{r}:{g}")
  scanner(u)
 else:
  scanner(username)
if __name__ == "__main__":
 main(args.username)