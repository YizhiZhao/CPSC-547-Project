# CPSC-547-Project

## Tests
### Trotter Step Scan
```
$ python evaluator.py
[backend] jakarta simulator
trotter_steps 4: fidelity = 0.11996016014283366 stderr = 0.0015499067997510497
trotter_steps 5: fidelity = 0.3158818146716372 stderr = 0.002447519969498689
trotter_steps 6: fidelity = 0.30448678435450605 stderr = 0.001955535878056974
trotter_steps 7: fidelity = 0.2764555744788494 stderr = 0.0016123564169305364
trotter_steps 8: fidelity = 0.45680129284056037 stderr = 0.00166610745947065
trotter_steps 9: fidelity = 0.3306099697646332 stderr = 0.0024108145543288847
trotter_steps 10: fidelity = 0.14395662859344904 stderr = 0.0010112370413819637
trotter_steps 11: fidelity = 0.13107957102976464 stderr = 0.0011502621445309265
trotter_steps 12: fidelity = 0.1407873154245824 stderr = 0.0014266364689778186
```
we can observe that the maximum fidelity is reached at ``trotter_steps = 8``

### Jakarta Simulator
When ``trotter_steps = 8``:
```
$ python evaluator.py
[backend] jakarta simulator
intermediate_trottor 1: fidelity = 0.7134578302122792 stderr = 0.0032937811022523086
intermediate_trottor 2: fidelity = 0.6489722313168782 stderr = 0.002736124567216378
intermediate_trottor 3: fidelity = 0.5920921942044766 stderr = 0.0016621665270982228
intermediate_trottor 4: fidelity = 0.5939738859564838 stderr = 0.001366084381173871
intermediate_trottor 5: fidelity = 0.5410491142948255 stderr = 0.0024117056958478083
intermediate_trottor 6: fidelity = 0.47612003326309804 stderr = 0.0017785771219324682
intermediate_trottor 7: fidelity = 0.42314728791355805 stderr = 0.0019457327674416226
intermediate_trottor 8: fidelity = 0.4571349823963583 stderr = 0.001570429326096145
[grade] fidelity = 0.42314728791355805
```