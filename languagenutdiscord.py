#---imports----------------------------------------------------------------------------------------------
import discord
import json
import requests

client = discord.Client()



@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    dm = "```  _                                              _   _       _   \n | |                                            | \ | |     | |  \n | |     __ _ _ __   __ _ _   _  __ _  __ _  ___|  \| |_   _| |_ \n | |    / _` | '_ \ / _` | | | |/ _` |/ _` |/ _ \ . ` | | | | __|\n | |___| (_| | | | | (_| | |_| | (_| | (_| |  __/ |\  | |_| | |_ \n |______\__,_|_| |_|\__, |\__,_|\__,_|\__, |\___|_| \_|\__,_|\__|\n                     __/ |             __/ |                     \n                    |___/             |___/                      \n      /$$   /$$  /$$$$$$   /$$$$$$  /$$   /$$\n     | $$  | $$ /$$__  $$ /$$__  $$| $$  /$$/\n     | $$  | $$| $$  \ $$| $$  \__/| $$ /$$/ \n     | $$$$$$$$| $$$$$$$$| $$      | $$$$$/  \n     | $$__  $$| $$__  $$| $$      | $$  $$  \n     | $$  | $$| $$  | $$| $$    $$| $$\  $$ \n     | $$  | $$| $$  | $$|  $$$$$$/| $$ \  $$\n     |__/  |__/|__/  |__/ \______/ |__/  \__/\n \nMade by Gideon Dyke\n  \nFor instructions to use this hack type: !help```"

    if message.content.lower() == '!dm':
        await message.channel.send("I have DM'ed you")
        await message.author.send(dm)

    if message.content.lower() == "!help":
        embed = discord.Embed(
            title='Help',
            description='Instructions to use the hack:',
            colour=discord.Color.from_rgb(36, 153, 191)
        )
        embed.set_footer(text='')
        embed.set_footer(text='')
        embed.add_field(name='1.', value='Store your login details by typing: **!login** ***yourUsername yourPassword***, \n(example, **!username GideonD Password123**, you only need to do this once, you can do it again to update login details)', inline=False)
        embed.add_field(name='2.', value='To start the hack type: **!languagenuthack** ***numberOfPointsYouWant***, \n(example, **!languagenuthack 1000000**)', inline=False)
        embed.add_field(name='3.', value='Wait for hack to complete.', inline=False)
        embed.add_field(name='Numbers', value='110 - 610, 1000 - 2100, 7000 - 7900, 10000 - 14000, 16000 - 20500, 41000 - 41100, 43000 - 47500, 5600 - 63000, 65000 - 66000', inline=False)

        await message.channel.send(content=None, embed=embed)

    if message.content.lower().startswith('!login'):
        message_text = message.content.split()
        discord_username = message.author.id
        username = message_text[1]
        password = message_text[2]
        filename = 'data.json'
        with open(filename, 'r') as f:
            data = json.loads(f.read())
        if str(discord_username) in data:
            data.pop(str(discord_username))
            data[discord_username] = {"username": username, "password": password}
        else:
            data[discord_username] = {"username": username, "password": password}
        json.dump(data, open(filename,'w'))

        await message.channel.send("Saved username: **" + username + "**")
        await message.channel.send("Saved password: **" + password + "**")

    if message.content.lower().startswith('!languagenuthack'):
        message_text = message.content.split()
        discord_username = message.author.id
        filename = 'data.json'
        with open(filename, 'r') as f:
            data = json.loads(f.read())
        login_username = data[str(discord_username)]["username"]
        login_password = data[str(discord_username)]["password"]
        url = 'https://api.languagenut.com/loginController/attemptlogin?cacheBreaker=1621610672902'
        body = 'username=' + str(login_username) + '&pass=' + str(
            login_password) + '&languagenutTimeMarker=1621610672902&lastLanguagenutTimeMarker=1621610672902&apiVersion=8'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
            'Accept': 'text/plain, */*; q=0.01',
            'Accept-Language': 'en-GB,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Content-Length': '122',
            'Origin': 'https://www.languagenut.com',
            'Referer': 'https://www.languagenut.com/',
            'Te': 'trailers',
            'Connection': 'close'
        }
        x = requests.post(url, data=body, headers=headers)
        jsonResponse = x.json()
        token = jsonResponse['newToken']
        points = str(message_text[1])
        score = 0
        if len(message_text) == 3:
            number = str(message_text[2])
        else:
            number = 110

        url = 'https://api.languagenut.com:443/gameDataController/addGameScore?cacheBreaker=1621543527060'
        print("number = " + str(number))
        body = 'moduleUid=' + str(number) + '&gameUid=10&gameType=reading&isTest=true&toietf=es&fromietf=en-GB&score=3800&correctVocabs=26097%2C27666%2C26090%2C26091%2C26093%2C27662%2C26094%2C26095%2C26089%2C26096%2C27666%2C26090%2C26091%2C26093%2C27662%2C26094%2C26095%2C26089%2C26096&incorrectVocabs=&isSentence=false&isVerb=false&grammarCatalogUid=12116&isGrammar=false&isExam=false&timeStamp=39250&vocabNumber=19&languagenutTimeMarker=1621543527060&lastLanguagenutTimeMarker=1621543527060&apiVersion=8&token=' + str(token)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
            'Accept': 'text/plain, */*; q=0.01',
            'Accept-Language': 'en-GB,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Content-Length': '794',
            'Origin': 'https://www.languagenut.com',
            'Referer': 'https://www.languagenut.com/',
            'Te': 'trailers',
            'Connection': 'close'
        }


        run = True
        percent_message = await message.channel.send(str(score) + "/" + str(points) + " points  - 0%")
        while True:
            for i in range(7):
                if int(score) > int(points):
                    run = False
                    break
                x = requests.post(url, data=body, headers=headers)
                if 'Error' in x.text:
                    print("Invalid Token or login details")
                    await message.channel.send("Invalid Token or login details")
                    run = False
                    break
                score += 3800
                percentage = int(score) / int(points) * 100
                if percentage > 100:
                    percentage = 100
                percentage = round(percentage, 2)
                await percent_message.edit(content=str(score) + "/" + str(points) + " points  - " + str(percentage) + "%")
                print(str(score) + "/" + str(points) + " points  - " + str(percentage) + "%", end="\r")
            if run == False:
                break
            number = int(number)
            number += 1
            if number == 611:
                number = 1000
            if number == 2101:
                number = 7000
            if number == 7901:
                number = 10000
            if number == 14001:
                number = 16000
            if number == 20501:
                number = 41000
            if number == 41100:
                number = 43000
            if number == 47500:
                number = 56000
            if number == 63000:
                number = 65000
            if number == 66000:
                number = 110
            body = 'moduleUid=' + str(number) + '&gameUid=10&gameType=reading&isTest=true&toietf=es&fromietf=en-GB&score=3800&correctVocabs=26097%2C27666%2C26090%2C26091%2C26093%2C27662%2C26094%2C26095%2C26089%2C26096%2C27666%2C26090%2C26091%2C26093%2C27662%2C26094%2C26095%2C26089%2C26096&incorrectVocabs=&isSentence=false&isVerb=false&grammarCatalogUid=12116&isGrammar=false&isExam=false&timeStamp=39250&vocabNumber=19&languagenutTimeMarker=1621543527060&lastLanguagenutTimeMarker=1621543527060&apiVersion=8&token=' + str(token)

        await message.channel.send("Finished hack")
        await message.channel.send("You have earned " + str(score) + " points!")


client.run('ODc1MTAzODE0MDQxMTA0Mzk0.YRQp7w.PWi3oTsQbSaBbf4Hib8PL822hYk')