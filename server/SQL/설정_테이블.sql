CREATE TABLE 설정_테이블 (
	id serial,
	cid INT,
	sid INT,
	eid INT,
	group_id INT,
	번호 INT,
	name TEXT,
	x INT,
	y INT,
	width INT,
	height INT,
	isdel CHAR(1),
	issync TIMESTAMP,
	PRIMARY KEY (id)
	);