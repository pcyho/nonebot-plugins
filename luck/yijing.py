from iching import iching
import time


def get_prodect(birthdy: str) -> str:
    iching.ichingDate(int(birthdy + time.strftime("%Y%m%d")))
    iching.getPredict()
    fixPred, changePred = iching.getPredict()
    iching.ichingName(fixPred, changePred)
    text = iching.ichingText(fixPred, iching).split("\n")
    return text[0] + text[4]
