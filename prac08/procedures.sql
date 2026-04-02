CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE name = p_name) THEN
        UPDATE contacts SET phone = p_phone WHERE name = p_name;
    ELSE
        INSERT INTO contacts (name, phone) VALUES (p_name, p_phone);
    END IF;
END;
$$;

CREATE OR REPLACE PROCEDURE bulk_insert_contacts(contacts_data TEXT[][])
LANGUAGE plpgsql AS $$
DECLARE
    contact_row TEXT[];
    current_name VARCHAR;
    current_phone VARCHAR;
    inserted_count INT := 0;
BEGIN
    FOREACH contact_row SLICE 1 IN ARRAY contacts_data
    LOOP
        current_name := contact_row[1];
        current_phone := contact_row[2];
        
        IF current_phone ~ '^[0-9]{10,15}$' THEN
            BEGIN
                INSERT INTO contacts (name, phone) 
                VALUES (current_name, current_phone);
                inserted_count := inserted_count + 1;
            EXCEPTION WHEN unique_violation THEN
                -- skip duplicate
            END;
        END IF;
    END LOOP;
    RAISE NOTICE 'Inserted % contacts', inserted_count;
END;
$$;

-- 5. Delete procedure by username or phone
CREATE OR REPLACE PROCEDURE delete_contact_by(p_identifier TEXT, p_type TEXT)
LANGUAGE plpgsql AS $$
BEGIN
    IF p_type = 'name' THEN
        DELETE FROM contacts WHERE name = p_identifier;
    ELSIF p_type = 'phone' THEN
        DELETE FROM contacts WHERE phone = p_identifier;
    ELSE
        RAISE EXCEPTION 'Invalid type. Use name or phone';
    END IF;
END;
$$;