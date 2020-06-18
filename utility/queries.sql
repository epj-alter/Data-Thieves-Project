-- amazon x goodread
SELECT
    DISTINCT g.title,
    g.author,
    a.reviews as amazon_reviews,
    g.reviews as goodreads_reviews
FROM goodreads g
INNER JOIN amazon a
ON a.title = g.title;

-- ny x goodreads
SELECT
    DISTINCT g.title,
    g.author,
    ny.weeks_in_ranking,
    ny.common_genre,
    g.reviews as goodreads_reviews
from goodreads g
INNER JOIN ny_times ny
ON g.title = ny.title;

-- amazon x ny times
SELECT
    DISTINCT a.title,
    a.author,
    ny.weeks_in_ranking,
    a.reviews as amazon_reviews
FROM amazon a
INNER JOIN ny_times ny
ON ny.title = a.title;

-- n reviews comparison amazon x goodreads
SELECT 
    sum(amazon.reviews) as amazon_review_count,
    sum(goodreads.reviews) as goodreads_review_count
FROM amazon, goodreads;