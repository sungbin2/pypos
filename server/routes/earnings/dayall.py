from server.main_ import app, orm, c



@app.route('/earnings/dayall', methods=['GET', ])
def _earnings_dayall():
    store_id = c.session['store']
    if c.is_GET():

        return c.display(store_id=store_id)
    else:
        return c.display(store_id=store_id)


@app.route('/earnings/dayall/<int:_id>', methods=['GET'])
def _earnings_dayall_(_id):
    store_id = c.session['store']
    cnt_days = {}
    cnt = 0
    if c.is_GET():
        with orm.session_scope() as ss:  # type:c.typeof_Session
            lst = ss.query(orm.판매_품목) \
                .filter_by(isdel='X') \
                .filter(orm.판매_품목.d >= "2018-01-01") \
                .filter(orm.판매_품목.d <= "2018-12-31") \
                .all()

            for each in lst:
                d = each.d.strftime('%Y-%m-%d')
                if d not in cnt_days:
                    cnt_days[d] = {'영업일자': d,
                                   '총거래액': 0, '총할인액': 0, '실거래액': 0, '세금': 0, '판매이익': 0, '영수건수' : 0 }
                cnt_days[d]['총거래액'] += each.단가
                cnt_days[d]['총할인액'] += each.할인
                cnt_days[d]['실거래액'] += each.합계
                cnt_days[d]['세금'] += each.세
                cnt_days[d]['판매이익'] += (each.공급가 + each.면세)
                cnt_days[d]['영수건수'] += 1


        return c.jsonify(cnt_days)
    c.abort(404)

@app.route('/earnings/dayalldetail', methods=['GET', ])
def _earnings_dayalldetail():
    store_id = c.session['store']
    if c.is_GET():

        return c.display(store_id=store_id)
    else:
        return c.display(store_id=store_id)
