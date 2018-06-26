CREATE TABLE 설정_메뉴그룹 (
	id serial,
	cid INT,
	sid INT,
	eid INT,
	번호 INT,
	그룹명 TEXT,
	상하칸 INT,
	좌우칸 INT,
	isdel CHAR(1),
	issync TIMESTAMP,
	PRIMARY KEY (id)
	);