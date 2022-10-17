import abc

class AsyncHttpReader(abc.ABC):
    """
    Interface for asynchronous HTTP reader.
    """

    @abc.abstractmethod
    async def get_text(self, url: str) -> str:
        """
        Implementation must raise native exception on status which is not 200
        """
        pass

    @abc.abstractmethod
    async def close(self, url: str) -> str:
        pass
