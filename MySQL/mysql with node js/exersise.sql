--find earliest data a user joined
select 
    data_format(min(created_at), "%M %D %Y") as earliest_date
from users;


--find email of the first user
select * from users where created_at = (select min(created_at) from users);


--users according to month they joined
select monthname(created_at) as month, count(*) as total from users GROUP BY month order by total desc;


--count the users who has yahoo
select count(*) yahoo_users from users where email like '%@yahoo.com%';


--total number of users for each email host
select
    case 
        when email like '%@gmail.com' then 'gmail'
        when email like '%@yahoo.com' then 'yahoo'
        when email like '%@hotmail.com' then 'hotmail'
        else 'others'
    end provider,count(*) count
from users
group by provider
order by count desc;