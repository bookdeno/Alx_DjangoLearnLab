# Retrieve Operation

```python
from bookshelf.models import Book

# Retrieve the book
book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year
```
