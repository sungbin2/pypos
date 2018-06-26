CREATE TABLE 상품_분류 (
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