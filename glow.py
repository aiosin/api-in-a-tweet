from sanic import *
from sanic.response import *
a = Sanic()

@a.route("/")
async def r(r):
	return text(r.ip)

a.run("0.0.0.0",8080)