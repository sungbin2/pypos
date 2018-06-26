CREATE TABLE 설정_테이블그룹 (
	id serial,
	cid INT,
	sid INT,
	eid INT,
	번호 INT,
	그룹명 TEXT,
	isdel CHAR(1),
	issync TIMESTAMP,
	PRIMARY KEY (id)
	);
