#!/usr/local/bin/python3

import sys
from bs4 import BeautifulSoup
import requests
import time
import subprocess
import json
#import urllib.request
import urllib
import os
import itertools
import distutils.dir_util
import shutil

#GitHub seems to require me to log in now to search the repos
#def loginToGitHub(session):

  #url = 'https://github.com/session' 
  #session.get(url)
  #response = BeautifulSoup(session.get(url).content,'html.parser')
  #token = response.find("input", {'name': "authenticity_token"})['value']
  #hidden = response.find("input", {'name': 'utf8'})['value']
  #print(token)
  #login_data = dict(login_field='ZackC', password='cde3XSW@zaq1', authenticity_token=token, utf8=hidden)
  #with session.post(url, data=login_data) as r:
  #  print(r)
  #  print(r.cookies)
    #print(session.cookies)
  #next four lines are repeated here for testing - delete later
  #time.sleep(1)
  #urlToSearch='https://github.com/search?l=Java&q=onCreate+&type=Code'
  #print(r.cookies)
  #print(session.cookies)
  #session.cookies['logged_in'] = 'yes'
  #print(session.cookies)
  #response = session.get(urlToSearch).content.decode('utf-8')
  #for line in response.splitlines():
  #  print(line)

#with requests.Session() as session:
#loginToGitHub(session)


runFlowDroidCommand= '/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/bin/java "-javaagent:/Applications/IntelliJ IDEA CE.app/Contents/lib/idea_rt.jar=59095:/Applications/IntelliJ IDEA CE.app/Contents/bin" -Dfile.encoding=UTF-8 -classpath /Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib/charsets.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib/deploy.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib/ext/cldrdata.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib/ext/dnsns.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib/ext/jaccess.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib/ext/jfxrt.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib/ext/localedata.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib/ext/nashorn.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib/ext/sunec.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib/ext/sunjce_provider.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib/ext/sunpkcs11.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib/ext/zipfs.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib/javaws.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib/jce.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib/jfr.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib/jfxswt.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib/jsse.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib/management-agent.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib/plugin.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib/resources.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib/rt.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/lib/ant-javafx.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/lib/dt.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/lib/javafx-mx.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/lib/jconsole.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/lib/packager.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/lib/sa-jdi.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/lib/tools.jar:/Users/zack/git/DirectiveTool/FlowDroidTest/target/scala-2.12/classes:/Users/zack/.sbt/boot/scala-2.12.7/lib/scala-library.jar:/Users/zack/git/FlowDroid/soot-infoflow-android/lib/junit.jar:/Users/zack/git/FlowDroid/soot-infoflow-android/lib/org.hamcrest.core_1.3.0.jar:/Users/zack/git/FlowDroid/soot-infoflow-android/lib/protobuf-java-2.5.0.jar:/Users/zack/git/FlowDroid/soot-infoflow/lib/cos.jar:/Users/zack/git/FlowDroid/soot-infoflow/lib/j2ee.jar:/Users/zack/git/FlowDroid/soot-infoflow/lib/junit.jar:/Users/zack/git/FlowDroid/soot-infoflow/lib/org.hamcrest.core_1.3.0.jar:/Users/zack/.ivy2/cache/commons-io/commons-io/jars/commons-io-2.6.jar:/Users/zack/.ivy2/cache/com.google.guava/guava/bundles/guava-18.0.jar:/Users/zack/.ivy2/cache/com.beust/jcommander/jars/jcommander-1.64.jar:/Users/zack/.ivy2/cache/com.google.code.findbugs/jsr305/jars/jsr305-1.3.9.jar:/Users/zack/.ivy2/cache/org.smali/dexlib2/jars/dexlib2-2.2.5.jar:/Users/zack/.ivy2/cache/org.smali/util/jars/util-2.2.2.jar:/Users/zack/.ivy2/cache/xmlpull/xmlpull/jars/xmlpull-1.1.3.4d_b4_min.jar:/Users/zack/.ivy2/cache/xerces/xmlParserAPIs/jars/xmlParserAPIs-2.6.2.jar:/Users/zack/.ivy2/cache/org.slf4j/slf4j-simple/jars/slf4j-simple-1.7.5.jar:/Users/zack/.ivy2/cache/org.slf4j/slf4j-api/jars/slf4j-api-1.7.5.jar:/Users/zack/.ivy2/cache/org.ow2.asm/asm-debug-all/jars/asm-debug-all-5.2.jar:/Users/zack/.ivy2/cache/net.sf.trove4j/trove4j/jars/trove4j-3.0.3.jar:/Users/zack/git/soot/target/scala-2.12/classes:/Users/zack/git/heros/target/scala-2.12/classes:/Users/zack/git/FlowDroid/soot-infoflow/target/scala-2.12/classes:/Users/zack/git/soot/src/main/target/scala-2.12/classes:/Users/zack/git/DirectiveTool/FlowDroidTest/out/production/arrayclone:/Users/zack/git/FlowDroid/soot-infoflow-summaries/target/scala-2.12/classes:/Users/zack/git/DirectiveTool/FlowDroidTest/out/production/ca.mcgill.sable.soot:/Users/zack/git/DirectiveTool/FlowDroidTest/out/production/test:/Users/zack/git/FlowDroid/soot-infoflow-android/target/scala-2.12/classes:/Users/zack/git/DirectiveTool/FlowDroidTest/out/production/axml:/Users/zack/git/FlowDroid/soot-infoflow-cmd/target/scala-2.12/classes DetectMissingSetHasOptionsMenu'


#I should consider putting the created files in there own directory so it
#is easier to keep track of them if the script fails without deleting the files
createdFileListToDelete = []
methodsToCompare = []
methodDeclarationStringToCompare = "public void onCreate" 

def saveLines(linesToSave, nestingCount, line): 
  linesToSave.append(line)
  savingLines = True
  for c in line:
    if c == '{':
      nestingCount = nestingCount + 1
    if c == '}':
      nestingCount = nestingCount - 1
  return (linesToSave, nestingCount)

def extractOriginalMethodsOfInterest():
  #I was going to search all Java files in the original project, 
  #but then I remembered that the checker prints out the file 
  #name with the problem, so finding all methods isn't needed
  #
  #I will need to later extract the file name of interest from the 
  #error message, but I'll hard code it now for development speed
  #since I probably need to make it easier to extract the class
  #name from the error message before I write code to extract the 
  #error message
  #
  #originalApplicationLocation = "/Users/zack/git/DirectiveTool/testFolder"
  #filesOfInterest = []j
  #for root, directories, filenames = os.walk(originalApplicationLocation):
    #for file in filenames:
      #if file.endswith('.java'):
        #Can't remember if I need to add the path seperator betweeen the
        #two variables or not
        #filesOfInterest.append(root+os.path.sep+file)
  fileToExtractFrom = "/Users/zack/git/DirectiveTool/testFolder/Application/src/main/java/com/example/android/lnotifications/HeadsUpNotificationFragment.java"
  with open(fileToExtractFrom,'r') as fin:
    nestingCountWasGreaterThanZero = False
    nestingCount = 0
    linesToSave = []
    foundMethodOfInterest = False
    for line in fin:
      if foundMethodOfInterest or nestingCount > 0:
        (linesToSave, nestingCount) = saveLines(linesToSave, nestingCount, line)
        #only use foundMethodOfInterest until we find the first { of the method
        if nestingCount > 0:
          nestingCountWasGreaterThanZero = True
          foundMethodOfInterest = False
              #this string check captures both the onCreate method and the onCreateOptionsMenu method
      elif methodDeclarationStringToCompare in line:
        methodName = line.split()[2].split('(')[0]
        (linesToSave, nestingCount) = saveLines(linesToSave, nestingCount, line)
        foundMethodOfInterest = True
        if nestingCount > 0:
          nestingCountWasGreaterThanZero = True
      elif nestingCountWasGreaterThanZero:
        nestingCountWasGreaterThanZero = False
        methodsToCompare.append(methodName)
        newFileName = 'original_{0}.txt'.format(methodName)
        createdFileListToDelete.append(newFileName)
        with open(newFileName,'w') as fout:
          for line in linesToSave:
            fout.write(line)
            #can't remember if the extra \n is needed. I should test and see
            #- tested and doesn't seem to be necessary here
            #fout.write('\n')
            linesToSave = []

def handleDiff(changeSet):
  for method in methodsToCompare:
    originalFileName = "original_{0}.txt".format(method)
    downloadedFileName = "downloaded_{0}.txt".format(method)
    commandList = ["diff", originalFileName, downloadedFileName]
    #diff returns a failure if the files are different, so setting
    #check to False so the code doesn't die with the files are not
    #equal
    commandOutput = subprocess.run(commandList, check=False, stdout=subprocess.PIPE).stdout.decode('utf-8') 
    #currently changes are just what others have added to the method
    #will need to improve the generality of this later
    for line in commandOutput.splitlines():
      #avoid checking if the methods are declared slightly differently
      if line.startswith('>') and not methodDeclarationStringToCompare in line:
        change = line[1:].strip()
        changeSet.add((change,method))
    #print(len(changeSet))
    for (change, method) in changeSet:
      print("found change: {0} in method {1}".format(change, method))
    #print(commandOutput)
    #print("")
  return changeSet

def addChangeToFile(change, method):
  #need to go back later and remove the common paths in the two different path variables 
  fileToChange = "/Users/zack/git/DirectiveTool/temporaryTestOfChange/Application/src/main/java/com/example/android/lnotifications/HeadsUpNotificationFragment.java" 
  fileContents = []
  with open(fileToChange,'r') as fin:
    fileContents = fin.read().splitlines()
  foundMethodOfInterest = False
  nestingCount = 0
  for lineCount, line in enumerate(fileContents):
    methodDeclaration = "public void {0}".format(method)
    if foundMethodOfInterest or nestingCount > 0:
      #use nesting count if they are both true
      if nestingCount > 0:
        foundMethodOfInterest = False
      for c in line:
        if c == '{':
          nestingCount = nestingCount + 1
        elif c == '}':
          nestingCount = nestingCount - 1
          if nestingCount < 1:
            print("inserting {0} into position {1}".format(change, lineCount))
            fileContents.insert(lineCount, change)
            print("inserted value: {0}".format(fileContents[lineCount]))
            #print(fileContents)
            with open(fileToChange,'w') as fout:
              for line in fileContents:
                #\n's are needed here
                fout.write(line)
                fout.write('\n')
            # we added the change to the end of the method, so we are done
            return
    elif line.strip().startswith(methodDeclaration):
      foundMethodOfInterest = True
      for c in line:
        if c == '{':
          nestingCount = nestingCount + 1
        elif c == '}': 
          nestingCount = nestingCount - 1

def testChanges(changeSet):
  #for all subsets of the changes
  for changeItem in itertools.chain.from_iterable(itertools.combinations(changeSet,n) for n in range(len(changeSet)+1)):
    #create a new directory if necessary
    #copy the application to the new directory
    print("starting directory: {0}".format(os.getcwd()))
    path = "/Users/zack/git/DirectiveTool/temporaryTestOfChange"
    if os.path.exists(path):
      shutil.rmtree(path)
    #try: 
    #  os.makedirs(path)
    #except OSError as e:
    #  print("Creation of the directory {0} failed".format(path))
    #  print(e)
    #  sys.exit(1)
    #distutils.dir_util.copy_tree("/Users/zack/git/DirectiveTool/testFolder/",path)
    shutil.copytree("/Users/zack/git/DirectiveTool/testFolder/",path)
    if len(changeItem) > 0:
      for (change, method) in changeItem:
        addChangeToFile(change, method)
        #essentially breaking the code here with the return - done for debugging
      print("before ant build")
      currentDir = os.getcwd()
      os.chdir(path)
      print("current directory: {0}".format(os.getcwd()))

      commandList = ['./gradlew','assembleDebug']
      commandSucceeded = False
      try: 
        commandOutput = subprocess.run(commandList, stderr=subprocess.PIPE, stdout=subprocess.PIPE, check=True)
        print(commandOutput.stdout)
        print(commandOutput.stderr)
      except:
        #try out the next change
        os.chdir(currentDir)
        continue
      # I need to split by space but not on quoted parts of the string
      unquotedAndQuotedList = runFlowDroidCommand.split('"')
      commandList = []
      for index, item in enumerate(unquotedAndQuotedList):
        if index % 2 == 0:
          #these should be the unquoted parts of the command
          commandList.extend(item.strip().split(' '))
        else:
          commandList.append("{0}".format(item))
      newAPKLocation = '/Users/zack/git/DirectiveTool/temporaryTestOfChange/Application/build/outputs/apk/debug/Application-debug.apk'
      commandList.append(newAPKLocation)
      try: 
        print("current directory for command: {0}".format(os.getcwd()))
        os.chdir("/Users/zack/git/DirectiveTool/FlowDroidTest")
        commandOutput = subprocess.run(commandList, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        #print(commandOutput)
        #print(commandOutput.stderr)
        for line in commandOutput.stderr.decode('utf-8').splitlines():
          print(line)
        for line in commandOutput.stdout.decode('utf-8').splitlines():
          print(line)
          if line.startswith('total number of caught problems:'):
            lineItems = line.split(' ')
            if int(lineItems[-1]) == 0:
              commandSucceeded = True
      except: 
        pass
      os.chdir(currentDir)
      if commandSucceeded: 
        #print("succeeded - change: {0}, method {1}".format(change, method))
        print("succeeded - change: added {0} to the end of method {1}".format(change, method))
        return 
    #add the change to the method call of the copied app
    #run the application and see if it still produces the problem
    #if the application does not produce the problem, then print the change
    #that fixed the issue and stop



extractOriginalMethodsOfInterest()
shouldLoadFromWebsite = True
saveFileName = 'savedSearch.json'
pageNumber = 1
notDone = True
changeSet = set()
while notDone: 
  if shouldLoadFromWebsite: 
    print('downloading page number: {0}'.format(pageNumber))
    command = 'curl -n https://api.github.com/search/code?q=onCreate+Fragment+onCreateOptionsMenu+in:file+language:java?page={0}&per_page=100&sort=stars&order=desc'.format(pageNumber)
    commandList = command.split(" ")
    commandOutput = subprocess.run(commandList, check=True, stdout=subprocess.PIPE).stdout.decode('utf-8') 
    searchResult = json.loads(commandOutput)
    with open(saveFileName,'w') as fout:
      json.dump(searchResult,fout)
  else: 
    print('loading page from file')
    with open(saveFileName,'r') as fin:
      searchResult = json.loads(fin.read())

  #print(searchResult['total_count'])
  currentCount = 0
  pageLimit = 100
  while notDone and currentCount < pageLimit - 1:
    containsFragment = False
  #urlToSearch='https://github.com/search?l=Java&q=onCreate+&type=Code'
  #response = session.get(urlToSearch).content.decode('utf-8')
  #print(type(response))
  #print(response)
  #with open('searchResult.txt','w') as fout:
  #print('start of page')
  #for line in response.splitlines():
  #  print(line)
  #print('end of page')
      #if('java' in line.decode('utf-8')):
      #  print(line)
      #fout.write(line.decode("utf-8"))

    currentCount = currentCount + 1
    urlToSearch = searchResult['items'][currentCount]['html_url']
    #print(searchResult['items'][currentCount])
    #print(urlToSearch)
    if urlToSearch.endswith('.java'):
      #response = session.get(urlToSearch).content.decode('utf-8')
      #soup = BeautifulSoup(response, 'html.parser')
      #for link in soup.find_all('a'):
        #print(link.contents)
      #  if(link.contents[0].endswith('.java')):
      time.sleep(1)
      #pageRequest = session.get(urlToSearch).content
      with urllib.request.urlopen(urlToSearch) as pageRequest:
        #read is read once, so save the result
        pageResult = pageRequest.read()
        soup2 = BeautifulSoup(pageResult, 'html.parser')
        rawLink = soup2.find_all(id='raw-url')[0]
        time.sleep(1)
        #print('raw link: {0}'.format(rawLink))
        rawLinkString = "https://github.com/" + rawLink['href']
        print('raw link string: {0}'.format(rawLinkString))
        with urllib.request.urlopen(rawLinkString) as finalResults:
          programOfInterest = finalResults.read().decode('utf-8')
          lookingForFragment = True
          lineIndex = 0 
          linesInProgram = programOfInterest.splitlines()
          while lookingForFragment and lineIndex < len(linesInProgram):
            line = linesInProgram[lineIndex]
            if ' Fragment ' in line:
              print('found fragment: {0}'.format(line))
              lookingForFragment = False
              containsFragment = True
            lineIndex = lineIndex + 1
          if not lookingForFragment: 
            savingLines = False
            linesToSave = []
            nestingCount = 0
            nestingCountWasGreaterThanZero = False
            methodName = ""
            createdFiles = False
            foundMethodOfInterest = False
            for line in programOfInterest.splitlines():
              #print(line)
              if foundMethodOfInterest or nestingCount > 0:
                (linesToSave, nestingCount) = saveLines(linesToSave, nestingCount, line)
                # only use foundMethodOfInterest until we find the first {
                if nestingCountWasGreaterThanZero > 0:
                  nestingCountWasGreaterThanZero = True
                  foundMethodOfInterest = False
              #this string check captures both the onCreate method and the onCreateOptionsMenu method
              elif methodDeclarationStringToCompare in line:
                methodName = line.split()[2].split('(')[0]
                (linesToSave, nestingCount) = saveLines(linesToSave, nestingCount, line)
                foundMethodOfInterest = True
                if nestingCount > 0:
                  nestingCountWasGreaterThanZero = True
              elif nestingCountWasGreaterThanZero:
                nestingCountWasGreaterThanZero = False
                newFileName = 'downloaded_{0}.txt'.format(methodName)
                createdFileListToDelete.append(newFileName)
                with open(newFileName,'w') as fout:
                  for line in linesToSave:
                    fout.write(line)
                    #can't remember if the extra \n is needed. I should test and see
                    #tested and seem to be required here
                    fout.write('\n')
                  createdFiles = True
                linesToSave = []
            if createdFiles:
              changeSet = handleDiff(changeSet)
              testChanges(changeSet)
              notDone = False
  if not containsFragment: 
    print('page {0} does not contain any Fragments!!!'.format(pageNumber))
  pageNumber = pageNumber + 1
#for f in createdFileListToDelete:
  #This is a quick and hacky solution to speed up development without digging
  #into the issue;
  #You should probably figure out why the script is trying to delete files
  #that don't exist later
#  try:
#    os.remove(f)
#  except:
#    pass