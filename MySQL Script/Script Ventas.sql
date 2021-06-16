create  database ERP;
use ERP;

/*==============================================================*/
/* Table:Productos				             					*/
/*==============================================================*/
create table Productos (
	idProducto int auto_increment  not null,
	nombre varchar(50) not null,
	descripcion varchar(100) not null,
	ingredienteActivo varchar(100) not null,
	bandaToxicologica varchar(80) not null,
	aplicacion varchar(200) not null,
	uso varchar(200) not null,
	estatus char not null,
	idLaboratorio int not null,
	idCategoria int not null,
	CONSTRAINT PK_Productos PRIMARY KEY (idProducto)
);
/*==============================================================*/
/* Table:UnidadesMedida				             				*/
/*==============================================================*/
create table UnidadesMedida (
	idUnidad int  not null,
	nombre varchar(80) not null,
	siglas varchar(20) not null,
	estatus char not null,
	CONSTRAINT PK_UnidadMedida PRIMARY KEY (idUnidad)
);
/*==============================================================*/
/* Table:Empaques				             				    */
/*==============================================================*/
create table Empaques (
	idEmpaque int not null,
	nombre varchar(80) not null,
	capacidad float not null,
	estatus char not null,
	idUnidad int not null,
	CONSTRAINT PK_Empaques PRIMARY KEY (idEmpaque)
);

/*==============================================================*/
/* Table:PresentacionesProducto				             		*/
/*==============================================================*/
create table PresentacionesProducto (
	idPresentacion int auto_increment  not null,
	precioCompra float not null,
	precioVenta float not null,
	puntoReorden float not null,
	idProducto int not null,
	idEmpaque int not null,
	CONSTRAINT PK_PresentacionesProducto PRIMARY KEY (idPresentacion)
);

/*==============================================================*/
/* Table:Ofertas				             					*/
/*==============================================================*/
create table Ofertas (
	idOferta int auto_increment  not null,
	nombre varchar(50) not null,
	descripcion varchar(100) not null,
	porDescuento float not null,
	fechaInicio date not null,
	fechaFin date not null,
	canMinProductos int not null,
	estatus char not null,
	idPresentacion int not null,
	CONSTRAINT PK_Ofertas PRIMARY KEY (idOferta)
);

/*==============================================================*/
/* Table:ExistenciasSucursal				             		*/
/*==============================================================*/

create table ExistenciasSucursal (
	idPresentacion int not null,
	idSucursal int not null,
	cantidad int not null,
	CONSTRAINT PK_ExistenciasSucursal PRIMARY KEY (idPresentacion, idSucursal)
);

/*==============================================================*/
/* Table:Laboratorios			             				    */
/*==============================================================*/
create table Laboratorios (
	idLaboratorio int auto_increment  not null,
	nombre varchar(50) not null,
	origen varchar(30) not null,
	estatus char not null,
	CONSTRAINT PK_Laboratorios PRIMARY KEY (idLaboratorio)
);

/*==============================================================*/
/* Table:Categorias				             				    */
/*==============================================================*/
create table Categorias (
	idCategoria int auto_increment  not null,
	nombre varchar(30) not null,
	estatus char not null,
	CONSTRAINT PK_Categorias PRIMARY KEY (idCategoria)
);

/*==============================================================*/
/* Table:ImagenesProducto							            */
/*==============================================================*/
create table ImagenesProducto (
	idImagen int  not null,
	nombreImagen varchar(100),
	imagen blob not null,
	principal char not null,
	idProducto int not null,
	CONSTRAINT PK_ImagenesProducto PRIMARY KEY (idImagen)
);

/*==============================================================*/
/* Table:Puestos									            */
/*==============================================================*/
Create Table Puestos(
idPuesto int  NOT NULL,
nombre varchar(60) NOT NULL,
salarioMinimo float NOT NULL,
salarioMaximo float NOT NULL,
estatus char NOT NULL,
CONSTRAINT PK_Puestos PRIMARY KEY (idPuesto)
);
/*==============================================================*/
/* Table:Departamentos									        */
/*==============================================================*/
Create Table Departamentos(
idDepartamento int NOT NULL,
nombre varchar(50) NOT NULL,
estatus char NOT NULL,
CONSTRAINT PK_Departamentos PRIMARY KEY (idDepartamento)
);
/*==============================================================*/
/* Table:Turnos											        */
/*==============================================================*/
Create Table Turnos(
idTurno int  NOT NULL,
nombre varchar(20) NOT NULL,
horaInicio date NOT NULL,
horaFin date NOT NULL,
dias varchar(30) NOT NULL,
CONSTRAINT PK_Turnos PRIMARY KEY (idTurno)
);


/*==============================================================*/
/* Table:Empleados											    */
/*==============================================================*/
Create Table Empleados(
idEmpleado int auto_increment NOT NULL,
Nombre varchar(30) NOT NULL,
apellidoPaterno varchar(30) NOT NULL,
apellidoMaterno varchar(30) NOT NULL,
sexo char NOT NULL,
fechaNacimiento date NOT NULL,
curp varchar(20) NOT NULL,
estadoCivil varchar(20) NOT NULL,
fechaContratacion date NOT NULL,
salarioDiario float NOT NULL,
nss varchar(10) NOT NULL,
diasVacaciones int NOT NULL,
diasPermiso int NOT NULL,
fotografia VARCHAR(100) NOT NULL,
direccion varchar(80) NOT NULL,
colonia varchar(50) NOT NULL,
codigoPostal varchar(5) NOT NULL,
escolaridad varchar(80) NOT NULL,
especialidad varchar(100) NOT NULL,
email varchar(100) NOT NULL,
passwor varchar(20) NOT NULL,
tipo varchar(10) NOT NULL,
estatus char NOT NULL,
idDepartamento int NOT NULL,
idPuesto int NOT NULL,
idCiudad int NOT NULL,
idSucursal int NOT NULL,
idTurno int NOT NULL,
CONSTRAINT PK_Empleados PRIMARY KEY (idEmpleado)
);
/*==============================================================*/
/* Table:Sucursales							             		*/
/*==============================================================*/
create table Sucursales (
	idSucursal int auto_increment not null,
	nombre varchar(50) not null,
	telefono varchar(15) not null,
	direccion varchar(80) not null,
	colonia varchar(50) not null,
	codigoPostal varchar(5) not null,
	presupuesto float not null,
	estatus char not null,
	idCiudad int not null,
	CONSTRAINT PK_Sucursales PRIMARY KEY (idSucursal)
);
/*==============================================================*/
/* Table: Ventas                                    			*/
/*==============================================================*/
create table Ventas(
idVenta int auto_increment not null,
fecha date not null,
subtotal float not null,
iva float not null,
total float not null,
cantPagada float not null,
comentarios varchar(100),
estatus char not null,
tipo char not null,
idCliente int not null,
idSucursal int not null,
idEmpleado int not null,
CONSTRAINT pk_Ventas PRIMARY KEY (idVenta)
);

/*==============================================================*/
/* Table: VentasDetalle                                         */
/*==============================================================*/
create table VentaDetalle(
   idVentaDetalle int auto_increment not null,
   idVenta int not null,
   idPresentación int not null,
   precioVenta float not null,
   cantidad float not null,
   subtotal float not null,
   estatus char not null,
   CONSTRAINT pk_VentaDetalle PRIMARY KEY (idVentaDetalle) 
);
/*==============================================================*/
/* Table: Cobros					                            */
/*==============================================================*/
create table Cobros(
idCobro int auto_increment not null,
fecha date not null,
importe float not null,
idVenta int not null,
estatus char not null,
CONSTRAINT pk_Cobros PRIMARY KEY (idCobro)
);
/*==============================================================*/
/* Table:Envios					             				  	*/
/*==============================================================*/
create table Envios(
idEnvio int auto_increment not null,
fechaInicio date not null,
fechaFin date not null,
idUnidadTransporte int not null,
pesoTotal float not null,
estatus char not null,
CONSTRAINT pk_Envios PRIMARY KEY (idEnvio)
);

/*==============================================================*/
/* Table: DetallesEnvio					                        */
/*==============================================================*/
create table DetallesEnvio(
idEnvio int auto_increment not null,
idVenta int not null,
idDireccion int not null,
fechaEntregaPlaneada date not null,
peso float not null,
estatus char not null,
idContacto int not null,
CONSTRAINT pk_Detalles_Envio PRIMARY KEY (idEnvio,idVenta)
);

create table Historial
(
   IdHistorial          INT AUTO_INCREMENT NOT NULL,
   Nombre          		VARCHAR(100) NOT NULL,
   Email          		VARCHAR(100) NOT NULL,
   CONSTRAINT pk_inicio_cliente PRIMARY KEY (IdHistorial)
);
alter table historial add constraint uq_email_historial unique (Email);
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
   Password             VARCHAR(12) NOT NULL,
   Tipo              	CHAR(1) NOT NULL,
   Estatus              CHAR(1) NOT NULL,
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


/*=================================================================================================================*/
/*=================================================================================================================*/
/*=================================================================================================================*/
/*================================================tablas unidad 2 =================================================*/

/*==============================================================*/
/* Table:Estados											    */
/*==============================================================*/

Create Table Estados(
idEstado int auto_increment NOT NULL,
nombre varchar(60) NOT NULL,
siglas varchar(10) NOT NULL,
estatus char NOT NULL,
CONSTRAINT PK_Estados PRIMARY KEY (idEstado)
);
/*==============================================================*/
/* Table:Ciudades											    */
/*==============================================================*/

Create Table Ciudades(
idCiudad int auto_increment NOT NULL,
idEstado int NOT NULL,
nombre varchar(80) NOT NULL,
estatus char NOT NULL,
CONSTRAINT PK_Ciudades PRIMARY KEY (idCiudad)
);


/*==============================================================*/
/* Table: DireccionesCliente                                   	*/
/*==============================================================*/

create table DireccionesCliente(
idDireccion int auto_increment not null,
idCliente int not null,
idCiudad int not null,
calle varchar(100) not null,
numero varchar(5) not null,
colonia varchar(100) not null,
codigoPostal varchar(5) not null,
tipo char not null,
estatus char not null,
CONSTRAINT pk_Direcciones_Cliente PRIMARY KEY (idDireccion)
);


/*==============================================================*/
/* Table:Mantenimiento			             				    */
/*==============================================================*/

create table Mantenimientos(
idMantenimiento int auto_increment not null,
idUnidadTransporte int not null,
fechaInicio date not null,
fechaFin date not null,
taller varchar(100) not null,
costo float not null,
comentarios varchar(200),
tipo varchar(30) not null,
estatus char not null,
CONSTRAINT pk_Mantenimientos PRIMARY KEY (idMantenimiento)
);


/*==============================================================*/
/* Table: Parcelas				                               	*/
/*==============================================================*/

create table Parcelas(
idParcela int auto_increment not null,
idCliente int not null,
idCultivo int not null,
idDireccion int not null,
extension float not null,
estatus char not null,
CONSTRAINT pk_Parcelas PRIMARY KEY (idParcela)
);


/*==============================================================*/
/* Table: UnidadesTransporte					                */
/*==============================================================*/

create table UnidadesTransporte(
idUnidadTransporte int auto_increment not null,
placas varchar(10) not null,
marca varchar(80) not null,
modelo varchar(80) not null,
anio int not null,
capacidad int not null,
tipo varchar(30) not null,
estatus char not null,
CONSTRAINT pk_UnidadesTransporte PRIMARY KEY (idUnidadTransporte)
);


/*==============================================================*/
/* Table: ContactosCliente						                */
/*==============================================================*/

create table ContactosCliente(
idContacto int auto_increment not null,
idCliente int not null,
nombre varchar(100) not null,
telefono varchar(12) not null,
email varchar(100) not null,
estatus char not null,
CONSTRAINT pk_ContactosCliente PRIMARY KEY (idContacto)
);

/*=================================================================================================================*/
/*=================================================================================================================*/
/*=================================================================================================================*/
/*=================================================================================================================*/
/*=================================================================================================================*/
/*=================================================================================================================*/




/*==============================================================*/
/* Table: OfertasAsociacion                                     */
/*==============================================================*/
create table OfertasAsociacion(
idAsosiacion int not null,
idOferta int not null,
estatus char not null,
CONSTRAINT pk_OfertaAsociacion PRIMARY KEY (idAsosiacion,idOferta)
);

/*==============================================================*/
/* Table: Tripulacion				                            */
/*==============================================================*/
create table Tripulacion(
idEmpleado int not null,
idEnvio int not null,
rol varchar(50) not null,
CONSTRAINT pk_Tripulacion PRIMARY KEY (idEmpleado,idEnvio,rol)
);



/*==============================================================*/
/* Table: Asesorias						                		*/
/*==============================================================*/
create table Asesorias(
idAsesoria int not null,
fecha date not null,
comentarios varchar(200) not null,
estatus char not null,
costo float not null,
idParcela int not null,
idEmpleado int not null, 
idUnidadTransporte int not null,
CONSTRAINT pk_Asesorias PRIMARY KEY (idAsesoria)
);





/*==============================================================*/
/* Table:ProductosProveedor							            */
/*==============================================================*/
create table ProductosProveedor (
	idProveedor int not null,
	idPresentacion int not null,
	diasRetardo int not null,
	precioEstandar float not null,
	precioUltimaCompra float not null,
	cantMinPedir int not null,
	cantMaxPedir int not null,
	CONSTRAINT PK_ProductosProveedor PRIMARY KEY (idProveedor, idPresentacion)
);
/*==============================================================*/
/* Table:PedidoDetalle								            */
/*==============================================================*/
create table PedidoDetalle (
	idPedidoDetalle int  not null,
	cantPedida int not null,
	precioCompra float not null,
	subTotal float not null,
	cantRecibida int not null,
	cantRechazada int not null,
	cantAceptada float not null,
	idPedido int not null,
	idPresentacion int not null,
	CONSTRAINT PK_PedidoDetalle PRIMARY KEY (idPedidoDetalle)
);
/*==============================================================*/
/* Table:Pedidos									            */
/*==============================================================*/
create table Pedidos (
	idPedido int  not null,
	fechaRegistro date not null,
	fechaRecepcion date not null,
	totalPagar float not null,
	cantidadPagada float not null,
	estatus char not null,
	idProveedor int not null,
	idSucursal int not null,
	idEmpleado int not null,
	CONSTRAINT PK_Pedidos PRIMARY KEY (idPedido)
);
/*==============================================================*/
/* Table:ContactosProveedor							            */
/*==============================================================*/
create table ContactosProveedor (
	idContacto int  not null,
	nombre varchar(80) not null,
	telefono varchar(12) not null,
	email varchar(100) not null,
	idProveedor int not null,
	CONSTRAINT PK_ContactosProveedor PRIMARY KEY (idContacto)
);
/*==============================================================*/
/* Table:Proveedores								            */
/*==============================================================*/
create table Proveedores (
	idProveedor int  not null,
	nombre varchar(80) not null,
	telefono varchar(12) not null,
	email varchar(100) not null,
	direccion varchar(80) not null,
	colonia varchar(50) not null,
	codigoPostal varchar(5) not null,
	CONSTRAINT PK_Proveedores PRIMARY KEY (idProveedor)
);
/*==============================================================*/
/* Table:CuentasProveedor							            */
/*==============================================================*/
create table CuentasProveedor (
	idCuentaProveedor int  not null,
	idProveedor int not null,
	noCuenta varchar(10) not null,
	banco varchar(30) not null,
	referenciaBancaria varchar(20) not null,
	CONSTRAINT PK_CuentasProveedor PRIMARY KEY (idCuentaProveedor)
);
/*==============================================================*/
/* Table:Pagos										            */
/*==============================================================*/
create table Pagos (
	idPago int not null,
	fecha date not null,
	importe float not null,
	idPedido int not null,
	idFormaPago int not null,
	CONSTRAINT PK_Pagos PRIMARY KEY (idPago)
);
/*==============================================================*/
/* Table:FormasPago									            */
/*==============================================================*/
Create Table FormasPago(
idFormaPago int  NOT NULL,
nombre varchar(50) NOT NULL,
estatus char NOT NULL,
CONSTRAINT PK_FormasPago PRIMARY KEY (idFormaPago)
);

/*==============================================================*/
/* Table:Periodos									            */
/*==============================================================*/
Create Table Periodos(
idPeriodo int  NOT NULL,
nombre varchar(50) NOT NULL,
fechaInicio date NOT NULL,
fechaFin date NOT NULL,
estatus char NOT NULL,
CONSTRAINT PK_Periodos PRIMARY KEY (idPeriodo)
);
/*==============================================================*/
/* Table:Deducciones								            */
/*==============================================================*/
Create Table Deducciones(
idDeduccion int NOT NULL,
nombre varchar(30) NOT NULL,
descripcion varchar(80) NOT NULL,
porcentaje float NOT NULL,
CONSTRAINT PK_Deducciones PRIMARY KEY (idDeduccion) 
);
/*==============================================================*/
/* Table:Percepciones								            */
/*==============================================================*/
Create Table Percepciones(
idPercepcion int  NOT NULL,
nombre varchar(30) NOT NULL,
descripcion varchar(80) NOT NULL,
diasPagar int NOT NULL,
CONSTRAINT PK_Percepciones PRIMARY KEY (idPercepcion)
);



/*==============================================================*/
/* Table:Asistencias											*/
/*==============================================================*/
Create Table Asistencias(
idAsistencia int  NOT NULL,
fecha date NOT NULL,
horaEntrada date NOT NULL,
horaSalida date NOT NULL,
dia varchar(10) NOT NULL,
idEmpleado int NOT NULL,
CONSTRAINT PK_Asistencias PRIMARY KEY (idAsistencia)
);
/*==============================================================*/
/* Table:HistorialPuetos										*/
/*==============================================================*/
Create Table HistorialPuestos(
idEmpleado int  NOT NULL,
idPuesto int NOT NULL,
idDepartamento int NOT NULL,
fechaInicio date NOT NULL,
fechaFin date NOT NULL,
CONSTRAINT PK_HistorialPuestos PRIMARY KEY (idEmpleado,idPuesto,idDepartamento,fechaInicio)
);
/*==============================================================*/
/* Table:AusenciaJustificadas								    */
/*==============================================================*/
Create Table AusenciasJustificadas(
idAusencia int  NOT NULL,
fechaSolicitud date NOT NULL,
fechaInicio date NOT NULL,
fechaFin date NOT NULL,
tipo char NOT NULL,
idEmpleadoSolicita int NOT NULL,
idEmpleadoAutoriza int NOT NULL,
evidencia  blob NOT NULL,
estatus char NOT NULL,
motivo varchar(100) NOT NULL,
CONSTRAINT PK_AusenciaJustificadas PRIMARY KEY (idAusencia)
);
/*==============================================================*/
/* Table:DocumentacionEmpleado								    */
/*==============================================================*/
Create Table DocumentacionEmpleado(
idDocumento int  NOT NULL,
nombreDocumento varchar(80) NOT NULL,
fechaEntrega date NOT NULL,
documento blob NOT NULL,
idEmpleado int NOT NULL,
CONSTRAINT PK_DocumentacionEmpleado PRIMARY KEY (idDocumento)
);
/*==============================================================*/
/* Table:Nominas										        */
/*==============================================================*/
Create Table Nominas(
idNomina int  NOT NULL,
fechaElaboracion date NOT NULL,
fechaPago date NOT NULL,
subtotal float NOT NULL,
retenciones float NOT NULL,
total float NOT NULL,
diasTrabajados int NOT NULL,
estatus char NOT NULL,
idEmpleado int NOT NULL,
idFormaPago int NOT NULL,
idPeriodo int NOT NULL,
CONSTRAINT PK_Nominas PRIMARY KEY (idNomina)
);
/*==============================================================*/
/* Table:NominasDeducciones								        */
/*==============================================================*/
Create Table NominasDeducciones(
idNomina int NOT NULL,
idDeduccion int  NOT NULL,
importe float NOT NULL,
CONSTRAINT PK_NominaDeducciones PRIMARY KEY (idNomina,idDeduccion)
);
/*==============================================================*/
/* Table:NominasPercepciones							        */
/*==============================================================*/
Create Table NominasPercepciones(
idNomina int NOT NULL,
idPercepcion int NOT NULL,
importe float NOT NULL,
CONSTRAINT PK_NominasPercepciones PRIMARY KEY (idNomina,idPercepcion)
);
/*==============================================================*/
/* Creacion de las claves foráneas                              */
/*==============================================================*/
alter table Miembros add constraint IdCliente_Miembro_FK foreign key (IdCliente)
      references Clientes (IdCliente);

alter table Miembros add constraint IdAsociacion_Miembro_FK foreign key (IdAsociacion)
      references Asociaciones (IdAsociacion);

/*======================================================================================================*/
/*======================================================================================================*/
/*=====================================RESTRICCIONES UNIDAD 2===========================================*/
/*======================================================================================================*/
alter table DireccionesCliente add constraint FK_DC_Cliente foreign key (IdCliente)
      references Clientes (IdCliente);

alter table DireccionesCliente add constraint FK_DC_Ciudad foreign key (idCiudad)
      references Ciudades (idCiudad);

alter table Ciudades add constraint FK_Ciudades_Estado foreign key (idEstado)
      references Estados (idEstado);

alter table Parcelas add constraint FK_Parcelas_Cliente foreign key (IdCliente)
      references Clientes (IdCliente);

alter table Parcelas add constraint FK_Parcelas_Cultivos foreign key (IdCultivo)
      references Cultivos (IdCultivo);

alter table Parcelas add constraint FK_Parcelas_DC foreign key (idDireccion)
      references DireccionesCliente (idDireccion);

alter table ContactosCliente add constraint FK_CC_Cliente foreign key (IdCliente)
      references Clientes (IdCliente);

alter table Mantenimientos add constraint FK_Mantenimientos_UniTransporte foreign key (idUnidadTransporte)
      references UnidadesTransporte (idUnidadTransporte);

alter table Empleados add constraint FK_Sucursal_Emple foreign key (idSucursal)
      references Sucursales (idSucursal);


/*======================================================================================================*/
/*======================================================================================================*/
/*======================================================================================================*/

/*==============================================================*/
/* Creacion del Usuario para la conexion   y permisos           */
/*==============================================================*/

CREATE USER 'Admin'@'localhost' IDENTIFIED BY 'hola.123';
GRANT ALL PRIVILEGES ON ERP.Clientes TO 'Admin'@'localhost';
GRANT ALL PRIVILEGES ON ERP.Asociaciones TO 'Admin'@'localhost';
GRANT ALL PRIVILEGES ON ERP.Miembros TO 'Admin'@'localhost';
GRANT ALL PRIVILEGES ON ERP.Cultivos TO 'Admin'@'localhost';

/*======================================================================================================*/
/*======================================================================================================*/
/*=====================================INSTRUCCIONES UNIDAD 2===========================================*/
/*======================================================================================================*/
GRANT ALL PRIVILEGES ON ERP.DireccionesCliente TO 'Admin'@'localhost';
GRANT ALL PRIVILEGES ON ERP.Parcelas TO 'Admin'@'localhost';
GRANT ALL PRIVILEGES ON ERP.ContactosCliente TO 'Admin'@'localhost';
GRANT ALL PRIVILEGES ON ERP.Mantenimientos TO 'Admin'@'localhost';
GRANT ALL PRIVILEGES ON ERP.UnidadesTransporte TO 'Admin'@'localhost';
GRANT ALL PRIVILEGES ON ERP.Ciudades TO 'Admin'@'localhost';
GRANT ALL PRIVILEGES ON ERP.Estados TO 'Admin'@'localhost';
GRANT ALL PRIVILEGES ON ERP.Historial TO 'Admin'@'localhost';

/*======================================================================================================*/
/*=====================================INSTRUCCIONES UNIDAD 3===========================================*/
/*======================================================================================================*/
GRANT ALL PRIVILEGES ON ERP.Ventas TO 'Admin'@'localhost';
GRANT ALL PRIVILEGES ON ERP.VentaDetalle TO 'Admin'@'localhost';
GRANT ALL PRIVILEGES ON ERP.Envios TO 'Admin'@'localhost';
GRANT ALL PRIVILEGES ON ERP.Cobros TO 'Admin'@'localhost';
GRANT ALL PRIVILEGES ON ERP.DetallesEnvio TO 'Admin'@'localhost';
GRANT ALL PRIVILEGES ON ERP.Sucursales TO 'Admin'@'localhost';
GRANT ALL PRIVILEGES ON ERP.Empleados TO 'Admin'@'localhost';
/*======================================================================================================*/
/*=====================================INSTRUCCIONES UNIDAD 3 implementación de ventas===========================================*/
/*======================================================================================================*/
GRANT ALL PRIVILEGES ON ERP.Productos TO 'Admin'@'localhost';
GRANT ALL PRIVILEGES ON ERP.Ofertas TO 'Admin'@'localhost';
GRANT ALL PRIVILEGES ON ERP.PresentacionesProducto TO 'Admin'@'localhost';
GRANT ALL PRIVILEGES ON ERP.ExistenciasSucursal TO 'Admin'@'localhost';
GRANT ALL PRIVILEGES ON ERP.Laboratorios TO 'Admin'@'localhost';
GRANT ALL PRIVILEGES ON ERP.Categorias TO 'Admin'@'localhost';
GRANT ALL PRIVILEGES ON ERP.UnidadesMedida TO 'Admin'@'localhost';
GRANT ALL PRIVILEGES ON ERP.Empaques TO 'Admin'@'localhost';
GRANT ALL PRIVILEGES ON ERP.FormasPago TO 'Admin'@'localhost';

/*======================================================================================================*/
/*======================================================================================================*/
/*======================================================================================================*/
/*======================================================================================================*/
insert into Sucursales 
(idSucursal, nombre, telefono , direccion ,colonia ,codigoPostal ,presupuesto ,estatus, idCiudad) 
values (1,"Sucursal 1","3511234567","Azucena1","LindaVista1","12345",1000.0,"A",1);
insert into Sucursales 
(idSucursal, nombre, telefono , direccion ,colonia ,codigoPostal ,presupuesto ,estatus, idCiudad) 
values (2,"Sucursal 2","3511234502","Azucena2","LindaVista2","12346",1000.0,"A",2);
insert into Sucursales 
(idSucursal, nombre, telefono , direccion ,colonia ,codigoPostal ,presupuesto ,estatus, idCiudad) 
values (3,"Sucursal 3","3511234503","Azucena3","LindaVista3","12347",1000.0,"A",3);
insert into Sucursales 
(idSucursal, nombre, telefono , direccion ,colonia ,codigoPostal ,presupuesto ,estatus, idCiudad) 
values (4,"Sucursal 4","3511234504","Azucena4","LindaVista4","12348",1000.0,"A",4);
insert into Sucursales 
(idSucursal, nombre, telefono , direccion ,colonia ,codigoPostal ,presupuesto ,estatus, idCiudad) 
values (5,"Sucursal 5","3511234505","Azucena5","LindaVista5","12349",1000.0,"A",5);


insert into Empleados 
(idEmpleado, nombre, apellidoPaterno , apellidoMaterno , sexo, fechaNacimiento , curp, estadoCivil, 
fechaContratacion, salarioDiario, nss, diasVacaciones, diasPermiso, fotografia, direccion , colonia, 
codigoPostal, escolaridad, especialidad, email,passwor, tipo, estatus, idDepartamento, idPuesto, idCiudad, 
idSucursal,idTurno ) 
values (1,"Empleado 1","AP1","AM1","H","1999-01-10","ABCD123456HMNDLL01","S","2020-05-11",200,
"ADBC123456",10,10,"1.jpg","direccion1 #1","colonia 1","12345","Licenciatura","Redes",
"email1@gmail.com", "PASS1","Vendedor","A",1,1,1,1,1);

insert into Empleados 
(idEmpleado, nombre, apellidoPaterno , apellidoMaterno , sexo, fechaNacimiento , curp, estadoCivil, 
fechaContratacion, salarioDiario, nss, diasVacaciones, diasPermiso, fotografia, direccion , colonia, 
codigoPostal, escolaridad, especialidad, email,passwor, tipo, estatus, idDepartamento, idPuesto, idCiudad, 
idSucursal,idTurno ) 
values (2,"Empleado 2","AP2","AM2","H","1999-01-10","ABCD123456HMNDLL02","S","2020-05-11",200,
"ADBC123456",10,10,"2.jpg","direccion2 #2","colonia 2","22345","Licenciatura","Redes",
"email2@gmail.com", "PASS2","Vendedor","A",1,1,2,1,1);

insert into Empleados 
(idEmpleado, nombre, apellidoPaterno , apellidoMaterno , sexo, fechaNacimiento , curp, estadoCivil, 
fechaContratacion, salarioDiario, nss, diasVacaciones, diasPermiso, fotografia, direccion , colonia, 
codigoPostal, escolaridad, especialidad, email,passwor, tipo, estatus, idDepartamento, idPuesto, idCiudad, 
idSucursal,idTurno ) 
values (3,"Empleado 3","AP3","AM3","H","1999-01-10","ABCD123456HMNDLL03","S","2020-05-11",200,
"ADBC123456",10,10,"3.jpg","direccion3 #3","colonia 3","32345","Licenciatura","Redes",
"email3@gmail.com", "PASS3","Vendedor","A",1,1,3,1,1);

insert into Empleados 
(idEmpleado, nombre, apellidoPaterno , apellidoMaterno , sexo, fechaNacimiento , curp, estadoCivil, 
fechaContratacion, salarioDiario, nss, diasVacaciones, diasPermiso, fotografia, direccion , colonia, 
codigoPostal, escolaridad, especialidad, email,passwor, tipo, estatus, idDepartamento, idPuesto, idCiudad, 
idSucursal,idTurno ) 
values (4,"Empleado 4","AP4","AM4","H","1999-01-10","ABCD123456HMNDLL04","S","2020-05-11",200,
"ADBC123456",10,10,"4.jpg","direccion3 #3","colonia 4","42345","Licenciatura","Redes",
"email4@gmail.com", "PASS4","Vendedor","A",1,1,4,1,1);

insert into Empleados 
(idEmpleado, nombre, apellidoPaterno , apellidoMaterno , sexo, fechaNacimiento , curp, estadoCivil, 
fechaContratacion, salarioDiario, nss, diasVacaciones, diasPermiso, fotografia, direccion , colonia, 
codigoPostal, escolaridad, especialidad, email,passwor, tipo, estatus, idDepartamento, idPuesto, idCiudad, 
idSucursal,idTurno ) 
values (5,"Empleado 5","AP5","AM5","H","1999-01-10","ABCD123456HMNDLL05","S","2020-05-11",200,
"ADBC123456",10,10,"5.jpg","direccion3 #3","colonia 5","52345","Licenciatura","Redes",
"email5@gmail.com", "PASS5","Vendedor","A",1,1,5,1,1);
insert into Empleados 
(idEmpleado, nombre, apellidoPaterno , apellidoMaterno , sexo, fechaNacimiento , curp, estadoCivil, 
fechaContratacion, salarioDiario, nss, diasVacaciones, diasPermiso, fotografia, direccion , colonia, 
codigoPostal, escolaridad, especialidad, email,passwor, tipo, estatus, idDepartamento, idPuesto, idCiudad, 
idSucursal,idTurno ) 
values (6,"Empleado 6","AP6","AM6","H","1999-01-10","ABCD123456HMNDLL06","S","2020-05-11",200,
"ADBC883456",10,10,"6.jpg","direccion3 #3","colonia 6","52345","Licenciatura","Redes",
"email6@gmail.com", "PASS6","Vendedor","A",1,1,5,2,1);
select * from VentaDetalle;


INSERT INTO CATEGORIAS (idCategoria,nombre, estatus) Values(1,"Herbicidas","A");
INSERT INTO CATEGORIAS (idCategoria,nombre, estatus) Values(2,"Fertilizantes","A");
INSERT INTO CATEGORIAS (idCategoria,nombre, estatus) Values(3,"Fungicidas","A");
INSERT INTO CATEGORIAS (idCategoria,nombre, estatus) Values(4,"Acaricidas","A");
INSERT INTO CATEGORIAS (idCategoria,nombre, estatus) Values(5,"Insecticidas","A");

INSERT INTO Laboratorios (idLaboratorio, nombre, origen, estatus) VALUES (1,"ABSSA","México","A");
INSERT INTO Laboratorios (idLaboratorio, nombre, origen, estatus) VALUES (2,"AMVAC","México","A");
INSERT INTO Laboratorios (idLaboratorio, nombre, origen, estatus) VALUES (3,"BIOIBÉRICA","México","A");
INSERT INTO Laboratorios (idLaboratorio, nombre, origen, estatus) VALUES (4,"CAMPO LIMPIO","México","A");
INSERT INTO Laboratorios (idLaboratorio, nombre, origen, estatus) VALUES (5,"COMPO","México","A");
INSERT INTO Laboratorios (idLaboratorio, nombre, origen, estatus) VALUES (6,"FORCROP","México","A");
INSERT INTO Laboratorios (idLaboratorio, nombre, origen, estatus) VALUES (7,"GREENHOW","México","A");
INSERT INTO Laboratorios (idLaboratorio, nombre, origen, estatus) VALUES (8,"IQC","México","A");
INSERT INTO Laboratorios (idLaboratorio, nombre, origen, estatus) VALUES (9,"BAYER","México","A");
INSERT INTO Laboratorios (idLaboratorio, nombre, origen, estatus) VALUES (10,"GENOMA LAB","México","A");

INSERT INTO PRODUCTOS (idProducto,nombre,descripcion,ingredienteActivo,bandaToxicologica,aplicacion,uso,estatus,idLaboratorio,idCategoria) 
VALUES (1,"Paraquat","Herbicida Líquido","Endotal amina", "Rojo", "Se aplica sobre las hojas o tallos de la hierba mala", "Combate las malas hierbas y las gramíneas en los cultivos de soja, maní, arroz y otras leguminosas de semilla grande",'D',1,1);
INSERT INTO PRODUCTOS (idProducto,nombre,descripcion,ingredienteActivo,bandaToxicologica,aplicacion,uso,estatus,idLaboratorio,idCategoria) 
VALUES (2,"Bromoxynil","Herbicida Líquido","Diquat", "Rojo", "Se aplica sobre las hojas o tallos de la hierba mala", "Combate las malas hierbas y las gramíneas en los cultivos de soja, maní, arroz y otras leguminosas de semilla grande",'D',2,1);
INSERT INTO PRODUCTOS (idProducto,nombre,descripcion,ingredienteActivo,bandaToxicologica,aplicacion,uso,estatus,idLaboratorio,idCategoria) 
VALUES (3,"Diclofop-metil","Herbicida Líquido","Propanil", "Amarillo", "Se aplica sobre las hojas o tallos de la hierba mala", "Combate las malas hierbas y las gramíneas en los cultivos de soja, maní, arroz y otras leguminosas de semilla grande",'D',3,1);
INSERT INTO PRODUCTOS (idProducto,nombre,descripcion,ingredienteActivo,bandaToxicologica,aplicacion,uso,estatus,idLaboratorio,idCategoria) 
VALUES (4,"Sal sódica","Herbicida Líquido","Glufosinato", "Amarillo", "Se aplica sobre las hojas o tallos de la hierba mala", "Combate las malas hierbas y las gramíneas en los cultivos de soja, maní, arroz y otras leguminosas de semilla grande",'D',4,1);
INSERT INTO PRODUCTOS (idProducto,nombre,descripcion,ingredienteActivo,bandaToxicologica,aplicacion,uso,estatus,idLaboratorio,idCategoria) 
VALUES (5,"Glifosato","Herbicida Líquido","Sulfometuron-metil", "Verde", "Se aplica sobre las hojas o tallos de la hierba mala", "Combate las malas hierbas y las gramíneas en los cultivos de soja, maní, arroz y otras leguminosas de semilla grande",'D',5,1);
INSERT INTO PRODUCTOS (idProducto,nombre,descripcion,ingredienteActivo,bandaToxicologica,aplicacion,uso,estatus,idLaboratorio,idCategoria) 
VALUES (6,"Aidrina","Insecticida Líquido","HHDN Octalene", "Verde", "Se aplica sobre las tierra", "Combate los insectos del suelo",'D',1,5);
INSERT INTO PRODUCTOS (idProducto,nombre,descripcion,ingredienteActivo,bandaToxicologica,aplicacion,uso,estatus,idLaboratorio,idCategoria) 
VALUES (7,"Carboxina","Fungicida Líquido","D-735 DCMO Vitavax", "Amarillo", "Se aplica sobre las hojas o tallos de la hierba mala", "Combate el carbón de la cebada, avena, trigo y plantones",'D',2,3);
INSERT INTO PRODUCTOS (idProducto,nombre,descripcion,ingredienteActivo,bandaToxicologica,aplicacion,uso,estatus,idLaboratorio,idCategoria) 
VALUES (8,"Apache","Acaricida Líquido","Abamectina", "Verde", "Se aplica sobre las hojas para eliminar acaros", "Combate los acaros en hojas y semillas",'D',3,4);
INSERT INTO PRODUCTOS (idProducto,nombre,descripcion,ingredienteActivo,bandaToxicologica,aplicacion,uso,estatus,idLaboratorio,idCategoria) 
VALUES (9,"Cal dolomítica","Fertilizante en polvo","Magnesio", "Rojo", "Se aplica sobre las semillas o raices", "Permite que las semillas y raices crezcan grandes y fuertes",'D',4,2);
INSERT INTO PRODUCTOS (idProducto,nombre,descripcion,ingredienteActivo,bandaToxicologica,aplicacion,uso,estatus,idLaboratorio,idCategoria) 
VALUES (10,"Cal agrícola","Fertilizane en polvo"," Piedra Caliza", "Verde", "Se aplica sobre las semillas o raices", "Permite que las semillas y raices crezcan grandes y fuertes",'D',5,2);

INSERT INTO UnidadesMedida (idUnidad,nombre,siglas,estatus)
values(1,"Litros","L","A");
INSERT INTO UnidadesMedida (idUnidad,nombre,siglas,estatus)
values(2,"Kilogramos","KG","A");
INSERT INTO UnidadesMedida (idUnidad,nombre,siglas,estatus)
values(3,"Toneladas","TON","A");

INSERT INTO Empaques (idEmpaque,nombre,capacidad,estatus,idUnidad)
VALUES (1,"Botella de Plástico","1","A",1);
INSERT INTO Empaques (idEmpaque,nombre,capacidad,estatus,idUnidad)
VALUES (2,"Bulto","50","A",2);
INSERT INTO Empaques (idEmpaque,nombre,capacidad,estatus,idUnidad)
VALUES (3,"Bulto","20","A",2);
INSERT INTO Empaques (idEmpaque,nombre,capacidad,estatus,idUnidad)
VALUES (4,"Mayoreo","1","A",3);
INSERT INTO Empaques (idEmpaque,nombre,capacidad,estatus,idUnidad)
VALUES (5,"Mayoreo","1000","A",1);

INSERT INTO PresentacionesProducto(idPresentacion,precioCompra,precioVenta,puntoReorden,idProducto,idEmpaque)
VALUES(1,100,150,5,1,1);
INSERT INTO PresentacionesProducto(idPresentacion,precioCompra,precioVenta,puntoReorden,idProducto,idEmpaque)
VALUES(2,100,160,5,2,1);
INSERT INTO PresentacionesProducto(idPresentacion,precioCompra,precioVenta,puntoReorden,idProducto,idEmpaque)
VALUES(3,90,170,5,3,1);
INSERT INTO PresentacionesProducto(idPresentacion,precioCompra,precioVenta,puntoReorden,idProducto,idEmpaque)
VALUES(4,110,180,5,4,1);
INSERT INTO PresentacionesProducto(idPresentacion,precioCompra,precioVenta,puntoReorden,idProducto,idEmpaque)
VALUES(5,100,150,5,5,1);
INSERT INTO PresentacionesProducto(idPresentacion,precioCompra,precioVenta,puntoReorden,idProducto,idEmpaque)
VALUES(6,120,170,5,6,1);
INSERT INTO PresentacionesProducto(idPresentacion,precioCompra,precioVenta,puntoReorden,idProducto,idEmpaque)
VALUES(7,80,120,5,7,1);
INSERT INTO PresentacionesProducto(idPresentacion,precioCompra,precioVenta,puntoReorden,idProducto,idEmpaque)
VALUES(8,100,200,5,8,1);
INSERT INTO PresentacionesProducto(idPresentacion,precioCompra,precioVenta,puntoReorden,idProducto,idEmpaque)
VALUES(9,100,200,5,9,2);
INSERT INTO PresentacionesProducto(idPresentacion,precioCompra,precioVenta,puntoReorden,idProducto,idEmpaque)
VALUES(10,70,150,5,9,3);
INSERT INTO PresentacionesProducto(idPresentacion,precioCompra,precioVenta,puntoReorden,idProducto,idEmpaque)
VALUES(11,100,200,5,10,2);
INSERT INTO PresentacionesProducto(idPresentacion,precioCompra,precioVenta,puntoReorden,idProducto,idEmpaque)
VALUES(12,80,160,5,10,3);
INSERT INTO PresentacionesProducto(idPresentacion,precioCompra,precioVenta,puntoReorden,idProducto,idEmpaque)
VALUES(13,4000,8000,5,9,4);
INSERT INTO PresentacionesProducto(idPresentacion,precioCompra,precioVenta,puntoReorden,idProducto,idEmpaque)
VALUES(14,100000,150000,5,1,5);

INSERT INTO Ofertas(idOferta,nombre,descripcion,porDescuento,fechaInicio,fechaFin,canMinProductos,estatus,idPresentacion)
			VALUES (1,"Oferta Mayoreo por Tonelada","10% de descuento por tonelada",10,"2021-05-27","2021-06-14",1,"A",13);
INSERT INTO Ofertas(idOferta,nombre,descripcion,porDescuento,fechaInicio,fechaFin,canMinProductos,estatus,idPresentacion)
			VALUES (2,"Mayoreo por Mil Litros","12% de descuento por cada mil litros",12,"2021-06-27","2021-06-14",1,"A",14);

INSERT INTO ExistenciasSucursal(idPresentacion, idSucursal,cantidad) VALUES (1,1,15);
INSERT INTO ExistenciasSucursal(idPresentacion, idSucursal,cantidad) VALUES (2,1,15);
INSERT INTO ExistenciasSucursal(idPresentacion, idSucursal,cantidad) VALUES (3,2,15);
INSERT INTO ExistenciasSucursal(idPresentacion, idSucursal,cantidad) VALUES (4,2,15);
INSERT INTO ExistenciasSucursal(idPresentacion, idSucursal,cantidad) VALUES (5,3,15);
INSERT INTO ExistenciasSucursal(idPresentacion, idSucursal,cantidad) VALUES (6,3,15);
INSERT INTO ExistenciasSucursal(idPresentacion, idSucursal,cantidad) VALUES (7,4,15);
INSERT INTO ExistenciasSucursal(idPresentacion, idSucursal,cantidad) VALUES (8,4,15);
INSERT INTO ExistenciasSucursal(idPresentacion, idSucursal,cantidad) VALUES (9,5,15);
INSERT INTO ExistenciasSucursal(idPresentacion, idSucursal,cantidad) VALUES (10,5,15);
INSERT INTO ExistenciasSucursal(idPresentacion, idSucursal,cantidad) VALUES (11,6,10);
INSERT INTO ExistenciasSucursal(idPresentacion, idSucursal,cantidad) VALUES (12,6,10);
INSERT INTO ExistenciasSucursal(idPresentacion, idSucursal,cantidad) VALUES (13,7,7);
INSERT INTO ExistenciasSucursal(idPresentacion, idSucursal,cantidad) VALUES (14,7,7);

INSERT INTO ExistenciasSucursal(idPresentacion, idSucursal,cantidad) VALUES (10,1,15);
INSERT INTO ExistenciasSucursal(idPresentacion, idSucursal,cantidad) VALUES (11,1,10);
INSERT INTO ExistenciasSucursal(idPresentacion, idSucursal,cantidad) VALUES (12,1,10);
INSERT INTO ExistenciasSucursal(idPresentacion, idSucursal,cantidad) VALUES (13,1,7);
INSERT INTO ExistenciasSucursal(idPresentacion, idSucursal,cantidad) VALUES (14,1,7);

INSERT INTO FormasPago(idFormaPago,nombre,estatus) VALUES(1,"Efectivo","A");
INSERT INTO FormasPago(idFormaPago,nombre,estatus) VALUES(2,"Tarjeta","A");
INSERT INTO FormasPago(idFormaPago,nombre,estatus) VALUES(3,"Transferencia","A");

INSERT INTO Clientes (IdCliente,Nombre,RazonSocial,LimiteCredito,Rfc,Telefono,Email,Password,Tipo,Estatus) 
VALUES (1,"Guillermo Godinez Guillen","Sindicato",500.0,"GOGG112233RFC","3931041660","memogodi@gmail.com","Hola.123#$","A","A");

INSERT INTO Clientes (IdCliente,Nombre,RazonSocial,LimiteCredito,Rfc,Telefono,Email,Password,Tipo,Estatus) 
VALUES (2,"Ernesto Perez","Sindicato",1500.0,"PTER112233RFC","3931041671","neto@gmail.com","Hola.123#$","A","A");

INSERT INTO Clientes (IdCliente,Nombre,RazonSocial,LimiteCredito,Rfc,Telefono,Email,Password,Tipo,Estatus) 
VALUES (3,"Mauro Castellanos Diaz","Sindicato",500.0,"CDMA112233RFC","3931041771","mauro@gmail.com","Hola.123#$","A","A");

CREATE PROCEDURE Procedimiento_Venta_Detalle (IN idVentaDETalle int, idVENta int, idPREsentacion int,precioVENta float,CANtidad float,SUBtotal float,ESTatus char)
	insert into VentaDetalle
	(idVentaDetalle, idVenta, idPresentacion,precioVenta,cantidad,subtotal,estatus)
	values(idVentaDETalle, idVENta, idPREsentacion,precioVENta,CANtidad,SUBtotal,ESTatus)
;

SHOW TABLES FROM ERP;
