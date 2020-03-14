import sys
def _taowa(n):
    a="套娃"
    count=0
    while True:
        if count >n:
            return
        yield a
        a="禁止"+ a
        count=count+1

f=_taowa(100)
while True:
    try:
        print(next(f))
    except StopIteration:
        sys.exit()