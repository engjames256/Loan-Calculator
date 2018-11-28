from flask import Flask, jsonify, request
app = Flask(__name__)

red_flags = [{'id':1,'title':'Abuse of Public Funds'}, {'id':2,'title':'Corruption to get a tender'}]
@app.route('/redflags/<int:id>', methods=['GET'])
def returnSpecific(title):
    redflags = [red_flag for red_flag in red_flags if red_flag['id'] == id]
    return jsonify({'red_flag':redflags[0]})
 
if __name__ == "__main__":
    app.run(debug=True,port=8080)
