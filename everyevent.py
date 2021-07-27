import os
import re
import bs4

events = [
  '100 metres',
  '200 metres',
  '400 metres',
  '800 metres',
  '1500 metres',
  '5000 metres',
  '10,000 metres',
  '5 miles'
]

for women in [ False, True ]:
  print('Women' if women else 'Men')
  for year in sorted(os.listdir('html')):
    soup = bs4.BeautifulSoup(open('html/' + year).read(), 'html.parser')
    if women:
      try: soup = soup.find('span', id = 'Women').find_next('table')
      except: continue
    medalists = None
    for evt in events:
      td = soup.select_one('td:-soup-contains("{}")'.format(evt))
      if td:
        evtmedals = { a.text for a in td.parent.find_all('a', href = re.compile('/wiki/.*_at_the_.*_Summer_Olympics$')) }
        if medalists is None: medalists = evtmedals
        else: medalists = { cnt for cnt in medalists if cnt in evtmedals }
    if (len(medalists) > 0): print(year, medalists)
