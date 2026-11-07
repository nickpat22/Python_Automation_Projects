################################################################
#
# Project Name : Platform Surveillance System
# Description  : Automated System Monitoring and Reporting
# Language     : Python
# Author       : Nikunj Patidar
# Date         : 07/11/2026
#
################################################################


################################################################
#
# Importing Required Libraries
#
################################################################

import psutil
import sys
import os
import time
import schedule


################################################################
#
# Function Name : ProcessScan
# Input         : None
# Output        : List of dictionaries containing process details
# Description   : Fetches information about all running processes,
#                 including PID, name, username, status, CPU usage
#                 and memory utilization.
#
################################################################

def ProcessScan():

    # List to store information about running processes
    listprocess = []

    # Iterate through all currently running processes
    for proc in psutil.process_iter():

        # Fetch basic information about the current process
        info = proc.as_dict(attrs=["pid", "name", "username", "status"])

        # Fetch CPU utilization of the process
        info["cpu_percent"] = proc.cpu_percent(None)

        # Fetch memory utilization of the process
        info["memory_percent"] = proc.memory_percent()

        # Append process information to the list
        listprocess.append(info)

    # Return the list containing all process information
    return listprocess


################################################################
#
# Function Name : PlatformSurvillance
# Input         : Name of Directory
# Output        : Generates a system monitoring log file
# Description   : Collects system information such as CPU usage,
#                 RAM utilization, network statistics and running
#                 processes. Stores the collected information
#                 in a timestamp-based log file.
#
################################################################

def PlatformSurvillance(FolderName):

    Border = "-" * 50

    Ret = False

    # Check whether the specified directory already exists
    Ret = os.path.exists(FolderName)

    if(Ret == True):

        # Verify whether the existing path is a directory
        Ret = os.path.isdir(FolderName)

        if(Ret == False):
            print("Unable to proceed as directory name is existing but it is not a directory")
            return

    else:

        # Create the directory for storing log files
        os.mkdir(FolderName)

        print("Directory for the logfile gets created successfully")

    # Generate the current timestamp
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    # Generate the log file path using the timestamp
    FileName = os.path.join(FolderName, "Platform_%s.log" % timestamp)

    # Open the log file in write mode
    fobj = open(FileName, "w")

    print(f"Log file gets successfully created with name {FileName}")

    # Write the system report header
    fobj.write(Border + "\n")
    fobj.write("---- Platform Surveillance System ----\n")
    fobj.write("Log file gets created at : " + timestamp + "\n")
    fobj.write(Border + "\n\n")

    fobj.write("---------------- System Report -----------------\n")

    ############################################################
    #
    # CPU Information
    #
    ############################################################

    # Fetch and record the number of available CPU cores
    fobj.write("Number of active CPU cores : %s\n" % psutil.cpu_count())

    # Fetch and record overall CPU utilization
    fobj.write("CPU Usage : %s %%\n" % psutil.cpu_percent())

    fobj.write(Border + "\n")

    ############################################################
    #
    # RAM Information
    #
    ############################################################

    # Fetch virtual memory statistics
    memory = psutil.virtual_memory()

    # Record RAM utilization percentage
    fobj.write("RAM Usage : %s %%\n" % memory.percent)

    # Record total installed RAM
    fobj.write("Total RAM available : %s\n" % memory.total)

    fobj.write(Border + "\n")

    ############################################################
    #
    # Network Usage Information
    #
    ############################################################

    # Fetch network input and output statistics
    netobj = psutil.net_io_counters()

    fobj.write("Network Usage Report\n")

    # Record total data sent in MB
    fobj.write("Sent : %.2f MB\n" % (netobj.bytes_sent / (1024 * 1024)))

    # Record total data received in MB
    fobj.write("Receive : %.2f MB\n" % (netobj.bytes_recv / (1024 * 1024)))

    ############################################################
    #
    # Running Process Information
    #
    ############################################################

    # Fetch information about all running processes
    Data = ProcessScan()

    # Write individual process information into the log file
    for info in Data:

        fobj.write("PID : %s\n" % info.get("pid"))
        fobj.write("Name : %s\n" % info.get("name"))
        fobj.write("User Name : %s\n" % info.get("username"))
        fobj.write("Status : %s\n" % info.get("status"))
        fobj.write("CPU usage : %.2f\n" % info.get("cpu_percent"))
        fobj.write("RAM usage : %.2f\n" % info.get("memory_percent"))

        fobj.write(Border + "\n")

    ############################################################
    #
    # Closing the System Report
    #
    ############################################################

    # Write the ending section of the log file
    fobj.write(Border + "\n")
    fobj.write("--------------- End of Log File ----------------\n")
    fobj.write(Border + "\n")

    # Close the log file
    fobj.close()


################################################################
#
# Function Name : main
# Input         : Command-Line Arguments
# Output        : Controls the execution of the program
# Description   : Handles help and usage instructions, accepts
#                 scheduling interval and log directory name,
#                 and starts periodic system monitoring.
#
################################################################

def main():

    Border = "-" * 50

    print(Border)
    print("---- Platform Surveillance System ----")
    print(Border)

    ############################################################
    #
    # Command-Line Help and Usage Handling
    #
    ############################################################

    # Check whether a single command-line argument is provided
    if(len(sys.argv) == 2):

        # Display information about the automation script
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):

            print("This automation script is used to perform ")
            print("1 : It fetches the information of running processes")
            print("2 : It fetches information about primary storage as RAM")
            print("3 : It fetches information about secondary storage as HDD")
            print("4 : It fetches information about the microprocessor")
            print("5 : It gets automatically scheduled periodically")
            print("6 : It maintains all records in log files")
            print("7 : It sends the log files through mail periodically")

        # Display instructions for executing the script
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):

            print("Use the automation script as : ")
            print(f"python {sys.argv[0]} Time_Interval Folder_Name")
            print("Time_Interval : Time in minutes for periodic execution")
            print("Folder_Name : Name of folder for log file creation")

        else:

            print("Unable to proceed as there is no matching argument")
            print("Please use --h or --u flag for getting more details")

    ############################################################
    #
    # Actual Project Execution
    #
    ############################################################

    # Check whether the required two arguments are provided
    elif(len(sys.argv) == 3):

        # Display scheduling information
        print("Scheduler started successfully")
        print("Press Ctrl + C to abort the automation script")

        # Schedule system monitoring at the specified time interval
        schedule.every(int(sys.argv[1])).minutes.do(
            PlatformSurvillance, sys.argv[2]
        )

        # Continuously check and execute pending scheduled tasks
        while True:

            schedule.run_pending()

            # Pause execution for one second
            time.sleep(1)

    else:

        print("Invalid number of arguments")
        print("Unable to proceed as arguments are not matching")
        print("Please use --h or --u flag for getting more details")

    print(Border)
    print("--- Thank you for using our automation System ---")
    print(Border)


################################################################
#
# Starter of the Automation Script
#
################################################################

if __name__ == "__main__":
    main()
