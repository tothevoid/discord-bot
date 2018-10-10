import datetime

async def stats(client):
    while True:
        users = dict()
        for member in client.get_all_members():
            users['time'] = str(datetime.datetime.now())
            if member.game == None:
                users[member.id] = 'null'
            else:
                users[member.id] = member.game.name
        