from controllers import *


# routing
app.add_api_route('/', index)
app.add_api_route('/admin', admin)
# app.add_api_route('/index_api', index_api)