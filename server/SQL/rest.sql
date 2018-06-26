CREATE TABLE 관리_대리점 (
	id serial,
	대리점명 TEXT,
	대표자 TEXT,
	사업자번호 TEXT,
	우편번호 TEXT,
	주소 TEXT,
	상세주소 TEXT,
	이메일 TEXT,
	휴대폰 TEXT,
	전화 TEXT,
	팩스 TEXT,
	isdel CHAR(1),
	issync TIMESTAMP,
	PRIMARY KEY (id)
	);

CREATE TABLE 관리_대리점가게 (
	id serial,
	대리점id INT,
	가게id INT,
	isdel CHAR(1),
	issync TIMESTAMP,
	PRIMARY KEY (id)
	);

CREATE TABLE 상품_분류p (
	id serial,
	cid INT,
	sid INT,
	eid INT,
	pid INT,
	분류명 TEXT,
	isdel CHAR(1),
	issync TIMESTAMP,
	PRIMARY KEY (id)
	);

CREATE TABLE 상품_분류pp (
	id serial,
	cid INT,
	sid INT,
	eid INT,
	pid INT,
	분류명 TEXT,
	isdel CHAR(1),
	issync TIMESTAMP,
	PRIMARY KEY (id)
	);

CREATE TABLE 상품_세트_그룹 (
	id serial,
	cid INT,
	sid INT,
	eid INT,
	세트코드 INT,
	순서 INT,
	그룹명 TEXT,
	선택개수 INT,
	isdel CHAR(1),
	issync TIMESTAMP,
	PRIMARY KEY (id)
	);

CREATE TABLE 상품_세트_항목 (
	id serial,
	cid INT,
	sid INT,
	eid INT,
	세트코드 INT,
	그룹코드 INT,
	품목코드 INT,
	가감액 INT,
	isdel CHAR(1),
	issync TIMESTAMP,
	PRIMARY KEY (id)
	);

CREATE TABLE 상품_옵션_그룹 (
	id serial,
	cid INT,
	sid INT,
	eid INT,
	옵션코드 INT,
	순서 INT,
	그룹명 TEXT,
	isdel CHAR(1),
	issync TIMESTAMP,
	PRIMARY KEY (id)
	);

CREATE TABLE 상품_옵션_항목 (
	id serial,
	cid INT,
	sid INT,
	eid INT,
	옵션코드 INT,
	그룹코드 INT,
	순서 INT,
	항목명 TEXT,
	isdel CHAR(1),
	issync TIMESTAMP,
	PRIMARY KEY (id)
	);

CREATE TABLE 상품_품목세트 (
	id serial,
	cid INT,
	sid INT,
	eid INT,
	분류no INT,
	분류nop INT,
	분류nopp INT,
	세트명 TEXT,
	설명 TEXT,
	가격산정방법 TEXT,
	세트가 INT,
	부가세과세 CHAR(1),
	부가세포함 CHAR(1),
	시가여부 CHAR(1),
	바코드 TEXT,
	isdel CHAR(1),
	issync TIMESTAMP,
	PRIMARY KEY (id)
	);

CREATE TABLE 상품_품목옵션 (
	id serial,
	cid INT,
	sid INT,
	eid INT,
	옵션명 TEXT,
	설명 TEXT,
	isdel CHAR(1),
	issync TIMESTAMP,
	PRIMARY KEY (id)
	);