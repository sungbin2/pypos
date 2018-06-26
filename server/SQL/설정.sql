CREATE TABLE 설정 (
	id serial,
	cid INT,
	sid INT,
	eid INT,
	번호 INT,
	키 TEXT,
	값 TEXT,
	isdel CHAR(1),
	issync TIMESTAMP,
	PRIMARY KEY (id)
	);