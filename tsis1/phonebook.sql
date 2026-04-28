-- ============================================================
-- DROP EVERYTHING (барлығын тазалау)
-- ============================================================
DROP TABLE IF EXISTS phones   CASCADE;
DROP TABLE IF EXISTS contacts CASCADE;
DROP TABLE IF EXISTS groups   CASCADE;

DROP PROCEDURE IF EXISTS upsert_contact(VARCHAR, VARCHAR, VARCHAR, DATE, VARCHAR);
DROP PROCEDURE IF EXISTS upsert_contact(VARCHAR, VARCHAR, VARCHAR, DATE, INT);
DROP PROCEDURE IF EXISTS insert_new_users(VARCHAR[], VARCHAR[], VARCHAR[], DATE[], INT[]);
DROP PROCEDURE IF EXISTS deleting_contacts(VARCHAR, VARCHAR, VARCHAR, DATE, INT);
DROP PROCEDURE IF EXISTS deleting_contacts(VARCHAR, VARCHAR);
DROP PROCEDURE IF EXISTS add_phone(VARCHAR, VARCHAR, VARCHAR);
DROP PROCEDURE IF EXISTS move_to_group(VARCHAR, VARCHAR);

DROP FUNCTION IF EXISTS get_contacts_paginated(INT, INT);
DROP FUNCTION IF EXISTS get_contacts_by_patterns(TEXT);
DROP FUNCTION IF EXISTS search_contacts(TEXT);

-- ============================================================
-- TABLES
-- ============================================================
CREATE TABLE groups (
    id   SERIAL PRIMARY KEY,
    name VARCHAR(50) UNIQUE NOT NULL
);

CREATE TABLE contacts (
    id         SERIAL PRIMARY KEY,
    name       VARCHAR(100),
    phone      VARCHAR(100),
    email      VARCHAR(100),
    birthday   DATE,
    group_name VARCHAR(50) REFERENCES groups(name)
);

CREATE TABLE phones (
    id         SERIAL PRIMARY KEY,
    contact_id INTEGER REFERENCES contacts(id) ON DELETE CASCADE,
    phone      VARCHAR(20) NOT NULL,
    type       VARCHAR(10) CHECK (type IN ('home', 'work', 'mobile'))
);

INSERT INTO groups(name) VALUES ('family'), ('work'), ('friend'), ('other');

-- ============================================================
-- FUNCTIONS & PROCEDURES
-- ============================================================

CREATE OR REPLACE FUNCTION get_contacts_by_patterns(p TEXT)
RETURNS TABLE(name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT c.name, c.phone FROM contacts c
    WHERE c.name  ILIKE '%' || p || '%'
    OR    c.phone ILIKE '%' || p || '%';
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE upsert_contact(
    p_name       VARCHAR,
    p_phone      VARCHAR,
    p_email      VARCHAR,
    p_birthday   DATE,
    p_group_name VARCHAR DEFAULT NULL
)
LANGUAGE plpgsql AS $$
BEGIN
    IF p_group_name IS NOT NULL AND NOT EXISTS (
        SELECT 1 FROM groups WHERE name = p_group_name
    ) THEN
        INSERT INTO groups(name) VALUES (p_group_name);
    END IF;

    IF EXISTS (SELECT 1 FROM contacts WHERE name = p_name) THEN
        UPDATE contacts
        SET phone = p_phone, group_name = p_group_name
        WHERE name = p_name;
    ELSE
        INSERT INTO contacts(name, phone, email, birthday, group_name)
        VALUES (p_name, p_phone, p_email, p_birthday, p_group_name);
    END IF;
END;
$$;

CREATE OR REPLACE PROCEDURE insert_new_users(
    names      VARCHAR[],
    phones     VARCHAR[],
    emails     VARCHAR[],
    birthdays  DATE[],
    groups_id  INT[] DEFAULT NULL
)
LANGUAGE plpgsql AS $$
DECLARE
    i            INT;
    invalid_data TEXT[] := ARRAY[]::TEXT[];
BEGIN
    FOR i IN 1..array_length(names, 1) LOOP
        IF phones[i] ~ '^\d+$' THEN
            CALL upsert_contact(names[i], phones[i], emails[i], birthdays[i]);
        ELSE
            invalid_data := array_append(invalid_data, names[i] || ':' || phones[i]);
        END IF;
    END LOOP;

    IF array_length(invalid_data, 1) IS NOT NULL THEN
        RAISE NOTICE 'Invalid data: %', array_to_string(invalid_data, ',');
    END IF;
END;
$$;

CREATE OR REPLACE FUNCTION get_contacts_paginated(p_limit INT, p_offset INT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR, email VARCHAR, birthday DATE, group_name VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT c.id, c.name, c.phone, c.email, c.birthday, c.group_name
    FROM contacts c
    ORDER BY c.id
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE PROCEDURE deleting_contacts(
    p_name       VARCHAR DEFAULT NULL,
    p_phone      VARCHAR DEFAULT NULL,
    p_email      VARCHAR DEFAULT NULL,
    p_birthday   DATE   DEFAULT NULL,
    p_group_name VARCHAR DEFAULT NULL
)
LANGUAGE plpgsql AS $$
BEGIN
    IF p_name IS NOT NULL THEN
        DELETE FROM contacts WHERE name = p_name;
    ELSIF p_phone IS NOT NULL THEN
        DELETE FROM contacts WHERE phone = p_phone;
    ELSE
        RAISE NOTICE 'No name or phone provided!';
    END IF;
END;
$$;

CREATE OR REPLACE PROCEDURE add_phone(
    p_contact_name VARCHAR,
    p_phone        VARCHAR,
    p_type         VARCHAR
)
LANGUAGE plpgsql AS $$
DECLARE
    v_contact_id INT;
BEGIN
    SELECT id INTO v_contact_id FROM contacts WHERE name = p_contact_name;
    INSERT INTO phones(contact_id, phone, type) VALUES (v_contact_id, p_phone, p_type);
END;
$$;

CREATE OR REPLACE PROCEDURE move_to_group(
    p_contact_name VARCHAR,
    p_group_name   VARCHAR
)
LANGUAGE plpgsql AS $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM groups WHERE name = p_group_name) THEN
        INSERT INTO groups(name) VALUES (p_group_name);
    END IF;
    UPDATE contacts SET group_name = p_group_name WHERE name = p_contact_name;
END;
$$;

CREATE OR REPLACE FUNCTION search_contacts(p_query TEXT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR, email VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT DISTINCT c.id, c.name, c.phone, c.email
    FROM contacts c
    LEFT JOIN phones p ON p.contact_id = c.id
    WHERE c.name  ILIKE '%' || p_query || '%'
    OR    c.email ILIKE '%' || p_query || '%'
    OR    p.phone ILIKE '%' || p_query || '%';
END;
$$ LANGUAGE plpgsql;

-- ============================================================
-- TEST DATA
-- ============================================================
CALL upsert_contact('Madina', '87767321438', 'turgynbekovamadina@gmail.com', '2008-04-10');
CALL upsert_contact('Merey',  '87765321438', 'turgynbekovamerey@gmail.com',  '2004-03-20', 'family');
CALL upsert_contact('Mingyu', '87956143855', 'kim.mingyu@gmail.com',         '1997-04-06', 'other');
CALL upsert_contact('Mdin',   '821438',      'gvfhsdhb@gmail.com',           '1852-02-25');

SELECT * FROM get_contacts_paginated(2, 0);
SELECT * FROM get_contacts_by_patterns('776732');

CALL insert_new_users(
    ARRAY['fghj', 'ghjk', 'ghjkjk'],
    ARRAY['74185', '85296', '8525'],
    ARRAY['cvghgfygf@gmail.com', 'hufhurfhuhu@gmail.com', 'qwerty@gmail.com'],
    ARRAY['2008-04-11', '1976-02-14', '2024-07-18']::DATE[]
);

SELECT * FROM contacts;

CALL deleting_contacts(p_name := 'Mdin');
CALL add_phone('Merey', '87767361498', 'work');
CALL move_to_group('Merey', 'other');

SELECT * FROM search_contacts('8776');
SELECT * FROM contacts;