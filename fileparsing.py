import re

def reader(filename):
    with open(filename) as f:
        info_file = open('INFOlog.txt','w')
        debug_file = open('DEBUGlog.txt','w')
        error_file = open('ERRORlog.txt','w')

        lines= f.readlines() 
        
        for line in lines:
            if re.search("INFO",line):
                info_file.writelines(line)
            elif re.search("DEBUG",line):
                debug_file.writelines(line)
            elif re.search("ERROR",line):
                error_file.writelines(line)
        
        
        info_file.close()
        debug_file.close()
        error_file.close()
        f.close()

if __name__ == '__main__':
    reader('log.txt')