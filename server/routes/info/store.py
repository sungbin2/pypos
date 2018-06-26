from server.main_ import app, orm, c
from dateutil import parser

form_types = [
    {'tag': None, 'name': '가게명', 'type': 'input', },
    {'tag': None, 'name': '대표자', 'type': 'input', },
    {'tag': '사업자번호', 'name': '사업자번호', 'type': 'input', },
    {'tag': None, 'name': '우편번호', 'type': 'input', },
    {'tag': None, 'name': '주소', 'type': 'input', },
    {'tag': None, 'name': '상세주소', 'type': 'input', },
    {'tag': None, 'name': '이메일', 'type': 'input', },
    {'tag': None, 'name': '휴대폰', 'type': 'input', },
    {'tag': None, 'name': '전화', 'type': 'input', },
    {'tag': None, 'name': '팩스', 'type': 'input', },
    {'tag': None, 'name': '가맹여부', 'type': 'radio', 'l': ['단독점포', '직영점', '가맹점'], },
    {'tag': None, 'name': '업종', 'type': 'input', },
    {'tag': None, 'name': '개점일', 'type': 'date', },
    {'tag': None, 'name': '폐점일', 'type': 'date', },
]


def _get_store(shop_id):
    with orm.session_scope() as ss:  # type:c.typeof_Session
        only = ss.query(orm.정보_가게) \
            .filter_by(i=shop_id) \
            .one()
        return c.OBJ_cp(only)


@app.route('/info/store')
def _info_store_():
    return c.redirect(c.url_for('_info_store', shop_id=c.session['shop_id']))


@app.route('/info/store/<int:shop_id>', methods=['GET', 'POST', 'PUT'])
def _info_store(shop_id):
    if c.is_GET():
        if c.is_json():
            return c.jsonify(_get_store(shop_id).for_json())
        else:
            return c.display(item=_get_store(shop_id),
                             form_types=form_types,
                             no=shop_id)
    elif c.is_POST() or c.is_PUT():
        with orm.session_scope() as ss:  # type:c.typeof_Session
            only = ss.query(orm.정보_가게) \
                .filter_by(i=shop_id) \
                .one()
            for k, v in c.data_POST().items():
                if getattr(only, k) != v:
                    print(k, 'is changed')
                    if k in ['개점일', '폐점일']:
                        try:
                            setattr(only, k, parser.parse(v))
                        except:
                            setattr(only, k, None)
                    else:
                        setattr(only, k, v)
            only.issync = None
        return 'modified'
