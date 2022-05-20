with t as (select p.id, p.request_at, p.status
from (select * from trips as a join users as b on a.client_id = b.users_id where banned = 'No') as p
join (select * from trips as a join users as b on a.driver_id = b.users_id where banned = 'No') as q
on p.id = q.id where p.request_at between '2013-10-01' and '2013-10-03')

select request_at as Day, round(count(case when status = 'cancelled_by_driver' or status = 'cancelled_by_client' then 1 end)/count(*), 2) as 'Cancellation Rate' from t group by request_at