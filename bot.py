import typing
import typing_extensions
import asyncio
import aiocqhttp.api
# import nonebot
import config
import logging

from os import path
from nonebot import on_request, on_notice, RequestSession
from config import 入群提示信息, WAIT_MINUTE, SUPERUSER, HOST, PORT


'''
# config ...

SUPERUSER: typing_extensions.Final[int] = 2300471354

WAIT_MINUTE: typing_extensions.Final[int] = 10

入群提示信息: typing_extensions.Final[str] = f'...LYZH，请在{WAIT_MINUTE}分钟内添加为管理员'

HOST: typing_extensions.Final[str] = '127.0.0.1'
PORT: typing_extensions.Final[int] = 5700

# ------------------------------'''


verified_group: typing.Set[int] = set()

from aiocqhttp import CQHttp, Event

bot = CQHttp()

# nonebot.init(config)

@bot.on_message('private')
async def gugugu(event: Event):
    await bot.send(event, f'你发了：{event.message}')

'''
@bot.on_message('group')
async def emm(event: Event):
    lst = await bot.get_group_member_list(group_id=event.group_id, self_id=SUPERUSER)
    await bot.send(event, f'群成员列表：{lst}')
'''

# '''
# @on_request('group')
@bot.on_request('group')
async def group_invite(event: Event):
    # 判断加群类型是被邀请
    if event.sub_type != 'invite':
        return
    group_id = event.group_id
    await bot.call_action(
                action='.handle_quick_operation_async',
                self_id=SUPERUSER,
                context=event,
                operation={'approve': True, 'remark': ''})
    # await bot.send_group_msg(group_id=group_id, message=入群提示信息, self_id=SUPERUSER)
    verified_group.add(group_id)
    await asyncio.sleep(WAIT_MINUTE*60)
    # await bot.get_group_member_list(group_id=group_id, self_id=SUPERUSER)
    if group_id in verified_group:
        await bot.set_group_leave(group_id=group_id, self_id=SUPERUSER)
        verified_group.remove(group_id)


@bot.on_notice('group_admin')
async def group_admin(event: Event):
    group_id = event.group_id
    user_id = event.user_id
    if  group_id not in verified_group:
        return
    if  event.sub_type == 'set'\
    and user_id == SUPERUSER:
        await bot.send_group_msg(group_id=group_id, message='不胜荣幸', self_id=SUPERUSER)
        verified_group.remove(group_id)
    elif event.sub_type == 'unset'\
    and user_id == SUPERUSER:
        verified_group.add(group_id)
        await asyncio.sleep(WAIT_MINUTE*60)
        if group_id in verified_group:
            await bot.set_group_leave(group_id=group_id, self_id=SUPERUSER)
            verified_group.remove(group_id)

# nonebot.run()
# '''
if __name__ == '__main__':
    bot.run(host=HOST, port=PORT)