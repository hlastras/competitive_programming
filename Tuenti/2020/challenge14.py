# This code is incomplete
# Slave processes do not handle their expulsion from the cluster
# The target is that server 9 (first to join) get the secret owner.
# There are some small unsolved problems in the code like exceptions,
# so not alwais find the sectet.
import telnetlib
import threading
import time
import random

class Slave(threading.Thread):
  tn = None # Telnet session
  master = None
  partners = []
  next = 9

  def run(self):
    self.tn = telnetlib.Telnet("52.49.91.111", 2092)

    # Search server id
    data = self.tn.read_until(b'\n').decode('ascii')
    self.serverId = int(data[data.index("ID: ")+4:])
    self.master.newPartner(self.getName(), self.serverId)

    # Waiting join to cluster
    data = self.tn.read_until(b'\n').decode('ascii')
    self.master.availablePartner(self.getName(), self.serverId)

    # Start work
    i = 500 
    while True:
      i+= 1

      round = self.readRound()
      servers, owner = self.extractData(round)
      
      if owner == 9:
        self.findSecret(owner)
        return
        
      newServers = self.changeServersInCluster(servers, set(self.partners), owner, self.next)
      
      # PREPARE commands
      outCommands = ""
      for server in servers:
        outCommands += 'PREPARE {%d,%d} -> %s\n' % (i, self.serverId, server)
      
      # ACCEPT commands
      serversList = ",".join(str(x) for x in newServers)
      if len(self.partners)*2 > len(servers):
        # We have mor than half of server, so we can make whoever we want
        for server in servers:
          outCommands += 'ACCEPT {id: {%d,%d}, value: {servers: [%s], secret_owner: 9}} -> %d\n' % (i, self.serverId, serversList, server)
      else:
        for server in servers:
          outCommands += 'ACCEPT {id: {%d,%d}, value: {servers: [%s], secret_owner: %d}} -> %d\n' % (i, self.serverId, serversList, owner, server)
      
      self.tn.write(outCommands.encode())

  def findSecret(self, owner):
    if owner == self.serverId:
      while True:
        line = self.tn.read_until(b'\n').decode('ascii')
        if line.startswith("SECRET IS"):
          print(line)
          self.master.workFinish()
          return

  def setMaster(self, master):
    self.master = master

  def setNext(self, id):
    self.next = id

  def setAvailable(self, id):
    self.partners.append(id)

  def setPartners(self, partners):
    self.partners = partners

  def readRound(self):
    return self.tn.read_until(b'(ROUND FINISHED)').decode('ascii')

  # From LEARN line, extract servers in the cluster and actual owner
  def extractData(self, round):
    servers = []
    owner = ""
    line = round[-87:]
    a = line.index('[')+1
    b = line.index(']')
    servers = [int(x) for x in line[a:b].split(',')] 
    inda=line.index("secret_owner: ")+14
    indb=line.index("}", inda)
    owner = int(line[inda:indb])
    return servers, owner

  # Remove first server that don't belong to this script
  # And add our next server that is waiting to join to cluster
  def changeServersInCluster(self, servers, not_remove, actual_owner, to_add):
    newServers = servers.copy()
    for server in newServers:
      if server not in not_remove and server != actual_owner:
        newServers.remove(server)
        break
    newServers.append(to_add)
    return newServers



class Master(threading.Thread):
  end = False
  serversWaitingJoin = {}
  availableServers = {}
  i = 0

  def run(self):
    while not self.end:
      if len(self.serversWaitingJoin) == 0:
        s_name = "Thread-{}".format(self.i)
        mythread = Slave(name = s_name)
        mythread.setMaster(self)
        mythread.setPartners(list(self.availableServers.keys()))
        self.serversWaitingJoin[s_name] = mythread
        self.i += 1
        mythread.start() 
    
    # stop
    for _, server in self.availableServers.items():
      server.stop()

  def availablePartner(self, server, id):
    # comunicar a todos avail
    for _, s in self.availableServers.items():
      s.setAvailable(id)
    # cambiar lista
    self.availableServers[id] = self.serversWaitingJoin[server]
    self.serversWaitingJoin.pop(server)


  def newPartner(self, server, id):
    for _, s in self.availableServers.items():
      s.setNext(id)

  def workFinish(self):
    self.end = True




if __name__ == '__main__':
    m = Master()
    m.start()