
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
/*==============================================================*/
/* Table: VentasDetalle                                         */
/*==============================================================*/
create table VentaDetalle(
   idVentaDetalle int not null,
   precioVenta float not null,
   cantidad float not null,
   subtotal float not null,
   idVenta int not null,
   CONSTRAINT pk_VentaDetalle PRIMARY KEY (idVentaDetalle) 
);
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
/* Table: Ventas                                    			*/
/*==============================================================*/
create table Ventas(
idVenta int not null,
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
/* Table: DireccionesCliente                                   	*/
/*==============================================================*/
create table DireccionesCliente(
idDireccion int not null,
calle varchar(100) not null,
numero varchar(15) not null,
colonia varchar(100) not null,
codigoPostal varchar(2) not null,
tipo char not null,
idCliente int not null,
idCiudad int not null,
CONSTRAINT pk_Direcciones_Cliente PRIMARY KEY (idDireccion)
);
/*==============================================================*/
/* Table: Parcelas				                               	*/
/*==============================================================*/
create table Parcelas(
idParcela int not null,
extension float not null,
idCliente int not null,
idCultivo int not null,
idDireccion int not null,
CONSTRAINT pk_Parcelas PRIMARY KEY (idParcela)
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
/* Table: Cobro						                            */
/*==============================================================*/
create table Cobro(
idCobro int  not null,
fecha date not null,
importe float not null,
idVenta int not null,
CONSTRAINT pk_Cobros PRIMARY KEY (idCobro)
);
/*==============================================================*/
/* Table: DetallesEnvio					                        */
/*==============================================================*/
create table DetallesEnvio(
idEnvio int not null,
idVenta int not null,
idDireccion int not null,
fechaEntregaPlaneada date not null,
peso float not null,
estatus char not null,
idContacto int not null,
CONSTRAINT pk_Detalles_Envio PRIMARY KEY (idEnvio,idVenta)
);
/*==============================================================*/
/* Table: UnidadesTransporte					                */
/*==============================================================*/
create table UnidadesTransporte(
idUnidadTransporte int not null,
placas varchar(10) not null,
marca varchar(80) not null,
modelo varchar(80) not null,
anio int not null,
capacidad int not null,
tipo varchar(30) not null,
CONSTRAINT pk_UnidadesTransporte PRIMARY KEY (idUnidadTransporte)
);
/*==============================================================*/
/* Table: ContactosCliente						                */
/*==============================================================*/
create table ContactosCliente(
idContacto int not null,
nombre varchar(100) not null,
telefono varchar(12) not null,
email varchar(100) not null,
idCliente int not null,
CONSTRAINT pk_ContactosCliente PRIMARY KEY (idContacto)
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
/* Table:Envios					             				  	*/
/*==============================================================*/
create table Envios(
idEnvio int  not null,
fechaInicio date not null,
fechaFin date not null,
idUnidadTransporte int not null,
pesoTotal float not null,
CONSTRAINT pk_Envios PRIMARY KEY (idEnvio)
);
/*==============================================================*/
/* Table:Mantenimiento			             				    */
/*==============================================================*/
create table Mantenimiento(
idMantenimiento int not null,
fechaInicio date not null,
fechaFin date not null,
taller varchar(100) not null,
costo float not null,
comentarios varchar(200),
tipo varchar(30) not null,
idUnidadTransporte int not null,
CONSTRAINT pk_Mantenimiestos PRIMARY KEY (idMantenimiento)
);

/*==============================================================*/
/* Table:Laboratorios			             				    */
/*==============================================================*/
create table Laboratorios (
	idLaboratorio int  not null,
	nombre varchar(50) not null,
	origen varchar(30) not null,
	estatus char not null,
	CONSTRAINT PK_Laboratorios PRIMARY KEY (idLaboratorio)
);
/*==============================================================*/
/* Table:Categorias				             				    */
/*==============================================================*/
create table Categorias (
	idCategoria int  not null,
	nombre varchar(30) not null,
	estatus char not null,
	CONSTRAINT PK_Categorias PRIMARY KEY (idCategoria)
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
/* Table:Ofertas				             					*/
/*==============================================================*/
create table Ofertas (
	idOferta int  not null,
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
/* Table:Productos				             					*/
/*==============================================================*/
create table Productos (
	idProducto int  not null,
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
/* Table:PresentacionesProducto				             		*/
/*==============================================================*/
create table PresentacionesProducto (
	idPresentacion int  not null,
	precioCompra float not null,
	precioVenta float not null,
	puntoReorden float not null,
	idProducto int not null,
	idEmpaque int not null,
	CONSTRAINT PK_PresentacionesProducto PRIMARY KEY (idPresentacion)
);
/*==============================================================*/
/* Table:ExistenciasSucursal				             		*/
/*==============================================================*/
create table ExistenciasSucursal (
	idPresentacion int not null,
	idSucursal int not null,
	cantidad float not null,
	CONSTRAINT PK_ExistenciasSucursal PRIMARY KEY (idPresentacion, idSucursal)
);
/*==============================================================*/
/* Table:Sucursales							             		*/
/*==============================================================*/
create table Sucursales (
	idSucursal int  not null,
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
/* Table:Estados											    */
/*==============================================================*/
Create Table Estados(
idEstado int  NOT NULL,
nombre varchar(60) NOT NULL,
siglas varchar(10) NOT NULL,
estatus char NOT NULL,
CONSTRAINT PK_Estados PRIMARY KEY (idEstado)
);
/*==============================================================*/
/* Table:Ciudades											    */
/*==============================================================*/
Create Table Ciudades(
idCiudad int  NOT NULL,
nombre varchar(80) NOT NULL,
idEstado int NOT NULL,
estatus char NOT NULL,
CONSTRAINT PK_Ciudades PRIMARY KEY (idCiudad)
);
/*==============================================================*/
/* Table:Empleados											    */
/*==============================================================*/
Create Table Empleados(
idEmpleado int  NOT NULL,
nombre varchar(30) NOT NULL,
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
fotografia blob NOT NULL,
direccion varchar(80) NOT NULL,
colonia varchar(50) NOT NULL,
codigoPostal varchar(5) NOT NULL,
escolaridad varchar(80) NOT NULL,
especialidad varchar(100) NOT NULL,
email varchar(100) NOT NULL,
pass varchar(20) NOT NULL,
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

/*==============================================================*/
/* Creacion del Usuario para la conexion   y permisos           */
/*==============================================================*/

CREATE USER 'Admin'@'localhost' IDENTIFIED BY 'hola.123';
GRANT ALL PRIVILEGES ON ERP.Clientes TO 'Admin'@'localhost';
GRANT ALL PRIVILEGES ON ERP.Asociaciones TO 'Admin'@'localhost';
GRANT ALL PRIVILEGES ON ERP.Miembros TO 'Admin'@'localhost';
GRANT ALL PRIVILEGES ON ERP.Cultivos TO 'Admin'@'localhost';

INSERT INTO Clientes (IdCliente,Nombre,RazonSocial,LimiteCredito,Rfc,Telefono,Email,Password,Tipo,Estatus) 
VALUES (1,"Guillermo Godinez Guillen","Sindicato",500.0,"GOGG112233RFC","3931041660","memogodi@gmail.com","Hola.123#$","A","A");
SHOW TABLES FROM ERP;
Select * from Clientes;