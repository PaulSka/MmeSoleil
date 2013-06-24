# -*- coding: utf-8 -*-

import tweepy
import conf
import subprocess

#Auth and create acces for application
auth = tweepy.OAuthHandler(conf.consumer_key, conf.consumer_secret)
auth.set_access_token(conf.access_token, conf.access_token_secret)

#Create acces application, only 1 time !
#auth.get_authorization_url()
#Copy url and paste into browser with your bot twitter account !
#Copy PIN Code
#pin_code = "ENTER PIN CODE HERE" 
#auth.get_access_token(pin_code)

#Get Api !
api = tweepy.API(auth)

#Get the current version of git repository
current_git_version = subprocess.check_output(["git", "rev-parse", "HEAD"])

while True:
    try:
        #Execute code
        #Sending welcome message
        api.update_status(u"J'ouvre ma boutique ! (version : %s)" %current_git_version)

        #Get message to mentions timeline (20 last)
        for tweet in api.mentions_timeline():
            if tweet.retweeted == False:
                #Send message
                api.update_status("Salut @%s" %tweet.user.screen_name)
                tweet.retweet()
            else:
                pass

    except KeyboardInterrupt:
        #Send message and exit
        api.update_status(u"Je ferme la boutique !")

    #Wait 25 sec
    time.sleep(25)
