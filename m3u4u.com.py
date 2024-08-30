import requests
from datetime import datetime

# Funções para executar os links
def execute_link1():
    response = requests.get("http://m3u4u.com/m3u/xe47yz1pd9spv21mn9vq")
    print(f"Link 1 executado com status: {response.status_code} às {datetime.now()}")

def execute_link2():
    response = requests.get("http://m3u4u.com/m3u/j67zn6m4w7fq9rv8yd1w")
    print(f"Link 2 executado com status: {response.status_code} às {datetime.now()}")

def execute_link3():
    response = requests.get("http://m3u4u.com/m3u/5z3endemwjfdzj52yqpk")
    print(f"Link 3 executado com status: {response.status_code} às {datetime.now()}")

# Executar as funções
execute_link1()
execute_link2()
execute_link3()