from cachetools import TTLCache, cached


class Cache:
    # Cache with a maximum size of 100 entries and a time-to-live of 300 seconds
    cache = TTLCache(maxsize=100, ttl=300)

    def __init__(self, cache_session):
        self.chat_session = chat_session

    def get_cache_list():
        res = []
        for chat_session in cache:
            res.append(chat_session)
            typer.echo(chat_session)
        return res

    def get_cache_entry():
        typer.echo(cache[chat_session])
