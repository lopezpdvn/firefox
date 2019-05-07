-- Get tags
SELECT DISTINCT title
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
