CREATE TABLE 설정_메뉴 (
	id serial,
	cid INT,
	sid INT,
	eid INT,
	group_id INT,
	번호 INT,
	품목코드 INT,
	x INT,
	y INT,
	width INT,
	height INT,
	isdel CHAR(1),
	issync TIMESTAMP,
	PRIMARY KEY (id)
	);