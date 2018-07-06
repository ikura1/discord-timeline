# -*- coding: utf-8 -*-
import discord
import asyncio
import os
import re
import urllib


client = discord.Client()
debug_mode = False


def get_timeline_channel():
    channels = client.get_all_channels()
    for channel in channels:
        # print(str(channel), channel)
        if str(channel) == 'timeline':
            return channel
    return None


def get_avatar(user):
    avatar = user.avatar_url
    if not avatar:
        avatar = user.default_avatar_url
    return avatar


def get_url(text):
    url_list = []
    re_url = re.compile(r'h?ttps?:\/\/.*')
    for row in text.split('¥n'):
        url_list.extend(re_url.findall(row))
    return list(set(url_list))


def is_url(url):
    # TODO: urllibの確認
    try:
        urllib.request.urlopen(url)
        return True
    except:
        return False


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    global debug_mode
    send_user = message.author
    if send_user == client.user:
        return
    # TODO: botが送信した発言への返信を元チャンネルに飛す
    channel = message.channel
    content = message.content
    if content.startswith('!debug'):
        debug_mode = not(debug_mode)
        message = 'DEBUG: ON' if debug_mode else 'DEBUG: OFF'
        await client.send_message(channel, message)
        return

    if str(channel).startswith('times_ikura1') and debug_mode is True:
        print('debug_mode: now')
        return

    timeline_channel = get_timeline_channel()
    if timeline_channel is None:
        print('not timeline channel')
        return

    if channel.startswith('times'):
        print('no times channel')
        return

    em = discord.Embed(description=content)  # , colour=0xDEADBF)
    avatar = get_avatar(send_user)
    em.set_author(name=send_user.display_name, icon_url=avatar)
    if message.attachments:
        attachment = message.attachments[0]
        url = attachment.get('url')
        em.set_image(url=url)

    await client.send_message(timeline_channel, embed=em)
    url_list = get_url(content)
    if not url_list:
        return
    # TODO: urlが2度表示されるのを修正
    for url in url_list:
        await client.send_message(timeline_channel, url)


async def sample(message):
    """
    sample code
    """
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')


def run(token):
    client.run(token)


if __name__ == '__main__':
    api_token = os.environ['DISCORD_API_TOKEN']
    run(api_token)
