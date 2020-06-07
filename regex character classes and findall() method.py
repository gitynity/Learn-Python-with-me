'''

The regex method findall() is passed a string, and returns all matches in it, not just the first match.
If the regex has 0 or 1 group, findall() returns a list of strings.
If the regex has 2 or more groups, findall() returns a list of tuples of strings.

Character classes: \d , \D , \w , \W , \s , \S
--------------------------------------------------------------------------
\d is a shorthand character class that matches digits. 
\w matches "word characters" (letters, numbers, and the underscore). 
\s matches whitespace characters (space, tab, newline).

The uppercase shorthand character classes \D, \W, and \S match charaters 
that are not digits, not word characters, and not whitespace respectively.
---------------------------------------------------------------------------

You can make your own character classes with square brackets: [aeiou]

A ^ caret makes it a negative character class, matching anything not in the brackets: [^aeiou]

'''

resume = '''

THOMAS B. SEEKER

1234 Northern Star Circle
Baltimore, MD 12345
H: 410-555-1212; W: 410-555-2121
E-mail: seeker@nettcom.com

CAREER GOAL

Client Server Systems Architect for a high technology firm.

QUALIFICATIONS SUMMARY

Nine years of experience in designing, installing, and troubleshooting computing systems; a proven track record in identifying problems and developing innovative solutions.

TECHNICAL SKILLS

* PROGRAMMING: C, C++, Visual BASIC, FORTRAN, Pascal, SQL, OSF/Motif, UNIX Shell Script (sh, ksh, csh), BASIC, Clipper, Algol 68, and 80X86 Assembler.

* OPERATING SYSTEMS: UNIX (bsd & SVr3/r4), MS Windows, MS DOS, MS Windows NT, Solaris, HP-UX, Ultrix, AIX, VAX/VMS, and Macintosh System 7.

* NETWORKING: TCP/IP, OSI, Microsoft LAN Manager, Novell Netware, DDN, Internet, Ethernet, Token Ring, SNA, X.25, LAN-WAN interconnection.

* APPLICATIONS: Microsoft Office, Microsoft Access, Microsoft Visual C++, Microsoft Project, Microsoft Publisher, Lotus 123, Lotus Freelance, System Architect, and others.

PROFESSIONAL EXPERIENCE

Systems Engineer

Computer Engineering Corporation, Los Angeles, CA, 1993-Present

* Provide systems engineering, software engineering, technical consulting, and marketing services as a member of the Systems Integration Division of a software engineering consulting company.

* Designed and managed the development of an enterprise-level client/server automated auditing application for a major financial management company migrating from mainframe computers, db2, and FOCUS to a workgroup oriented, client/server architecture involving Windows for Workgroups, Windows NT Advanced Server, Microsoft SQL Server, Oracle7, and UNIX.

* Designed an enterprise level, high performance, mission-critical, client/server database system incorporating symmetric multiprocessing computers (SMP), Oracle7’s Parallel Server, Tuxedo’s on-line transaction processing (OLTP) monitor, and redundant array of inexpensive disks (RAID) technology.

* Conducted extensive trade studies of a large number of vendors that offer leading-edge technologies; these studies identified proven (low-risk) implementations of SMP and RDBMS systems that met stringent performance and availability criteria.

Systems Analyst

Business Consultants, Inc., Washington, DC 1990-1993

* Provided technical consulting services to the Smithsonian Institute’s Information Technology Services Group, Amnesty International, and internal research and development initiatives.

* Consolidated and documented the Smithsonian Laboratory's Testing, Demonstration, and Training databases onto a single server, maximizing the use of the laboratory's computing resources.

* Brought the Smithsonian Laboratory on-line with the Internet.

* Successfully integrated and delivered to Amnesty International an $80,000 HP 9000/750 Server consisting of 8 Gigabytes of disk space and 9 software systems that required extensive porting work and documentation.

Automated Data Processor

US Army Infantry, Germany 1986-1990

* Analyzed problems and ADP processes; designed, tested, and implemented software and hardware systems for an organizational operations center.

* Supervised the maintenance, deployment, installation, and operation of a battalion's personnel system that monitored and controlled up to 12 platoons in a fast-paced, technically demanding environment.

* Designed a maintenance reporting program that converted the labor intensive task of producing weekly status reports from a 4-day to a 2-hour process.

* Developed a departmental computer literacy training program, teaching classes on microcomputer operating systems, office automation software, and introductory programming.

* Taught a "Structured Programming and Problem Solving" course for the Community Education Center after work hours.

EDUCATION

* Computer Systems Technology Program, Air Force Institute of Technology (AFIT), Graduate Courses in Software Engineering and Computer Communications (24 quarter units); GPA: 3.43

* BS, Mathematics/Computer Science, University of California, Los Angeles (UCLA), GPA: 3.57; Major GPA: 3.62

SPECIALIZED TRAINING

* Database Administration, Performance Tuning, and Benchmarking with Oracle7; Oracle Corporation.

* Software Requirements Engineering and Management Course; Computer Applications International Corporation.

* X.400 Messaging and Allied Communications Procedures-123 Profile; ComTechnologies, Inc.

* GOSIP LAN Operating System Network Administration; ETC, Inc.

* Interactive UNIX System V r4 (POSIX) System Administration; ETC, Inc.

* Effective Briefing Techniques and Technical Presentations; William French and Associates, Inc.

* Transmission Control Protocol/Internet Protocol (TCP/IP); Technology Systems Institute.

* LAN Interconnection Using Bridges, Routers, and Gateways; Information Systems Institute.

* OSI X.400/X.500 Messaging and Directory Service Protocols; Communication Technologies, Inc.

* US Army Signal Officer Advanced Course, US Army Signal Center, Georgia; Honor Graduate.

CERTIFICATION, HONORS, & PROFESSIONAL AFFILIATIONS

* MCP Trainer, DCS.

* MCP Trainer, SDD.

* MCP Certified Systems Engineer.

* MCP Certified Product Specialist, Networking, MS TCP/IP, and MS Mail 3.2 for PC Networks.

* Member, Armed Forces Communications and Electronics Association (AFCEA).

* Recipient, Department of Defense Meritorious Service Medal, Defense Information Systems Agency (DISA).

'''
import re

PhoneNumberRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = PhoneNumberRegex.search(resume)
print(mo.group())	#returned a string	:	410-555-1212

mo = PhoneNumberRegex.findall(resume)
print(mo)	#returned a list of string	:	['410-555-1212', '410-555-2121']

PhoneNumberRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = PhoneNumberRegex.findall(resume)
print(mo)		#returns a list of tuples of string	:	[('410', '555', '1212'), ('410', '555', '2121')]

#Creating your own character class:

vowelsRegex = re.compile(r'[aeiou]')		# is same as writing r'a|e|i|o|u'
mo = vowelsRegex.findall("hello pythoners")
print(mo)	#prints ['e', 'o', 'o', 'e']

smallletterRegex = re.compile(r'[a-z]')
mo = smallletterRegex.findall("Hello Pythoners")
print(mo)		#prints ['e', 'l', 'l', 'o', 'y', 't', 'h', 'o', 'n', 'e', 'r', 's']

letterRegex = re.compile(r'[a-zA-Z]')
mo = letterRegex.findall("Hello Pythoners")
print(mo)		#prints ['H', 'e', 'l', 'l', 'o', 'P', 'y', 't', 'h', 'o', 'n', 'e', 'r', 's']

#lets say I wanna match 2 vowels one after the other

vowelsRegex = re.compile(r'[aeiouAEIOU]{2}')
mo = vowelsRegex.findall("Hello FriEnds")
print(mo)		#prints ['iE']

#lets say I wanna match consonants only
consonantsRegex = re.compile(r'[^aeiouAEIOU]')
mo = consonantsRegex.findall("Hello FriEnds")
print(mo)		#prints ['H', 'l', 'l', ' ', 'F', 'r', 'n', 'd', 's']

#lets say i wanna match string begining with Hello

beginwith = re.compile(r'^Hello')
mo = beginwith.findall("Hello there , whassup!")
print(mo)

#lets say I wanna match string ending with up

endswith = re.compile(r'up$')
mo = endswith.findall("Hello there, wassup")
print(mo)

#lets say I wanna match a string which only has hello in it

onlyhas = re.compile(r'^hello$')
mo = onlyhas.findall('hello')
print(mo)

# . = any 1 character
a = re.compile(r'.ello')	#any 1 character before ello
mo = a.findall("hello")
print(mo)	#prints [hello]

mo = a.findall("chello")
print(mo)		#prints [hello]

#.* any number of any character except new line

b = re.compile(r'.*')
mo = b.findall('hey there pythoner')
print(mo)		#prints ['hey there pythoner', '']

#Find and replace/substitute using sub() function


names = re.compile(r'Agent \w+')
mo = names.findall("Agent Alice gave some secret documents to Agent Bob")
print(mo)

#I wanna replace the names of agents with something else

secret = names.sub('???' , 'Agent Alice gave some secret documents to Agent Bob' )
print(secret)		#prints ??? gave some secret documents to ???


#I wanna replace the names of agents by their first letter

names = re.compile(r'Agent (\w)(\w+)')
shortnames = names.sub(r'Agent \1' , 'Agent Alice gave some secret documents to Agent Bob')
print(shortnames)		#prints Agent A gave some secret documents to Agent B


#Print pattern : 54321 4321 321 21 1

count = 5
while count>0:
	for i in range(count,0,-1):
		print(i,end='')
	count=count-1
	print(" ",end='')
