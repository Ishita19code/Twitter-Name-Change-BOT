import tweepy
import os # Operating System Library
def create_api(): 
  consumer_key = os.getenv('consumer_key')
  consumer_secret = os.getenv('consumer_secret')
  access_token = os.getenv('access_token')
  access_token_secret = os.getenv('access_token_secret')

  auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  #authorisation
  auth.set_access_token(access_token, access_token_secret)

  api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True) 
  api.verify_credentials() #it verify the API entered, telling if they are correct or not.
  print('API Created') # A cofirmation that API created.
  return api

# Complete Code 
import time

def follower_count(user):
  emoji_numbers ={0 : '0️⃣',  
                  1 : '1️⃣',
                  2 : '2️⃣',
                  3 : '3️⃣',
                  4 : '4️⃣',
                  5 : '5️⃣',
                  6 : '6️⃣',
                  7 : '7️⃣',
                  8 : '8️⃣',
                  9 : '9️⃣'}
  emoji_numbers.keys()

  uf_split = [int(i) for i in str(user.followers_count)]

  emoji_followers = ''.join([emoji_numbers[j] for j in uf_split if j in emoji_numbers.keys()])
  return(emoji_followers)

api = create_api()

while True:
  user = api.get_user('IshitaG16391629')
  api.update_profile(name = f'Ishita Gupta | {follower_count(user)} Followers')
  print(f'Updatting twitter name : Ishita Gupta | {follower_count(user)} Followers')
  print('Waiting to Refresh')
  time.sleep(60)
