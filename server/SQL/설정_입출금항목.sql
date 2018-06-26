CREATE TABLE 설정_입출금항목 (
	id serial,
	cid INT,
	sid INT,
	eid INT,
	순서 INT,
	구분 TEXT,
	상세 TEXT,
	isdel CHAR(1),
	issync TIMESTAMP,
	PRIMARY KEY (id)
	);
