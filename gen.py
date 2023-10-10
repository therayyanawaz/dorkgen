import os, time
from colorama import Fore

banner = Fore.YELLOW + """
██████╗░░█████╗░██████╗░██╗░░██╗░██████╗░███████╗███╗░░██╗
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝░██╔════╝████╗░██║
██║░░██║██║░░██║██████╔╝█████═╝░██║░░██╗░█████╗░░██╔██╗██║
██║░░██║██║░░██║██╔══██╗██╔═██╗░██║░░╚██╗██╔══╝░░██║╚████║
██████╔╝╚█████╔╝██║░░██║██║░╚██╗╚██████╔╝███████╗██║░╚███║
╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚══╝
                            By @therayyanawaz
"""

def dork():
    print(banner)
    world = input("Enter your word for the dork : ")
    resultfile = open(f"Dork_Result_{world}.txt", "w")
    resultfile.write(f"""--------------------
dork list :
1. "{world}"
2. intitle:"{world}"
3. intitle:"index of" "{world}"
4. inurl:/{world}
5. filetype:txt "{world}"
6. filetype:db "{world}"
7. filetype:mysql "{world}"
8. filetype:png | "{world}"
9. "{world}" filetype:yml "config/parameters.yml"
10. "{world}" filetype:env
11. "{world}" inurl:"/etc/main.cfg"
12. intitle:"{world}" filetype:pdf
13. intext:"{world}" site:.edu
14. intext:"{world}" site:.gov
15. "{world}" inurl:wp-content
16. "{world}" inurl:wp-admin
17. intitle:"{world}" inurl:admin
18. "{world}" inurl:login
19. "{world}" intext:password
20. intitle:"{world}" intext:username
21. "{world}" inurl:login.php
22. "{world}" intitle:"login"
23. intitle:"{world}" intext:"powered by WordPress"
24. "{world}" intext:"admin" inurl:login
25. "{world}" inurl:admin/login
26. "{world}" intitle:"index of" inurl:backup
27. "{world}" intitle:"index of" inurl:database
28. intext:"{world}" inurl:.git
29. "{world}" intext:"index of" inurl:.git
30. "{world}" inurl:config.ini
31. "{world}" filetype:xml
32. "{world}" filetype:json
33. "{world}" filetype:csv
34. "{world}" filetype:log
35. "{world}" filetype:conf
36. "{world}" filetype:sql
37. "{world}" filetype:html
38. "{world}" filetype:php
39. "{world}" filetype:asp
40. "{world}" filetype:aspx
41. "{world}" filetype:jsp
42. "{world}" filetype:sh
43. "{world}" filetype:bat
44. "{world}" filetype:pl
45. "{world}" filetype:py
46. "{world}" filetype:java
47. "{world}" filetype:c
48. "{world}" filetype:cpp
49. "{world}" filetype:cs
50. "{world}" filetype:rb
51. "{world}" filetype:ini
52. "{world}" filetype:cfg
53. "{world}" filetype:yaml
54. "{world}" filetype:json
55. "{world}" filetype:xml
56. "{world}" filetype:env
57. "{world}" filetype:htpasswd
58. "{world}" filetype:htaccess
59. "{world}" filetype:htpasswd intext:password
60. "{world}" filetype:htaccess intext:password
61. "{world}" filetype:sql intext:password
62. "{world}" filetype:log intext:password
63. "{world}" inurl:robots.txt
64. "{world}" intitle:"index of" inurl:robots.txt
65. "{world}" inurl:sitemap.xml
66. "{world}" intitle:"index of" inurl:sitemap.xml
67. "{world}" inurl:.svn
68. "{world}" inurl:.hg
69. "{world}" inurl:.cvs
70. "{world}" inurl:.bak
71. "{world}" inurl:.old
72. "{world}" inurl:.swp
73. "{world}" inurl:.tmp
74. "{world}" inurl:.temp
75. "{world}" inurl:.backup
76. "{world}" inurl:.db
77. "{world}" inurl:.sql
78. "{world}" inurl:.log
79. "{world}" inurl:.conf
80. "{world}" inurl:.ini
81. "{world}" inurl:.cfg
82. "{world}" inurl:.yaml
83. "{world}" inurl:.json
84. "{world}" inurl:.xml
85. "{world}" inurl:.env
86. "{world}" inurl:.htpasswd
87. "{world}" inurl:.htaccess
88. "{world}" inurl:.bak
89. "{world}" inurl:.old
90. "{world}" inurl:.swp
--------------------
                    """)
    resultfile.close()
    print(Fore.GREEN + "The file has been successfully created !")
    time.sleep(1)  # import time
    os.system('cls')
    dork()



if __name__ == "__main__":
    dork()
