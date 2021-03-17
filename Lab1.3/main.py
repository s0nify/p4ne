from pysnmp.hlapi import *

ip_port = ("10.31.70.107", 161)
community_name = "public"
snmp_var_version = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)

result = getCmd(SnmpEngine(), CommunityData(community_name, mpModel=0),
                UdpTransportTarget(ip_port), ContextData(), ObjectType(snmp_var_version))

for i in result:
    for v in i[3]:
        print(v)
