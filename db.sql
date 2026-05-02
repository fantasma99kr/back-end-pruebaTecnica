/*
Base de datos creada en SQL SERVER
*/

CREATE DATABASE aeropuerto;
GO

USE aeropuerto;
GO

CREATE TABLE aerolineas(
	id_aerolinea INTEGER PRIMARY KEY IDENTITY(1,1),
	nombre_aerolinea NVARCHAR(100) NOT NULL
);

INSERT INTO aerolineas 
VALUES
('Volaris'),
('Aeromar'),
('Interjet'),
('Aeromexico');

CREATE TABLE aeropuertos(
	id_aeropuerto INTEGER PRIMARY KEY IDENTITY(1,1),
	nombre_aeropuerto NVARCHAR(100) NOT NULL
);

INSERT INTO aeropuertos
VALUES
('Benito Juarez'),
('Guanajuato'),
('La Paz'),
('Oaxaca');

CREATE TABLE movimientos(
	id_movimiento INTEGER  PRIMARY KEY IDENTITY(1,1),
	descripcion NVARCHAR(100) NOT NULL
);

INSERT INTO movimientos
VALUES
('salida'),
('llegada');

CREATE TABLE vuelos(
	id_vuelo INTEGER PRIMARY KEY IDENTITY(1,1),
	Id_aerolinea INTEGER,
	id_aeropuerto INTEGER,
	id_movimiento INTEGER,
	dia date,
	CONSTRAINT FK_AEROLINEA_VUELOS FOREIGN KEY(id_aerolinea) REFERENCES aerolineas(id_aerolinea),
	CONSTRAINT FK_AEROPUERTO_VUELOS FOREIGN KEY(id_aeropuerto) REFERENCES aeropuertos(id_aeropuerto),
	CONSTRAINT FK_MOVIMIENTO_VOELOS FOREIGN KEY(id_movimiento) REFERENCES movimientos(id_movimiento)
);

INSERT INTO vuelos
VALUES
(1,1,1,'2021-05-02'),
(2,1,1,'2021-05-02'),
(3,2,2,'2021-05-02'),
(4,3,2,'2021-05-02'),
(1,3,2,'2021-05-02'),
(2,1,1,'2021-05-02'),
(2,3,1,'2021-05-04'),
(3,4,1,'2021-05-04'),
(3,4,1,'2021-05-04');
	