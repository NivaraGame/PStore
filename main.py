import wmi
import psutil
from windows_tools.installed_software import get_installed_software

f = wmi.WMI()


# def list_specific_processes(process_name):
#     processes = []
#
#     for proc in psutil.process_iter(['pid', 'name', 'username']):
#         print(proc)
#         try:
#             if process_name.lower() in proc.info['name'].lower():
#                 processes.append(proc.info)
#         except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#             pass
#
#     return processes
#
#
# if __name__ == "__main__":
#     process_name = "opera"
#     processes = list_specific_processes(process_name)
#     if processes:
#         for proc in processes:
#             print(f"PID: {proc['pid']}, Name: {proc['name']}, User: {proc['username']}")
#     else:
#         print(f"No processes found for: {process_name}")

def unique(list1):
    # initialize a null list
    unique_list = []

    # traverse for all elements
    for x in list1:
        # check if exists in unique_list or not
        if x not in unique_list:
            unique_list.append(x)
    # print list
    return unique_list


installed_soft = unique(get_installed_software())
# for soft in installed_soft:
#     if "opera" in soft["name"].lower():
#         print(soft)

processes = f.Win32_Process()
# for process in processes:
#     print(process)

running_processes = []

for soft in installed_soft:
    for process in processes:
        if soft["name"] in process.Name:
            if process.CommandLine is not None:
                commandLine = process.CommandLine.split('" ')[0].strip('"')
            else:
                commandLine = None
            running_processes.append([process.Name, commandLine])
            # print(process.Name)

running_processes = unique(running_processes)
for process in running_processes:
    print(process, '\n')
# counter = 0
# for proces in processes:
#     for soft in installed_soft:
#         if soft["name"] == proces.Name:
#             counter += 1
# print(counter)


# print(len(processes))
# processes = f.Win32_Process()
# print(processes[0], processes[1])
