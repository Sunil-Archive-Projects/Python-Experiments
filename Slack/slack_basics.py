#!/usr/bin/python
#pip install slackclient
from slackclient import SlackClient
import os

#subroutine to read the token from slack_token.ini file
def read_token(token_filePath):
    if not os.path.isfile(token_filePath):
        print("File path {} does not exist. Exiting...".format(filepath))
        print("Create a File Named slack_token.ini and paste the Token")
        sys.exit()

    fp = open('./slack_token.ini', 'r')  
    token = fp.read()
    fp.close()
    return token

#subroutine to send a text to a channel as message
def sendtext(channel,text,username="Raspi_Bot"):
    sc.api_call("chat.postMessage",channel=channel,text=text,username="Raspi_Bot")

#read token form slack_token.ini and initialize slack client
#create token for your app from https://api.slack.com/custom-integrations/legacy-tokens

slack_token = read_token("./slack_token.ini")
sc = SlackClient(slack_token)

#api documentation at https://api.slack.com/methods/chat.postMessage#authorship
sendtext(channel = "#general", text = "Hello World!")
