import praw
import requests
import discord
from discord import Webhook, RequestsWebhookAdapter, File

# ENTER YOUR WEBHOOK ID AND WEBHOOK TOKEN HERE
id = ""
token = ""

# ENTER REDDIT CLIENT ID, SECRET, USER AGENT, USERNAME PASSWORD
# User agent example : Python:com.rohan.fashionscraper:v1
reddit = praw.Reddit(client_id="",
                     client_secret="",
                     user_agent="",
                     username="",
                     password="")

# ENTER DESIRED subreddit to monitor and get notis
sub = "sneakers"
WEBHOOK_ID = id
WEBHOOK_TOKEN = token
# Create webhook
webhook = Webhook.partial(WEBHOOK_ID, WEBHOOK_TOKEN,\
 adapter=RequestsWebhookAdapter())

#submission_stream = (reddit.freps.stream.submissions(pause_after=-1)

for submission in reddit.subreddit(sub).stream.submissions():
        print(submission.title)
        if submission is None:
                continue
        if("USA" in submission.title):
            embd = discord.Embed()
            embd.description = submission.title
            embd.title= submission.url
            webhook.send(embed=embd)
