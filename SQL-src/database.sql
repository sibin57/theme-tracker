DROP TABLE IF EXISTS theme;
DROP TABLE IF EXISTS student;
DROP TABLE IF EXISTS discipline;
DROP TABLE IF EXISTS "group";
DROP TABLE IF EXISTS qualification;


CREATE TABLE IF NOT EXISTS qualification (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    name            TEXT
);

CREATE TABLE IF NOT EXISTS "group" (
    code            TEXT PRIMARY KEY,
    qualification_id   TEXT, --FK

    FOREIGN KEY (qualification_id)
        REFERENCES qualification (id)
);

CREATE TABLE IF NOT EXISTS discipline ( --Возможно тоже стоит упростить до одного поля
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    name            TEXT
);

CREATE TABLE IF NOT EXISTS student (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    "name"          TEXT,
    group_code      TEXT, --FK

    FOREIGN KEY (group_code)
        REFERENCES "group" (code)

);


CREATE TABLE IF NOT EXISTS theme (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    discipline_id   INTEGER, --FK
    student_id      INTEGER, --FK
    type      TEXT,
    content   TEXT,

    FOREIGN KEY (discipline_id)
        REFERENCES discipline (id),
    FOREIGN KEY (student_id)
        REFERENCES student (id)
);
