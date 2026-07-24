"""predict.py — compute predicted F^3 trace integers from Sol Pro's published spectra
BEFORE measurement. Also exact-check their normalized s1 values against my F8 integers."""
from fractions import Fraction as F
import pickle
ts = pickle.load(open('checkpoints/trace_separation.pkl','rb'))
pred = {}

# --- s1 cross-checks (their fractions vs my exact level-1 traces) ---
chk = {}
chk[('17','s1')] = (ts[17]['TrU_p'] == 29*17**8)
chk[('23','s1')] = (F(ts[23]['TrU_p'], 23**12) == F(-235,529))          # 1 - 764/529
chk[('21','s1')] = (F(23*ts[23]['TrU_pm2'], 23**12) == F(326,529))       # 1 - 203/529
chk[('29','s1')] = (F(ts[29]['TrU_p'], 29**15) == F(-48674,24389))       # -a
chk[('27','s1')] = (F(29*ts[29]['TrU_pm2'], 29**15) == F(16745,24389))   # -a' = +16745/24389
print("s1 cross-checks vs my F8 integers:", chk)

# --- predicted Tr(F^3|U_k) ---
# dim 2, reciprocal: p3bar = e1^3 - 3 e1  (e2 = 1)
e1 = F(29,17); p3 = e1**3 - 3*e1
pred['U17'] = p3 * F(17)**27
pred['U15'] = 0
# dim 3: eps=+1 central, quadratic sum t
for name, t, w in (('U23', F(-764,529), 36), ('U21', F(-203,529), 33)):
    p3 = 1 + t**3 - 3*t
    pred[name] = p3 * F(23)**w
# dim 4 palindromic: p3bar = -a^3 + 3ab - 3a
for name, a, b, w in (('U29', F(48674,24389), F(1531538,707281), 45),
                      ('U27', F(-16745,24389), F(140088,707281), 42)):
    p3 = -a**3 + 3*a*b - 3*a
    pred[name] = p3 * F(29)**w
for k,v in pred.items():
    assert v.denominator == 1, (k, v)
    pred[k] = int(v)
    print(f"predicted Tr(F^3|{k}) = {pred[k]}")
pickle.dump(dict(pred=pred, s1_checks=chk), open('checkpoints/f3_predictions.pkl','wb'))
