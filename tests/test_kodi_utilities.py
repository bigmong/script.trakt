# -*- coding: utf-8 -*-
#

import json
import pytest
import sys
sys.modules['xbmc'] = __import__('tests.xbmc_mock')
sys.modules['xbmcaddon'] = __import__('tests.xbmcaddon_mock')


def test_kodiJsonRequest():
    data1 = '1'
    test = xbmcaddon.Addon('script.trakt')
    assert test == data1