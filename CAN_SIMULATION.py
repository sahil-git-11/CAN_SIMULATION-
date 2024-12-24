import time  #measures time 
import random #for generating random numbers 

class SimpleCANBusSimulator:
    def __init__ (self):
        self.bus_type = "virtual" #indicate that we are using a virtual can bus not a real one 
        self.channel = "vcan0" #virtual channel name 
        self.bitrate = 500000 
        self.allowed_ids = [256,257,258] #these are a unique ids, they help distinguish different ids , am unexpected id is considered as a anomaly 
    def send_message(self,message_id , data) :
        #simulates sending a message to the can bus 
        print(f"[Send] Message sent: ID={message_id}, Data={data}")
    
    def receive_message(self):
        #randomly decides whether a message is received or not 
        if random.choice([True,False]):
            message_id = random.choice(self.allowed_ids + [512]) #invalid id for testing since it is not it the defined id list 
            data = [random.randint(0,255) for _ in range(8)]
            print(f"[Receive] Message received : ID={message_id}, Data={data}")
            return{"id":message_id , "data":data}
        else:
            print("[Receive] No message received")
            return None 
    
    def detect_anomaly(self,message):
        #checks the id of the received message id is present  in the list or not 
        if message['id'] not in self.allowed_ids:
            
            print(f"[ALERT] Anomaly: Unauthorized ID {message['id']}")
            return True 
        
        #checking if the first data byte exceeds the threshold 

        if message['data'][0] > 100 :
            print(f"[Alert] Anomaly: Data out of range - {message}['data'][0]")
            return True
        # No anomaly is detected 
        print("[Detect]) message is normal ")
        return False
    
    def run_simulation(self , simulation_time):
        #starts the simulation \
        print("Starting the simulation :")
        start_time = time.time() # records the start time 

        while time.time() - start_time < simulation_time:
            random_id = random.choice(self.allowed_ids + [512]) # includes an interval for testing\
            random_data = [random.randint(0,255) for _ in range (8) ] #generates a 8 byte random data 
            self.send_message(random_id , random_data)

            # Simulate receiving a message 

            message = self.receive_message()
            if message : # if a message is received check for anomalies
                self.detect_anomaly(message)
 
            time.sleep(0.5) #wait for .5 seconds between cycles 

        print("Simulation complete")


if __name__ == "__main__":
    simulator = SimpleCANBusSimulator()  # Create an instance of the simulator
    simulator.run_simulation(simulation_time=10)  # Run the simulation for 10 seconds
        
    