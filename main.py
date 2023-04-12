import socket

import customtkinter
import pandas as pd
import customtkinter as ctk
from PIL import ImageTk, Image


def webSrcClick():
    def check_port():
        host = webEnt.get()


        if host.startswith('https://'):
            host = host[len('https://'):]
        elif host.startswith('http://'):
            host = host[len('http://'):]
        if '/' in host:
            host = host.split('/')[0]
        print(host)
        port_info = pd.DataFrame()
        port_name = []
        port_use = []
        port_status = []
        important_ports = [
            (21, "FTP"),
            (22, "SSH"),
            (23, "Telnet"),
            (25, "SMTP"),
            (53, "DNS"),
            (67, "DHCP client"),
            (68, "DHCP server"),
            (69, "TFTP"),
            (80, "HTTP"),
            (88, "Kerberos"),
            (110, "POP3"),
            (119, "NNTP"),
            (123, "NTP"),
            (135, "Microsoft RPC"),
            (139, "NetBIOS"),
            (143, "IMAP"),
            (161, "SNMP"),
            (162, "SNMP traps"),
            (179, "BGP"),
            (194, "IRC"),
            (389, "LDAP"),
            (443, "HTTPS"),
            (445, "Microsoft DS"),
            (465, "SMTPS"),
            (514, "Syslog"),
            (548, "AFP"),
            (587, "SMTP (mail submission)"),
            (636, "LDAPS"),
            (993, "IMAPS"),
            (995, "POP3S"),
            (1080, "SOCKS proxy"),
            (1433, "Microsoft SQL Server"),
            (1434, "Microsoft SQL Monitor"),
            (1521, "Oracle database"),
            (1723, "Microsoft PPTP VPN"),
            (2049, "NFS"),
            (2082, "cPanel"),
            (2083, "cPanel SSL"),
            (2086, "WHM"),
            (2087, "WHM SSL"),
            (2181, "Apache ZooKeeper"),
            (2222, "DirectAdmin"),
            (3128, "HTTP proxy"),
            (3306, "MySQL"),
            (3389, "Microsoft Remote Desktop Protocol (RDP)"),
            (5432, "PostgreSQL"),
            (5500, "VNC Server"),
            (5800, "VNC over HTTP"),
            (5900, "VNC"),
            (5901, "VNC"),
            (5902, "VNC"),
            (5984, "CouchDB"),
            (6379, "Redis"),
            (8000, "HTTP alternative"),
            (8008, "HTTP alternative"),
            (8080, "HTTP alternative"),
            (8443, "HTTPS alternative"),
            (8888, "HTTP alternative"),
            (9090, "HTTP alternative"),
            (9091, "HTTP alternative"),
            (11211, "Memcached"),
            (27017, "MongoDB"),
            (28017, "MongoDB web interface")
        ]
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            for i in important_ports:
                result = sock.connect_ex((host, i[0]))
                if result == 0:
                    port_name.append(i[0])
                    port_use.append(i[1])
                    port_status.append('Open')
                else:
                    port_name.append(i[0])
                    port_use.append(i[1])
                    port_status.append('Close')

            port_info['Port'] = port_name
            port_info['Use'] = port_use
            port_info['Status'] = port_status
            port_info.to_csv('Port Info.csv')
            tempL = ctk.CTkLabel(btmFrame, text='File exported as Port Info.csv', font=('Poppins', 15))
            tempL.grid(row=2, column=0, pady=10)

        except Exception as e:
            print(e)
            tempL = ctk.CTkLabel(btmFrame, text='Domain/IPV4 not found', font=('Poppins', 15))
            tempL.grid(row=2, column=0, pady=10)

    webSrcBtn.destroy()


    webEnt = ctk.CTkEntry(btmFrame, placeholder_text='Enter your domain or local IPV4 address', font=('Poppins', 20), width=400)
    webEnt.grid(row=0, column=0, pady=20)
    webBtn = ctk.CTkButton(btmFrame, text='Submit', font=('Poppins', 20), command=check_port)
    webBtn.grid(row=1, column=0, ipadx=10, ipady=10)





customtkinter.set_appearance_mode('dark')
win = ctk.CTk()
win.geometry("1024x768+10+10")

img1 = ImageTk.PhotoImage(Image.open('images/VulnaProof.png'))

imgLab = ctk.CTkLabel(win, image=img1, text='')
imgLab.pack()

btmFrame = ctk.CTkFrame(win,fg_color='transparent')
btmFrame.pack(pady=50)

webSrcBtn = ctk.CTkButton(btmFrame, text='Website Port Scan', font=('Poppins', 30), command=webSrcClick)
webSrcBtn.grid(row=0, column=0, padx=20, ipadx=20, ipady=20)

win.mainloop()