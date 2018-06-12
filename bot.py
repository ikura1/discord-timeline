# -*- coding: utf-8 -*-
import discord
import asyncio
import os

client = discord.Client()


def get_timeline_channel():
    channels = client.get_all_channels()
    for channel in channels:
        # print(str(channel), channel)
        if str(channel) == 'timeline':
            return channel
    return None


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    send_user = message.author
    if send_user == client.user:
        return
    # TODO: botが送信した発言への返信を元チャンネルに飛す
    channel = message.channel
    if str(channel).startswith('times_'):
        # TODO: 送信者のアイコン表示
        # TODO: bot名の変更
        # TODO: botアイコンの変更
        timeline_channel = get_timeline_channel()
        if timeline_channel is None:
            timeline_channel = channel
        print(send_user.display_name)
        user_name = send_user.display_name
        content = f'{user_name}: {message.content}'
        await client.send_message(timeline_channel, content)
    elif message.content.startswith('!test'):
        await client.send_message(message.channel, 'TESTだーよー')


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
