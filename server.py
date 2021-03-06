from http.server import HTTPServer, BaseHTTPRequestHandler

from io import BytesIO
import os
import base64
import chardet
import socket
from tensorflow.python.keras.models import model_from_json
import numpy as np
import os,cv2
from tensorflow.python.keras.utils import np_utils
import csv
import json


def EncodeDecode(img):
    #Get the type of encoding the bytes are saved in from the chardet.detect call
    #chardet returns a dictonary
    #ex: {'encoding': 'ascii', 'confidence': 1.0, 'language': ''}
    encode_type = list(chardet.detect(img).values())
    
    if encode_type[0] == None:
        pass
    #once encoding is decode back into a string
    else:
        img = img.decode(encode_type[0])
        img = img.encode('utf-8')
    #encode once again in base64 to ensure all information is received as a base64 byte str
    
    img = base64.b64encode(img)

    return img

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        sumplant = []
        #obtain the length of the message being sent
        content_length = int(self.headers['Content-Length'])
        
        #parse the information
        body = self.rfile.read(content_length)
        
        #confirm successful request
        self.send_response(200)
        self.end_headers()
        
        #determine what type of encoding the file is in by calling
        #EncodeDecode to obtain ensure encoding is base64
        body = EncodeDecode(body)

        #decode the file and download into pwd
        decode = base64.b64decode(body)
        output_file = open("new_aloe.jpg", "wb")
        output_file.write(decode)
        output_file.close()


        NETp = '../MeaKanu'
        Best_weightsp = 'Best-weights-PLANT'
        #'NewOrchBestPLANT'
        data_listp = []
        print(type(cv2.imread('./new_aloe.jpg')))
        input_imgp =cv2.imread('./new_aloe.jpg')
        input_imgp_resize=cv2.resize(input_imgp,(224,224))
        data_listp.append(input_imgp_resize)
        img_datap = np.array(data_listp)
        img_datap = img_datap.astype('float32')
        img_datap = img_datap/255
        #print (img_datap.shape)
        json_filep = open('./' + 'model.json', 'r')
        loaded_model_json = json_filep.read()
        json_filep.close()
        modelp = model_from_json(loaded_model_json)
        # load weights into new model
        modelp.load_weights('./' + Best_weightsp +'.hdf5')
        # evaluate loaded model on test data
        modelp.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        ##### IMPORTANT: OUTPUT ALL ##########
        outputp = modelp.predict(img_datap)
        for i in range(0,100): 
            sumplant.append(sum(outputp[:,i]))
        else:
            for i in range(0,100): 
                sumplant.append(0)
        ###########################################################################
                numbTILES = 1
                FINAL =[]
                ClassPlantPred =[]
                PlantPredClass=[]
                TilesPlant=[]
                Z=[]

        for j in range(1,6):
            ClassPlantPred.append(sorted(set(sumplant))[-j])
            PlantPredClass.append(sumplant.index(ClassPlantPred[j-1]))
            Z = [x for _,x in sorted(zip(ClassPlantPred,PlantPredClass), reverse=True)]

        print(Z)
        #print(ClassPlantPred)
        percentages = []
        for percent in ClassPlantPred:
            percentages.append(round(percent * 100, 2))
        print(percentages)

        data = {
            "PNO": Z,
            "Percents" : percentages
        }
        
        json_string = json.dumps(data)
        print(json_string)
        self.wfile.write(json_string.encode('utf-8'))
        
        
        #self.send_response(200, "Success")
        #self.end_headers()


httpd = HTTPServer(('localhost', 8080), SimpleHTTPRequestHandler)
httpd.serve_forever()