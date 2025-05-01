import random
import os
import streamlit

class Number:
    def Generate_Number():
        Ticket_Number = random.randint(1000, 9999)
        print(Ticket_Number)
        
    
    Generate_Number()