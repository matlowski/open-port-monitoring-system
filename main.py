import smtplib
import subprocess
from email.mime.text import MIMEText
import xml.etree.ElementTree as ET



SMPT_EMAIL = ""     # Sender email address
SMTP_PASSWORD = ""  # App-specific password for the sender email
ADMIN_EMAIL = ""    # Recipient email address, e.g. admin


# Run nmap command and suppress its output
def run_nmap(): # Set your own IP addresses of target machines
    subprocess.run(["nmap", "-oX", "scan_output.xml", "", ""], stdout=subprocess.DEVNULL) 

# Send an email with the comparison result
def send_email(subject, body):
    # # Uncomment to see results in terminal without email sending
    # print(ADMIN_EMAIL) 
    # print(subject)
    # print(body)
    # return 

    message = MIMEText(body)
    message["Subject"] = subject
    message["From"] = SMPT_EMAIL
    message["To"] = ADMIN_EMAIL

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.ehlo()
        server.starttls()
        server.login(SMPT_EMAIL, SMTP_PASSWORD)
        server.send_message(message)


class Host:
    def __init__(self, hostnames, addr, state, extraports, ports, is_reference):
        self.addr = addr # e.g. 127.0.0.1
        self.state = state # e.g. up 
        self.state_text = f'Host is {self.state}.' # e.g. Host is up
        self.hostnames = hostnames # e.g. localhost
        self.host_text = ', '.join(sorted(self.hostnames)) + f' {self.addr}' # e.g. localhost 127.0.0.1
        self.extraports = extraports # Extraports object
        self.extraports_text = f"Not shown: {self.extraports.count} {self.extraports.state} ports" # e.g. Not shown: 1000 closed ports
        self.ports = ports # list of Port objects

        self.compare_to_host = None # Host object or None
        self.is_reference = is_reference # e.g. True / False

    # Main comparison logic between matching hosts
    def __str__(self):
        # Logic for a host from 'reference.xml' that has a matching host to compare 
        if self.is_reference and self.compare_to_host:
            lines = []
            lines.append(f'Host:{self.host_text}')

            next_host = self.compare_to_host
            if self.extraports_text != next_host.extraports_text: 
                lines.append(f'-{self.extraports_text}')      # e.g. - 1000 closed
                lines.append(f'+{next_host.extraports_text}') # e.g. + 997 closed
            if self.state_text != next_host.state_text: 
                lines.append(f'-{self.state_text}')           # e.g. - Host is 'up' 
                lines.append(f'+{next_host.state_text}')      # e.g. + Host is 'up' 

            # Determine prefix for the header line, e.g. '-' PORT STATE SERVICE VERSION
            if self.ports or next_host.ports:
                if not self.ports:
                    prefix = '+'
                elif not next_host.ports:
                    prefix = '-'
                else:
                    prefix = ' '

                # Remove duplicates and sort port_protocols in ascending order (ndiff style)
                port_protocol_to_port1 = { # e.g. 80/tcp: 80/tcp  up  http -> (Port object)  
                    port.port_protocol: port for port in self.ports
                } 
                port_protocol_to_port2 = { 
                    port.port_protocol: port for port in next_host.ports
                } 
                unique_port_protocols = sorted({*port_protocol_to_port1.keys(), *port_protocol_to_port2.keys()})

                # Logic for matching ports between two compared hosts
                ports_lines = []
                for port_protocol in unique_port_protocols:
                    port1 = port_protocol_to_port1.get(port_protocol)
                    port2 = port_protocol_to_port2.get(port_protocol)
                    if port1 and port2: 
                        if str(port1) != str(port2): # Possible difference: service  
                            ports_lines.append(f'-{port1}')
                            ports_lines.append(f'+{port2}')
                    elif port1:
                        ports_lines.append(f'-{port1}')
                    elif port2:
                        ports_lines.append(f'+{port2}')

                if ports_lines:
                    # Recalculate column widths
                    Port.recalculate_column_widths(*self.ports, *next_host.ports) 
                    # Add header - PORT STATE SERVICE VERSION
                    lines.append(f'{prefix}{Port.header()}') 
                    # Add changes in ports
                    lines.extend(ports_lines)
                else:
                    lines.append('no port changes')
            else:
                lines.append('no port changes')

            return '\n'.join(lines)

        else:
            # Logic for a host from 'reference.xml' that does NOT have a matching host to compare
            if self.is_reference:
                prefix = '-'
            # Logic for a host from 'scan_output.xml' that may or may not have a matching host to compare
            else:
                prefix = '+'

            Port.recalculate_column_widths(*self.ports)
            ports_text = Port.header() + '\n' + '\n'.join(f'{prefix}{port}' for port in self.ports)
            return (
                f"{prefix}{self.host_text}\n"
                f"{prefix}{self.state_text}\n"
                f"{prefix}{self.extraports_text}\n"
                f"{prefix}{ports_text}"
            )


class ExtraPorts:
    def __init__(self, state, count):
        self.state = state
        self.count = count


class Port:
    # Static column widths for PORT, STATE, and SERVICE headers
    column_width_port_protocol = len("PORT")
    column_width_state = len("STATE")
    column_width_service = len("SERVICE")

    def __init__(self, port, protocol, state, service):
        self.port = port # e.g. 80
        self.protocol = protocol # e.g. tcp
        self.port_protocol = f"{self.port}/{self.protocol}" # e.g. 80/tcp
        self.state = state # e.g. up
        self.service = service # e.g. http

    # Display Port object as e.g. 80/tcp  up   http
    def __str__(self): 
        return (
            f"{self.port_protocol:{self.column_width_port_protocol}} "
            f"{self.state:{self.column_width_state}} "
            f"{self.service:{self.column_width_service}}"
        ) 

    # Recalculate column widths
    @classmethod
    def recalculate_column_widths(cls, *ports):
        for port in ports:
            if len(port.port_protocol) > Port.column_width_port_protocol:
                Port.column_width_port_protocol = len(port.port_protocol)
            if len(port.state) > Port.column_width_state:
                Port.column_width_state = len(port.state)
            if len(port.service) > Port.column_width_service:
                Port.column_width_service = len(port.service)

    # Display header line: PORT STATE SERVICE VERSION
    @classmethod
    def header(cls): 
        return (
            f"{'PORT':{cls.column_width_port_protocol}} "
            f"{'STATE':{cls.column_width_state}} "
            f"{'SERVICE':{cls.column_width_service}} "
            f"VERSION"
        )



# Extract information about hosts and ports from XML file
def get_hosts(root, is_reference):
    hosts = [] # List of hosts extracted from XML 
    # Extract unnecessary data from each host in XML
    for host_tag in root.findall('host'):
        addr = host_tag.find('address').attrib['addr'] # Extract 'addr' attribute value from <address> tag
        hostnames = set()
        for hostname in host_tag.find('hostnames').findall('hostname'):
            hostnames.add(hostname.attrib['name'])  

        ports_tag = host_tag.find('ports')
        # Extract information about 'extraports'
        extraports_tag = ports_tag.find('extraports') 
        state = extraports_tag.attrib['state'] 
        count = extraports_tag.attrib['count']
        extraports = ExtraPorts(state, count)

        # Extract information about 'ports'
        ports = [] # List of ports associated with the given host
        for port_tag in ports_tag.findall('port'):
            portid = port_tag.attrib['portid'] # e.g. 80
            protocol = port_tag.attrib['protocol'] # e.g. tcp
            state = port_tag.find('state').attrib['state'] # e.g. open
            service = port_tag.find('service').attrib['name'] # e.g. http
            ports.append(Port(portid, protocol, state, service))

        # Extract host state
        status_tag = host_tag.find('status') 
        state = status_tag.attrib['state'] # e.g. up

        host = Host(hostnames, addr, state, extraports, ports, is_reference)
        hosts.append(host)

    return hosts


def compare_xml_files(file1, file2):
    # Parse XML file
    tree1 = ET.parse(file1)
    tree2 = ET.parse(file2)
    # Get 'root element' of XML file (e.g., <nmaprun> in nmap XML)
    root1 = tree1.getroot()
    root2 = tree2.getroot() 
    # Return list of hosts extracted from XML file
    hosts1 = get_hosts(root1, is_reference=True) 
    hosts2 = get_hosts(root2, is_reference=False)  

    # Associate host from 'reference.xml' with its equivalent in 'scan_output.xml'
    for host1 in hosts1:
        for host2 in hosts2:
            if host2.compare_to_host:
                continue
            
            if host1.addr == host2.addr:
                host1.compare_to_host = host2
                host2.compare_to_host = host1
                break

    # Merge hosts from both files and sort by IP address for consistent output
    hosts = [*hosts1, *hosts2]
    # hosts = sorted(hosts, key=lambda host: host.host_text) - zobacz jak będzie bez tego działać
    hosts = sorted(hosts, key=lambda host: host.addr)

    output_data = [] # Data to be sent in the email
    for host in hosts:
        # Skip processing if host is from 'scan_output.xml' and already has a match in 'reference.xml' to avoid duplicates
        if host.compare_to_host and not host.is_reference:
            continue

        # Add to 'output_data' only hosts from 'reference.xml' that have a match in 'scan_output.xml'
        # Skip unmatched hosts, as they have no data to display
        host_text = str(host)
        if host_text:
            output_data.append(host_text)

    # If 'output_data' is not empty, send an email
    if output_data: 
        output = '\n\n'.join(output_data)
        send_email("Nmap scan results changed", output)


def main():
    run_nmap()
    compare_xml_files("reference.xml", "scan_output.xml")



if __name__ == "__main__":
    main()