# -*- coding: utf-8 -*-
#


def load_params_from_json(json_path):
    with open(json_path) as f:
        return json.load(f)