from matplotlib import pyplot as plt
import base64
from io import BytesIO

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(x, y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(12,5))
    plt.title("Covid Record")
    plt.plot(x, y, label='Confirmed Cases in Millions')
    plt.xticks(rotation=50)
    plt.xlabel('Country')
    plt.ylabel('Confirmed-cases')
    plt.tight_layout()
    graph = get_graph()
    return graph

def get_bar(x, y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,4))
    plt.title("Covid Record")
    plt.bar(x, y, width=0.5)
    plt.xticks(rotation=90)
    plt.xlabel('Country')
    plt.ylabel('Confirmed-cases (In Billion)')
    plt.tight_layout()
    graph = get_graph()
    return graph

def get_pie(cases, type, clrs):
    plt.switch_backend('AGG')
    plt.figure(figsize=(5,4))
    plt.title("India Covid Update")
    plt.pie(cases, labels=type, colors=clrs, autopct='%2.2f%%')
    plt.tight_layout()
    graph = get_graph()
    return graph
