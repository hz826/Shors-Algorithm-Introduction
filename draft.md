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

乘法酉矩阵：
$$
f(x) = a^x\ \mathrm{mod}\ N\\
U \ket{x,1} \mapsto \ket{x,f(x)}
$$




$2n$ 个 qubit，初始状态为 
$$
\ket\psi = \frac{1}{\sqrt{2^n}}\ \sum_{i=0}^{2^n-1} \ket{i,000\dots1}
$$


受控酉矩阵（一种可行的构造）：
$$
U_i : \ket{x,y} \mapsto \begin{cases}
\ket{x,(y\times a^{2^i})\ \mathrm{mod}\ N} & i \in x\ \text{ and }\ 1\le y <N\ \text{ and }\ \gcd(y,N)=1\\
\ket{x,y} & \text{otherwise}\\
\end{cases}
$$


乘法：
$$
\ket{\psi'} = U_{n-1}U_{n-2} \dots U_0 \ket\psi = \frac{1}{\sqrt{2^n}}\ \sum_{i=0}^{2^n-1} \ket{i,f(i)}
$$
QFT :
$$
\begin{aligned}
(Q\otimes I^{\otimes n}) \ket{\psi'} &= \frac{1}{2^n} \sum_{i=0}^{2^n-1} \sum_{j=0}^{2^n-1} \omega_n^{ij} \ket{j,f(i)}\\
\end{aligned}
$$

