#!/usr/bin/python
from __future__ import print_function 
import json
import datetime
import sys
import requests

def pr(dd,last=False):
    if not last:
		print(dd,end=' ')
		return
    print(dd)
if len(sys.argv) != 2:
	pr("Usage : grid2agent [grid api key]")
	sys.exit()

#with open('stats') as data_file:    
#    data = json.load(data_file)

url = 'https://the-grid.org/r/export/?key=' + sys.argv[1]
data = requests.get(url,verify=False).json()
for d in data:
	pr(datetime.datetime.fromtimestamp(d['timestamp']).strftime('%Y-%m-%d %H:%M:%S')) # Date (yyyy-mm-dd) Time (hh:mm:ss) 
	stats=d['stats']
	pr(stats['ap']) #ap
	pr(stats['portals_visited']) #explorer
	pr(stats['portals_discovered']) #seer
	pr(stats['xm_collected']) #collector
	pr(stats['opr_agreements']) #recon
	pr(stats['distance_walked']) #trekker
	pr(stats['resonators_deployed']) #builder
	pr(stats['links_created']) #connector
	pr(stats['fields_created']) #mind-controller
	pr(stats['mu_captured']) #illuminator
	pr(stats['longest_link']) #binder
	pr(stats['largest_field']) #country-master
	pr(stats['xm_recharged']) #recharcger
	pr(stats['portals_captured']) #liberator
	pr(stats['unique_portals_captured']) #pioneer
	pr(stats['mods_deployed']) #engineer
	pr(stats['resonators_destroyed']) #purifier
	pr(stats['portals_neutralized']) #neutralizer
	pr(stats['fields_destroyed']) #disruptor
	pr(stats['fields_destroyed']) #salvator
	pr(stats['max_time_portal_held']) #guardian
	pr(stats['link_maintained_max_days']) #smuggler
	pr(stats['link_length_x_days_max']) #link-master
	pr(stats['field_held_max_days']) #contrioller
	pr(stats['largest_field_x_days_max']) #field master
	pr(stats['unique_missions_completed']) #specops
	pr(stats['mission_days_attended']) #missionday
	pr(stats['hacks']) #hacker
	pr(stats['glyph_points']) #translator
	pr(stats['hacking_streak_max_days']) #soujurner
	pr(stats['agents_recruited']) #recruiter
	pr("0") #exo5
	pr('"import from tg"',last=True) #comment


