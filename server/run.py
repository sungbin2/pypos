import os
import sys

import werkzeug.serving

sys.path.append(os.getcwd())

framework = 'flask'
_host = '0.0.0.0'
_port = 8080

print('********************************************************')
print(' FRAMEWORK: ', framework)
print(' HOST: ', _host)
print(' PORT: ', _port)
print('********************************************************')


#
#
#
#
@werkzeug.serving.run_with_reloader
def _gevent():
    from server.main_ import app
    from gevent.pywsgi import WSGIServer
    WSGIServer((_host, _port), app).serve_forever()


if framework == 'flask':
    from server.main_ import app

    app.run(host=_host, port=_port)


elif framework == 'gevent':
    _gevent()

elif framework == 'cherrypy':
    from server.main_ import app
    import cherrypy

    cherrypy.tree.graft(app, '/')
    cherrypy.config.update(
        {
            'server.socket_host': _host,
            'server.socket_port': _port,
            'engine.autoreload.on': True,
            'log.screen': True,
        }
    )
    cherrypy.engine.start()
    cherrypy.engine.block()
