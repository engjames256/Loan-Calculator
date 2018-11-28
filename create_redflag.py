from flask import Flask, jsonify, request
app = Flask(__name__)

red_flags = [{'title':'Abuse of Public Funds'}, {'title':'Corruption to get a tender'}]

@app.route('/redflags', methods=['GET','POST'])
def addRedflag():
    red_flag = {'title': request.json['title']}

    red_flags.append(red_flag)
    return jsonify({'red_flags':red_flags})
    
if __name__ == "__main__":
    app.run(debug=True,port=8080)
