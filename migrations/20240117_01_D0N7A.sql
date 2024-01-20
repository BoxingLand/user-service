CREATE TABLE "user" (
    id UUID PRIMARY KEY,
    email VARCHAR(255),
    password VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    middle_name VARCHAR(255),
    phone_number VARCHAR(255),
    birthday DATE,
    country VARCHAR(255),
    region VARCHAR(255),
    city VARCHAR(255),
    verify_token VARCHAR(255),
    updated_at timestamp,
    created_at timestamp,
    is_active BOOLEAN,
    is_deleted BOOLEAN
);

CREATE TABLE "boxer" (
    id UUID PRIMARY KEY,
    weight float,
    height float,
    athletic_distinction VARCHAR(255),
    user_id UUID,
    club_id UUID,
    updated_at timestamp,
    created_at timestamp,
    is_deleted BOOLEAN
);

CREATE TABLE "coach" (
    id UUID PRIMARY KEY,
    user_id UUID,
    updated_at timestamp,
    created_at timestamp,
    is_deleted BOOLEAN
);

CREATE TABLE "judge" (
    id UUID PRIMARY KEY,
    user_id UUID,
    judical_rank VARCHAR(255),
    updated_at timestamp,
    created_at timestamp,
    is_deleted BOOLEAN
);

CREATE TABLE "organizer" (
    id UUID PRIMARY KEY,
    user_id UUID,
    updated_at timestamp,
    created_at timestamp,
    is_deleted BOOLEAN
);

ALTER TABLE "boxer" ADD FOREIGN KEY (user_id) REFERENCES "user" (id);

ALTER TABLE "coach" ADD FOREIGN KEY (user_id) REFERENCES "user" (id);

ALTER TABLE "judge" ADD FOREIGN KEY (user_id) REFERENCES "user" (id);

ALTER TABLE "organizer" ADD FOREIGN KEY (user_id) REFERENCES "user" (id);
