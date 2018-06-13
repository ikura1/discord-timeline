# -*- coding: utf-8 -*-
import discord
import asyncio
import os

client = discord.Client()
mention_type = 0


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


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    global mention_type
    send_user = message.author
    if send_user == client.user:
        return
    # TODO: botが送信した発言への返信を元チャンネルに飛す
    channel = message.channel
    content = message.content
    if str(channel).startswith('times_'):
        # TODO: bot名の変更
        # TODO: botアイコンの変更
        # TODO: 前回の投稿と同じ場合、投稿を結合するか検討
        em = None
        timeline_channel = get_timeline_channel()
        if timeline_channel is None:
            timeline_channel = channel
        if mention_type == 0:
            em = discord.Embed(description=content)  # , colour=0xDEADBF)
            avatar = get_avatar(send_user)
            em.set_author(name=send_user.display_name, icon_url=avatar)
            content = None
        else:
            user_name = send_user.display_name
            content = f'{user_name}: {content}'
        await client.send_message(timeline_channel, content, embed=em)
    elif content.startswith('!test'):
        await client.send_message(message.channel, 'TESTだーよー')

    elif content.startswith('!copy'):
        em = discord.Embed(title=str(channel), description=content, colour=0xDEADBF)
        em.set_author(name=send_user.display_name, icon_url=send_user.avatar_url)
        await client.send_message(message.channel, embed=em)

    elif content.startswith('!change'):
        mention_type = 1 if mention_type == 0 else 0


async def sample(message):
    """
    hogehoge
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


def test_plain(hoge):
    """Plain
    hogehoge
    """
    return hoge


def test_epytext(hoge):
    """Epytext
    hogehoge

    @param hoge:
    @return:
    """
    return hoge


def test_restructuredtext(hoge):
    """reStructuredText
    hogehoge

    :param hoge:
    :return:
    """
    return hoge


def test_numpy(hoge):
    """Numpy
    hogehoge

    Parameters
    ----------
    hoge

    Returns
    -------

    """
    return hoge


def test_google(hoge):
    """Google
    hogehoge

    Args:
        hoge:

    Returns:

    """
    return hoge


if __name__ == '__main__':
    api_token = os.environ['DISCORD_API_TOKEN']
    run(api_token)
