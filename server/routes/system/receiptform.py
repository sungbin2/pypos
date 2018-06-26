import pprint

from server.main_ import app, orm, c

pp = pprint.PrettyPrinter(indent=4)


@app.route('/system/receiptform', methods=['GET', 'POST'])
def _system_receiptform():
    shop_id = c.session['shop_id']
    only = c.get_setting_영수증서식(orm, shop_id)

    if c.is_GET():
        if c.is_json():
            return c.jsonify(only.j)
        else:
            return c.display()
    elif c.is_POST():
        with orm.session_scope() as ss:  # type:c.typeof_Session
            next_one = c.newitem_web(orm.setting_영수증서식, c.session)

            _j = c.data_json()
            for k in _j:
                _j[k] = [x for x in _j[k].split(c.EOL) if len(x.strip()) > 0]
                # pp.pprint(_j)

            next_one.j = _j

            ss.add(next_one)
            return 'modified'
