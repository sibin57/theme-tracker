--theme request
SELECT
    discipline.name as discipline,
    student.name as student,
    theme.type as "theme type",
	theme.content as "theme content"
FROM
    theme
INNER JOIN discipline
    ON theme.discipline_id = discipline.id
INNER JOIN student
    ON theme.student_id = student.id;

