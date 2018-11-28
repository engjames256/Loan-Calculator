from flask import Flask, jsonify, request
app = Flask(__name__)

red_flags = [{'id':1,'title':'Abuse of Public Funds'}, {'id':2,'title':'Corruption to get a tender'}]

@app.route('/redflags/<int:id>', methods=['DELETE'])
def removeRedflag(id):
    redflags = [red_flag for red_flag in red_flags if red_flag['id'] == id]
    red_flags.remove (redflags[0])
    return jsonify({'red_flags':red_flags})

if __name__ == "__main__":
    app.run(debug=True,port=8080)
