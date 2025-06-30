import json

class Config:
    def __init__(self, config_path='config.json'):
        self.config = self._load_config(config_path)

    def _load_config(self, config_path):
        with open(config_path, 'r') as f:
            return json.load(f)

    def get(self, key, default=None):
        return self.config.get(key, default)
