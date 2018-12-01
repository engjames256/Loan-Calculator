from flask import request,jsonify, Flask

app = Flask(__name__)

red_flags = [{'id':1,'title':'Abuse of Public Funds'}, {'id':2,'title':'Corruption to get a tender'}]
@app.route('/api/v1/redflags/<int:id>', methods=['GET'])
def returnSpecific(id):
    redflags = [red_flag for red_flag in red_flags if red_flag['id'] == id]
    return jsonify({'red_flag':redflags[0]})
 
@app.route('/api/v1/redflags', methods=['POST'])
def addRedflag():
    red_flag = {'title': request.json['title']}

    red_flags.append(red_flag)
    return jsonify({'red_flags':red_flags})

@app.route('/api/v1/redflags/<int:id>', methods=['DELETE'])
def removeRedflag(id):
    redflags = [red_flag for red_flag in red_flags if red_flag['id'] == id]
    red_flags.remove(redflags[0])
    return jsonify({'red_flags':red_flags})

@app.route('/api/v1/redflags/<int:id>', methods=['PUT'])
def editSpecific(id):
    redflags = [red_flag for red_flag in red_flags if red_flag['id'] == id]
    redflags[0]['title'] = request.json['title']
    return jsonify({'red_flag':red_flags})

@app.route('/api/v1/redflags', methods=['GET'])
def returnAll():
    return jsonify({'red_flags':red_flags})