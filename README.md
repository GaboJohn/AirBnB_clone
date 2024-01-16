0x00. AirBnB clone - The console

The AirBnB_clone project is a hands-on initiative designed to mimic the core functionalities of the popular AirBnB platform. This endeavor delves deeply into the backend facets of web development, emphasizing robust data management, efficient storage solutions, and user-centric command-line interactions.

Shell works like this in interactive mode:
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

On non_interactive mode: 
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
