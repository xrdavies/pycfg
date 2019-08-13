'''
Python module to handle configurations.
Compatiable with TOML 0.5.0
'''

import os
import toml
import json

class Config:
    def __init__(self):
        self._set = {}
    
    def __repr__(self):
        return json.dumps(self._set)

    def __load_config__(self, path):
        if not path:
            raise ValueError("Empty path!", path)
        elif not os.path.exists(path):
            raise ValueError("Invalid path!", path)
        self._set = toml.load(open(path, 'r', encoding='utf-8'))
        pass

    def get(self, key, default_val=None):
        '''get config by key.'''
        if not key:
            return default_val

        key_path = key.split('.')
        if len(key_path) == 1:
            return self._set.get(key, default_val)
        if key_path[0] not in self._set:
            return default_val

        cur_val = self._set
        for k in key_path:
            if k not in cur_val:
                return default_val
            cur_val = cur_val[k]
        return cur_val

def load_config(path):
    cfg = Config()
    cfg.__load_config__(path)
    return cfg

if __name__ == '__main__':
    cfg = load_config('./test.toml')
    print(cfg)
    print(cfg.get('products'))
    print(cfg.get('user.name'))
    pass