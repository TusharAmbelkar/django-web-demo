#!/usr/bin/env python
import os
import sys
import threading

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    
    import visiondemo.external_app as startup
    t1 = threading.Thread(target=startup.run)
    t1.start()
	
    from django.core.management import execute_from_command_line
    t2 = threading.Thread(target=execute_from_command_line,args = (sys.argv,))
    #execute_from_command_line(sys.argv)
    t2.start()
    
