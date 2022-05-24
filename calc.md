### 加法器

$$
\ket{\phi(a)} = QFT \ket{a} = \frac{1}{\sqrt{2^n}} \sum_{j=0}^{2^n-1} \omega_Q^{aj} \ket j\\
$$

Draper 加法器：$\ket b \mapsto \ket{(b+a)\ \mathrm{mod}\ 2^q}$

QFT -> 相移 -> IQFT



Beauregard 加法器：$\ket b \mapsto \ket{(b+a)\ \mathrm{mod}\ N}$

先扩展一位，使 $N \le 2^{q-1}$ ，还需要一位辅助位，设为 $\ket 0$

step0 : $\ket b \otimes \ket 0$

step1 : $\mapsto \ket{(b+a-N)\ \mathrm{mod}\ 2^{q}} \otimes \ket{0}$

step2 : $\mapsto \ket{(b+a-N)\ \mathrm{mod}\ 2^{q}} \otimes \ket{[b+a-N<0]}$

step3 : $\mapsto \ket{(b+a)\ \mathrm{mod}\ N}\otimes \ket{[b+a-N<0]}$

step4 : $\mapsto \ket{(b+a)\ \mathrm{mod}\ N-a}\otimes \ket{[b+a-N<0]}$

step5 : $\mapsto \ket{(b+a)\ \mathrm{mod}\ N-a}\otimes \ket 0$

step6 : $\mapsto \ket{(b+a)\ \mathrm{mod}\ N}\otimes \ket 0$



有两种情况：

case1 : $b+a\ge N$，

$(b+a)\ \mathrm{mod}\ N = b+a-N$

$b+a-N\ge 0$

$(b+a)\ \mathrm{mod}\ N-a = b-N < 0$



case2 : $b+a<N$，

$(b+a)\ \mathrm{mod}\ N = b+a$

$b+a-N<0$

$(b+a)\ \mathrm{mod}\ N-a = b > 0$



因此，我们可以构造Beauregard 加法器：$\ket b \otimes \ket 0 \mapsto \ket{(b+a)\ \mathrm{mod}\ N} \otimes \ket 0$







