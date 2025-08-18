from post import Post
from post_repository import PostRepository

repo = PostRepository()
repo.add(Post(0, 'prueba', 'Esto es una prueba'))
repo.add(Post(1, 'prueba dos', 'Esto es la segunda prueba'))
repo.add(Post(2, 'prueba final', 'Esto es la ultima prueba'))

print(repo.get_all())

repo.update(Post(1, 'prueba update', 'Esto es la un update'))
print(repo.get(1))

repo.delete(Post(2, 'prueba final', 'Esto es la ultima prueba'))
print(repo.get_all())