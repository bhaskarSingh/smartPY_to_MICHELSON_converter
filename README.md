# smartPY_to_MICHELSON_converter
# smartPY to Michelson Converter

### Converting SmartPY contract to SMLSE expression
* Go to smartpyTOsmlse.py file
* Simply add Two inputs to initiate the process on line 47 and 48
```
 
filename = "CryptoBot.py" (SmartPY contract file)

class_call = "Cryptobot(sp.address('tz1aoQSwjDU4pxSwT5AsBiK5Xk15FWgBJoYr'),True)" 
(Parameters to initiate the Contract Class)
```
* Run python3 smartpyTOsmlse.py

**Output: SMLSE Expression**
```
SMLSE EXPRESSION: 
(storage (record -1 (myParameter1 (literal (intOrNat 20) -1)) (myParameter2 (literal (intOrNat 21) -1)))
messages ((myEntryPoint ((verify (le (attr (data) "myParameter1" -1) (literal (intOrNat 123) -1) -1) False -1) (set (attr (data) "myParameter1" -1) (add (attr (data) "myParameter1" -1) (params -1) -1) -1))))
flags())


```


### Converting SMLSE to Michelson Code
* In order to get the Michelson code, we need to pass SMLSE of the particular contract as input.

* Go to smartmlbasics.js
* Update the File Path to the desired SMLSE expression file

```
var file_Path = './smlse_expr_files/CryptoBot.py.smlse'

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

**Output: Michelson Code**
```
smartmlbasic.js
parameter int;
storage   (pair (int %myParameter1) (int %myParameter2));
code
  {
    DUP;        # pair(params, storage).pair(params, storage)
    CDR;        # storage.pair(params, storage)
    SWAP;       # pair(params, storage).storage
    CAR;        # params.storage
    # Entry point: myEntryPoint # params.storage
    # sp.verify(self.data.myParameter1 <= 123) # params.storage
    PUSH int 123; # int.params.storage
    DIG 2;      # storage.int.params
    DUP;        # storage.storage.int.params
    DUG 3;      # storage.int.params.storage
    CAR;        # int.int.params.storage
    COMPARE;    # int.params.storage
    LE;         # bool.params.storage
    IF
      {}
      {
        PUSH string "WrongCondition: self.data.myParameter1 <= 123"; # string.params.storage
        FAILWITH;   # FAILED
      }; # params.storage
    # self.data.myParameter1 += params # params.storage
    SWAP;       # storage.params
    DUP;        # storage.storage.params
    DUG 2;      # storage.params.storage
    CDR;        # int.params.storage
    SWAP;       # params.int.storage
    DUP;        # params.params.int.storage
    DUG 2;      # params.int.params.storage
    DIG 3;      # storage.params.int.params
    DUP;        # storage.storage.params.int.params
    DUG 4;      # storage.params.int.params.storage
    CAR;        # int.params.int.params.storage
    ADD;        # int.int.params.storage
    PAIR;       # pair int int.params.storage
    DUG 2;      # params.storage.pair int int
    DROP;       # storage.pair int int
    DROP;       # pair int int
    NIL operation; # list operation.pair int int
    PAIR;       # pair (list operation) (pair int int)
  } # pair (list operation) (pair int int)


```
