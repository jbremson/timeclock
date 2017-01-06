CREATE TABLE IF NOT EXISTS
    fm.FilterJob
    (
        id BIGINT NOT NULL AUTO_INCREMENT,
        user_id BIGINT NOT NULL,
        filter_id BIGINT NOT NULL,
        create_date DATETIME,
        mod_date DATETIME,
        last_date DATETIME,
        CONSTRAINT FilterJob_pk_idx PRIMARY KEY (id)
    )
    ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS
    fm.User
    (
        id BIGINT NOT NULL AUTO_INCREMENT,
        name VARCHAR(128) DEFAULT 'No Name' NOT NULL,
        email VARCHAR(64) DEFAULT 'Nope@Nope.Gov' NOT NULL,
        password VARCHAR(128) DEFAULT 'empty' NOT NULL,
        phone VARCHAR(32),
        address VARCHAR(128),
        address2 VARCHAR(128),
        city VARCHAR(128),
        state VARCHAR(16),
        country VARCHAR(128) DEFAULT 'USA' NOT NULL,
        CONSTRAINT User_pk_idx PRIMARY KEY (id)
    )
    ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS
    fm.Filter
    (
        id BIGINT NOT NULL AUTO_INCREMENT,
        user_id BIGINT NOT NULL,
        name VARCHAR(64) DEFAULT 'unnamed filter' NOT NULL,
        period ENUM('annual', 'semiannual', 'triannual', 'quarterly', 'bimonthly',
                    'monthly', 'semimonthly','weekly', 'daily') DEFAULT 'annual' NOT NULL,
        type_id BIGINT DEFAULT '0' NOT NULL,
        item_brand VARCHAR(128),
        filter_brand VARCHAR(128),
        item_model VARCHAR(128),
        filter_model VARCHAR(128),
        is_active BOOL DEFAULT 1 NOT NULL,
        item_year BIGINT,
        description VARCHAR(256),
        CONSTRAINT Filter_pk_idx PRIMARY KEY (id)
    )
    ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS
    fm.FilterType
    (
        id BIGINT AUTO_INCREMENT,
        name VARCHAR(128) DEFAULT 'unknown',
        item_class BIGINT,
        CONSTRAINT FilterType_pk_idx PRIMARY KEY (id)
    )
    ENGINE=InnoDB DEFAULT CHARSET=utf8;