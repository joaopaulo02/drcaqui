CREATE DATABASE DR_CAQUI_DB;
GO

USE DR_CAQUI_DB;
GO

CREATE TABLE tipoUsuario(
	idTipoUsuario tinyint primary key identity,
	nomeTipo varchar(15) not null unique
);
GO

CREATE TABLE raca(
	idRaca tinyint primary key identity,
	raca varchar(15) not null unique
);
GO

CREATE TABLE mchat(
	idMchat tinyint primary key identity,
	marco varchar(80) not null unique,
	descricao varchar(400) not null 
);
GO

CREATE TABLE endereco(
	idEndereco int primary key identity,
	cidade varchar(40) not null,
	bairro varchar(40) not null,
	rua varchar (100) not null,
	numero smallint not null
);
GO

CREATE TABLE usuario (
	idUsuario int primary key identity,
	idTipoUsuario tinyint foreign key references tipoUsuario(idTipoUsuario),
	"login" varchar(50) not null unique,
	senha varchar(50) not null
);
GO

CREATE TABLE pai(
	idPai int primary key identity,
	idUsuario int foreign key references usuario(idUsuario),
	idEndereco int foreign key references endereco(idEndereco),
	nomePai varchar(50) not null,
	cpfPai varchar(12) not null unique
);
GO

CREATE TABLE mae(
	idMae int primary key identity,
	idUsuario int foreign key references usuario(idUsuario),
	idEndereco int foreign key references endereco(idEndereco),
	nomeMae varchar(50) not null,
	cpfMae varchar(12) not null unique,
	gravidez binary not null,
	zs1 binary not null,
	a53 binary not null,
	b18 binary not null,
	b58 binary not null,
);
GO

CREATE TABLE crianca(
	idCrianca int primary key identity,
	idMae int foreign key references mae(idMae),
	idPai int foreign key references pai(idPai),
	idRaca tinyint foreign key references raca(idRaca),
	nomeCrianca varchar(50) not null,
	dataNascimento date not null,
	cpfCrianca varchar(12) not null unique,
	municipioNascimento varchar(40) not null,
	ortolani binary not null,
	reflexoVermelho binary not null,
	pezinho binary not null,
	triagemAuditiva binary not null,
);
GO

CREATE TABLE nutricao(
	idCrianca int primary key identity,
	idMae int foreign key references mae(idMae),
	suplemento varchar(70) not null
);
GO

CREATE TABLE marcoCrianca(
	idMarcoCrianca int primary key identity,
	idCrianca int foreign key references crianca(idCrianca),
	idMchat tinyint foreign key references mchat(idMchat),
	idadeCrianca smallint not null
);
GO

CREATE TABLE exame(
	idExame int primary key identity,
	idCrianca int foreign key references crianca(idCrianca),
	tituloExame varchar(50) not null,
	descricaoExame varchar(400) not null,
);
GO

CREATE TABLE medAntropometrica(
	idMed int primary key identity,
	idCrianca int foreign key references crianca(idCrianca),
	dataMed date not null,
	idade tinyint not null,
	peso decimal not null,
	estatura decimal not null,
	perimetroCefalico decimal not null,
	imc decimal not null
);
GO



