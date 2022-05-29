## DFT matrix 

$$
U = \frac{1}{\sqrt n}
\left(\begin{array}\\
\omega_n^{-0\times0} & \omega_n^{-0\times1} & \dots & \omega_n^{-0\times (n-1)}\\
\omega_n^{-1\times0} & \omega_n^{-1\times1} & \dots & \omega_n^{-1\times (n-1)}\\
\vdots & \vdots & \ddots & \vdots\\
\omega_n^{-(n-1)\times0} & \omega_n^{-(n-1)\times1} & \dots & \omega_n^{(n-1)\times -(n-1)}\\
\end{array}\right)\\
\\
U \text{ is unitary}
$$


$$
\\
\\
\forall i,j \in \Z, 0\le i,j<n\\
\sum_{k=0}^{n-1} \overline{\omega_n^{ik}} \omega_n^{jk} = \sum_{k=0}^{n-1} \omega_n^{(j-i)k}\\
\sum_{k=0}^{n-1} \overline{\omega_n^{ik}} \omega_n^{jk} = 0 \iff i=j\\
$$



DFT : $2^n$ 个经典 bit 储存 $v_0, \dots v_{2^n-1}$ ，单次操作需要进行 $O(n2^n)$ 次运算

QFT : $n$ 个 qubuit 用叠加态表示 $\ket{\psi} = v_0\ket{00\dots0} + v_1\ket{00\dots1} + \dots + v_{2^n-1}\ket{11\dots1}$ ，单次操作需要 $n^2$ 个量子门



（广义的）周期识别：

$1\le r<n,\ 0\le x<r,\ n^2\le Q=2^q < 2n^2$

若 $v = \frac{1}{C} \sum_{i=0}^{Q/r} \ket {ir+x}$ ，考虑dft后 $b_j$ 的值
$$
\begin{aligned}
b_j &= C\sum_{k=0}^{Q-1} \omega_Q^{-jk} v_k\\
&= C\sum_{i=0}^{Q/r} \omega_Q^{-j(ir+x)}\\
\\
|b_j|^2 &= C^2\left|\sum_{i=0}^{Q/r} (\omega_Q^{-jr})^i\right|^2\\
\omega &= \omega_Q^{-jr}\\
|b_j|^2 &= C^2\left|\frac{1-\omega^{Q/r+1}}{1-\omega}\right|^2\\
\\
\exists j_1,j_2,\dots j_{Q/r},\quad &j_i r\ \mathrm{mod}\ Q < \frac{r}{2}\\
\alpha &= \sum |b_{j_i}|^2
\end{aligned}
$$

当 $r \mid Q$ 时，$\alpha=1$ ，其他时候观察发现 $\alpha > 0.773$





根据数论知识，只需要坍缩到 $r$ 的倍数即可



## 如何用量子电路描述 $\Z_N$ 上的乘法？

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







