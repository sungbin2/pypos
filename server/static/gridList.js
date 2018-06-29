

function loaddata() {
    data0 = [];
    var a = 0;
    var week = new Array('일', '월', '화', '수', '목', '금', '토');

    for( i in _data ) {
        data0.push(_data[i]);
    }

    for( i in data0) {

        a = parseInt(data0[i]['총거래액']) / parseInt(data0[i]['영수건수'])
        d = new Date(data0[i]['영업일자']).getDay()

        gridList[i] = {};
        gridList[i].a = data0[i]['영업일자'];
        gridList[i].b = week[d];
        gridList[i].c = 1;
        gridList[i].d1 = data0[i]['총거래액'];
        gridList[i].d2 = data0[i]['총할인액'];
        gridList[i].d3 = data0[i]['실거래액'];
        gridList[i].d4 = data0[i]['판매이익'];
        gridList[i].d5 = data0[i]['세금'];
        gridList[i].d6 = data0[i]['영수건수'];
        gridList[i].d7 = Math.round(a);
        gridList[i].a = data0[i]['영업일자'];
        gridList[i].a = data0[i]['영업일자'];
        gridList[i].a = data0[i]['영업일자'];
        gridList[i].a = data0[i]['영업일자'];


    }

    load()

}