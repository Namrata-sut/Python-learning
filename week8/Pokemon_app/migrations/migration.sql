BEGIN;

CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL,
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> e3917a8f0be7

CREATE TABLE pokemon_new_data (
    id SERIAL NOT NULL,
    name VARCHAR NOT NULL,
    height INTEGER NOT NULL,
    weight INTEGER NOT NULL,
    xp INTEGER NOT NULL,
    image_url VARCHAR NOT NULL,
    pokemon_url VARCHAR NOT NULL,
    abilities JSON NOT NULL,
    stats JSON NOT NULL,
    types JSON,
    PRIMARY KEY (id)
);

DROP TABLE pokemon_table;

DROP TABLE pokemon_new_data_table;

INSERT INTO alembic_version (version_num) VALUES ('e3917a8f0be7') RETURNING alembic_version.version_num;

-- Running upgrade e3917a8f0be7 -> dbd7f123512a

UPDATE alembic_version SET version_num='dbd7f123512a' WHERE alembic_version.version_num = 'e3917a8f0be7';

-- Running upgrade dbd7f123512a -> 2c1ac237b69f

UPDATE alembic_version SET version_num='2c1ac237b69f' WHERE alembic_version.version_num = 'dbd7f123512a';

-- Running upgrade 2c1ac237b69f -> 5704396ca9a5

UPDATE alembic_version SET version_num='5704396ca9a5' WHERE alembic_version.version_num = '2c1ac237b69f';

-- Running upgrade 5704396ca9a5 -> 8cf85fc27c5c

UPDATE alembic_version SET version_num='8cf85fc27c5c' WHERE alembic_version.version_num = '5704396ca9a5';

-- Running upgrade 8cf85fc27c5c -> 1ce3ce8dd198

ALTER TABLE pokemon_new_data ALTER COLUMN types SET NOT NULL;

UPDATE alembic_version SET version_num='1ce3ce8dd198' WHERE alembic_version.version_num = '8cf85fc27c5c';

-- Running upgrade 1ce3ce8dd198 -> f94930f37bb5

ALTER TABLE pokemon_new_data ALTER COLUMN types DROP NOT NULL;

UPDATE alembic_version SET version_num='f94930f37bb5' WHERE alembic_version.version_num = '1ce3ce8dd198';

-- Running upgrade f94930f37bb5 -> bd2e91979ad0

UPDATE alembic_version SET version_num='bd2e91979ad0' WHERE alembic_version.version_num = 'f94930f37bb5';

-- Running upgrade bd2e91979ad0 -> e9772df9b2ec

ALTER TABLE pokemon_new_data ALTER COLUMN stats DROP NOT NULL;

ALTER TABLE pokemon_new_data ALTER COLUMN types SET NOT NULL;

UPDATE alembic_version SET version_num='e9772df9b2ec' WHERE alembic_version.version_num = 'bd2e91979ad0';

COMMIT;

--migration script generated--
