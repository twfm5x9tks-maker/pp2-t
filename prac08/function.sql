CREATE OR REPLACE FUNCTION search_contacts_pattern(search_text TEXT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT contacts.id, contacts.name, contacts.phone
    FROM contacts
    WHERE contacts.name ILIKE '%' || search_text || '%'
       OR contacts.phone ILIKE '%' || search_text || '%'
    ORDER BY contacts.name;
END;
$$ LANGUAGE plpgsql;

CREATE OR REPLACE FUNCTION get_contacts_paginated(page_num INT, rows_per_page INT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT contacts.id, contacts.name, contacts.phone
    FROM contacts
    ORDER BY contacts.id
    LIMIT rows_per_page
    OFFSET (page_num - 1) * rows_per_page;
END;
$$ LANGUAGE plpgsql;