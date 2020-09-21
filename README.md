# smartPY_to_MICHELSON_converter

### Converting SmartPY contract to SMLSE expression
* Go to smartpyTOsmlse.py file
* Simply add Two inputs to initiate the process on line 47 and 48
```
 
filename = "CryptoBot.py" (SmartPY contract file)

class_call = "Cryptobot(sp.address('tz1aoQSwjDU4pxSwT5AsBiK5Xk15FWgBJoYr'),True)" 
(Parameters to initiate the Contract Class)
```
* Run python3 smartpyTOsmlse.py


### Converting SMLSE to Michelson Code
* In order to get the Michelson code, we need to pass SMLSE of the particular contract as input.

* Go to smartmlbasics.js
* Change file name in the smlseToMichelsonConverter function

```
function smlseToMichelsonConverter(){
  const s_expr = fs.readFileSync('Cryptobot.py.smlse', 'utf8');
  // console.log(s_expr)
  try {
    const contract = smartml.importContract(s_expr);
    // console.log(contract)
    const compiledContract = smartml.compileContract(contract);
    const michelsonCode = smartml.compiledContract_to_michelson(compiledContract);
    console.log(michelsonCode);
  }
  catch(exn) {
    console.error("Exception while handling " + args[1])
    console.error(smartml.stringOfException(false, exn));
    process.exit(1)
  }
}
```
* Run node smartmlbasics.js
