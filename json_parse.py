# import json
# import time

# with open('test_2.json', 'r', encoding='utf-8') as fr:
#     data = json.load(fr)

# current_date = str(time.localtime()[0]) + '.' + str(time.localtime()[1]) + '.' + str(time.localtime()[2])
# data['date'].insert(0, current_date)
# comment = 'huangqimin123'
# data['comment'].insert(0, comment)

# with open('test_2.json', 'w', encoding='utf-8') as fr:
#     json.dump(data, fr, indent=3, ensure_ascii=False)



@app.route('/comment', methods=['POST'])
def comment():
    ## backup
    with open('/www/web_app/comment.txt', 'a') as fr:
        fr.write(time.asctime(time.localtime(time.time())) + '\n')
        fr.write(request.form.get('comment') + '\n')
        fr.write('\n')
    with open('/www/web_app/static/json/comment_test.json', 'r', encoding='utf-8') as fr: 
        data = json.load(fr)  
    
    current_date = str(time.localtime()[0]) + '.' + str(time.localtime()[1]) + '.' + str(time.localtime()[2])
    if current_date == data['date'][0]:
        data['comment'][0] += (request.form.get('comment') + '。')
    else:
        data['date'].insert(0, current_date)
        comment = request.form.get('comment') + '。'
        data['comment'].insert(0, comment)
    
    with open('/www/web_app/static/json/comment_test.json', 'w', encoding='utf-8') as fr:
        json.dump(data, fr, indent=3, ensure_ascii=False)
    return render_template('comment.html')
