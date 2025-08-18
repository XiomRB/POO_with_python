from abc import ABC, abstractmethod
from post import Post

class Repository[T](ABC):
    @abstractmethod
    def get(self,id)->T:
        raise NotImplementedError
    
    @abstractmethod
    def get_all(self) -> list[T]:
        raise NotImplementedError
    
    @abstractmethod
    def add(self,value) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def update(self,id,value) -> None:
        raise NotImplementedError
    
    @abstractmethod
    def delete(self,id) -> None:
        raise NotImplementedError