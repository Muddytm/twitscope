import oauth2
import os
import json


def oauth_req(url, key, secret, http_method="GET", post_body="",
              http_headers=None):
    """Generate oauth tokens and such."""
    consumer = oauth2.Consumer(key=os.environ.get("TWITSCOPE_CONSUMER_TOKEN"),
                               secret=os.environ.get("TWITSCOPE_CONSUMER_SECRET"))
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request(url, method=http_method, body=post_body,
                                   headers=http_headers)
    return content


def run():
    """Run the script."""
    results = oauth_req("https://api.twitter.com/1.1/search/tweets.json?q=%40lifeatfulcrum&result_type=recent",
                        os.environ.get("TWITSCOPE_APP_TOKEN"),
                        os.environ.get("TWITSCOPE_APP_SECRET"))

    tweets = []

    for i in json.loads(results)["statuses"]:
        tweet = {}
        tweet["user"] = (i["user"]["name"] + " @" + i["user"]["screen_name"])
        tweet["text"] = i["text"]
        tweet["time"] = i["created_at"]
        tweets.append(tweet)

    return json.dumps(tweets)


if __name__ == "__main__":
    print run()
