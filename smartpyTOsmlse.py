## Copyright 2019 Smart Chain Arena LLC. ##

import browser
import smartpyio
import argparse
import os
import json
from version import version
from urllib.request import urlopen

def compileContract(contract, targetBaseFilename = None, targetDirectory = None, targetSmlse = None, targetCode = None, targetStorage = None, targetTypes = None):
  
    import subprocess
    if targetDirectory is None and targetBaseFilename is not None:
        targetDirectory = os.path.dirname(targetBaseFilename)
    if targetDirectory is not None:
        os.makedirs(targetDirectory, exist_ok = True)
        if targetBaseFilename is None:
            targetBaseFilename = targetDirectory + "/contract"
    if targetBaseFilename is not None:
        if targetSmlse is None:
            targetSmlse = targetBaseFilename + "Expression.smlse"
        if targetCode is None:
            targetCode = targetBaseFilename + "Code.tz"
        if targetStorage is None:
            targetStorage = targetBaseFilename + "Storage.tz"
        if targetTypes is None:
            targetTypes = targetBaseFilename + "Types.tz"

    if targetSmlse is not None:
        open(targetSmlse, 'w').write(contract.export())
        command = ["node", os.path 
.dirname(os.path.realpath(__file__)) + "/smartmlbasic.js",]
        for (opt, arg) in [("--compile", targetSmlse), ("--targetCode", targetCode), ("--targetStorage", targetStorage), ("--targetTypes", targetTypes)]:
            if arg is not None:
                os.makedirs(os.path.dirname(arg), exist_ok = True)
                command += [opt, arg]
        subprocess.run(command)

if __name__ == "__main__":


    # filename = "demo.py"
    # class_call = "MyContract(50,80)"

    filename = "CryptoBot.py"
    class_call = "Cryptobot(sp.address('tz1aoQSwjDU4pxSwT5AsBiK5Xk15FWgBJoYr'),True)"

    if filename.startswith("http"):
        code = urlopen(args.filename).read().decode("utf8")
    else:
        code = open(filename, 'r').read()

    adaptedCode = smartpyio.adaptBlocks(code)
    context = globals()
    context['alert'] = browser.alert
    context['window'] = browser.window

    compiledCode = compile(adaptedCode, filename, 'exec')
    # print(compiledCode)
    exec(compiledCode, context)
    # print(type(num)
   
    print("_"*40)
        

    if class_call is not None:
        contract = eval(class_call, context)
    else:
        print("Class initial parameter NOT Provided")
    
    print("SMLSE EXPRESSION:",contract.export())
    
