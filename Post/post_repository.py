from repository import Repository
from post import Post

class PostRepository(Repository[Post]):
    def __init__(self,posts:dict[int,Post]={}):
        self.posts = posts
    
    def get(self, id) -> Post:
        return self.posts[id]
    
    def get_all(self)->list[Post]:
        return list(self.posts.values())
    
    def add(self,entry)->None:
        self.posts[len(self.posts)] = entry

    def update(self,entry) -> None:
        if(entry.id is None):
            raise ValueError('No se puede actualizar el post')
        self.posts[entry.id] = entry
    
    def delete(self,entry) -> None:
        if entry.id is None:
            raise ValueError('No existe el id a eliminar')
        del self.posts[entry.id]
        
