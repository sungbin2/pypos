CREATE TABLE 정보_회사 (
	id serial,
	cid INT,
	sid INT,
	eid INT,
	회사명 TEXT,
	대표자 TEXT,
	사업자번호 TEXT,
	우편번호 TEXT,
	주소 TEXT,
	상세주소 TEXT,
	이메일 TEXT,
	휴대폰 TEXT,
	전화 TEXT,
	팩스 TEXT,
	isdel CHAR(1),
	issync TIMESTAMP,
	PRIMARY KEY (id)
	);