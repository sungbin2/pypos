CREATE TABLE settings (
	no serial,
	s INT,
	isdel CHAR(1),
	issync TIMESTAMP,
	j jsonb,
	PRIMARY KEY (no)
	);

CREATE TABLE 영업_준비금 (
	no serial,
	s INT,
	a INT,
	d DATE,
	isdel CHAR(1),
	issync TIMESTAMP,
	영업준비금 INT,
	사용직원번호 TEXT,
	PRIMARY KEY (no)
	);

CREATE TABLE 영업_입출금 (
	no serial,
	s INT,
	a INT,
	d DATE,
	isdel CHAR(1),
	issync TIMESTAMP,
	항목 TEXT,
	입금액 INT,
	출금액 INT,
	메모 TEXT,
	사용직원번호 TEXT,
	발생시점 TIMESTAMP,
	PRIMARY KEY (no)
	);

CREATE TABLE 판매_대기명단 (
	no serial,
	s INT,
	a INT,
	d DATE,
	isdel CHAR(1),
	issync TIMESTAMP,
	고객명 TEXT,
	연락처 TEXT,
	인원 TEXT,
	메모 TEXT,
	접수시각 TIMESTAMP,
	처리 CHAR(1),
	PRIMARY KEY (no)
	);

CREATE TABLE 판매_예약명단 (
	no serial,
	s INT,
	a INT,
	d DATE,
	isdel CHAR(1),
	issync TIMESTAMP,
	고객명 TEXT,
	연락처 TEXT,
	인원 TEXT,
	메모 TEXT,
	예약일시 TIMESTAMP,
	처리 CHAR(1),
	PRIMARY KEY (no)
	);

CREATE TABLE 영업_시작마감 (
	no serial,
	s INT,
	a INT,
	d DATE,
	isdel CHAR(1),
	issync TIMESTAMP,
	순서 INT,
	사용직원번호 TEXT,
	시작시간 TIMESTAMP,
	마감시간 TIMESTAMP,
	j jsonb,
	PRIMARY KEY (no)
	);

CREATE TABLE 영업_출퇴근 (
	no serial,
	s INT,
	a INT,
	d DATE,
	isdel CHAR(1),
	issync TIMESTAMP,
	사용직원번호 TEXT,
	출근시간 TIMESTAMP,
	퇴근시간 TIMESTAMP,
	메모 TEXT,
	PRIMARY KEY (no)
	);


CREATE TABLE 회원 (
	no serial,
	s INT,
	isdel CHAR(1),
	issync TIMESTAMP,
	j jsonb,
	이름 TEXT,
	연락처 TEXT,
	PRIMARY KEY (no)
	);


CREATE TABLE 히스토리_동기화_설정 (
	no serial,
	s INT,
	isdel CHAR(1),
	issync TIMESTAMP,
	발생시점 TIMESTAMP,
	항목수 INT,
	PRIMARY KEY (no)
	);

CREATE TABLE 계정 (
	no serial,
	s INT,
	isdel CHAR(1),
	issync TIMESTAMP,
	아이디 TEXT,
	패스워드 TEXT,
	이름 TEXT,
	이메일 TEXT,
	연락처 TEXT,
	최근접속s TIMESTAMP,
	최근접속c TIMESTAMP,
	PRIMARY KEY (no)
	);

CREATE TABLE 상품_분류 (
	no serial,
	s INT,
	isdel CHAR(1),
	issync TIMESTAMP,
	분류명 TEXT,
	parent_no INT,
	PRIMARY KEY (no)
	);

CREATE TABLE 상품_품목 (
	no serial,
	s INT,
	isdel CHAR(1),
	issync TIMESTAMP,
	분류no INT,
	분류nop INT,
	분류nopp INT,
	품목명 TEXT,
	설명 TEXT,
	품목형태 TEXT,
	단가 INT,
	부가세과세 CHAR(1),
	부가세포함 CHAR(1),
	시가여부 CHAR(1),
	옵션j jsonb,
	프린터j jsonb,
	바코드 TEXT,
	PRIMARY KEY (no)
	);

CREATE TABLE 정보_가게 (
	no serial,
	s INT,
	isdel CHAR(1),
	issync TIMESTAMP,
	가게명 TEXT,
	대표자 TEXT,
	사업자번호 TEXT,
	우편번호 TEXT,
	주소 TEXT,
	상세주소 TEXT,
	이메일 TEXT,
	휴대폰 TEXT,
	전화 TEXT,
	팩스 TEXT,
	가맹여부 TEXT,
	업종 TEXT,
	개점일 DATE,
	폐점일 DATE,
	PRIMARY KEY (no)
	);

CREATE TABLE 정보_직원 (
	no serial,
	s INT,
	isdel CHAR(1),
	issync TIMESTAMP,
	직원번호 TEXT,
	직원암호 TEXT,
	직원명 TEXT,
	직무 TEXT,
	재직상태 TEXT,
	입사일 TIMESTAMP,
	퇴사일 TIMESTAMP,
	PRIMARY KEY (no)
	);


CREATE TABLE 돈통사용기록 (
	no serial,
	s INT,
	a INT,
	d DATE,
	isdel CHAR(1),
	issync TIMESTAMP,
	j jsonb,
	발생시각 TIMESTAMP,
	직원 TEXT,
	메모 TEXT,
	PRIMARY KEY (no)
	);
