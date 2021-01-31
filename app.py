from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbhomework


# HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    # 여길 채워나가세요!
    # 클라이언트가 준 name, count, contact 가져오기
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    contact_receive = request.form['contact_give']

    # DB에 삽입할 order 만들기
    order = {
        'name': name_receive,
        'count': count_receive,
        'contact': contact_receive
    }

    # orders에 order 저장하기
    db.orders.insert_one(order)

    # 성공여부
    return jsonify({'result': 'success'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    # 여길 채워나가세요!
    orders = list(db.orders.find({}, {'_id': 0}))
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
