from nonebot import on_command, CommandSession


from .get_fumo_info import get_fomo_info

__plugin_name__ = 'fumo'
__plugin_usage__ = r"""
从雅虎获取有关fumo的信息
命令参数：
/fumo
"""


# on_command 装饰器将函数声明为一个命令处理器
# 这里 fumo 为命令的名字，同时允许使用别名
@on_command('fumo', aliases=('玩偶', 'fumofumo'))
async def fumofumo(session: CommandSession):
    # 获取fumo信息
    fumo_info = await get_fomo_info()
    # 向用户发送fumo信息
    await session.send(fumo_info)
