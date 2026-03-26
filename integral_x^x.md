$$

\int_{0}^{1} x^x \, dx = \int_{0}^{1} e^{x\,\ln x} \, dx
\\
\begin{align*}
    \\ \text{Since,} \quad
    e^x &= \sum_{n=0}^{\infty} \, \frac{x^n}{n!}\\
        &= 1 + \frac{x}{1!} + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots \\

    \implies e^{x\ln x} &= 1 + \frac{(x\,\ln x)}{1!} + \frac{(x\,\ln x)^2}{2!} + \frac{(x\ln x)^3}{3!} + \cdots \\
    &= \sum_{n=0}^{\infty} \, \frac{(x\,\ln x)^n}{n!}\\
\end{align*}

\\

\begin{align*}
    \\ \text{Therefore, }  \\
    &\int_{0}^{1} e^{x\,\ln x} \, dx \, 
    = \, \int_{0}^{1}\, \left(\sum_{n=0}^{\infty} \, \frac{(x\,\ln x)^n}{n!} \right) \,dx \,\,\,
    = &\sum_{n=0}^{\infty} \frac{1}{n!} \, \int_{0}^{1} x^n(\ln x)^n \,dx


    \\\text{Let, } \,\, &\ln x = u \implies x = e^u \\
    \implies \, &\frac{1}{x} \,dx = du

    &\begin{align*}
        &x \to 0 \implies u \to \infty \\
        &x \to 1 \implies u \to 0
    \end{align*}
\end{align*}

\\

\begin{align*}
    &\begin{align*}
        \\\text{Now, }& \\ 
        &\sum_{n=0}^{\infty} \frac{1}{n!} \, \int_{\infty}^{0} \, (e^u)^{n+1} \,u^n \,du\,
    \end{align*}

    \\&
    \begin{align*}
    \text{Let, } \, u = -t &\\ 
    &\sum_{n=0}^{\infty} \frac{1}{n!} \, \int_{0}^{\infty} \, e^{-(n+1)t}\, t^n \,dt\, \\
    \end{align*}

\end{align*}

\\

\begin{align*}
    \text{We know, }& \\
    &\Gamma (n) = \int_{0}^{\infty}e^{-t}\,t^{n-1}\,dt = (n-1)! \\
    \implies &\Gamma (n+1) = \int_{0}^{\infty}e^{-t}\,t^{n}\,dt = n!
\end{align*}

\\

\begin{align*}
    \\ &\text{From our obtained integral, } \quad
    \sum_{n=0}^{\infty} \frac{1}{n!} \, \int_{0}^{\infty} \, e^{-(n+1)t}\, t^n \,dt\, \\

    \\&\text{Let, } \, s = (n+1) \, t \implies ds = (n+1)\,dt\\

    \\&\implies \sum_{n=0}^{\infty} \frac{1}{(n+1)^{n+1} \, n!} \, \int_{0}^{\infty} \, e^{-s}\, s^n \,ds\, \\
    \\&\implies \sum_{n=0}^{\infty} \, \frac{\Gamma (n+1)}{(n+1)^{n+1} \, n!} \\
    \\&\implies \sum_{n=0}^{\infty} \, \frac{1}{(n+1)^{n+1}} \\
\end{align*}

\\

\begin{align*}
    % \\ \text{Therefore, } \, &\\
    \\\therefore&\quad
    \int_{0}^{1} x^x \, dx 
    = \sum_{n=0}^{\infty} \, \frac{1}{(n+1)^{n+1}}
    = \frac{1}{1^1} + \frac{1}{2^2} + \frac{1}{3^3} + \cdots \\

    \\ &\implies \boxed{\quad\int_{0}^{1} x^x \, dx \approx 0.7834305 \quad}
\end{align*}

$$