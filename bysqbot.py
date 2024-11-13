import asyncio
import time
from nonebot import on_command, on_keyword
from nonebot.adapters.onebot.v11 import Bot
from nonebot.adapters.onebot.v11 import Bot, Event, Message
from datetime import datetime #24小时
from nonebot.adapters import MessageTemplate
from zhipuai import ZhipuAI
from nonebot.adapters.onebot.v11 import Bot, GroupMessageEvent, MessageEvent
from nonebot.params import ArgPlainText, CommandArg, ArgStr
#初始化
usebot_id:int = 1904568840 #使用者的QQ
leetcode_state:bool = False


#--------------------help-------------------
w = on_command(cmd="help",priority=5)
@w.handle()
async def leet00code(bot: Bot,  event:Event, arg: Message = CommandArg()):
    await bot.send(event=event,message=
"""1./ai + 问题 可以使用ai机器人
2.会告诫人们不要撸管
3.提醒写题：
    (需要输入/start 启动)
    1-发送我已完成更新完成时间
    2-发送完成了其他的会宽松一天时间
    3-发送我有多久没有...会返回距离上一次题目完成时间"""
)




#--------------------------------ai机器人-----------------------------------
w = on_command(cmd="ai",priority=5)
@w.handle()
async def leet00code(bot: Bot,  event:Event, arg: Message = CommandArg()):
    client = ZhipuAI(api_key="7e7615b5f14e68b7803af3f2856748da.JQdEjcoE7MfiSSyc") # 填写您自己的APIKey
    tools = [{
    "type": "web_search",#是否开启网络搜寻
    "web_search": {
        "enable": True #默认为关闭状态（False） 禁用：False，启用：True。
        }
    }]
    response = client.chat.completions.create(
        model="GLM-4-Air",  # 填写需要调用的模型编码
        messages=[
            {"role": "system","content":"为了优化产品经理的工作日报，我们可以构建一个提示词（Prompt），这个提示词将指导AI生成一份结构清晰、内容全面的工作日报。下面是一个示例：\n\n```markdown\n# 工作日报提示词\n\n## 上下文（Context）\n- **角色**：产品经理\n- **日期**：[填写日期]\n- **工作重点**：[填写当天或本周的主要工作重点，例如“用户体验优化”、“新功能开发”等]\n\n## 目标（Objective）\n- **主要目标**：撰写一份详细的工作日报，反映当天或本周的工作进展、遇到的问题及解决方案、下一步计划。\n\n## 风格（Style）\n- **写作风格**：正式、清晰、简洁\n- **语言要求**：中文\n\n## 语气（Tone）\n- **情感调**：客观、专业\n\n## 受众（Audience）\n- **主要受众**：团队领导、同事、利益相关者\n\n## 响应（Response）\n- **输出格式**：Markdown\n- **内容要求**：包括工作总结、问题与解决方案、下一步计划三个部分\n\n## 工作流程（Workflow）\n1. **工作总结**：简要概述当天或本周完成的主要工作。\n2. **问题与解决方案**：列出在工作中遇到的问题及采取的解决措施。\n3. **下一步计划**：描述接下来一天或一周的工作计划。\n\n## 示例（Examples）\n- **工作总结**：完成了新功能的用户调研，与开发团队讨论了技术实现方案。\n- **问题与解决方案**：遇到了数据集成的问题，已与技术团队沟通，计划在下周前解决。\n- **下一步计划**：准备新功能的原型设计，与设计团队协调工作。"},
            {"role": "user", "content": str(arg.extract_plain_text().strip())}
        ],
        tools=tools
    )
    await bot.send(event=event,message=str(response.choices[0].message.content))




#------------------提醒做题--------------------
def convert_seconds(seconds):#将秒转换为时钟和分钟和秒
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    return hours, minutes, remaining_seconds


w = on_keyword(keywords={"已经完成"},priority=5)
@w.handle()
async def leetcode(bot: Bot,event: Event):
    if(event.get_user_id() != str(usebot_id)):
        return
    time_ = time.time()
    with open('timestamp.txt', 'w') as file:
        file.write(str(time_))
    await bot.send_private_msg(user_id=usebot_id,message="不错不错，继续加油。")
    

w = on_keyword(keywords={"完成了其他的"},priority=5)
@w.handle()
async def leetcode(bot: Bot,event: Event):
    if(event.get_user_id() != str(usebot_id)):
        return
    with open('timestamp.txt', 'r') as file:
        time_read = float(file.read())
    time_ = time_read + 86400.0
    with open('timestamp.txt', 'w') as file:
        file.write(str(time_))
    await bot.send_private_msg(user_id=usebot_id,message="看着学了的分上，就勉为其难给你减少一天吧。")


w = on_keyword(keywords={"我有多久没有"},priority=5)
@w.handle()
async def leetcode(bot: Bot,event: Event):
    if(event.get_user_id() != str(usebot_id)):
        return
    time_ = time.time()
    with open('timestamp.txt', 'r') as file:
        time_read = float(file.read())
    total_seconds = time_ - time_read
    hours, minutes, seconds = convert_seconds(total_seconds)
    await bot.send_private_msg(user_id=usebot_id,message=f"你有{int(hours)}小时 {int(minutes)}分钟 {int(seconds)}秒没有写题了。")


w = on_command(cmd="start",priority=5)
# #timestamp.txt需要提前创建一个，然后在里面随便打点数字，因为我没有做初始化
leetcode_state:bool = False
@w.handle()
async def leetcode(bot: Bot,event: Event):
    if(event.get_user_id() == str(usebot_id)):
        global leetcode_state
        if leetcode_state:
            await bot.send_private_msg(user_id=usebot_id,message="已经启动，请勿重复操作。")
            return
        await bot.send_private_msg(user_id=usebot_id,message="已经启动。")
        while True:
            leetcode_state = True
            time_ = time.time()
            now = datetime.now()
            with open('timestamp.txt', 'r') as file:
                time_read = float(file.read())
            if (time_ - time_read) > 259200:#判断时间间隔
                await bot.send_private_msg(user_id=usebot_id,message="已经三天没有写算法了，今天必须写了，我会一直发，直到写了为止。")
                #(datetime.now().hour == 12 and datetime.now().minute >= 30) 因为hour == 12，所有这个条件实际上是12：30 到 13：00
            elif (time_ - time_read) > 172800 and ((datetime.now().hour == 12 and datetime.now().minute >= 30) or (datetime.now().hour == 13 and datetime.now().minute < 30)):
                await bot.send_private_msg(user_id=usebot_id,message="已经两天没有写算法了，快快快。")
            elif (time_ - time_read) > 86400 and ((datetime.now().hour == 12 and datetime.now().minute >= 30) or (datetime.now().hour == 13 and datetime.now().minute < 30)):
                await bot.send_private_msg(user_id=usebot_id,message="已经一天没有写算法了。")
            await asyncio.sleep(3600)  # 暂停 3600 秒后再进行下一次循环




#-------------------------------撸管-----------------------------
w = on_keyword(keywords={"撸管"},priority=5)
@w.handle()
async def leet00code(bot: Bot, event: Event):
    await bot.send(event=event, message="撸管虽一时愉悦，却潜藏身心危害。为了健康，请自控自律，培养良好习惯，让生活更加充实精彩。拒绝沉迷，拥抱健康人生。")