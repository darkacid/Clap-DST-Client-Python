import socket
import datetime
import pyaudio  
import wave  
chunk = 1024  

#open a wav format music  
f = wave.open(r"slapclap.wav","rb")  
#instantiate PyAudio  
p = pyaudio.PyAudio()  
#open stream  
stream = p.open(format = p.get_format_from_width(f.getsampwidth()),  
                channels = f.getnchannels(),  
                rate = f.getframerate(),  
                output = True)  
#read data  
data = f.readframes(chunk)  
if __name__ == "__main__":
    TCP_IP ='127.0.0.1'
    TCP_PORT=5005
    BUFFER_SIZE=1024
    MESSAGE = "You suck"
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    while data != '':  
        stream.write(data)  
        data = f.readframes(chunk) 
    timeS=datetime.datetime.now()
      
    s.send(MESSAGE)
    data = s.recv(BUFFER_SIZE)
    timeF=datetime.datetime.now()
    timeDelta= timeF-timeS
    print"Time was: "
    print(timeDelta)
    stream.stop_stream()  
    stream.close()  

    #close PyAudio  
    p.terminate()  

    s.close()
    print "received data:", data
