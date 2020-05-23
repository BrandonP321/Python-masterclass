import shelve

with shelve.open('typing-phrases') as phrases:
    phrases['0'] = "There was no time. He ran out of the door without half the " \
                   "stuff he needed for work, but it didn't matter. He was late " \
                   "and if he didn't make this meeting on time, someone's life " \
                   "may be in danger."
    phrases['1'] = "Sometimes there isn't a good answer. No matter how you " \
                   "try to rationalize the outcome, it doesn't make sense. " \
                   "And instead of an answer, you are simply left with a " \
                   "question. Why?"
    phrases['2'] = "What was beyond the bend in the stream was unknown. " \
                   "Both were curious, but only one was brave enough to want " \
                   "to explore. That was the problem. There was always one " \
                   "that let fear rule her life."
    phrases['3'] = "She counted. One. She could hear the steps coming closer. " \
                   "Two. Puffs of breath could be seen coming from his mouth. " \
                   "Three. He stopped beside her. Four. She pulled the trigger " \
                   "of the gun."
    phrases['4'] = "There was no time. He ran out of the door without half the " \
                   "stuff he needed for work, but it didn't matter. He was late " \
                   "and if he didn't make this meeting on time, someone's life " \
                   "may be in danger."

