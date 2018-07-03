from server.main_ import app, orm, c



@app.route('/earnings/day', methods=['GET', ])
def _earnings_day():
    store_id = c.session['store']
    if c.is_GET():

        return c.display(store_id=store_id)
    else:
        return c.display(store_id=store_id)


@app.route('/earnings/day/<int:_id>', methods=['GET'])
def _earnings_day_(_id):
    store_id = c.session['store']
    cnt_days = {}
    cnt_days['상품목록'] = {}
    cnt_days['상품분류'] = {}
    cnt_days['일자별'] = {}

    cnt = 0
    if c.is_GET():
        with orm.session_scope() as ss:  # type:c.typeof_Session
            lst = ss.query(orm.판매_품목) \
                .filter_by(s=store_id) \
                .filter_by(isdel='X') \
                .all()


            for each in lst:

                d = each.d.strftime('%Y-%m-%d')

                if d not in cnt_days['일자별']:
                    cnt_days['일자별'][d] = {'영업일자': d,
                                   '총거래액': 0, '총할인액': 0, '실거래액': 0, '세금': 0, '판매이익': 0, '영수건수' : 0 , '분류별' : {} ,'상품별' : {}}
                cnt_days['일자별'][d]['총거래액'] += each.단가
                cnt_days['일자별'][d]['총할인액'] += each.할인
                cnt_days['일자별'][d]['실거래액'] += each.합계
                cnt_days['일자별'][d]['세금'] += each.세
                cnt_days['일자별'][d]['판매이익'] += (each.공급가 + each.면세)
                cnt_days['일자별'][d]['영수건수'] += 1

                p = str(each.품목pi)


                if p not in cnt_days['일자별'][d]['분류별']:
                    cnt_days['일자별'][d]['분류별'][p] = { '총거래액': 0, '총할인액': 0, '실거래액': 0, '세금': 0, '판매이익': 0, '영수건수' : 0 }

                cnt_days['일자별'][d]['분류별'][p]['총거래액'] += each.단가
                cnt_days['일자별'][d]['분류별'][p]['총할인액'] += each.할인
                cnt_days['일자별'][d]['분류별'][p]['실거래액'] += each.합계
                cnt_days['일자별'][d]['분류별'][p]['세금'] += each.세
                cnt_days['일자별'][d]['분류별'][p]['판매이익'] += (each.공급가 + each.면세)
                cnt_days['일자별'][d]['분류별'][p]['영수건수'] += 1

                s = each.품목i
                if s not in cnt_days['일자별'][d]['상품별']:
                    cnt_days['일자별'][d]['상품별'][s] = { 'ppi' : {}, '총거래액': 0, '총할인액': 0, '실거래액': 0, '세금': 0, '판매이익': 0, '영수건수' : 0 }
                cnt_days['일자별'][d]['상품별'][s]['ppi'] = each.품목pi
                cnt_days['일자별'][d]['상품별'][s]['총거래액'] += each.단가
                cnt_days['일자별'][d]['상품별'][s]['총할인액'] += each.할인
                cnt_days['일자별'][d]['상품별'][s]['실거래액'] += each.합계
                cnt_days['일자별'][d]['상품별'][s]['세금'] += each.세
                cnt_days['일자별'][d]['상품별'][s]['판매이익'] += (each.공급가 + each.면세)
                cnt_days['일자별'][d]['상품별'][s]['영수건수'] += 1


            lst1 = ss.query(orm.상품_품목) \
                .filter_by(s=store_id) \
                .filter_by(isdel='X') \
                .all()

            for each in lst1:
                cnt_days['상품목록'].update({each.i : each.품목명})

            lst2 = ss.query(orm.상품_분류) \
                .filter_by(s=store_id) \
                .filter_by(isdel='X') \
                .all()

            for each in lst2:
                cnt_days['상품분류'].update({each.i: each.분류명})

        print(cnt_days)

        return c.jsonify(cnt_days)
    c.abort(404)


@app.route('/earnings/modal', methods=['GET', ])
def _earnings_modal():
    store_id = c.session['store']
    if c.is_GET():

        return c.display(store_id=store_id)
    else:
        return c.display(store_id=store_id)

@app.route('/earnings/day1', methods=['GET', ])
def _earnings_day1():
    store_id = c.session['store']
    if c.is_GET():

        return c.display(store_id=store_id)
    else:
        return c.display(store_id=store_id)

@app.route('/earnings/day2', methods=['GET', ])
def _earnings_day2():
    store_id = c.session['store']
    if c.is_GET():

        return c.display(store_id=store_id)
    else:
        return c.display(store_id=store_id)


@app.route('/earnings/day3', methods=['GET', ])
def _earnings_day3():
    store_id = c.session['store']
    if c.is_GET():

        return c.display(store_id=store_id)
    else:
        return c.display(store_id=store_id)


@app.route('/earnings/day4', methods=['GET', ])
def _earnings_day4():
    store_id = c.session['store']
    if c.is_GET():

        return c.display(store_id=store_id)
    else:
        return c.display(store_id=store_id)


@app.route('/earnings/day5', methods=['GET', ])
def _earnings_day5():
    store_id = c.session['store']
    if c.is_GET():

        return c.display(store_id=store_id)
    else:
        return c.display(store_id=store_id)


@app.route('/earnings/day6', methods=['GET', ])
def _earnings_day6():
    store_id = c.session['store']
    if c.is_GET():

        return c.display(store_id=store_id)
    else:
        return c.display(store_id=store_id)


@app.route('/earnings/day7', methods=['GET', ])
def _earnings_day7():
    store_id = c.session['store']
    if c.is_GET():

        return c.display(store_id=store_id)
    else:
        return c.display(store_id=store_id)


@app.route('/earnings/day8', methods=['GET', ])
def _earnings_day8():
    store_id = c.session['store']
    if c.is_GET():

        return c.display(store_id=store_id)
    else:
        return c.display(store_id=store_id)


@app.route('/earnings/day9', methods=['GET', ])
def _earnings_day9():
    store_id = c.session['store']
    if c.is_GET():

        return c.display(store_id=store_id)
    else:
        return c.display(store_id=store_id)
