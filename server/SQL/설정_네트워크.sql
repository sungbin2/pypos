CREATE TABLE 설정_네트워크 (
	id serial,
	cid INT,
	sid INT,
	eid INT,
	기기명 TEXT,
	ip TEXT,
	port TEXT,
	db CHAR(1),
	계산 CHAR(1),
	주문 CHAR(1),
	프린터 CHAR(1),
	isdel CHAR(1),
	issync TIMESTAMP,
	PRIMARY KEY (id)
	);