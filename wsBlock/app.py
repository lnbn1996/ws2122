# Web Service
from flask import Flask
app = Flask(__name__)


# from OpenSSL import SSL
# context = SSL.Context(SSL.PROTOCOL_TLSv1_2)
# context.use_privatekey_file('key.pem')
# context.use_certificate_file('cer.pem')


@app.route('/', methods= ['GET'])
def hello():
    # print("Hello From Python WS")
    return 'Hello From Python WS'

app.run(port=2212)

if __name__ == '__main__':
	# app.run(port=2122,debug=True)
	app.run(ssl_context='adhoc',port=2122,debug=True)
	# app.run(port=2122, debug=True, ssl_context=context)
	# app.run(ssl_context=('cert.pem', 'key.pem'),port=2122,debug=True)