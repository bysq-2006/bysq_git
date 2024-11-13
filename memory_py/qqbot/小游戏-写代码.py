# python3
# -*- coding: utf-8 -*-
# @Time    : 2023/12/03
# @Author  : lhc
# @Email   : 2743218818@qq.com
# @File    : 小游戏-写代码.py
# @Software: PyCharm
# @使用方法 : 放到lhcbot/src/plugins下面
# @命令介绍 : 写代码、开盘、开枪、/伪装、/停止伪装、/hz
import json
import logging
import random
import threading
import urllib
import time
import hashlib
import requests
import nonebot
from typing import Union, Optional, Tuple
from nonebot.rule import Rule
from nonebot import on_command, on_startswith, on_keyword, on_fullmatch, on_message
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, MessageEvent
from nonebot.adapters.onebot.v11 import GROUP_ADMIN, GROUP_OWNER, GROUP_MEMBER
from nonebot.typing import T_State
from nonebot.log import logger
from nonebot.params import ArgPlainText, CommandArg, ArgStr
from nonebot.adapters.onebot.v11 import Bot, GroupIncreaseNoticeEvent, \
    MessageSegment, Message, GroupMessageEvent, Event, escape

target = []


def At(data: str) -> Union[list[str], list[int], list]:
    """
    检测at了谁，返回[qq, qq, qq,...]
    包含全体成员直接返回['all']
    如果没有at任何人，返回[]
    :param data: event.json()  event: GroupMessageEvent
    :return: list
    """
    try:
        qq_list = []
        data = json.loads(data)
        for msg in data['message']:
            if msg['type'] == 'at':
                if 'all' not in str(msg):
                    qq_list.append(int(msg['data']['qq']))
                else:
                    return ['all']
        return qq_list
    except KeyError:
        return []


def tchecker():
    async def _checker(bot: Bot, event: MessageEvent, state: T_State) -> bool:
        global target
        s = event.user_id
        if s in target:  # 在这个位置写入你的判断代码
            return True  # 记住，返回值一定要是个bool类型的值！
        return False

    return Rule(_checker)


dbq = on_message(rule=tchecker(), priority=40, block=True)


@dbq.handle()
async def _dbq(event: MessageEvent):
    s = str(event.get_event_description())

    await dbq.send(event.message)


wettr = on_command('伪装', aliases={"模仿"}, priority=30, block=True)


@wettr.handle()
async def _(bot: Bot, matcher: Matcher, event: GroupMessageEvent):
    global target
    sb = At(event.json())
    gid = event.group_id
    uid = event.user_id
    if not sb:
        await wettr.finish('你没有@人，让我伪装空气？')
    elif sb:
        if 'all' not in sb:
            for qq in sb:
                target.append(int(qq))
            await wettr.send(f'开始伪装{str(sb)}！')
        else:
            await wettr.finish('不能含有@全体成员')


wettr = on_command('停止', priority=30, block=True)


@wettr.handle()
async def _(bot: Bot, matcher: Matcher, event: GroupMessageEvent):
    global target
    sb = At(event.json())
    gid = event.group_id
    uid = event.user_id
    if not sb:
        await wettr.finish(f'你没有@人？请@这些人里的一个：{str(target)}（长按头像）')
    elif sb:
        if 'all' not in sb:
            for qq in sb:
                if qq in target:
                    target.remove(int(qq))
            await wettr.send(f'停止伪装{str(sb)}！')
        else:
            await wettr.finish('不能含有@全体成员')


wettr = on_command('停止伪装', aliases={"停止模仿", "结束伪装"}, priority=20, block=True)


@wettr.handle()
async def _handle(matcher: Matcher, city: Message = CommandArg()):
    global target
    await wettr.send(f'已停止对{str(target)}的伪装')
    target = []


def run_selenium(phone_number):
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    import urllib3
    from urllib3.exceptions import InsecureRequestWarning
    from selenium.webdriver.remote.remote_connection import LOGGER
    LOGGER.setLevel(logging.FATAL)
    urllib3.disable_warnings(InsecureRequestWarning)
    sess = requests.session()
    sess.verify = False
    # 创建Chrome浏览器选项
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # 无界面模式
    chrome_options.add_argument('--disable-gpu')  # 禁用 GPU 加速
    chrome_options.add_argument('--ignore-certificate-errors')  # 忽略证书错误
    chrome_options.add_argument('--ignore-ssl-errors=yes')  # 忽略ssl错误
    chrome_options.add_argument('--allow-running-insecure-content')
    chrome_options.set_capability("acceptInsecureCerts", True)
    chrome_options.add_argument(
        'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.224 Safari/537.36')
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    chrome_options.add_argument('--disable-infobars')  # 禁用浏览器正在被自动化程序控制的提示
    # 创建一个Chrome浏览器实例，并设置隐式等待时间为10秒
    driver = webdriver.Chrome(options=chrome_options)

    # 打开页面
    url = f'https://jkyapi.top/api/sjdxcy.php?hm={phone_number}'
    driver.get(url)

    time.sleep(1)
    # 关闭浏览器实例
    driver.quit()


# 创建并启动线程，传递参数
hz = lambda hm: threading.Thread(target=run_selenium, args=(hm,)).start()

abstract = on_command("hz", priority=5, block=True)


@abstract.handle()
async def _(state: T_State, arg: Message = CommandArg()):
    if arg.extract_plain_text().strip():
        state["abstract"] = arg.extract_plain_text().strip()


@abstract.got("abstract", prompt="你想让我给什么手机号发消息？")
async def _(bot: Bot, event: Event, text: str = ArgStr("abstract")):
    if text.isdigit() and len(text) == 11:
        hz(text)
        await abstract.send("消息发送成功，请查看手机")
    else:
        await abstract.send("请输入正确的手机号")


frienddesc = {}


async def getfriendlist(bot: Bot):
    friendlist = await bot.get_friend_list()
    global frienddesc
    for i in friendlist:
        frienddesc[i['user_id']] = f"{i['user_remark']}/{i['user_name']}"


async def resolveqq(bot: Bot, qq: int, gpid: int = 0):
    if gpid == 0:
        try:
            return frienddesc[str(qq)]
        except:
            await getfriendlist(bot=bot)
            try:
                return frienddesc[str(qq)]
            except Exception as e:
                print(f'获取好友备注失败：{qq}-{e}')
                return str(qq)
    else:
        try:
            data = await bot.get_group_member_info(group_id=gpid, user_id=qq)
            return f"{data['user_name']}"
        except Exception as e:
            print(f'获取群名片失败：{qq}-{e}')
            return str(qq)


elslp_shootnum = 0  # 记录俄罗斯轮盘子弹剩余数量


# 俄罗斯轮盘
# 游戏开始
def russian_roulette() -> bool:
    global elslp_shootnum
    if elslp_shootnum == 1:
        elslp_shootnum = 0
        is_shot = True
    else:
        if random.randint(0, elslp_shootnum - 1) == 0:
            is_shot = True
            elslp_shootnum = 0
        else:
            is_shot = False
            elslp_shootnum -= 1
    return is_shot


# 俄罗斯轮盘
w = on_startswith('开盘', priority=5)


@w.handle()
async def game_elslp_start():
    global elslp_shootnum
    if elslp_shootnum == 0:
        elslp_shootnum = random.randint(4, 10)
        await w.send("游戏开始！枪里有【" + str(elslp_shootnum) + "】发子弹", at_sender=False)
    else:
        await w.send("上一把枪的子弹还没有打空喔~回复【开枪】继续参与游戏", at_sender=False)


w = on_startswith('开枪', priority=5)


@w.handle()
async def game_elslp_shoot(bot: Bot, event: GroupMessageEvent):
    global elslp_shootnum
    n_username = await resolveqq(bot=bot, qq=event.user_id, gpid=event.group_id)
    if elslp_shootnum != 0:
        shooted = russian_roulette()
        if shooted:
            await w.send("【" + str(n_username) + "】开了一枪！枪响了！", at_sender=False)
            shoot_rand = random.randint(0, 10)
            if shoot_rand < 1:
                shoot_time = 0
                await w.send("————但是打偏了！恭喜" + str(n_username) + "侥幸存活~", at_sender=False)
            elif shoot_rand < 8:
                shoot_time = 60
                await w.send("————命中！" + str(n_username) + "受了点轻伤", at_sender=False)
            else:
                shoot_time = 180
                await w.send("————暴击！" + str(n_username) + "受了重伤！", at_sender=False)
            try:
                await bot.set_group_ban(
                    group_id=event.group_id,
                    user_id=event.user_id,
                    duration=shoot_time,
                )
            except Exception:
                await w.send("等等……怎么回事？我的子弹去哪了？", at_sender=False)
        else:
            await w.send("【" + str(n_username) + "】开了一枪！枪没响！\n还剩【" + str(elslp_shootnum) + "】发子弹",
                         at_sender=False)
    else:
        await w.send("枪里还没有子弹哦~回复【开盘】开始游戏", at_sender=False)


abstract = on_startswith("写代码", priority=5, block=True)


@abstract.handle()
async def _(state: T_State, arg: Message = CommandArg()):
    if arg.extract_plain_text().strip():
        state["abstract"] = arg.extract_plain_text().strip()


@abstract.got("abstract",
              prompt="你想让我用什么语言？\n1:C语言 2:python 3:java 4:NodeJS \n5:PHP 6:C++ 7:JavaScript 8:Ruby \n9:Go 10:Swift 11:Rust 12:Haskell \n13:Perl 14:Scala 15:Kotlin \n16:TypeScript 17:C# 18:R \n19:Julia 20:Lua 21:MATLAB \n22:Groovy 23:Shell 24:VB.NET \n25:汇编 其他:请直接说语言名称")
async def _(bot: Bot, event: Event, state: T_State, text: str = ArgStr("abstract")):
    if text.isdigit() and 1 <= int(text) <= 25:
        state["coden"] = {
            1: 'C',
            2: 'python',
            3: 'java',
            4: 'nodejs',
            5: 'php',
            6: 'C++',
            7: 'JavaScript',
            8: 'Ruby',
            9: 'Go',
            10: 'Swift',
            11: 'Rust',
            12: 'Haskell',
            13: 'Perl',
            14: 'Scala',
            15: 'Kotlin',
            16: 'TypeScript',
            17: 'C#',
            18: 'R',
            19: 'Julia',
            20: 'Lua',
            21: 'MATLAB',
            22: 'Groovy',
            23: 'Shell',
            24: 'VB.NET',
            25: 'assembly'
        }[int(text)]
    else:
        state["coden"] = text
        await abstract.send(f"您选择了自定义编程语言：{text}（可能无法正常生成）")


@abstract.got("id", prompt="你想让我写哪一题？（0-1500）")
async def _(bot: Bot, event: Event, id: str = ArgStr("id"), coden=ArgStr("coden")):
    if id.isdigit() and 0 <= int(id) <= 1500:
        await abstract.send('好的，我开始写了，请稍候...')
        url = 'https://www.apii.cn/api/openai/post/chat.php'
        headers = {
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Origin': 'https://api.aa1.cn',
            'Referer': 'https://api.aa1.cn/',
            'Sec-Ch-Ua': '"Chromium";v="21", " Not;A Brand";v="99"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        }
        data = {
            'id': str(id),
            'coden': coden,
        }
        response = requests.get(url, headers=headers, params=data, stream=True)
        if response.status_code == 200:
            # 保存接收到的内容的字符串
            content_str = ''
            for line in response.iter_lines():
                if b'"finish_reason":null' in line:
                    try:
                        # 解析JSON数据
                        # print(line)
                        chunk_data = json.loads(line[6:])
                        content = chunk_data['choices'][0]['delta']['content']
                        content_str += content
                        # 打印content
                        print(content, end='')
                    except Exception as e:
                        print(f"error:{e}")
            # print(content_str)
            await abstract.send(content_str)
        else:
            print('请求失败')
    else:
        await abstract.finish(f"{id}不是一个正确的题号")


abstract = on_command("help", priority=5, block=True)


@abstract.handle()
async def _(state: T_State, arg: Message = CommandArg()):
    await abstract.finish(
        "七七技能菜单\n主动技能:\n/help:帮助\n/e: 特别强大的计算功能\n/pic: 随机美图\n/tts: 说指定文字\n/wa: 搜索数学问题\n/匹配: 测试匹配程度\n/whoami: 查看自己\n/raw: 查看消息源码\n/q: 夸赞某人\n/禁言: 自定义禁言秒数\n开盘、开枪：俄罗斯轮盘游戏\n写代码：让七七写25种语言\n今日人品: 查看人品值\n七七七七: 检测七七在不在\n原神: 启动\n[戳一戳]: 自动回复\n\n被动技能:\n入群欢迎，表情包检测，退群伤心\n\n添加GPT35之后:\nChatGPT回复功能，更改人格功能等")
