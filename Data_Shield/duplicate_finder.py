################################################################
#
# Project Name : Data Shield
# Description  : Duplicate File Detection and Removal System
# Language     : Python
# Author       : Nikunj Patidar
# Date         : 07/11/2026
#
################################################################

#
# Importing Required Libraries
#

import os
import hashlib


################################################################
#
# Function Name : CalculateChecksum
# Input         : File Name
# Output        : MD5 Checksum of the File
# Description   : Calculates the MD5 checksum of a file by
#                 reading its contents in chunks of 1024 bytes.
#
################################################################

def CalculateChecksum(FileName):

    # Open the file in binary read mode
    with open(FileName, "rb") as fobj:

        # Create an MD5 hash object
        hobj = hashlib.md5()

        # Read the first 1024 bytes from the file
        Buffer = fobj.read(1024)

        # Continue reading until the end of the file
        while(len(Buffer) > 0):

            # Update the checksum using the current buffer
            hobj.update(Buffer)

            # Read the next 1024 bytes
            Buffer = fobj.read(1024)

    # Return the final hexadecimal checksum
    return hobj.hexdigest()


################################################################
#
# Function Name : FindDuplicate
# Input         : Name of Directory
# Output        : Dictionary containing duplicate file groups
# Description   : Traverses the specified directory and its
#                 subdirectories and identifies duplicate files
#                 using their MD5 checksums.
#
################################################################

def FindDuplicate(DirectoryName):

    Ret = False

    # Check whether the specified path exists
    Ret = os.path.exists(DirectoryName)

    if Ret == False:
        print("Path is invalid")
        return

    # Check whether the specified path is a directory
    Ret = os.path.isdir(DirectoryName)

    if Ret == False:
        print("It is not a directory")
        return

    # Dictionary to store files grouped by their checksums
    Duplicate = {}

    # Traverse the directory and all its subdirectories
    for FolderName, SubFolder, FileName in os.walk(DirectoryName):

        # Process each file found in the current directory
        for fname in FileName:

            # Generate the complete file path
            fname = os.path.join(FolderName, fname)

            # Calculate the MD5 checksum of the file
            Checksum = CalculateChecksum(fname)

            # Check whether the checksum already exists
            if Checksum in Duplicate:

                # Add the file to the existing duplicate group
                Duplicate[Checksum].append(fname)

            else:

                # Create a new checksum entry
                Duplicate[Checksum] = [fname]

    # Return the dictionary containing all file groups
    return Duplicate


################################################################
#
# Function Name : DeleteDuplicate
# Input         : Name of Directory
# Output        : Total number of deleted duplicate files
# Description   : Identifies duplicate files and deletes all
#                 duplicate copies while preserving the first
#                 occurrence of each file.
#
################################################################

def DeleteDuplicate(DirectoryName):

    # Find all files grouped by their checksums
    MyDict = FindDuplicate(DirectoryName)

    # Filter only those groups containing duplicate files
    Result = list(filter(lambda x: len(x) > 1, MyDict.values()))

    Count = 0
    TotalDeleted = 0

    # Process each group of duplicate files
    for value in Result:

        for subvalue in value:

            Count = Count + 1

            # Preserve the first file and delete remaining copies
            if(Count > 1):

                os.remove(subvalue)

                TotalDeleted = TotalDeleted + 1

        # Reset counter for the next duplicate group
        Count = 0

    # Display the total number of deleted file
    print("Total deleted files : ", TotalDeleted)


################################################################
#
# Function Name : main
# Input         : None
# Output        : Controls the execution of the program
# Description   : Calls the duplicate deletion function for
#                 the specified directory.
#
################################################################

def main():

    # Directory to be scanned for duplicate files
    DeleteDuplicate("Test")


################################################################
#
# Starter of the Program
#
################################################################

if __name__ == "__main__":
    main()
