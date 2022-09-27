from flask import Flask, request, render_template

app = Flask("app")

class api:
    #class w is the "write" class, it handles all write statements such as messages and member join events
    class w:
        @staticmethod
        def message(user, content):
            with open("messages.txt", "a") as E:
                E.write(f"\n{user} : {content}")
                E.close()
        
        @staticmethod
        def members(user):
            with open("members.txt", "r") as P:
                if user in P.readlines():
                    return
                else:
                    with open("members.txt", "a") as E:
                        E.write(f"\n{user}")

    #class r is the "read" class, it handles all read statements such as message lists and member lists
    class r:
        @staticmethod
        def message():
            with open("messages.txt", "r") as E:
                return E.read()
        
        @staticmethod
        def members():
            with open("members.txt", "r") as E:
                return E.read()
        

@app.route("/api/messages", methods=["GET", "POST"])
def ret_message():
    if request.method == "GET":
        return api.r.message()
    else:
        return "Invalid method"

@app.route("/api/send", methods=["POST"])
def send_message():
    user = request.headers.get("user")
    content = request.headers.get("content")
    api.w.message(user, content)
    return "hello"

@app.route("/api/join", methods=["POST"])
def join_msg():
    user = request.headers.get("user")
    api.w.members(user)
    api.w.message(user="Server", content=f"{user} has joined the channel")
    
@app.route("/api/members")
def member_list():
    return api.r.members()

app.run(host="0.0.0.0", port=80)