--1.finding 5 oldest users

select * from users
order by created_at
limit 5;

--2.Most Popular Registration Date

select 
dayname(created_at) as day,
count(*) as total
from users group by day
order by total desc
limit 3;

--3.Identify inactive users (users with no photos)

select username, image_url status
 from users
left join photos 
on users.id = photos.user_id where photos.id is NULL;

--4.Identify most popular photo (and user who created it)
select username,photos.id, photos.image_url,count(*) as total
from photos
inner join likes
    on likes.photo_id = photos.id
inner join users
    on photos.user_id = users.id
group by photos.id
order by total desc limit 1;

--5.calculate avg number of photos per user
--total number of photos / total number of users
select
(select count(*) from photos)/(select count(*) from users) as avg;


--6. five most popular hashtags
select  tags.tag_name,count(*) total
from photo_tags
join tags 
    ON photo_tags.tag_id = tags.id group by tags.id 
    order by total desc LIMIT 5;


--7. FInding Bots - users who haveliked every single photo

select username,count(*) num_likes from users
inner join likes
    on users.id = likes.user_id
group by likes.user_id
having num_likes = (select count(*) from photos);
