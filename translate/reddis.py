class WriteDictionary:

    def __init__(self, redis_, phrase, *translate_dicts):
        with redis_.pipeline() as pipe:
            for lang_phrase in translate_dicts:
                pipe.hset(phrase, mapping=lang_phrase)
            pipe.execute()


class GetDictionary:
    @staticmethod
    def get_dictionary(redis_, phrase, lang=None):
        if lang:
            return redis_.hget(phrase, lang).decode("utf-8")
        return redis_.hgetall(phrase)

