CREATE TABLE 정보_직원 (
	id serial,
	cid INT,
	sid INT,
	eid INT,
	직원번호 TEXT,
	직원암호 TEXT,
	직원명 TEXT,
	직무 TEXT,
	재직상태 TEXT,
	입사일 TIMESTAMP,
	퇴사일 TIMESTAMP,
	isdel CHAR(1),
	issync TIMESTAMP,
	PRIMARY KEY (id)
	);
