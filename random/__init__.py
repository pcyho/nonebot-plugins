from nonebot import on_command, CommandSession
from random import randint, choice

__plugin_name__ = 'random'
__plugin_usage__ = """random"""


@on_command('rd', aliases=('random', 'rm'), only_to_me=False)
async def rd(session: CommandSession):
    args = session.get('args', prompt='请输入参数')
    if args.find(' '):
        arg = args.split(" ")
    else:
        arg = [args]
    print(arg)
    if len(arg) == 1:
        if arg[0].isdigit():
            await session.send(str(randint(0, int(arg[0])) + 1))
        else:
            await session.send(arg[0])
    else:
        await session.send(choice(arg))


@rd.args_parser
async def _(session: CommandSession):
    stripped_arg = session.current_arg_text.strip()

    if session.is_first_run:
        # 该命令第一次运行（第一次进入命令会话）
        if stripped_arg:
            session.state['args'] = stripped_arg
            return

    if not stripped_arg:
        pass
        session.pause("input args")

    session.state[session.current_key] = stripped_arg
