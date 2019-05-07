-- Get tags
SELECT *
FROM moz_bookmarks
WHERE 1=1
  AND parent IN (
    SELECT id
    FROM moz_bookmarks
    WHERE 1=1
      AND guid = 'tags________'
      AND title = 'Tags')
ORDER BY title


-- Select tagged bookmarks
SELECT *
FROM moz_bookmarks
WHERE 1=1
  AND fk IN (
  
  SELECT fk
FROM moz_bookmarks
WHERE 1=1
  AND parent IN (
    SELECT id
    FROM moz_bookmarks
    WHERE 1=1
      AND parent IN (
        SELECT id
        FROM moz_bookmarks
        WHERE 1=1
          AND guid = 'tags________'
          AND title = 'Tags')
  )
ORDER BY id
  
  )
  AND title IS NOT NULL


  
  
SELECT b.*, p.*
FROM moz_places p
INNER JOIN moz_bookmarks b
  ON b.fk = p.id
--ORDER  BY p.url
WHERE b.id IN (

  SELECT id
  FROM moz_bookmarks
  WHERE 1=1
    AND parent IN (
      SELECT id
      FROM moz_bookmarks
      WHERE 1=1
        AND parent IN (
          SELECT id
          FROM moz_bookmarks
          WHERE 1=1
            AND guid = 'tags________'
            AND title = 'Tags')
    )

)



SELECT b.fk, b.title , p.url, b.*
FROM moz_bookmarks b
  INNER JOIN moz_places p
ON p.id = b.fk
--WHERE b.title IS NOT NULL
ORDER BY p.url, b.title
	
SELECT *
FROM moz_bookmarks
WHERE fk = 30