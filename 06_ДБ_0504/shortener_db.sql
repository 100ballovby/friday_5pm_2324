CREATE TABLE Users (
    id INTEGER NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (id)  /* первичный ключ таблицы можно задать после создания всех полей */
);


CREATE TABLE Links (
    id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    original_url VARCHAR(2048) NOT NULL,
    short_url VARCHAR(255) UNIQUE NOT NULL,
    clicks INTEGER NOT NULL DEFAULT 0,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES Users(id)
    /*ВНЕШНИЙ КЛЮЧ user_id СВЯЗЫВАЕТСЯ С таблица_Users(поле_id)*/
);


CREATE TABLE Clicks (
    id INTEGER NOT NULL,
    link_id INTEGER NOT NULL,
    ip_address VARCHAR(45) NOT NULL,
    UserAgent VARCHAR(255) NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,

    PRIMARY KEY (id),
    FOREIGN KEY (link_id) REFERENCES Links(id)
);


