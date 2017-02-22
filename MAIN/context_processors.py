#-*- coding: utf-8 -*-
from __future__ import unicode_literals

import random
secure_random = random.SystemRandom()

def customContextProcessor(request):
    return {
        "customColor": "#528DD9",
    }