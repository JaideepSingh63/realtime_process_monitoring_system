import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

#function to retrieve the cpu usage
def get_cpu_percent():
    return psutil.cpu_percent()

#function to retrieve the memory usage 
def get_memory_percent():
    return psutil.virtual_memory().percent

#function to retrieve the network utilization 
def get_network_utilization():
    network_io = psutil.net_io_counters()
    network_sent = network_io.bytes_sent
    network_recv = network_io.bytes_recv
    return network_sent,network_recv

#function to retrieve the disk usage 
def get_disk_usage():
    return psutil.disk_usage('/').percent

#function to retrieve the process count 
def get_process_count():
    return len(psutil.pids())

#function to update the cpu plot 
def update_cpu_plot(frame):
    cpu_percent = get_cpu_percent()
    cpu_time.append(frame)
    cpu_data.append(cpu_percent)
    ax_cpu.clear()
    ax_cpu.plot(cpu_time,cpu_data,label='CPU Usage (%) ')
    ax_cpu.legend()

#function to update the memory plot 
def update_memory_plot(frame):
    memory_percent=get_memory_percent()
    memory_time.append(frame)
    memory_data.append(memory_percent)
    ax_memory.clear()
    ax_memory.plot(memory_time,memory_data,label='Memory usage (%)')
    ax_memory.legend()


#function to update the network plot
def update_network_plot(frame):
    network_sent, network_recv = get_network_utilization()
    network_time.append(frame)
    network_sent_data.append(network_sent)
    network_recv_data.append(network_recv)
    ax_network.clear()
    ax_network.plot(network_time,network_sent_data, label='Network Sent (bytes)')
    ax_network.plot(network_time,network_recv_data, label='Network Recieve (bytes)')
    ax_network.legend()

#function to update the disk plot
def update_disk_plot(frame):
    disk_percent = get_disk_usage()
    disk_time.append(frame)
    disk_data.append(disk_percent)
    ax_disk.clear()
    ax_disk.plot(disk_time, disk_data, label='Disk Usage (%)')
    ax_disk.legend()

#function to update the process count plot
def update_process_plot(frame):
    process_count=get_process_count()
    process_time.append(frame)
    process_data.append(process_count)
    ax_process.clear()
    ax_process.plot(process_time, process_data, label='Process Count')
    ax_process.legend()
    
#initialize lists to store data from plotting
cpu_time=[]
cpu_data=[]
memory_time=[]
memory_data=[]
network_time=[]
network_sent_data=[]
network_recv_data=[]
disk_time=[]
disk_data=[]
process_time=[]
process_data=[]

#create figure and axes for each plot
fig_cpu, ax_cpu =plt.subplots()
fig_memory,ax_memory=plt.subplots()
fig_network,ax_network=plt.subplots()
fig_disk,ax_disk=plt.subplots()
fig_process, ax_process=plt.subplots()

#set up plots
plot=[
    (ax_cpu,'CPU Usage (%)',update_cpu_plot),
    (ax_memory,'Memory Usage (%)',update_memory_plot),
    (ax_network,'Network Utilisation (bytes)',update_network_plot),
    (ax_disk,'Disk Usage (%)',update_disk_plot),
    (ax_process,'Process Count',update_process_plot)
]
for ax, title, _ in plot:
    ax.set_xlabel('Time')
    ax.set_ylabel(title)
    ax.set_title(title)

#set animation for each plot 
ani_cpu= FuncAnimation(fig_cpu,update_cpu_plot,frames=np.arange(0,100),interval=1000)
ani_memory= FuncAnimation(fig_memory,update_memory_plot,frames=np.arange(0,100),interval=1000)
ani_network= FuncAnimation(fig_network,update_network_plot,frames=np.arange(0,100),interval=1000)
ani_disk= FuncAnimation(fig_disk,update_disk_plot,frames=np.arange(0,100),interval=1000)
ani_process= FuncAnimation(fig_process,update_process_plot,frames=np.arange(0,100),interval=1000)

#show the plot
plt.show()






    

