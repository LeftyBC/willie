# coding=utf8
from __future__ import unicode_literals

import anydbm
import uuid
import random
import threading
import time

from willie.module import commands, rule, interval, example

_topic_lock = threading.Lock()
_timestamp_lock = threading.Lock()

def get_db(namespace):
        return anydbm.open("%s_topics" % namespace,"c")

def get_timestamps_db():
        return anydbm.open("topic_change_timestamps","c")

def set_timestamp(channel):
        with _timestamp_lock:
                db = get_timestamps_db()
                timestamp = str(time.time())
                db[str(channel)] = timestamp
                db.close()

def get_timestamp(channel):
        with _timestamp_lock:
                channel = str(channel)
                db = get_timestamps_db()
                timestamp = time.time()
                try:
                        if db[channel]:
                                timestamp = db[channel]
                        else:
                                db[channel] = str(timestamp)
                except KeyError:
                        db[channel] = str(timestamp)

                db.close()
                return float(timestamp)
                

def set_topic(bot, channel, newtopic):
        bot.write( ('TOPIC', '%s :%s' % (channel, newtopic)) )

def configure(config):
        if config.option('Periodically set a random topic in some channels?', False):
                config.add_section('topics')
                config.add_list('topics','channels',
                        'Enter the list of channels you\'d like to set up periodic topic changes for',
                        'Channel:')
                config.interactive_add('topics','interval','How often (in hours) should the bot set the topic?','48')


@interval(600)
def periodic_topic_change(bot):

        if not (bot.config.has_option('topics','channels') and bot.config.topics.get_list('channels')):
                return

        if not (bot.config.has_option('topics','interval') and bot.config.topics.interval > 0):
                return

        period = float(bot.config.topics.interval) * 3600.0   # interval is in hours, change it to seconds

        channels = bot.config.topics.get_list('channels')

        for channel in channels:
                timestamp = get_timestamp(str(channel))

                cutoff = (time.time() - period)
                age = time.time() - timestamp
                if cutoff > timestamp:
                        db = get_db(channel)
                        if len(db.keys()) > 0:
                                random_topic = random.choice(db.keys())
                                set_topic(bot, channel, db[random_topic])
                                set_timestamp(channel)




@example("addtopic yay my new topic - adds 'yay my new topic' to the bot's list of random topics")
@commands("addtopic")
def add_topic(bot, trigger):
        with _topic_lock:
                db = get_db(trigger.sender)
                newtopic = trigger.group(2).upper()
                newtopic_id = str(uuid.uuid4())
                bot.say("Added [%s] to the list of topics I'm remembering." % newtopic)
                db[newtopic_id] = newtopic
                db.close()


@example("topics - shows which topics are currently in the bot's list")
@commands("topics")
def topics(bot, trigger):
        with _topic_lock:
                db = get_db(trigger.sender)
                num_keys = len(db.keys())
                if num_keys > 10:
                        # too many topics to list, get a random sampling
                        bot.say("I know of %d topics, here's a few:" % num_keys)
                        sample = random.sample(db.keys(), 10)
                        for k in sample:
                                bot.say("* %s" % db[k])

                elif num_keys > 0:
                        bot.say("Here are the %d topics I'm remembering for later:" % num_keys)
                        for k in db.keys():
                                bot.say("* %s" % db[k])
                else:
                        bot.say("Hmm, nothing in my list.")
                db.close()


@example("searchtopic - searches for topics that match a substring")
@commands("searchtopic")
def search_topic(bot, trigger):
    with _topic_lock:
        channel = trigger.sender
        db = get_db(channel)

        if len(db.keys()) > 0:
                searchstring = trigger.group(2).upper()
                found = [ v for k,v in db.iteritems() if searchstring in v ]

                total = len(found)
                if total > 10:
                    bot.say("Found %d results for '%s', here's a few:" % (total, searchstring))
                    sample = random.sample(found, 10)
                    for l in sample:
                        bot.say("* %s" % l)
                elif total > 0:
                    bot.say("Found %d results, here they are:" % total)
                    for l in found:
                        bot.say("* %s" % l)
                else:
                   bot.say("Nope, nothing in my list.")
        db.close


@example("randomtopic - sets a random topic from the list")
@commands("randomtopic")
def random_topic(bot, trigger):
        with _topic_lock:
                db = get_db(trigger.sender)
                channel = trigger.sender
                bot.say("OK, setting a topic from my list in %s." % channel)

                if len(db.keys()) > 0:
                        topicid = random.choice(db.keys())
                        newtopic = db[topicid]

                        set_topic(bot, channel, newtopic)
                        set_timestamp(channel)

                else:
                        bot.say("Hmm, nothing in my list.")

                db.close()
        
