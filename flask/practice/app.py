from flask import Flask, jsonify, request

app = Flask(__name__)

my_post={}

@app.route("/post", methods=["POST"])
def add_post():
    post_data= request.get_json()
    if 'user' in post_data and 'caption' in post_data:
        post_id = len(my_post)+1
        post_data['post_id']=post_id
        my_post[post_id]= post_data
        return jsonify({"mes":"post created successfully"})
    else:
        return jsonify({'error':"invalid post data"})



@app.route("/post/<int:post_id>", methods=["DELETE"])
def delete_post(post_id):
    if post_id in my_post:
        del my_post[post_id]
        return jsonify({"mes":f"post with ID {post_id} has deleted"})
    else:
        return jsonify({"error":"unable to delete post"})
       

    
@app.route("/post", methods=["GET"])
def get_posts():
    return jsonify(list(my_post.values()))





if __name__ == '__main__':
    app.run()
