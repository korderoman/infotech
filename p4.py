from flask import Flask,request
import os

#hacer pip install Flask

app=Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    query=request.args.__len__()
    pares=[]
    if query== 0:
        return "Debe agregar una ruta como: ?D:/programacion/proyectos/xertica/banbif/chatbot_banbif"
    else:
        ruta:str=request.args.get('ruta')
       
        lista=os.listdir(ruta)
        for archivo in lista:
            location="{}/{}".format(ruta,archivo)
            tamano=os.path.getsize(location)
            pares.append((tamano,archivo))
            #print(location)
        pares.sort(key=lambda s: s[0])

        for par in pares:
            print(par)
    return {"lista": pares}
if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')

