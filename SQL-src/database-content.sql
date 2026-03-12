--resetting sequence:
--UPDATE `sqlite_sequence` SET `seq` = 0 WHERE `name` = 'table_name';

DELETE FROM qualification;
INSERT INTO qualification (name)
VALUES
    ('программирование в компьютерных системах'),
    ('информационные системы');


DELETE FROM "group";
INSERT INTO "group" (code, qualification_id)
VALUES
    ('П1-20', 1),
    ('П2-20', 1),
    ('ИС1-20', 2);


DELETE FROM discipline;
INSERT INTO discipline (name)
VALUES
    ('УП 01 01 Графические интерфейсы'),
    ('УП 02 01 Базы данных'),
    ('УП 01 01 Проектирование компьютерных систем');


DELETE FROM student;
INSERT INTO student (name, group_code)
VALUES
    ('Корников Николай', 'П1-20'),
    ('Барболина Катерина', 'П1-20'),
    ('Вагизом Роман', 'П2-20'),
    ('Даркин Кирилл', 'П2-20'),
    ('Крюков Сергей', 'ИС1-20');


DELETE FROM theme;
INSERT INTO theme (discipline_id, student_id, type, content)
VALUES
    (1,1,'Разработка ГИ для', ' приложения магазина'),
    (2,2,'Разработка БД для', ' аптеки'),
    (1,3,'Разработка ГИ для', ' сайта викторины'),
    (2,4,'Разработка БД для', ' аэропорта'),
    (2,5,'Разработка БД для', ' музея'),
    (3,5,'Проектирование компьютерной системы для', ' больницы');
