DROP TABLE IF EXISTS movies;

CREATE TABLE movies (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 movie_name TEXT NOT NULL,
 theatre_name TEXT NOT NULL
);

INSERT INTO movies VALUES (1, "GodFather", "PVR Cinemas");
INSERT INTO movies VALUES (2, "PS-1", "Gopalan Cinemas");
INSERT INTO movies VALUES (3, "Doctor G", "Abhinay Theatre");
INSERT INTO movies VALUES (4, "Kantara", "Cinepolis");
INSERT INTO movies VALUES (5, "Vikram Vedha", "Cinepolis: Royal Meenakshi Mall");