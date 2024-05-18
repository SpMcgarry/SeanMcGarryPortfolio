CREATE TABLE publishers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE creators (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE comics (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    publisher_id INTEGER,
    release_date DATE,
    edition INTEGER,
    FOREIGN KEY (publisher_id) REFERENCES publishers(id)
);

CREATE TABLE comic_creators (
    comic_id INTEGER,
    creator_id INTEGER,
    PRIMARY KEY (comic_id, creator_id),
    FOREIGN KEY (comic_id) REFERENCES comics(id),
    FOREIGN KEY (creator_id) REFERENCES creators(id)
);
