CREATE TABLE 설정_프린터 (
	id serial,
	cid INT,
	sid INT,
	eid INT,
	프린터명 TEXT,
	사용여부 CHAR(1),
	영수증 CHAR(1),
	고객주문서 CHAR(1),
	주방주문서 CHAR(1),
	통신포트 TEXT,
	통신속도 TEXT,
	isdel CHAR(1),
	issync TIMESTAMP,
	PRIMARY KEY (id)
	);