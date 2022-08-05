import requests
import json
from flask import Flask, render_template , jsonify
from flask_restful import Resource, Api
from flask_mysqldb import MySQL

app = Flask(__name__)
api = Api(app)

#conexion BD
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USERT']='root'
app.config['MYSQL_PASSWORD']='1234'
app.config['MYSQL_DB']='moneda'

conexion = MySQL(app)

@app.route('/monedacambio')

def listar_cur():
    data={}
    try:
        cursor=conexion.connection.cursor()
        sql="select mo_nombre  from moneda m, moneda2 mo where m.mo_id=mo.mo_id and  m.mo_id=2 and mo.mon_mo_id =1 "
        cursor.execute(sql)
        moneda=cursor.fetchall()
        print(moneda)
        data['menaje'] ='exito..'
        data['moneda'] = moneda
    except Exception as ex:
        data['menaje'] ='error..'
    return jsonify(data)

@app.route('/monedacambio/<moneda2>', methods=['GET'])

def bus_moneda(moneda2):
    try:
        #webhooj_url="https://webhook.site/#!/190b8f7b-0998-4f25-926b-4dc71b0ccac1"
        cursor=conexion.connection.cursor()
        sql="SELECT m.mo_nombre as 'moneda 1', v.va_moneda_valor as 'valor moneda 1', mo.mo_nombre as 'moneda 2', va.va_moneda_valor as 'valor moneda 2', v.va_fecha as 'fecha' FROM moneda m inner join moneda2 k on m.mo_id=k.mo_id inner join moneda mo on k.mon_mo_id=mo.mo_id inner join valor v on m.mo_id=v.mo_id inner join valor va on va.mo_id=k.mon_mo_id where k.mo_id = 2  and v.va_fecha=va.va_fecha and mo.mo_nombre ='{0}'".format(moneda2)
        cursor.execute(sql)
        moneda=cursor.fetchall()
        if moneda != None:
            cambio={'DIA 1':moneda[0], 'DIA 2':moneda[1], 'DIA 3':moneda[2], 'DIA 4':moneda[3], 'DIA 5':moneda[4]}
            #r=requests.post(webhooj_url,cambio=json.dumps(cambio),headrs={'Content-Type':'aplication/json'})
            return jsonify({'cambio':cambio,'mensaje':"moneda lista"})
        else:
            return jsonify({'mensaje':"moneda sorry"})
        
    except Exception as ex:
        return jsonify({'mensaje':" sorry"})

@app.route('/monedacambio/<moneda2>/<fecha>', methods=['GET'])

def bus_mone(moneda2,fecha):
    try:
        cursor=conexion.connection.cursor()
        sql="SELECT m.mo_nombre as 'moneda 1', v.va_moneda_valor as 'valor moneda 1', mo.mo_nombre as 'moneda 2', va.va_moneda_valor as 'valor moneda 2', v.va_fecha as 'fecha' FROM moneda m inner join moneda2 k on m.mo_id=k.mo_id inner join moneda mo on k.mon_mo_id=mo.mo_id inner join valor v on m.mo_id=v.mo_id inner join valor va on va.mo_id=k.mon_mo_id where k.mo_id = 2  and v.va_fecha=va.va_fecha and mo.mo_nombre ='{0}' and v.va_fecha='{1}'".format(moneda2, fecha)
        cursor.execute(sql)
        moneda=cursor.fetchone()
        if moneda != None:
            cambio={'DIA 1':moneda[0], 'DIA 2':moneda[1], 'DIA 3':moneda[2], 'DIA 4':moneda[3], 'DIA 5':moneda[4]}
            return jsonify({'cambio':cambio,'mensaje':"moneda lista"})
        else:
            return jsonify({'mensaje':"moneda sorry"})
        
    except Exception as ex:
        return jsonify({'mensaje':" sorry"})



def di_Hola():
    print('27 otra vez')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)