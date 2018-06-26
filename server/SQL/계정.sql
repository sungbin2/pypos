CREATE TABLE 계정 (
	id serial,
	cid INT,
	sid INT,
	eid INT,
	아이디 TEXT,
	패스워드 TEXT,
	이름 TEXT,
	이메일 TEXT,
	연락처 TEXT,
	최근접속s TIMESTAMP,
	최근접속c TIMESTAMP,
	isdel CHAR(1),
	issync TIMESTAMP,
	PRIMARY KEY (id)
	);