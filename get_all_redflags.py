from flask import Flask, jsonify, request
app = Flask(__name__)

red_flags = [{'id':1,'title':'Abuse of Public Funds'}, {'id':2,'title':'Corruption to get a tender'}]

@app.route('/redflags', methods=['GET'])
def returnAll():
    return jsonify({'red_flags':red_flags})

if __name__ == "__main__":
    app.run(debug=True,port=8080)
