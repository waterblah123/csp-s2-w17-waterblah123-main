import plotly as py
import plotly.graph_objs as go

def getdata():
   file = open("./games-civic.csv")
   dataset = []
   for line in file:
      dataset.append(line.strip().split(","))
   return dataset

def extractcolumn(data, colNum):
    col = []
    for row in data[1:]:
        col.append(row[colNum])
    return col

def getuniques(column):
   uniqs = []
   for item in column:
      if item not in uniqs:
         uniqs.append(item)
   return uniqs

def getcountofunique(column, value):
   count = 0
   for item in column:
      if item == value:
         count += 1
   return count

def handleuniquevalues(column, uniqs):
   counts = [] 
   for uni in uniqs:
      counts.append(getcountofunique(column, uni))
   return counts

def chartIt(xaxis, yaxis, name):
   data = [go.Bar(
       x=xaxis,
       y=yaxis
   )]
   py.offline.plot(data, filename=name)

def pieChart(labels, values):
   fig = go.Figure(data=[go.Pie(labels=labels, values=values)])   
   fig.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                  marker=dict(line=dict(color='#000000', width=2)))               
   fig.show()  

def stackedBars():
   fig = go.Figure(data=[
    go.Bar(name='SF Zoo', x=animals, y=[20, 14, 23]),
    go.Bar(name='LA Zoo', x=animals, y=[12, 18, 29])])
   # Change the bar mode
   fig.update_layout(barmode='stack')
   fig.show() 

def main():
   # bar chart
   # data = getdata()
   # col = extractcolumn(data, 3)
   # uniqs = getuniques(col)
   # print(uniqs)
   # counts = handleuniquevalues(col, uniqs)
   # print(counts)
   # chartIt(uniqs, counts, "./games-civic.html") 

   # pie chart
   data = getdata()
   col = extractcolumn(data, 5)
   uniqs = getuniques(col)
   counts = handleuniquevalues(col, uniqs)
   pieChart(uniqs, counts)

main()
