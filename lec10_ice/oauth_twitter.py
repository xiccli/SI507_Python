#507lec_0206
# Step1: get api key that let's me have access to twitter (we did that last week)
# Step2: temporary credentials acquisition: get a temp credentials from the server, so you go to twitter with your key and ask twitter if you can get data of sth.
# Step3: you sends a request to sth. and sth. agrees your request, so you can now get access
# Step4: such access token can be expired for a short time.
# we need to know how to pass the right info at the right time

# OAuth is created to make 2 servers communicate with each other.
# token actions allows you to get your own twitter information without all these stpes, only for yourself


from requests_oauthlib import OAuth1Session
import secrets
import json

client_key = secrets.api_key
client_secret = secrets.api_secret

resource_owner_key = secrets.access_token
resource_owner_secret = secrets.access_token_secret

protected_url = 'https://api.twitter.com/1.1/account/settings.json'

oauth = OAuth1Session(client_key,
                          client_secret=client_secret,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret)

protected_url = 'https://api.twitter.com/1.1/search/tweets.json'
params = {'q':'food'}
r = oauth.get(protected_url, params=params)
r_str = r.text
get_twitter_dict=json.loads(r_str)

for each in get_twitter_dict["statuses"]:
    print ("----------")
    outputs_1=each["user"]["name"]+" :"+"\n"
    outputs_2=each["text"]
    print (outputs_1)
    print (outputs_2)
    print ("\n")
