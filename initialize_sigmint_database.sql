BEGIN TRANSACTION;

-- Table: ComicBooks
CREATE TABLE IF NOT EXISTS ComicBooks (
    ComicBookID INTEGER PRIMARY KEY,
    Title TEXT,
    IssueNumber INTEGER,
    Volume INTEGER,
    PublicationDate TEXT,
    PublisherID INTEGER,
    CreatorID INTEGER,
    CoverArtist TEXT,
    Writer TEXT,
    Description TEXT,
    FOREIGN KEY (PublisherID) REFERENCES Publishers(PublisherID),
    FOREIGN KEY (CreatorID) REFERENCES Creators(CreatorID)
);

-- Table: Publishers
CREATE TABLE IF NOT EXISTS Publishers (
    PublisherID INTEGER PRIMARY KEY,
    Name TEXT,
    Description TEXT,
    ImportantNumbers TEXT,
    Website TEXT
);

-- Table: Creators
CREATE TABLE IF NOT EXISTS Creators (
    CreatorID INTEGER PRIMARY KEY,
    Name TEXT,
    Role TEXT,
    Description TEXT,
    ImportantNumbers TEXT,
    Website TEXT
);

-- Table: LamborghiniCollectibles
CREATE TABLE IF NOT EXISTS LamborghiniCollectibles (
    CollectibleID INTEGER PRIMARY KEY,
    Name TEXT,
    ModelNumber TEXT,
    ReleaseYear INTEGER,
    SignificantNumbers TEXT,
    EditionsMade INTEGER,
    PublisherID INTEGER,
    FOREIGN KEY (PublisherID) REFERENCES Publishers(PublisherID)
);

-- Table: SignificantNumbers
CREATE TABLE IF NOT EXISTS SignificantNumbers (
    NumberID INTEGER PRIMARY KEY,
    Number INTEGER,
    Description TEXT
);

-- Table: CollectibleSignificantNumbers
CREATE TABLE IF NOT EXISTS CollectibleSignificantNumbers (
    AssociationID INTEGER PRIMARY KEY,
    CollectibleID INTEGER,
    NumberID INTEGER,
    FOREIGN KEY (CollectibleID) REFERENCES LamborghiniCollectibles(CollectibleID),
    FOREIGN KEY (NumberID) REFERENCES SignificantNumbers(NumberID)
);

COMMIT;
