import json
import storage.config

async def get_token_src():
    try:
        if storage.config.token == None:
                with open("data/config.json", "r", encoding="utf-8") as file:
                    var = json.loads(file)
                    storage.config.token = var["token"]
        return storage.config.token
    except Exception as e:
        print(f"get_token(): {e}")
        return 