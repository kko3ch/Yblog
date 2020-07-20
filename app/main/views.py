from flask import render_template,request,redirect,url_for,abort
from flask_login import login_required,current_user
from .. requestquote import get_random_quote
from .. import db,photos
from . import main
from . forms import Post_Form,CommentsForm
from ..models import User,Post,Comment,PhotoProfile,PostPhoto

@main.route('/', methods = ["GET","POST"])
def index():
    '''
    function that define route to index page
    '''
    quote = get_random_quote()
    post_list = Post.query.all()
    return render_template('index.html',quote = quote, post_list = post_list)

@main.route('/user/userprofile')
def home():

    username = current_user.username
    render_template('profile.html', username = username)

@main.route('/user/newblog', methods = ["GET","POST"])
def new_post():
    post_form = Post_Form()
    if post_form.validate_on_submit():
        title = post_form.title.data
        author = post_form.author.data
        content = post_form.content.data
        new_post = Post(title=title,author=author,content=content,user_id = current_user.id)
        new_post.save_post()
        return redirect(url_for('main.index'))
    return render_template('newblog.html',post_form = post_form)

@main.route('/post/<post_id>', methods = ["GET","POST"])
def post(post_id):
    comments = Comment.query.filter_by(post_id = post_id).all()
    post = Post.query.filter_by(id = post_id).first()
    comment_form = CommentsForm()
    if comment_form.validate_on_submit():
        alias = comment_form.alias.data
        comment = comment_form.comment.data
        new_comment = Comment(alias = alias,comment = comment,post_id = post_id)
        new_comment.save_comment()
    return render_template('singleblog.html',comment_form = comment_form,comments = comments, post = post,current_user = current_user)

@main.route('/post/delete/<int:post_id>/',methods= ['GET','POST'])
def delete_post(post_id):
    username = current_user.username
    post = Post.query.filter_by(id = post_id).first()
    db.session.delete(post)
    return redirect(url_for('main.profile',post_id = post_id,uname = username,post = post))

@main.route('/user/<uname>/')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    userblogs = Post.query.filter_by(user_id = user.id).all()
    if user is None:
        abort(404)
    return render_template("Profile/profile.html", user = user, userblogs = userblogs,)

@main.route('/user/<uname>/update_pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))
