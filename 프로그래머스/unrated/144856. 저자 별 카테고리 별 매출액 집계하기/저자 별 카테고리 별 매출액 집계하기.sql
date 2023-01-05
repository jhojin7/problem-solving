select author_id, author_name, category, sum(sales*bookinfo.price) as total_sales
from book_sales
left join (
    select book.book_id, author.author_id, author.author_name, book.category, book.price
    from book
    left join author on book.author_id=author.author_id
) as bookinfo on book_sales.book_id=bookinfo.book_id
where date_format(book_sales.sales_date,"%Y-%m")="2022-01"
group by bookinfo.author_id, bookinfo.category
order by bookinfo.author_id asc, bookinfo.category desc