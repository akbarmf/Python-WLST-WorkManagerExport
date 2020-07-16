def exportMin(file):
  try:
    cd('/SelfTuning')
    domain=ls(returnMap='true')

    for dom in domain:
      cd(dom + '/MinThreadsConstraints')
      minCons=ls(returnMap='true')

      for min in minCons:
        cd('/SelfTuning/' + dom + '/MinThreadsConstraints/' + min)
        minName = cmo.getName()
        minCount = cmo.getCount()
        minTarget = cmo.getTargets()
        serverTarget = ''
    
        for target in minTarget:
          serverTarget = serverTarget + target.getName() + ':' + target.getType() + '|'

        print('# Minimum Threads Constraint: ' + str(minName) )
        print('# Count: ' + str(minCount) )
        print('# target: ' + str(serverTarget) )
        print('\n')
      
        if str(minCount) == 'None':
          minCount = ''
        elif str(serverTarget) == 'None':
          serverTarget = ''
      
        exp = 'minThreadCon,' + str(minName) + ',' + str(minCount) + ',' + str(serverTarget) +'\n'
        file.write(exp)
  except Exception, e:
    print e

def exportMax(file):
  try:
    cd('/SelfTuning')
    domain=ls(returnMap='true')

    for dom in domain:
      cd(dom + '/MaxThreadsConstraints')
      maxCons=ls(returnMap='true')

      for max in maxCons:
        cd('/SelfTuning/' + dom + '/MaxThreadsConstraints/' + max)
        maxName = cmo.getName()
        maxCount = cmo.getCount()
        maxTarget = cmo.getTargets()
        serverTarget = ''
    
        for target in maxTarget:
          serverTarget = serverTarget + target.getName() + ':' + target.getType() + '|'

        print('# Maximum Threads Constraint: ' + str(maxName) )
        print('# Count: ' + str(maxCount) )
        print('# target: ' + str(serverTarget) )
        print('\n')
      
        if str(maxCount) == 'None':
          maxCount = ''
        elif str(serverTarget) == 'None':
          serverTarget = ''
      
        exp = 'maxThreadCon,' + str(maxName) + ',' + str(maxCount) + ',' + str(serverTarget) +'\n'
        file.write(exp)
  except Exception, e:
    print e

def exportCap(file):
  try:
    cd('/SelfTuning')
    domain=ls(returnMap='true')

    for dom in domain:
      cd(dom + '/Capacities')
      capacity=ls(returnMap='true')

      for cap in capacity:
        cd('/SelfTuning/' + dom + '/Capacities/' + cap)
        name = cmo.getName()
        count = cmo.getCount()
        targets = cmo.getTargets()
        serverTarget = ''
    
        for target in targets:
          serverTarget = serverTarget + target.getName() + ':' + target.getType() + '|'

        print('# Capacity Constraint: ' + str(name) )
        print('# Count: ' + str(count) )
        print('# target: ' + str(serverTarget) )
        print('\n')
      
        if str(count) == 'None':
          count = ''
        elif str(serverTarget) == 'None':
          serverTarget = ''
      
        exp = 'maxThreadCon,' + str(name) + ',' + str(count) + ',' + str(serverTarget) +'\n'
        file.write(exp)
  except Exception, e:
    print e


def exportRes(file):
  try:
    cd('/SelfTuning')
    domain=ls(returnMap='true')

    for dom in domain:
      cd(dom + '/ResponseTimeRequestClasses')
      resTime=ls(returnMap='true')

      for res in resTime:
        cd('/SelfTuning/' + dom + '/ResponseTimeRequestClasses/' + res)
        name = cmo.getName()
        goal = cmo.getGoalMs()
        targets = cmo.getTargets()
        serverTarget = ''
    
        for target in targets:
          serverTarget = serverTarget + target.getName() + ':' + target.getType() + '|'

        print('# Response Time Request Class : ' + str(name) )
        print('# Response time goal : ' + str(goal) )
        print('# target : ' + str(serverTarget) )
        print('\n')
      
        if str(goal) == 'None':
          goal = ''
        elif str(serverTarget) == 'None':
          serverTarget = ''
      
        exp = 'resTimeReqClass,' + str(name) + ',' + str(goal) + ',' + str(serverTarget) +'\n'
        file.write(exp)
  except Exception, e:
    print e


def exportFair(file):
  try:
    cd('/SelfTuning')
    domain=ls(returnMap='true')

    for dom in domain:
      cd(dom + '/FairShareRequestClasses')
      fairShare=ls(returnMap='true')

      for fair in fairShare:
        cd('/SelfTuning/' + dom + '/FairShareRequestClasses/' + fair)
        name = cmo.getName()
        fairShare = cmo.getFairShare()
        targets = cmo.getTargets()
        serverTarget = ''
    
        for target in targets:
          serverTarget = serverTarget + target.getName() + ':' + target.getType() + '|'

        print('# Fair Share Request Class : ' + str(name) )
        print('# Fair Share : ' + str(fairShare) )
        print('# target : ' + str(serverTarget) )
        print('\n')
      
        if str(fairShare) == 'None':
          fairShare = ''
        elif str(serverTarget) == 'None':
          serverTarget = ''
      
        exp = 'resTimeReqClass,' + str(name) + ',' + str(fairShare) + ',' + str(serverTarget) +'\n'
        file.write(exp)

  except Exception, e:
    print e


def exportCon(file):
  try:
    cd('/SelfTuning')
    domain=ls(returnMap='true')

    for dom in domain:
      cd(dom + '/ContextRequestClasses')
      conReq=ls(returnMap='true')

      for con in conReq:
        cd('/SelfTuning/' + dom + '/ContextRequestClasses/' + con)
        name = cmo.getName()
        targets = cmo.getTargets()
        serverTarget = ''
    
        for target in targets:
          serverTarget = serverTarget + target.getName() + ':' + target.getType() + '|'

        print('# Context Request Class : ' + str(name) )
        print('# target : ' + str(serverTarget) )
        print('\n')
      
        #if str(fairShare) == 'None':
        #  fairShare = ''
        if str(serverTarget) == 'None':
          serverTarget = ''
      
        exp = 'conReqClass,' + str(name) + ',' + str(serverTarget) +'\n'
        file.write(exp)

  except Exception, e:
    print e


def exportWM(file):
  try:
    cd('/SelfTuning')
    domain=ls(returnMap='true')

    for dom in domain:
      cd(dom + '/WorkManagers')
      workmanager=ls(returnMap='true')

      for wm in workmanager:
        cd('/SelfTuning/' + dom + '/WorkManagers/' + wm)
        name = cmo.getName()
        
        try:
          max = cmo.getMaxThreadsConstraint().getName()
        except AttributeError, e:
          max = 'None'

        try: 
          min = cmo.getMinThreadsConstraint().getName()
        except AttributeError, e:
          min = 'None'

        try:
          conReqClass = cmo.getContextRequestClass().getName()
          conReqClassStat = 0
        except AttributeError, e:
          conReqClassStat = 1

        try: 
          fairReqClass = cmo.getFairShareRequestClass().getName()
          fairReqClassStat = 0
        except AttributeError, e:
          fairReqClassStat = 1

        try:
          resReqClass = cmo.getResponseTimeRequestClass().getName()
          resReqClassStat = 0
        except AttributeError, e:
          resReqClassStat = 1

        if conReqClassStat == 0:
          reqClass = conReqClassStat
        elif fairReqClassStat == 0:
          reqClass = fairReqClass
        elif resReqClassStat == 0:
          reqClass = resReqClass
        else:
          reqClass = 'None'

        try:
          capacity = cmo.getCapacity().getName()
        except AttributeError, e:
          capacity = 'None'


        targets = cmo.getTargets()
        serverTarget = ''
    
        for target in targets:
          serverTarget = serverTarget + target.getName() + ':' + target.getType() + '|'

        print('# Work Manager: ' + str(name) )
        print('# Max Constraint : ' + str(max) )
        print('# Min Constraint : ' + str(min) )
        print('# Request Class : ' + str(reqClass) )
        print('# Capacity : ' + str(capacity) )
        print('\n')
      
        #if str(count) == 'None':
        #  count = ''
        if str(serverTarget) == 'None':
          serverTarget = ''
      
        exp = 'workManager,' + str(name) + ',' + str(max) + ',' + str(min) + ',' + str(reqClass) + ',' + str(capacity) + '\n'
        file.write(exp)
  except Exception, e:
    print e


def main():

    from java.io import FileInputStream
    propInputStream = FileInputStream(sys.argv[1])
    configProps = Properties()
    configProps.load(propInputStream)

    url=configProps.get("adminUrl")
    username = configProps.get("importUser")
    password = configProps.get("importPassword")
    csvLoc = configProps.get("csvLoc")

    connect(username,password,url)
  
    #print('======= Export Work Manager =======\n')  
  
    file=open(csvLoc, 'a+')
  
    print('======== Export Minimum Threads Constraint ========')
    exportMin(file)
    print('----- End of Minimum Threads Constraint -----\n')
    print('======== Export Maximum Threads Constraint ========')
    exportMax(file)
    print('----- End of Maximum Threads Constraint -----\n')
    print('======== Export Capacity Constraint ========')
    exportCap(file)
    print('----- End of Capacity Constraint -----\n')
    print('======== Export Response Time Request Class ========')
    exportRes(file)
    print('----- End of Response Time Request Class -----\n')
    print('======== Export Fair Share Request Class ========')
    exportFair(file)
    print('----- End of Response Time Request Class -----\n')
    print('======== Export Context Request Class ========')
    exportCon(file)
    print('----- End of Context Request Class -----\n')
    print('======== Export Work Manager ========')
    exportWM(file)
    print('----- End of Work Manager -----\n')
            
    disconnect()

main()
