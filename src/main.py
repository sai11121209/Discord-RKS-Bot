# インストールした discord.py を読み込む
import discord
import os
from discord.utils import get

try:
    from local_settings import *

    LOCAL_HOST = True
except ImportError:
    import keep_alive

    keep_alive.keep_alive()


# 自分のBotのアクセストークンに置き換えてください
if os.getenv("TOKEN"):
    TOKEN = os.getenv("TOKEN")
    LOCAL_HOST = False

intents = discord.Intents.all()
intents.members = True
intents.reactions = True

# 接続に必要なオブジェクトを生成
client = discord.Client(intents=intents)

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print("ログインしました!")


# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == "/init":
        channel = client.get_channel(890461420330819586)
        embed = discord.Embed(
            title="ようこそロケッターズDiscordサーバへ!",
            description="""
僕はロケッターズサーバの案内イルカのカイル君だよ!よろしくね!
これからロケッターズDiscordサーバに参加するにあたってやらなければならないことがいくつかあります!
まずそのやることを一緒にやっていきましょう!
            """,
            color=0x4169E1,
        )
        img = "./imgs/welcomgif.gif"
        file = discord.File(img)
        embed.set_image(url="attachment://welcomgif.gif")
        embed.set_thumbnail(
            url="http://drive.google.com/uc?export=view&id=17Xe7Pf-0VjJ9Sx9GzgtVMjqbjE9DxyVa",
        )
        await channel.send(embed=embed, file=file)

        embed = discord.Embed(
            title="サーバ通知説明",
            description="""
ロケッターズサーバは夜遅く～深夜にかけて活動することが多くメンションをしないとサーバメンバーに通知が行かないようになっています!
そのためメンションのやり方をここでマスターしましょう!!
            """,
            color=0x4169E1,
        )
        embed.add_field(
            name="全体通知",
            value="""
            > サーバに参加してる人全員に通知を送りたいときはメッセージのあとに@everyoneと入力すると通知を送れます!
            """,
            inline=False,
        )
        embed.add_field(
            name="オンライン参加者通知",
            value="""
            > サーバに参加していて現在オンラインの人にのみ通知を送りたいときはメッセージのあとに@hereと入力すると通知を送れます!
            """,
            inline=False,
        )
        embed.add_field(
            name="特定ロール参加者通知",
            value="""
            > サーバに参加していて特定ロール参加者の人にのみ通知を送りたいときはメッセージのあとに@ロール名と入力すると通知を送れます!
            """,
            inline=False,
        )
        embed.add_field(
            name="個人通知",
            value="""
            > サーバに参加している個人にのみ通知を送りたいときはメッセージのあとに@ユーザ名と入力すると通知を送れます!
            """,
            inline=False,
        )
        embed.set_thumbnail(
            url="http://drive.google.com/uc?export=view&id=17Xe7Pf-0VjJ9Sx9GzgtVMjqbjE9DxyVa",
        )
        await channel.send(embed=embed)

        embed = discord.Embed(
            title="サーバカテゴリ説明",
            description="""
※PC以外の端末で表示すると一部表示が省略されてしまいフォーマットが崩れる可能性があります。
ロケッターズサーバには以下のカテゴリがあります!1つ1つ見ていきましょう!
            """,
            color=0x4169E1,
        )
        embed.add_field(
            name="INFORMATION",
            value="""
            > Escape from Tarkov公式の情報を配信するテキストチャンネル __`#eft-announcements`__ や
            > botの更新情報 __`#bot-update-information`__ などテキストチャンネル __`#bot-update-request`__ を除きメッセージを投稿することができない特別カテゴリです!
            """,
            inline=False,
        )
        embed.add_field(
            name="ESCAPE FROM TARKOV",
            value="""
            > Escape from Tarkovの会話をするテキストチャンネル __`#escape-from-tarkov`__ です!
            """,
            inline=False,
        )
        embed.add_field(
            name="TEXT CHANNEL",
            value="""
            > 雑談でもなんでもできるカテゴリです!
            > テキストチャンネル __`#notification-general`__ に書き込むとbotが自動的にメッセージに対して@everyoneを追記して全員にメッセージを配信してくれます!夜中の使用は避けましょう。
            > 通知で目が覚めてしまうかもしれません。。
            """,
            inline=False,
        )
        embed.add_field(
            name="VOICE CHAT",
            value="""
            > 基本的にボイスチャットはここで!
            > 聞き専の人がいたらテキストチャンネル __`#voicechat-general`__ を使うといいでしょう!
            """,
            inline=False,
        )
        embed.add_field(
            name="ESCAPE FROM TARKOV VOICE CHAT",
            value="""
            > Escape from Tarkovをプレイするうえでパーティーを分けた際に使用するボイスチャンネルです!
            > (BEAR又はUSECロールを取得していないと表示されません)
            """,
            inline=False,
        )
        embed.add_field(
            name="PRIVATE CATEGORY",
            value="""
            > 日常生活におけるメモ帳感覚で使ってください!
            > ただしDiscordの仕様上隊長には筒抜けなので隊長の悪口は別で書いてあげてください。
            """,
            inline=False,
        )
        embed.add_field(
            name="PHOTO ALBUM",
            value="""
            > サバゲーに参加した際に撮影してもらった写真のアルバムカテゴリです!
            > このカテゴリもメッセージを投稿することができない特別カテゴリです!
            """,
            inline=False,
        )
        embed.set_thumbnail(
            url="http://drive.google.com/uc?export=view&id=17Xe7Pf-0VjJ9Sx9GzgtVMjqbjE9DxyVa",
        )
        sendMessage = await channel.send(embed=embed)

        embed = discord.Embed(
            title="サーバBOT説明",
            description="""
ロケッターズサーバにはいくつかのBOTがいます!それぞれが機能を持っているよ!
それではロケッターズサーバにいるBOT!1つ1つ見ていきましょう!
            """,
            color=0x4169E1,
        )
        embed.add_field(
            name="Rocketers Guide",
            value="""
            > 本サーバーの案内担当BOT!
            > 今のところ最初の説明をする機能しかしかないけどいつか機能が増えるかも!
            """,
            inline=False,
        )
        embed.add_field(
            name="EFT(Escape from Tarkov) Wiki Bot",
            value="""
            > 本サーバーのメインBOT!ボイスチャンネル参加通知やEscape from Tarkovの情報をいち早く教えてくれます!
            > ここでは本BOTの使い方を書き切れないので興味があったら __`/help`__ と打ち込みどんな機能があるか見てみてください!
            """,
            inline=False,
        )
        embed.add_field(
            name="tarkov-market-bot",
            value="""
            > Escape from Tarkovのフリーマーケット情報を教えてくれるよ!
            > __`!p アイテム名`__で実行できるよ!
            """,
            inline=False,
        )
        embed.add_field(
            name="Among Us Bot",
            value="""
            > Among Usをプレイするときにとても便利な機能を提供してくれるBOTだよ!
            > 具体的には自動ミュート機能とかがあります!
            """,
            inline=False,
        )
        embed.set_thumbnail(
            url="http://drive.google.com/uc?export=view&id=17Xe7Pf-0VjJ9Sx9GzgtVMjqbjE9DxyVa",
        )
        await channel.send(embed=embed)

        embed = discord.Embed(
            title="ロール選択",
            description="""
最後にロケッターズサーバで活動するためにはロールという役職が必要になるよ!
これがないとサーバで発言したり、ボイスチャットに参加できないから参加しよう!
下に書いてある番号に従って当てはまるリアクションボタンを1つ以上選択してね!
※間違えて選択してしまっても大丈夫だよ!もう一度選択してキャンセルするとロールが解除されるよ!

:one: 隊員(ロケッターズクラン参加者)
:two: BEAR(EFTをプレイしている方用、EFT所属部隊を選択)
:three: USEC(EFTをプレイしている方用、EFT所属部隊選択)
:four: 無所属(どれにも当てはまらない方用)
    """,
            color=0x4169E1,
        )
        embed.set_thumbnail(
            url="http://drive.google.com/uc?export=view&id=17Xe7Pf-0VjJ9Sx9GzgtVMjqbjE9DxyVa",
        )
        sendMessage = await channel.send(embed=embed)
        await sendMessage.add_reaction("1️⃣")
        await sendMessage.add_reaction("2️⃣")
        await sendMessage.add_reaction("3️⃣")
        await sendMessage.add_reaction("4️⃣")
        embed = discord.Embed(
            title="さいごに",
            description="""
ロール選択が済んだらやることはすべて完了だよ!!
これですべてのカテゴリにアクセスできるようになったはずだよ!!
それじゃあロケッターズサーバで良い時間を過ごしてね!
行ってらっしゃい(｡･ω･)ﾉﾞ

　　　　　　　　　　　, '´l,
　　　　　　　, -─-'- 、i_
　　　 ＿_, '´　　　　　　　ヽ、
　　　',ー--　●　　　　　　　ヽ、
　　　 ｀"'ゝ、_　　　　　　　　　 ',
　　　　　　〈｀'ｰ;＝=ヽ、〈ｰ- 、 !
　　　　　　 ｀ｰ´　　　　ヽi｀ヽ iﾉ
　　　　　　　　　　　　　　　 ! /
　　　　　　　　　　　　　　r'´、ヽ
　　　　　　　　　　　　　　｀´ヽノ
    """,
            color=0x4169E1,
        )
        embed.set_thumbnail(
            url="http://drive.google.com/uc?export=view&id=17Xe7Pf-0VjJ9Sx9GzgtVMjqbjE9DxyVa",
        )
        sendMessage = await channel.send(embed=embed)


# 役職追加時発火
@client.event
async def add_role(member, roleId):
    role = member.guild.get_role(roleId)
    await member.add_roles(role)


# 役職剥奪時発火
@client.event
async def remove_role(member, roleId):
    role = member.guild.get_role(roleId)
    await member.remove_roles(role)


@client.event
async def on_raw_reaction_add(payload):
    if not payload.member.bot:
        if payload.channel_id == 890461420330819586:
            await add_role(payload.member, 890451203631218719)
            if payload.emoji.name == "1️⃣":
                await add_role(payload.member, 820310764652462130)
            if payload.emoji.name == "2️⃣":
                await add_role(payload.member, 803829039138603049)
            if payload.emoji.name == "3️⃣":
                await add_role(payload.member, 803828927805259796)
            if payload.emoji.name == "4️⃣":
                pass


@client.event
async def on_raw_reaction_remove(payload):
    guild = client.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)
    if not member.bot:
        if payload.channel_id == 890461420330819586:
            if payload.emoji.name == "1️⃣":
                await remove_role(member, 820310764652462130)
            if payload.emoji.name == "2️⃣":
                await remove_role(member, 803829039138603049)
            if payload.emoji.name == "3️⃣":
                await remove_role(member, 803828927805259796)
            if payload.emoji.name == "4️⃣":
                pass


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)