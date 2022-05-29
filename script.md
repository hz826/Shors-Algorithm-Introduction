# PPT

## 引入

### 大数分解

我们可以很快地计算出两个大质数的乘积，但将两个大质数分解则是一个很难的问题



239 * 311 = 74329

71101 = ？211 * 337



计算两个1000位大质数的乘积，使用一台普通的电路，可以在1秒内得出结果，但是，将它分解成两个1000位大质数的乘积，使用现在最快的计算机，也需要？年的时间

（TODO: 数值待修改）



基于这个性质，我们得到了 RSA 公钥加密算法

>  如果得到了两个大质数 $p,q$ （可以通过素性测试简单得到），我们可以快速计算出 $n=pq$ 和 $\varphi(n)=(p-1)(q-1)$ ，而只知道 $n$，则很难求得 $\varphi(n)$
>
> 因此，我们可以定义公开的加密映射 $E: x\mapsto x^a \text{ mod } n$ 和通过公开信息难以求出的解密映射 $D=E^{-1}: x \mapsto x^{\text{inv}(a,\varphi(n))}\text{ mod } n$
>
> （这部分以图解的形式展示）



然而量子计算机理论上可以快速完成大数分解（量子计算的历史）

> 1900年，德国物理学家普朗克提出量子概念，从此“量子论”就宣告诞生。
> 1926年，薛定谔提出薛定谔方程，为量子力学奠定了坚实的基础。
> 1980年，保罗·贝尼奥夫在一篇论文中描述了第一台计算机的量子力学模型。
> 1981年，波士顿麻省理工名为“计算物理学”会议，被认为是量子计算的起源
> 1994年，彼得·肖尔开发的肖尔算法问世，它被认为是量子计算历史上的一个里程碑。该算法允许量子计算机以更高的速度分解大整数，也可以破解许多密码系统。



### 封面：如何用shor算法分解质因数

那么，什么是shor算法，如何用量子计算机分解质因数？



标题：如何用量子计算机分解质因数？

（量子电路的动画）



### shor算法简介

shor算法对于输入的大整数 N ，可以使用 O(log N) 个量子比特得到 N 的一个非平凡质因子



shor算法分为传统部分和量子部分，

传统部分使用传统计算机，将分解问题转换为求阶问题，接下来使用量子计算机，通过量子模意义乘法电路和量子傅里叶变换，高效求出指定元素的阶，从而实现分解

（展示流程图）

## 传统部分

### 流程

shor算法传统部分的实现如下：

（展示伪代码）

先找一个整数 $1<a<N$ , 计算 $\gcd(a, N)$ ，如果 $\gcd(a,N)\not=1$ 则我们已经找到了 $N$ 的一个非平凡因子（尽管对于大数这一步的概率很低）

若 $\gcd(a,N)=1$，则**用量子算法找到 $a$ 模 $N$ 的阶 ** （也称作 $a$ 模 $N$ 的阶，$r=\mathrm{ord}_N(a)$）

也就是最小的满足 $a^r \equiv 1 \pmod N$ 的正整数 $r$

（是否需要介绍一下阶？）



如果 $r$ 是偶数，我们可以将上式写作 $N \mid (a^{\frac r2}+1)(a^{\frac r2}-1)$ ，为方便下文记 $b = a^\frac r2$

根据阶的定义，显然不可能有 $b \equiv 1 \pmod N$ ，如果还满足  $b \not\equiv -1 \pmod N$ ，可以证明 $\gcd(b+1,N)$ 和 $\gcd(b-1,N)$ 都是 $N$ 的非平凡因子：



我们现在已经知道 $N \nmid b+1,\ N \nmid b-1$ ，使用反证法，如果 $\gcd(b+1,N)$ 不是非平凡因子，也就是说 $\gcd(b+1,N)=1$ ，那么将会得到 $N \mid b-1$ ，矛盾

（如果这一段过于 trivial 也可以删去）



### 成功率

接下来，关于传统部分我们只需要关注对于随机的 $a$ ，这个算法的成功率，也就是 $r=\text{ord}_N(a)$ 为偶数，且 $a^{\frac r2} \not\equiv -1 \pmod N$ 的概率，我们可以通过观察模 $N$ 乘法群 $(\Z/N\Z)^\times$ 的结构得到答案：



将 $N$ 分解为一系列质数的乘积： $N=p_1^{\alpha_1}p_2^{\alpha_2} \dots p_m^{\alpha_m}$ ，模 $N$ 乘法群可以表示为模 $p_i^{\alpha_i}$ 乘法群的直积（$(\Z/N\Z)^\times \cong (\Z/p_1^{\alpha_1}\Z)^\times \times (\Z/p_2^{\alpha_2}\Z)^\times \times \dots \times (\Z/p_m^{\alpha_m}\Z)$），并且，对于奇质数 $p_i$ ，模 $p_i^{\alpha_i}$ 乘法群是 $\varphi(p_i^{\alpha_i})$ 阶循环群 $(\Z/p_i^{\alpha_i}\Z)^\times \cong C_{\varphi(p^\alpha)}$



定义 $r=\mathrm{ord}_N(a),\ r_i = \mathrm{ord}_{p_i^{\alpha_i}}(a)$ ，有 $r = \mathrm{lcm}(r_1,r_2,\dots,r_m)$ 

$2\nmid r \iff \forall i,\ 2\nmid r_i$ 



定义 $v_2(n)$ 表示 $n$ 的因子中 $2$ 的次数，
$$
\begin{aligned}
a^{\frac{r}{2}} \equiv -1 \pmod N &\iff \forall i,\ a^{\frac{r}{2}} \equiv -1 \pmod {p_i^{\alpha_i}}\\
&\iff \forall i,\ 2\nmid r/r_i\\
&\iff \forall i,j,\ v_2(r_i)=v_2(r_j)
\end{aligned}
$$
对于随机的 $a$ ，不能通过 $a$ 找到 $N$ 的非平凡因子当且仅当 $\forall i,j,\ v_2(r_i) = v_2(r_j)$



接下来我们考虑 $r_i$ 的分布，根据中国剩余定理，$\forall i\neq j,\ r_i$ 与 $r_j$ 的分布是独立的

对于 $p_i^{\alpha_i}$ ，$v_2(r_i)$ 的分布为
$$
P(v_2(r_i) = t) &= \begin{cases}
\frac{1}{2^{v_2(\varphi(p_i^{\alpha_i}))}} & t=0\\
\frac{1}{2^{v_2(\varphi(p_i^{\alpha_i}))-t+1}} & 1\le t\le v_2(\varphi(p_i^{\alpha_i}))
\end{cases}
$$
（柱状图）



因此，对于与 $N$ 互质的所有 $a$ ，失败概率
$$
P(\text{fail}) = P(2\nmid r \or a^{\frac{r}{2}} \equiv -1\!\! \pmod N) = \sum_t \prod_i P(f_2(r_i) = t) \le \frac{1}{2}
$$


## 量子电路简介

接下来，我们只需要通过量子电路实现高效的求阶算法 `QPF(a, N)`



（TODO: 介绍量子计算及其优势）



量子电路部分的大致流程如下：

我们使用 $2q$ 个量子比特进行控制，使用 $q$ 个量子比特进行模意义乘法运算



（假设我们已经制造出了模意义乘法门 Ua 和量子傅里叶变换电路 QFT）



一开始，我们使用 Hadamard 门和 X 门将状态初始化为 $\ket{\psi_0} = \frac{1}{\sqrt Q} \sum_{x=0}^{Q-1} \ket{x,1}$

（3D-bar）

接下来，我们使用前 $2q$ 个量子比特控制乘法门，用后 $q$ 个量子比特计算乘法，当 $\ket x$ 的第 $i$ 位为 $1$ 时，会使控制乘法电路使答案乘上 $a^{2^i}$

此时的量子态是 $\ket{\psi} = \frac{1}{\sqrt{Q}} \sum_{x=0}^{Q-1} \ket{x, f(x)}$

（3D-bar）

这样，我们通过量子计算的并行特性就得到了 $a$ 的 $0$ 到 $Q-1$ 次幂，因为 $a^r \equiv 1 \pmod N$，这是一个以 $r$ 为周期的数列，而由于量子计算的限制，我们还需要使用一些技巧获得这个周期

由于周期性，$f(x)=z \iff x=x_0+kr$，我们将量子态这样表示： 
$$
\begin{aligned}
\ket{\psi} &= \frac{1}{\sqrt{Q}} \sum_{x=0}^{Q-1} \ket{x, f(x)}\\
&= \frac{1}{\sqrt Q} \sum_{z} \sum_{x=0}^{Q-1} [f(x)=z] \ket{x,z}\\
&= \frac{1}{\sqrt Q} \sum_{z} \sum_{k} \ket{x_0+kr,z}\\
\end{aligned}\\
$$


我们对前 $2q$ 个量子比特做 QFT ，并进行测量，结果如图所示，后 $q$ 位不同的量子态得到了几乎一样的结果，并且都有 $r$ 个峰值等间距分布，接下来我们将证明为什么 QFT 能得到这样的结果

（3D-bar）

因为只对前 $2q$ 个量子比特进行了 QFT，所以在经过 QFT 后，后 $q$ 位不同的量子态之间不会互相影响



因此，只考虑 $f(x)=z$ 的情况，我们观察 QFT 后的结果
$$
\begin{aligned}
\mathrm{QFT}(\ket{\psi}) &= \frac{1}{Q} \sum_{z=0}^{N-1} \sum_{y=0}^{Q-1} \sum_{k} \omega_Q^{-(x_0+kr)y} \ket{y,z}\\
\\
P(\ket{y,z}) &= \left|\frac{1}{Q} \sum_{k} \omega_Q^{-(x_0+kr)y}\right|^2\\
&= \frac{1}{Q^2} \left|\sum_{k=0}^{Q/r \text{ or } Q/r-1} (\omega_Q^{ry})^k\right|^2\\
&= \frac{1}{Q^2} \left|\frac{1-\omega^m}{1-\omega}\right|^2\\
\end{aligned}
$$

其中 $\omega = w_Q^{ry},\ y=0\dots Q-1,\quad m = Q/r \text{ or } Q/r+1$



我们画出 $\omega$ 的幅角（$-\pi\sim \pi$）与 $P(\ket{y,z})$ 关系的图像，可以证明，函数关于 $y$ 轴对称，而且在 $[0,\omega_Q^{Q/m}]$ （大约是 $[0,\omega_Q^r]$ ）内单调递减



（动画）



我们模拟这个过程，可以发现，幅角从 $0$ 递增到 $\omega_Q^{(Q-1)r}$，$\omega$ 会绕 $x$ 轴旋转 $r$ 圈，每经过 $r$ 轴一次，一定存在一个 $y_i$ 满足 $\omega_Q^{ry_i}$ 的幅角在 $\omega_Q^{-\frac r2}$ 到 $\omega_Q^{\frac r2}$ 之间，因此概率
$$
P(\ket{y_i,z}) \ge \frac{1}{Q^2} \left|\frac{1-(\omega_Q^\frac{r}{2})^m}{1-\omega_Q^\frac{r}{2}}\right|^2 \approx \frac{1}{Q^2} \frac{\sin^2(\frac{\pi}{2})}{\sin^2(\frac{r\pi}{2Q})} = \frac{1}{Q^2\sin^2(\frac{r\pi}{2Q})}=\frac{4}{\pi^2 r^2} \approx 0.4 \frac{1}{r^2}\\
$$


有 $r$ 个 $z$ 满足 $\exists x,\ f(x)=z$ ，它们的 $P(\ket{y_i,z})$ 几乎没有区别（只有 $m = Q/r$ 还是 $m=Q/r+1$ 的区别）

而在测量的时候，只测量前 $2q$ 个量子比特，其中有 $r$ 个 $y_i$ 满足 $P(\ket{y_i}) \ge 0.4 \frac 1r$



现在，我们还需要找到 $y_i$ 与 $r$ 的关系，现在已知：$\exists d \in \{0,1,\dots r-1\}$ （圈数），$|ry_i-dQ|\le \frac{r}{2}$

两边同除 $Qr$ ，$|\frac{y}{Q}-\frac{d}{r}| \le \frac{1}{2Q}$ ，其中 $\frac{y}{Q}$ 已知，而 $\frac{d}{r}$ 是一个分子分母均小于 $N$ 的分数



对于两个分子分母均小于 $N$ 的不同的分数，它们的间距 $\left|\frac{a}{b} - \frac{c}{d}\right| = \left|\frac{ad-bc}{bd} \right| \ge \frac{1}{bd} \ge \frac{1}{N^2} > \frac{1}{Q}$ （这也是为什么控制部分需要 $2q$ 个量子比特的原因）

此时，通过 $\frac{y}{Q}$ 可以唯一确定 $\frac{d}{r}$ （可以用 stern brocot tree 或者 连分数求解）



（数轴可视化）



（程序模拟）

## 量子电路细节

现在这个问题只剩下最关键的一步：如何构建模意义乘法运算，在这里，我们参考这篇论文

（Circuit for Shor’s algorithm using 2n+3 qubits）给出一种构造



### （模 $2^q$，加常数）加法器

量子加法器有很多种实现方法，在这里介绍的是一种基于 QFT 的加法器，对于 $q$ 个量子比特，它实现了模 $2^q$ 的加法，并且不需要辅助量子比特



QFT 能将一个数转为它的相位，$\text{QFT} : \ket{a} \mapsto \ket{\phi(a)}$ ，

而逆变换可以将相位转换为数，$\text{QFT}^\dagger : \ket{\phi(a)} \mapsto \ket{a}$ ，

（指针旋转动画）



$\ket{a}$ 与 $\ket{a+b}$ 之间的关系较难找出，但 $\ket{\phi(a)}$ 与 $\ket{\phi(a+b)}$ 之间有着非常明显的关系：

对于 $\ket{x}$ ，$\ket{\phi(a)}$ 与 $\ket{\phi(a+b)}$ 相差 $\omega_Q^{bx}$ 的相位，由于其具有线性性，我们可以简单的构造出相位加法门：



（量子电路）



在两边加上 QFT 和逆 QFT 即可得到量子加法门



### （模 $N$，加常数）加法器

模意义加法可以这样表示：
$$
(a+b) \text{ mod } N = \begin{cases}
a+b & a+b-N < 0\\
a+b-N & a+b-N \ge 0\\
\end{cases}
$$
我们可以先计算 $a+b-N$ ，用一个辅助量子比特记录结果是否小于 $0$ （溢出）

但做到这点我们还需要扩充一位用于区分是否溢出，因此需要两个辅助量子比特



为了节省量子比特，我们还需要恢复记录溢出用的量子比特，但这也不难实现

> |x>  -->  |x+a-N>    -->  |(x+a)%N>   -->  |(x+a)%N-a>  -->  |(x+a)%N>
>
> |0>  -->  |[x+a-N<0]>  -->  |[x+a-N<0]>  -->  |0>      -->  |0>

（量子电路）

由于之后乘法器需要，我们还需要将其设计成受控的



### （模 $N$，乘常数）乘法器

将 $q$ 个加法器组合，就能得到一个乘加器，这里需要 $q$ 个辅助量子比特用于储存计算结果

同样地，我们还需要通过重叠两个乘加器恢复辅助量子比特

（量子电路）



这样，我们就成功构造了一种乘法器，并得到了一个使用 $4n+2$ 个量子比特的求阶算法，我们也在 pyqpanda 中成功模拟了这一电路

### 2n+3 trick

通过对 QFT 电路的观察，我们可以提前测量一些控制量子比特，并复用它们，最终优化到 $2n+3$ 个量子比特



## 结语

真实的量子计算

未来破解RSA，量子hard问题



比起破解RSA，Shor算法更展现出了量子计算的实用性



所有代码都已上传我们本次项目的 github 仓库，链接可以在评论区找到

[hz826/Shors-Algorithm-Introduction (github.com)](https://github.com/hz826/Shors-Algorithm-Introduction)



## 参考

Shor, P.W. "Algorithms for quantum computation: discrete logarithms and factoring"

Stephane Beauregard "Circuit for Shor's algorithm using 2n+3 qubits"

S. Parker, M.B. Plenio "Efficient factorization with a single pure qubit and logN mixed qubits"

Eric R. Johnston, Nic Harrigan, Mercedes Gimeno-Segovia "Programming Quantum Computers_ Essential Algorithms and Code Samples"

Shor's algorithm - Wikipedia

Shor's Algorithm - Qiskit

Q# 中的量子算法 - Azure Quantum | Microsoft Docs
