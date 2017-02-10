#-*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
secure_random = random.SystemRandom()

combinations = [
    ('coral','rgb(233,90,97)'),
    ('red','rgb(206,24,50)'),
    ('light-blue','rgb(114,196,231)'),
    ('yellow','rgb(244,159,46)'),
]

def customContextProcessor(request):
    return {
        "customColor": secure_random.choice(combinations),
    }