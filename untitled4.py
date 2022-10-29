import matplotlib.pyplot as plt
import psutil as p

app_name_list= []
app_name_percentage_list= []
count= 0
app_name_dict= ("")
keymax= max(app_name_dict,key= app_name_dict.get)
keymax= min(app_name_dict,key= app_name_dict.get)
count= count+1
for process in p.process_iter():
       name= process.name()
       cpu_usage= p.cpu_percent()
       print("name:", name, "cpu_usage:",cpu_usage)
       app_name_list.append(name)
       app_name_percentage_list.append(cpu_usage)


plt.figure(figsize=(15,7))   
plt.xlabel("Application")  
plt.ylabel("Usage")
plt.bar(app_name_list,app_name_percentage_list,width= 0.6,
        color=("red","orange","yellow","green","blue","purple"))
plt.show()


                                                           