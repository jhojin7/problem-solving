select book.book_id, author.author_name, date_format(book.published_date,"%Y-%m-%d") as pubdate
from book
inner join author on book.author_id = author.author_id
where book.category = "경제"
order by pubdate asc
