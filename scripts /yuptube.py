#! /usr/bin/python3
banner = r'''
#EXTINF:-1 group-title="SonyLiv" tvg-logo="https://i.imgur.com/otcZgao.png" tvg-id="SETHD.in" tvg-chno="206", SET HD
https://dai.google.com/linear/hls/event/dBdwOiGaQvy0TA1zOsjV6w/master.m3u8

#EXTINF:-1 group-title="SonyLiv" tvg-logo="https://i.imgur.com/OEoQcet.png" tvg-id="SONYSABHD.in" tvg-chno="207", Sony SAB HD
https://dai.google.com/linear/hls/event/CrTivkDESWqwvUj3zFEYEA/master.m3u8

#EXTINF:-1 group-title="SonyLiv" tvg-logo="https://i.imgur.com/aKTbdBj.png" tvg-id="SonyPal.in" tvg-chno="208", Sony Pal
https://dai.google.com/linear/hls/event/dhPrGRwDRvuMQtmlzppzQQ/master.m3u8

#EXTINF:-1 group-title="SonyLiv" tvg-logo="https://i.imgur.com/XBzYhFl.png" tvg-id="SONYMAXHD.in" tvg-chno="256", Sony MAX HD
https://dai.google.com/linear/hls/event/UcjHNJmCQ1WRlGKlZm73QA/master.m3u8

#EXTINF:-1 group-title="SonyLiv" tvg-logo="https://i.imgur.com/R3fXqJL.png" tvg-id="SONYMAX2.in" tvg-chno="257", Sony MAX 2
https://dai.google.com/linear/hls/event/MdQ5Zy-PSraOccXu8jflCg/master.m3u8

#EXTINF:-1 group-title="SonyLiv" tvg-logo="https://i.imgur.com/HtgPSH0.png" tvg-id="SonyWah.in" tvg-chno="", Sony WAH
https://dai.google.com/linear/hls/event/gX5rCBf6Q7-D5AWY-sovzQ/master.m3u8

#EXTINF:-1 group-title="SonyLiv" tvg-logo="https://i.imgur.com/l0lNxsR.png" tvg-id="SONYSPORTSTEN1HD.in" tvg-chno="301", Sony Ten 1 HD
https://dai.google.com/linear/hls/event/wG75n5U8RrOKiFzaWObXbA/master.m3u8

#EXTINF:-1 group-title="SonyLiv" tvg-logo="https://i.imgur.com/vkiabNb.png" tvg-id="SONYSPORTSTEN2HD.in" tvg-chno="302", Sony Ten 2 HD
https://dai.google.com/linear/hls/event/V9h-iyOxRiGp41ppQScDSQ/master.m3u8

#EXTINF:-1 group-title="SonyLiv" tvg-logo="https://i.imgur.com/h3SCSM1.png" tvg-id="SONYSPORTSTEN3HD.in" tvg-chno="303", Sony Ten 3 HD
https://dai.google.com/linear/hls/event/ltsCG7TBSCSDmyq0rQtvSA/master.m3u8

#EXTINF:-1 group-title="SonyLiv" tvg-logo="https://i.imgur.com/JTtYQsS.png" tvg-id="SONYSPORTSTEN5HD.in" tvg-chno="304", Sony Ten 5 HD
https://dai.google.com/linear/hls/event/Sle_TR8rQIuZHWzshEXYjQ/master.m3u8

#EXTINF:-1 group-title="SonyLiv" tvg-logo="https://i.imgur.com/kGT3Akw.png" tvg-id="SONYBBCEarthHD.in" tvg-chno="414", SONY BBC Earth HD
https://dai.google.com/linear/hls/event/6bVWYIKGS0CIa-cOpZZJPQ/master.m3u8

#EXTINF:-1 group-title="SonyLiv" tvg-logo="https://i.imgur.com/Tu0nWsp.png" tvg-id="SONYYAY!.in" tvg-chno="516", Sony YAY
https://dai.google.com/linear/hls/event/GPY7RqOrSkmKJ8z1GbVNhg/master.m3u8
'''
import requests
import os
import sys

windows = False
if 'win' in sys.platform:
    windows = True

def grab(url):
    response = requests.get(url, timeout=15).text
    if '.m3u8' not in response:
        #response = requests.get(url).text
        if '.m3u8' not in response:
            if windows:
                print('https://simperpie.github.io/yuptube/assets/info.m3u8')
                return
            #os.system(f'wget {url} -O temp.txt')
            os.system(f'curl "{url}" > temp.txt')
            response = ''.join(open('temp.txt').readlines())
            if '.m3u8' not in response:
                print('https://simperpie.github.io/yuptube/assets/info.m3u8')
                return
    end = response.find('.m3u8') + 5
    tuner = 100
    while True:
        if 'https://' in response[end-tuner : end]:
            link = response[end-tuner : end]
            start = link.find('https://')
            end = link.find('.m3u8') + 5
            break
        else:
            tuner += 5
    print(f"{link[start : end]}")

print('#EXTM3U x-tvg-url="https://simperpie.github.io/TVGuide/simper_epg.xml.gz"')
#s = requests.Session()
with open('../yuptube.txt') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        if not line.startswith('https:'):
            line = line.split('|')
            ch_name = line[0].strip()
            grp_title = line[1].strip().title()
            tvg_logo = line[2].strip()
            tvg_id = line[3].strip()
            tvg_chno = line[4].strip()
            print(f'\n#EXTINF:-1 group-title="{grp_title}" tvg-logo="{tvg_logo}" tvg-id="{tvg_id}" tvg-chno="{tvg_chno}", {ch_name}')
        else:
            grab(line)
print(banner)
            
if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')
