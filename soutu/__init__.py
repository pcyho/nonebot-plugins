from nonebot import on_command, CommandSession

from .soutu import soutu

__plugin_name__ = 'soutu'
__plugin_usage__ = r"""
利用saucenao查找发送的图片，一次一张
use https://saucenao.com/search.php search image, you can use 'koishis search_img' to search image
"""


# on_command 装饰器将函数声明为一个命令处理器
# 这里 soutu 为命令的名字，同时允许使用别名
@on_command('soutu', aliases=('搜图', '找图', 'search_img'), only_to_me=False)
async def Sou_tu(session: CommandSession):
    # 获取信息
    cq = session.get('image', prompt='请发送您要查询的图片！')
    # 向用户发送结果信息
    mesg = await soutu(cq)
    # await session.send(CQ)
    await session.send(mesg)
