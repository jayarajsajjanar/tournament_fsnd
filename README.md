###*******************Tournament_fsnd******************

###             Second project as part of the Udacity/Google - Full Stack Web Developer - Nanodegree
 
###Key things learnt:
1. Using vagrant and virtualbox
2. Database designing. Using the database in the python program via the library provided by the database engine. 

###About Project:
1. Its an implementation of the Swiss Tournament system.
2. New player can be registered. Matches can be reported.
3. Pairing for next round is done based on current standings.1st and 2nd are matched, 3rd and 4th are matched.......

###Environment :
1. The virtual machine provided is Ubuntu 14.04, 32 bits.
2. Database engine - Postgre SQL.
3. Python 2.7.3

###Steps for running the project:
1. Install virtualbox and vagrant on your local machine.
2. **Clone** the repo using  - `git clone https://github.com/jayarajsajjanar/fullstack-nanodegree-vm.git`
3. **Clone** the repo of the current project into the folder created in step 2 using - `git clone https://github.com/jayarajsajjanar/tournament_fsnd.git`  
4. `cd` to the directory containing the **vagrantfile**
5. `vagrant up` boots and configures the machine based on the vagrant file.
6. `vagrant ssh` logs into the machine.
7. \Vagrant on virtual machine is shared with the \Vagrant folder containing vagrant file on the host.                     
8. Once you are into the virtual machine :

   **Follow the below steps:**

   `cd` to the directory of the current project which should be under `\vagrant`
  
   execute command `psql` to connect to the Postgres database engine.
  
   **In postgres:**
  
   `\i tournament.sql` imports and executes a few sql statements from *tournament.sql* which sets up the database that will be used for the current project.
  
   `\q` quits from the postgres.

   execute the command `python tournament_test.py` which will execute the test cases. Success message will be displayed if all the test cases are successful.
      

