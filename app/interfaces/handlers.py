from abc import ABC


class APIHandler(ABC):
    @classmethod
    async def get_result(self, *args, **kwargs):
        pass
