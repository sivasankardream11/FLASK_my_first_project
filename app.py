from flask import Flask 

AI=Flask(__name__)
@AI.route('/wish')
def wish():
    return "hey iam creating my first flask project successfully"
@AI.route('/second')
def second():
    return "sare gani secound yendhi antavu"
if __name__=='__main__':
    AI.run(debug=True,host='192.168.190.82',port=5001)