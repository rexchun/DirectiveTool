#!/bin/bash

#manual set up steps currently required
#1. Change the Violations of directives repo to the right application to fix
#2. create the APK for the application (the code here should also do this if you skip this step, 
#.  but I haven't checked and I'm not 100% sure)
#3. change the programName variable in the runChecker function 
#4. run this file to make sure everything is set up correctly
#5. change the method declaration string to compare in repairMethodFromExampleOnGitHub.py 
# to the callback of interest
#6. change the checkerToRun variable in the repairMethodFromExampleOnGitHub
#7. change the fileToChange if required
#8. change the search (curl) command around line 730 (I say around because I keep adding 
#.  and deleting lines, so the line count may not be exactly correct)
#9. Might need to change all the paths in repairMethodFromExample.. to your path settings
#10. Delete the savedGitHubSearches folder unless the search query remained the same 
#.   or you can reuse the old results
#11. repairMethodExampleOnGitHub.. is now ready to run

#call with the file to save the check results to as the first parameter
function runChecker
{
previousDir=`pwd`
cd ~/git/DirectiveTool/FlowDroidTest
#programName=DetectMissingSetHasOptionsMenu
#programName=DetectSetArgumentsMain
programName=DetectInvalidInflateCallMain
/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/bin/java "-javaagent:/Applications/IntelliJ IDEA CE.app/Contents/lib/idea_rt.jar=59095:/Applications/IntelliJ IDEA CE.app/Contents/bin" -Dfile.encoding=UTF-8 -classpath /Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib/charsets.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib/deploy.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib/ext/cldrdata.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib/ext/dnsns.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib/ext/jaccess.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib/ext/jfxrt.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib/ext/localedata.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib/ext/nashorn.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib/ext/sunec.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib/ext/sunjce_provider.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib/ext/sunpkcs11.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib/ext/zipfs.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib/javaws.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib/jce.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib/jfr.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib/jfxswt.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib/jsse.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib/management-agent.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib/plugin.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib/resources.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/jre/lib/rt.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/lib/ant-javafx.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/lib/dt.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/lib/javafx-mx.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/lib/jconsole.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/lib/packager.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/lib/sa-jdi.jar:/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home/lib/tools.jar:/Users/zack/git/DirectiveTool/FlowDroidTest/target/scala-2.12/classes:/Users/zack/.sbt/boot/scala-2.12.7/lib/scala-library.jar:/Users/zack/git/FlowDroid/soot-infoflow-android/lib/junit.jar:/Users/zack/git/FlowDroid/soot-infoflow-android/lib/org.hamcrest.core_1.3.0.jar:/Users/zack/git/FlowDroid/soot-infoflow-android/lib/protobuf-java-2.5.0.jar:/Users/zack/git/FlowDroid/soot-infoflow/lib/cos.jar:/Users/zack/git/FlowDroid/soot-infoflow/lib/j2ee.jar:/Users/zack/git/FlowDroid/soot-infoflow/lib/junit.jar:/Users/zack/git/FlowDroid/soot-infoflow/lib/org.hamcrest.core_1.3.0.jar:/Users/zack/.ivy2/cache/commons-io/commons-io/jars/commons-io-2.6.jar:/Users/zack/.ivy2/cache/com.google.guava/guava/bundles/guava-18.0.jar:/Users/zack/.ivy2/cache/com.beust/jcommander/jars/jcommander-1.64.jar:/Users/zack/.ivy2/cache/com.google.code.findbugs/jsr305/jars/jsr305-1.3.9.jar:/Users/zack/.ivy2/cache/org.smali/dexlib2/jars/dexlib2-2.2.5.jar:/Users/zack/.ivy2/cache/org.smali/util/jars/util-2.2.2.jar:/Users/zack/.ivy2/cache/xmlpull/xmlpull/jars/xmlpull-1.1.3.4d_b4_min.jar:/Users/zack/.ivy2/cache/xerces/xmlParserAPIs/jars/xmlParserAPIs-2.6.2.jar:/Users/zack/.ivy2/cache/org.slf4j/slf4j-simple/jars/slf4j-simple-1.7.5.jar:/Users/zack/.ivy2/cache/org.slf4j/slf4j-api/jars/slf4j-api-1.7.5.jar:/Users/zack/.ivy2/cache/org.ow2.asm/asm-debug-all/jars/asm-debug-all-5.2.jar:/Users/zack/.ivy2/cache/net.sf.trove4j/trove4j/jars/trove4j-3.0.3.jar:/Users/zack/git/soot/target/scala-2.12/classes:/Users/zack/git/heros/target/scala-2.12/classes:/Users/zack/git/FlowDroid/soot-infoflow/target/scala-2.12/classes:/Users/zack/git/soot/src/main/target/scala-2.12/classes:/Users/zack/git/DirectiveTool/FlowDroidTest/out/production/arrayclone:/Users/zack/git/FlowDroid/soot-infoflow-summaries/target/scala-2.12/classes:/Users/zack/git/DirectiveTool/FlowDroidTest/out/production/ca.mcgill.sable.soot:/Users/zack/git/DirectiveTool/FlowDroidTest/out/production/test:/Users/zack/git/FlowDroid/soot-infoflow-android/target/scala-2.12/classes:/Users/zack/git/DirectiveTool/FlowDroidTest/out/production/axml:/Users/zack/git/FlowDroid/soot-infoflow-cmd/target/scala-2.12/classes $programName > $1 2>/dev/null
cd $previousDir
}

#1. Get an app with a problem
#Currently, the app is located in ~/git/ViolationOfDirectives
testDir=/Users/zack/git/DirectiveTool/testFolder
originalAppDir=~/git/ViolationOfDirectives 
rm -rf $testDir
cp -r $originalAppDir $testDir

#2. run the tool to detect the problem
cd $testDir
#This next line seems to not be needed
#cd `basename $originalAppDir`
#print errors to terminal but not normal build messages
./gradlew assembleDebug >/dev/null
#The application will be built to the file /Users/zack/git/DirectiveTool/testFolder/Application/build/outputs/apk/debug/Application-debug.apk
initialTestFile=$testDir/initialTest.txt
runChecker $initialTestFile
#currently matching the line 'total number of caught problems: #'
#might need to change if other totals are printed
problemCount=$(awk '$1 ~ /^total/ {print $NF}' $initialTestFile)
echo "initial problem count: $problemCount"
#loop until the problem has been removed
if [ -z $problemCount ]
then 
  echo "Error: problemCount was not found after running checker"
  exit 1
fi
#while [ $problemCount -ne 0 ]
#do
#  echo "in loop"
#  sleep 2
#done




