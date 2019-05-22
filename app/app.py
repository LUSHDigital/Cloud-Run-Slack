import os
import slack
import hug

client = slack.WebClient(token=os.environ['SLACK_API_TOKEN'])

@hug.get(examples='message=hello world&channel=cloud-run')
@hug.local()
def post_to_channel(message: hug.types.text, channel: hug.types.text, hug_timer=3):
    """Post a message to a Slack Channel"""

    response = client.chat_postMessage(
        channel='#' + channel,
        text=message)
    assert response["ok"]
    assert response["message"]["text"] == message

    return {'message': message,
            'channel': channel,
            'took': float(hug_timer)}

@hug.get(examples='message=hello world&userId=U0BDT1R0W')
@hug.local()
def post_to_user_by_id(message: hug.types.text, userId: hug.types.text, hug_timer=3):
    """Post a message to a Slack User by UserId"""

    response = client.chat_postMessage(
        channel=userId,
        text=message)
    assert response["ok"]
    assert response["message"]["text"] == message

    return {'message': message,
            'user': userId,
            'took': float(hug_timer)}

@hug.get()
@hug.local()
def slash():
    """Post a message to a Slack User by UserId"""

    return {'text': "hello"}
