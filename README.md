# Social-Networking-Site<br/>
https://user-images.githubusercontent.com/46949426/69986775-0cfe3a80-150c-11ea-8920-d473637ce19e.PNG<br/>
![Capture](https://user-images.githubusercontent.com/46949426/69986850-34550780-150c-11ea-93ca-c7a95d53ba97.PNG)<br/>

# first step: database set up.(mysql localhost 3306)<br/>
go C:\Users\fwu7\Desktop\fp\DatabaseScript   find migration_script.sql<br/>
use mysql workbench import or excute the script or mysql shell type: source C:\Users\fwu7\Desktop\fp\DatabaseScript\migration_script.sql
then type: show databases;<br/>
see if exists, then type: use fp2bb, type: show tables;<br/>
You should see 14 tables there.<br/>

# how to run in windows<br/>
1.dowaload and unzip to your desktop<br/>
2.open ur command and goes to type: cd C:\Users\14049\Desktop\fp\env\Scripts<br/>
3.then type: activate<br/>
4.then type: cd C:\Users\14049\Desktop\fp\pjflask<br/>
5.then type: python pj.py<br/>
you might receive some error msg when your dependency not fully inject, or library you have not downloaded.<br/>
just follow the error code and in C:\Users\14049\Desktop\fp\pjflask type: pip install 'flask' or 'flask_socket' depends on error msg<br/>

# how to run in linux<br/>
1.dowaload and unzip to your desktop<br/>
2.open ur command and goes to type: cd C:/Users/14049/Desktop/fp/env/Scripts<br/>
3.then type: activate<br/>
4.then type: cd C:/Users/14049/Desktop/fp/pjflask<br/>
5.then type: python pj.py<br/>
you might receive some error msg when your dependency not fully inject, or library you have not downloaded.<br/>
just follow the error code and in C:/Users/14049/Desktop/fp/pjflask type: pip install 'flask' or 'flask_socket' depends on error msg<br/>
