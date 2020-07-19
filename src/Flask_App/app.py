from flask import Flask, render_template, request, url_for, redirect
import joblib
import numpy as np
from text_proc import text_process
app = Flask(__name__) #creating flask app with unique name
model = joblib.load(open('NB1.joblib','rb'))
posts = {}           #global variable and 0 is unique post_id

@app.route('/')  #home page of web app (decorator)
def home():
        #return 'Hello World!'
    return render_template('home.jinja2',posts=posts)


@app.route('/review/<int:post_id>')  #/post/0
def post(post_id):
    post = posts.get(post_id)
    if not post: #if post not found or None
        return render_template('404.jinja2', message= f'Post with ID {post_id} was not found.')
    return render_template('post.jinja2',post=post)
    #return f"Post {post['title']}, content:\n\n{post['content']} "

#@app.route('/post/form')
#def form():
#   return render_template('create.jinja2')

@app.route("/review/create", methods=['GET','POST'])
def create():
    #title = request.args.get('title')
    #content = request.args.get('content')
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        post_id = len(posts)
        data =[content]
        inputs =np.asarray(data)
        my_prediction = model.predict(inputs)
        if my_prediction == 1:
            return render_template('404.jinja2')
        else:


            posts[post_id] = {'id':post_id,'title': title, 'content':content}

            return redirect(url_for('post',post_id=post_id))
    return render_template('create.jinja2')


if __name__ == '__main__':
    app.run(debug=True)     #starting the server and gives debug info
