DROP TABLE IF EXISTS movies;

CREATE TABLE movies (
 id INTEGER PRIMARY KEY AUTOINCREMENT,
 movie_name TEXT NOT NULL,
 theatre_name TEXT NOT NULL,
 seats TEXT,
 booked_seats TEXT,
 posters TEXT
);

INSERT INTO movies VALUES (1, "GodFather", "PVR Cinemas",'','',"Godfather.jpg");
INSERT INTO movies VALUES (2, "PS-1", "Gopalan Cinemas",'','',"Ponniyin-Selvan1.jpg");
INSERT INTO movies VALUES (3, "Doctor G", "Abhinay Theatre",'','',"Doctor G.jpg");
INSERT INTO movies VALUES (4, "Kantara", "Cinepolis",'','',"Kantara.jpg");
INSERT INTO movies VALUES (5, "Vikram Vedha", "Cinepolis: Royal Meenakshi Mall",'','',"Vikram vedha.jpg");
INSERT INTO movies VALUES (6, "Minions: The Rise Of Gru", "INOX",'','',"minions.jpg");
