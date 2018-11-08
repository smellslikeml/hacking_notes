#!/bin/sh
# hiding open ports by showing all ports open
# requires rebuilding linux kernel
HOST="192.168.1.20"
/usr/sbin/tcpdump -e -S -n -p -l "(tcp[13] == 2) and (dst host $HOST)" | /bin/awk
'{
# Output numbers as unsigned
  CONVFMT="%u";
# Seed the randomizer
  srand();
# Parse the tcpdump input for packet information
  dst_mac = $2;
  src_mac = $3;
  split($6, dst, "."); split($8, src, ".");
  src_ip = src[1]"."src[2]"."src[3]"."src[4];
  dst_ip = dst[1]"."dst[2]"."dst[3]"."dst[4];
  src_port = substr(src[5], 1, length(src[5])-1);
  dst_port = dst[5];
# Increment the received seq number for the new ack number
  ack_num = substr($10,1,index($10,":")-1)+1;
# Generate a random seq number
  seq_num = rand() * 4294967296;
# Precalculate the sequence number for the next packet
  seq_num2 = seq_num + 1;
# Feed all this information to nemesis
  exec_string = "nemesis tcp -fS -fA -S "src_ip" -x "src_port" -H "src_mac" -D "dst_ip" -y "dst_port" -M "dst_mac" -s "seq_num" -a "ack_num";
# Display some helpful debugging info.. input vs. output
  print "[in] "$1" "$2" "$3" "$4" "$5" "$6" "$7" "$8" "$9" "$10";
  print "[out] "exec_string";
# Inject the packet with nemesis
  system(exec_string);
# Do it again to craft the second packet, this time ACK/PSH with a banner
  exec_string = "nemesis tcp -v -fP -fA -S "src_ip" -x "src_port" -H "src_mac" -D "dst_ip" -y "dst_port" -M "dst_mac" -s "seq_num2" -a "ack_num" -P "banner";
# Display some helpful debugging info..
  print "[out2] "exec_string";
# Inject the second packet with nemesis
  system(exec_string);
}'
