from lxml import etree
from server.main_ import app, orm, c
from flask import json
from flask import Response

def get_config(orm, store_id):
    with orm.session_scope() as ss:  # type:c.typeof_Session
        only = ss.query(orm.기능설정) \
            .filter_by(s=store_id) \
            .order_by(ss.desc(orm.기능설정.no)) \
            .first()
        return c.OBJ_cp(only)

@app.route('/system/config', methods=['GET','POST'])
def _system_config():
    store_id = c.session['store']
    if c.is_GET():

        return c.display(store_id=store_id)
    else:
        return c.display(store_id=store_id)

    # return c.redirect(c.url_for('_system_config', store_id=c.session['store']))

@app.route('/system/config/<int:store_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def _system_config_(store_id):
    only1 = get_config(orm, store_id)

    if c.is_GET():
        if c.is_json():
            response = Response(
                response= json.dumps(only1.func),
                status=200,
                mimetype='text/plain')

            return response
        else:
            return c.display()
    elif c.is_POST():
        if c.is_json():
            with orm.session_scope() as ss:  # type:c.typeof_Session
                next_one = c.newitem_web1(orm.기능설정, c.session)
                next_one.func = only1.func.copy()
                for each in c.data_POST():
                    next_one.func = c.json.loads(each)

                ss.add(next_one)

                return 'modified'
