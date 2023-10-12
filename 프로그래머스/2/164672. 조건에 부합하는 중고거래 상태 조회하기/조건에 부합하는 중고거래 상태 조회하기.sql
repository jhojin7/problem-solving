select 
	BOARD_ID,
    WRITER_ID,
    TITLE,
    PRICE,
    (case
     when status="RESERVED" then "예약중"
     when status="DONE" then "거래완료"
     when status="SALE" then "판매중"
     end
    ) as STATUS
from used_goods_board
where created_date = "2022-10-05"
order by board_id desc