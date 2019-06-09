# -*- coding: UTF-8 -*-
# 统计一段由字符和和空格组成的字符串中有多少个单词
# 使用状态机
from enum import Enum

# 枚举 need python3
class State(Enum):
    INIT_STATE = 1
    WORD_STATE = 2
    SPACE_STATE = 3

count = 0
state = State.INIT_STATE

def word_count(text):
    global state
    global count
    for c in text:
        if state == State.INIT_STATE:
            if " " != c:
                count += 1
                state = State.WORD_STATE
            else:
                state = State.SPACE_STATE
        elif state == State.WORD_STATE:
            if " " == c:
                state = State.SPACE_STATE
        elif state == State.SPACE_STATE:
            if " " != c:
                count += 1
                state = State.WORD_STATE

word_count("  aaa b  cdd ")
print(count)