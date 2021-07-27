from flask import Flask, jsonify
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class FibonacciBackend(Resource):

    def get(self, sequenceOfFibNumbers):
        return jsonify({
            sequenceOfFibNumbers : [
                self.fibIterative(i) for i in range(1, sequenceOfFibNumbers+1) 
            ]
        })
    
    def fibIterative(self, n):
        fib = [0,1]
        for i in range(2, n+2):
            fib.append(fib[i-1]+fib[i-2])
        res = fib[n-1]
        n = 0
        return res

class FactorialBackend(Resource):
    
    def get(self, sequenceOfFactNumbers):
        return jsonify({
            sequenceOfFactNumbers : [
                self.factorialIterative(i) for i in range(1, sequenceOfFactNumbers+1)
            ]
        })
    
    def factorialIterative(self, n):
        res = 1
        for i in range(1, n+1):
            cur = res * i
            res = cur
        return res

api.add_resource(FibonacciBackend, "/fib/<int:sequenceOfFibNumbers>")
api.add_resource(FactorialBackend, "/fact/<int:sequenceOfFactNumbers>")

if __name__ == '__main__':
    
    app.run(
        debug=True,
        host='localhost',
        port='8080'
    )
