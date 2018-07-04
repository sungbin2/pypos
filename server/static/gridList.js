

function loaddata() {
    data0 = [];
    var a = 0;var n=0;
    var week = new Array('일', '월', '화', '수', '목', '금', '토');

    for( i in _data['일자별'] ) {
        data0.push(_data['일자별'][i]);
    }

    for( i in data0) {

        n = parseInt(data0[i]['총거래액']) / parseInt(data0[i]['영수건수'])
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
        gridList[i].d7 = Math.round(n);
        gridList[i].k1 = data0[i]['총할인액'];
//        gridList[i].a = data0[i]['영업일자'];
//        gridList[i].a = data0[i]['영업일자'];
//        gridList[i].a = data0[i]['영업일자'];

        for (j in data0[i]['분류별']) {
            gridList[i]['pt'+j] = data0[i]['분류별'][j]['실거래액'];
            gridList[i]['prc'+j] = data0[i]['분류별'][j]['영수건수'];
        }

        for (k in data0[i]['상품별']) {
            gridList1[a] = {};
            gridList1[a].a = data0[i]['영업일자'];
            gridList1[a].ppi = _data['상품분류'][data0[i]['상품별'][k]['ppi']]
            gridList1[a].pi = k
            gridList1[a].pn = _data['상품목록'][k]
            gridList1[a].pc = data0[i]['상품별'][k]['영수건수']
            gridList1[a].pt = data0[i]['상품별'][k]['총거래액']
            gridList1[a].pe = data0[i]['상품별'][k]['총할인액']
            gridList1[a].pr = data0[i]['상품별'][k]['실거래액']

            a++;
        }

    }

}