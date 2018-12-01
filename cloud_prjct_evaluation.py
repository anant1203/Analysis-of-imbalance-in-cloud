#Import libraries to read the data and plot the graphs.
#Library pandas - Used to read the dataset and store as dataframes.
#Library matplotlib - Used to plot graphs selecting certain fields from dataset.
#Library CSV - Used to create .csv file after sorting the dataset.
#Library plotly - Used to create heapmaps from the data set.

import pandas
import matplotlib.pyplot as matplot
import csv
import plotly
import plotly.plotly as ploty
import plotly.graph_objs as go

#Read 'server_usage.csv' data set and store as dataframe.
df=pandas.read_csv('server_usage.csv')
#Sort the values in 'server_usage.csv' dataset based on 'machine_id' field and store in data list.
data=df.sort_values(['machine_id'], ascending=True)
#Store the list as .csv file.
data.to_csv('serverusage_sorted.csv', index=False)
#Read sorted 'serverusage_sorted.csv' file and store as dataframe.
df1=pandas.read_csv('serverusage_sorted.csv')
#Read the first element of the file.
df1['CPU_UTIL'][0]

#Plot 2D graph for CPU Utilization using matplotlib.
#Set graph title.
matplot.title("Machine CPU UTILZATION")
#Set X-axis label.
matplot.xlabel("Machine ID")
#Set Y-axis label.
matplot.ylabel("CPU Utilized")
#plot graph taking 'machine_id' as Xaxis and 'CPU_UTIL' as Yaxis.
matplot.plot(df1.machine_id,df1.CPU_UTIL)
#Show the plotted graph.
matplot.show()

#Plot 2D graph for Memory Utilization using matplotlib.
#Set graph title.
matplot.title("Machine Memory UTILZATION")
#Set X-axis label.
matplot.xlabel("Machine ID")
#Set Y-axis label.
matplot.ylabel("Memory Utilized")
#plot graph taking 'machine_id' as Xaxis and 'MEM_UTIL' as Yaxis.
matplot.plot(df1.machine_id,df1.MEM_UTIL)
#Show the plotted graph.
matplot.show()

#Use online plotly service and generate Heatmaps for CPU Utilization.
#Logging in with credentials to plotly.
plotly.tools.set_credentials_file(username='Srujana', api_key='2bct8zpyWFfaFfWGudZM')
#Generate Heat map trace using plotly graph object taking 'CPU_UTIL' as Zaxis, 'timestamp' as Xaxis, 'machine_id' as Yaxis.
trace = go.Heatmap(z=df1.CPU_UTIL,
                   x=df1.timestamp,
                   y=df1.machine_id)
#Store the trace in 'data' list
data=[trace]
#Using iplot method in plotly library, display the heatmap.
ploty.iplot(data, filename='labelled-heatmap')

#HeatMap for Memory Utilization.
#Generate Heat map trace using plotly graph object taking 'MEM_UTIL' as Zaxis, 'timestamp' as Xaxis, 'machine_id' as Yaxis.
trace = go.Heatmap(z=df1.MEM_UTIL,
                   x=df1.timestamp,
                   y=df1.machine_id)
#Store the trace in 'data' list
data=[trace]
#Using iplot method in plotly library, display the heatmap.
ploty.iplot(data, filename='labelled-heatmap')

#Graph for CPU request for each job.
#Read 'batch_task.csv' dataset and store as data frame.
df2=pandas.read_csv('batch_task.csv')
#Set title of the graph.
matplot.title("CPU REQ/BATCHJOB")
#Set label to Xaxis
matplot.xlabel("numbers of CPU request (average per task)")
#Set label to Yaxis
matplot.ylabel("no of jobs")
#Use 'semilogx' method to convert Xaxis values to exponential of 10 and store them.
cpureq=(matplot.semilogx(df2.CPU_REQ))
#Plot the graph using converted cpu requests as Xaxis and job_id as Yaxis.
matplot.plot(cpureq,df2.job_id)
#Show the plotted graph.
matplot.show()

