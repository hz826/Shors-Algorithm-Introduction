## Shor's algorithm

通过以下的Shor算法，能找到 $N$ 的一个非平凡因子：

1: 找一个整数 $1<a<N$ , 计算 $\gcd(a, N)$

2: 若 $\gcd(a, N)>1$，则已经找到了 $N$ 的一个非平凡因子

3: 若 $\gcd(a,N)=1$，则**用量子算法找到最小的满足 $a^r \equiv 1 \pmod N$ 的正整数 $r$** （也称作 $a$ 模 $N$ 的阶，$r=\mathrm{ord}_N(a)$）

4: 若 $2\nmid r$，或 $a^{\frac r2} \equiv -1 \pmod N$，则返回第一步重新找一个 $a$

5: 若 $2\mid r$，且 $a^{\frac r2} \not\equiv -1 \pmod N$，可以证明，通过求出 $\gcd(a^{\frac r2}+1, N)$ 或 $\gcd(a^{\frac r2}-1, N)$ 一定可以找到 $N$ 的一个非平凡因子



## Classical part

### not-trivial square root of 1 （1的非平凡平方根）

#### 在分解中的作用

如果 $b^2 \equiv 1 \pmod N,\ b\not\equiv\pm1 \pmod N$ ，则称 $b$ 是 $1$ 的一个非平凡平方根

如果找到了一个满足条件的 $b$，就一定可以找到 $n$ 的一个非平凡因子：
$$
\left\{
\begin{aligned}
(b+1)(b-1)\equiv 0\pmod N\\
b+1\not\equiv 0\pmod N\\
b-1\not\equiv 0\pmod N\\
\end{aligned}
\right.
\ \Longrightarrow\ 
\left\{
\begin{aligned}
1<\gcd(b+1,N) <N\\
1<\gcd(b-1,N) <N\\
\end{aligned}
\right.
$$
证明1: 考虑任意一个质数 $p\mid N$，有 $p\mid (b+1)$ 或 $p\mid (b-1)$，若 $p\mid (b+1)$，则 $p\mid\gcd(b+1,N)$，又有 $\gcd(b+1,N) \neq N$，对 $b-1$ 同理

证明2: 考虑裴蜀定理，证明 $(b+1)u+Nv=1$ 不成立即可，左右同乘 $b-1$，$(b^2-1)u+(b-1)Nv=b-1$，左式是 $N$ 的倍数，而右式不是



#### not-trivial square root of 1 的存在性和规律

将 $N$ 分解为质数乘积，设 $N=p_1^{\alpha_1}p_2^{\alpha_2} \dots p_m^{\alpha_m}$ ，接下来可以使用中国剩余定理分析：



> 根据群论知识，模 $N$ 乘法群 $(\Z/N\Z)^\times$ 可以分解为若干循环群的直积：
> 
> $(\Z/N\Z)^\times \cong (\Z/p_1^{\alpha_1}\Z)^\times \times (\Z/p_2^{\alpha_2}\Z)^\times \times \dots \times (\Z/p_m^{\alpha_m}\Z)$ ，其中当 $p_i>2$ 时 $(\Z/p_i^{\alpha_i}\Z)^\times \cong C_{\varphi(p^\alpha)}$



首先，$b^2 \equiv 1 \pmod N \ \Longrightarrow\ b^2 \equiv 1 \pmod {p_i^{\alpha_i}}$ ，

因为 $(\Z/p_i^{\alpha_i}\Z)^\times$ 是循环群，所以若 $b^2 \equiv 1 \pmod {p_i^{\alpha_i}}$，可证明 $b \equiv \pm 1\pmod {p_i^{\alpha_i}}$ 



所以，当且仅当 $b\ \mathrm{mod}\ p_i^{\alpha_i} = \pm1$ ，且不全为 $1$ （根据阶的定义，显然不会全为 $1$），也不全为 $-1$ 时，$b$ 是模 $N$ 的 not-trivial square root of 1




这里有三种特殊情况：

case1: $\exists p_i^{\alpha_i} = 2$，此时 $+1\equiv -1 \pmod 2$，若 $N=2 p^{\alpha}$ ， $N$ 不存在not-trivial square root of 1，但我们可以先除2简单地避免这种情况

case2: $N=p_i^{\alpha_i}$ ，此时 $N$ 不存在not-trivial square root of 1，但我们可以枚举很少的 $k$，判断 $\sqrt[k]{N}$ 是否为整数解决

case3: $N=p$，这种情况我们可以通过素性测试检测出来



可以发现，除了上述三种特殊情况，$N$ 都存在 not-trivial square root of 1，且数量不少于2



### Classical part 的正确性和成功率

下面将证明，对于随机的 $a$，$2\nmid r$ 且 $a^{\frac{r}{2}} \not\equiv -1 \pmod N$ 的概率不低于 $50\%$



继续考虑模 $N$ 乘法群 $(\Z/N\Z)^\times$，

定义 $r=\mathrm{ord}_N(a),\ r_i = \mathrm{ord}_{p_i^{\alpha_i}}(a)$ ，有 $r = \mathrm{lcm}(r_1,r_2,\dots,r_m)$ ，$2\nmid r \iff \forall i,\ 2\nmid r_i$



定义 $f_2(n) = \max_k \{2^k \mid n\}$ 表示 $n$ 中因子 $2$ 的次数，
$$
\begin{aligned}
a^{\frac{r}{2}} \equiv -1 \pmod N &\iff \forall i,\ a^{\frac{r}{2}} \equiv -1 \pmod {p_i^{\alpha_i}}\\
&\iff \forall i,\ 2\nmid r/r_i\\
&\iff \forall i,j,\ f_2(r_i)=f_2(r_j)
\end{aligned}
$$


综上所述，对于随机的 $a$ ，不能通过 $a$ 找到 $N$ 的非平凡因子当且仅当 $\forall i,j,\ f_2(r_i) = f_2(r_j)$



接下来我们考虑 $r_i$ 的分布，根据中国剩余定理，$\forall i\neq j,\ r_i$ 与 $r_j$ 的分布是独立的

因为 $(\Z/p_i^{\alpha_i}\Z)^\times \cong C_{\varphi(p_i^{\alpha_i})}$ ，该群存在生成元（原根）$g$ ，也存在唯一的整数 $0\le x < \varphi(p_i^{\alpha_i})$ ，$a\equiv g^x \pmod{p_i^{\alpha_i}}$ ，$r_i$ 可以通过 $x$ 表示：
$$
r_i = \mathrm{ord}(g^x) = \min_{r>0} \{\varphi(p_i^{\alpha_i}) \mid rx\} = \frac{\varphi(p_i^{\alpha_i})}{\gcd(\varphi(p_i^{\alpha_i}),x)}\\
\\
f_2(r_i) = \max(0, f_2(\varphi(p_i^{\alpha_i})) - f_2(x))
$$


进一步的，对于非特殊情况的 $N$ ，和随机的与 $N$ 互质的 $a$，
$$
\begin{aligned}
P(f_2(r_i) = t) &= \begin{cases}
\frac{1}{2^{f_2(\varphi(n))}} & t=0\\
\frac{1}{2^{f_2(\varphi(n))-t+1}} & 1\le t\le f_2(\varphi(n))
\end{cases}\\
\\
P(2\nmid r \or a^{\frac{r}{2}} \equiv -1 \pmod N) &= \sum_t \prod_i P(f_2(r_i) = t) \le \frac{1}{2}
\end{aligned}
$$


## 参考

[Shor's algorithm - Wikipedia](https://en.wikipedia.org/wiki/Shor's_algorithm)

[Multiplicative group of integers modulo n - Wikipedia](https://en.wikipedia.org/wiki/Multiplicative_group_of_integers_modulo_n)