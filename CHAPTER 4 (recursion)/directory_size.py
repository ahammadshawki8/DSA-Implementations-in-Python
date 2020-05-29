def disk_usage(my_path):
    import os
    
    total=os.path.getsize(my_path)
    if os.path.isdir(my_path):
        for file in os.listdir(my_path):
            child_path=os.path.join(my_path,file)
            total+=os.path.getsize(child_path)

    print("{0:<7}".format(total),my_path)
    return total


if __name__=="__main__":
    print(disk_usage("C:\\Users\\User\\Desktop\\Study_Work\\Python\\5. DataStructures and Algorithms"))
