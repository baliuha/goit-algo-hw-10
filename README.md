# Monte Carlo method: Calculating the Integral

The project implements the **Monte Carlo method** to calculate the definite integral of a function. 
To verify the accuracy of the Monte Carlo algorithm, the result is compared with the highly precise `scipy.integrate.quad` function.

1.  **Function:** $f(x) = \sin(x)$
2.  **Interval:** $[0, \pi]$
3.  **Bounding Box:** Rectangle with width $[0, \pi]$ and height $[0, 1]$
4.  **Algorithm steps:**
    * Generate $N$ random points $(x, y)$ within the bounding box
    * Count points that fall under the curve $y < \sin(x)$
    * Calculate the area ratio: $\text{Area} \approx \text{BoxArea} \times \frac{\text{Points under curve}}{\text{Total points}}$

## Results

| Method | Result (Area) |
| :--- | :--- |
| **Analytical / SciPy** | 2.00 |
| **Monte Carlo (N=15000)** | ~1.99 - 2.01* |

*\*Note: Results vary slightly with each execution*

## Conclusions

1. The Monte Carlo method provides an **approximation** of the integral. With 15,000 iterations, the result is reasonably accurate. However, the precision fluctuates between runs due to the random generation of points

2. The accuracy of the Monte Carlo integration depends on the number of points $N$. Increasing $N$ reduces the error rate, but increases computational time

3. For this specific one-dimensional task, `scipy.integrate.quad` is faster and more precise than the Monte Carlo method

4. While the Monte Carlo method is not the most efficient choice for simple integrals, it is a powerful tool for high-dimensional integration in physics, finance and machine learning