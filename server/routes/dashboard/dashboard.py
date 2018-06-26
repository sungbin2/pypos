from server.main_ import app, c


@app.route('/dashboard', methods=['GET', 'POST'])
def _dashboard():
    if c.is_GET():
        pass
    elif c.is_POST():
        pass

    return c.display()
