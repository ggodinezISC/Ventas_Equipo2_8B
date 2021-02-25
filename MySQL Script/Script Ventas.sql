create  database ERP;
use ERP;

/*==============================================================*/
/* Table: Clientes                                              */
/*==============================================================*/
create table Clientes
(
   IdCliente            INT AUTO_INCREMENT NOT NULL,
   Nombre          		VARCHAR(100) NOT NULL,
   RazonSocial    		VARCHAR(100) NOT NULL,
   LimiteCredito        FLOAT NOT NULL,
   Rfc              	CHAR(13) NOT NULL,
   Telefono             CHAR(12) NOT NULL,
   Email              	VARCHAR(100) NOT NULL,
   Tipo              	CHAR(1) NOT NULL,
   CONSTRAINT pk_sales_cliente PRIMARY KEY (IdCliente)
);
/*==============================================================*/
/* Table: Asociaciones                                          */
/*==============================================================*/
create table Asociaciones
(
   IdAsociacion         INT AUTO_INCREMENT NOT NULL,
   Nombre          		VARCHAR(100)       NOT NULL,
   Estatus    			CHAR(1)            NOT NULL,
   CONSTRAINT pk_sales_asociacion PRIMARY KEY (IdAsociacion)
);
/*==============================================================*/
/* Table: Miembros                                              */
/*==============================================================*/
create table Miembros
(
   IdCliente           INT 		    NOT NULL,
   IdAsociacion         INT      	NOT NULL,
   Estatus    			CHAR(1)     NOT NULL,
   FechaIncorporacion   DATE        NOT NULL,
   CONSTRAINT pk_sales_miembro PRIMARY KEY (IdCliente,IdAsociacion)
);
/*==============================================================*/
/* Table: Cultivos                                              */
/*==============================================================*/
create table Cultivos
(
   IdCultivo      INT AUTO_INCREMENT NOT NULL,
   Nombre         VARCHAR(100)  	 NOT NULL,
   CostoAsesoria  FLOAT          	 NOT NULL,
   Estatus    	  CHAR(1)       	 NOT NULL,
   CONSTRAINT pk_sales_cultivo PRIMARY KEY (IdCultivo)
);


/*==============================================================*/
/* Creacion de las claves foráneas                              */
/*==============================================================*/
alter table Miembros add constraint IdCliente_Miembro_FK foreign key (IdCliente)
      references Clientes (IdCliente);

alter table Miembros add constraint IdAsociacion_Miembro_FK foreign key (IdAsociacion)
      references Asociaciones (IdAsociacion);
      
/*==============================================================*/
/* Creacion del Usuario para la conexion   y permisos           */
/*==============================================================*/

CREATE USER 'Admin'@'localhost' IDENTIFIED BY 'hola.123';
GRANT ALL PRIVILEGES ON ERP.Clientes TO 'Admin'@'localhost';
GRANT ALL PRIVILEGES ON ERP.Asociaciones TO 'Admin'@'localhost';
GRANT ALL PRIVILEGES ON ERP.Miembros TO 'Admin'@'localhost';
GRANT ALL PRIVILEGES ON ERP.Cultivos TO 'Admin'@'localhost';