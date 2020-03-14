from nonebot import on_command, CommandSession
from random import randint, choice
from .yijing import get_prodect
__plugin_name__ = 'luck'
__plugin_usage__ = """luck
通过输入生日来用易经占卜今天运势，例如：
19990315"""


@on_command('运势', aliases=('luck', '运气'), only_to_me=False)
async def luck(session: CommandSession):
    arg = session.get('args', prompt='请输入生日')
    await session.send(str(get_prodect(str(arg))))



@luck.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            session.state['args'] = stripped_arg
            return

    if not stripped_arg:
        pass
        session.pause("请输入生日，格式如下： 20000101")

    session.state[session.current_key] = stripped_arg