# coding=utf8
"""minecraft_logins.py - Willie module to watch for
users to go online/offline on a minecraft server

Currently gets its data from minecraft dynmap, a bukkit
plugin, but bukkit's future is uncertain, so it won't be
a good source of info for very long.

"""
from __future__ import unicode_literals

import json

from multiprocessing import Process

from willie import web
from willie.module import commands, example, NOLIMIT, interval

def poll_minecraft(bot):

	url = bot.config.minecraft.url

	try:
		minecraft_data = json.loads(web.get(url))
		players = [player['name'] for player in minecraft_data['players']]
	except Exception as e:
		return ['Unable to enumerate players: %s' % e]

	return players

def configure(config):
	if config.option('Monitor a minecraft server for logins/logouts?',False):
		config.add_section('minecraft')
		config.interactive_add('minecraft','url','URL to the Dynmap JSON output (typically http://<minecraft_server>/up/world/world/):','')
		config.add_list('minecraft','channels','Channels to display joins/parts to','Channel:')

@interval(15)
def check_for_changed_players(bot):
	""" 
	check to see if any players have joined/left
	every 15 seconds
	"""

	if not (bot.config.has_option('minecraft','url')):
		return

	if not (bot.config.minecraft.get_list('channels')):
		return

	channels = bot.config.minecraft.get_list('channels')

	players = poll_minecraft(bot)

	last_onlines = []
	try:
		last_onlines = bot.memory['last_onlines']
	except KeyError:
		bot.memory['last_onlines'] = players
		last_onlines = players

	for pname in players:
		if pname in last_onlines:
			# we've seen this user before
			pass
		else:
			# this user is newly joined
			for channel in channels:
				bot.msg(channel, "[minecraft] %s joined the server" % pname)

	
	for pname in last_onlines:
		if pname in players:
			# this player is currently online
			pass
		else:
			# this player is no longer online
			for channel in channels:
				bot.msg(channel, "[minecraft] %s quit the server" % pname)

	bot.memory['last_onlines'] = players


@commands('online', 'minecraft')
@example('online - shows which users are logged into the minecraft server')
def who_is_online(bot, trigger):

	result = poll_minecraft(bot)

	onlines = "[minecraft] Players currently online: %s" % ", ".join(result)

	if len(result) == 0:
		onlines = "[minecraft] Nobody is currently online."

	bot.say(onlines)

