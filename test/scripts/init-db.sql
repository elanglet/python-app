CREATE TABLE IF NOT EXISTS client (
  idclient INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
  nom varchar(100) NOT NULL,
  adresse varchar(200) NOT NULL,
  codepostal varchar(10) NOT NULL,
  ville varchar(100) NOT NULL,
  activite varchar(200) NOT NULL
);

INSERT INTO client VALUES (1,'ENI Service','7bis Avenue Jacques Cartier','44800','Saint-Herblain','Formation Informatique'),
						    (2,'Guerin Peintures','365 route de Vannes','44400','Orvault','Peinture en batiment'),
						    (3,'Store Nantais','Forum','44800','Saint-Herblain','Storiste');
