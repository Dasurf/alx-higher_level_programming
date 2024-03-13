--Import the database dump from hbtn_0d_tvshows
SELECT tv_show_genres.genre_id AS genre,
       COUNT(tv_shows.title) AS number_of_shows
FROM tv_show_genres
JOIN tv_shows ON tv_show_genres.tv_show_id = tv_shows.id
GROUP BY tv_show_genres.genre_id
HAVING COUNT(tv_shows.title) > 0
ORDER BY number_of_shows DESC;
