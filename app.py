# se intala boto3 
# se instala flask para conectarse con AWS 
import boto3
from flask import Flask, request, jsonify
import joblib

client = boto3.client("s3")

print('PyCharm')

response = client.list_buckets()


print(response['Buckets'])

## Establece la conexion al servidor 

app = Flask(__name__)
@app.route("/")

def index():
    return "Hi Flask"

@app.route("/predict", methods=["POST"])
def predict():
    request_data = request.get_json()
    ros_valor = request_data["ROS_VALOR_TRANSACCIÓN"]
    tiene_adjunto = request_data["TIENE_ADJUNTO"]
    sector = request_data["SECTOR"]
    entidad = request_data["ENTIDAD"]
    notifico_autoridad = request_data["NOTIFICO_AUTORIDAD"]
    califica_analista = request_data["CALIFICA_ANALISTA"]
    tipo_entidad = request_data["TIPO_ENTIDAD"]
    moneda = request_data["MONEDA"]
    prediction=model.predict([[ros_valor,tiene_adjunto,sector,entidad,notifico_autoridad,califica_analista,tipo_entidad,moneda]])
    model.transform([[ros_valor,tiene_adjunto,sector,entidad,notifico_autoridad,califica_analista,tipo_entidad,moneda]])
    return jsonify({"prediction":prediction.tolist()})


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

s3 = boto3.resource('s3')

s3.meta.client.download_file('mibucket223322223','Model/modelRFC.tar.gz','modelRFC.joblib') 

model = joblib.load('modelRFC.joblib')
