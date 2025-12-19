import matplotlib.pyplot as plt
import scipy.integrate as spi
import numpy as np


def f(x):
    return np.sin(x)


def monte_carlo_impl(a: float, b: float, n: int) -> float:
    """
    Performs Monte Carlo integration and visualizes the result
    Args:
        a (float): Lower bound of integration
        b (float): Upper bound of integration
        n (int): Number of random experiments (points)
    Returns:
        float: The estimated value of the integral
    """
    # generate n random x points between a and b
    x_rand = np.random.uniform(a, b, n)

    # bounding box height (y max for sin)
    y_max = 1
    # generate n random y points between 0 and 1
    y_rand = np.random.uniform(0, y_max, n)

    # if random y is less than f(x) at that point, it is under the curve
    under_curve = y_rand < f(x_rand)

    # calculate the area
    rectangle_area = (b - a) * y_max
    fraction_under_curve = np.sum(under_curve) / n
    mc_integral = rectangle_area * fraction_under_curve

    # draw the figure
    _, ax = plt.subplots(figsize=(10, 6))
    x_linspace = np.linspace(a, b, 400)
    y_linspace = f(x_linspace)
    ax.plot(x_linspace, y_linspace, "k", linewidth=2, label="f(x) = sin(x)")
    ax.scatter(x_rand[under_curve], y_rand[under_curve], color='green', s=1, alpha=0.3, label="points under curve")
    ax.scatter(x_rand[~under_curve], y_rand[~under_curve], color='red', s=1, alpha=0.3, label="points above curve")
    ax.set_xlim([a, b])
    ax.set_ylim([0, y_max])
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title(f"Monte Carlo method (N={n})\nCalculated Area: {mc_integral:.4f}")
    ax.legend(loc="upper right")

    plt.grid(True, which="both", linestyle="--", linewidth=0.5)
    plt.show()

    return mc_integral


if __name__ == "__main__":
    lower_bound = 0
    upper_bound = np.pi
    experiments_num = 15000

    mc_result = monte_carlo_impl(lower_bound, upper_bound, experiments_num)
    quad_result, _ = spi.quad(f, lower_bound, upper_bound)

    print("-------------Results-------------")
    print(f"Monte Carlo result (N = {experiments_num}): {mc_result}")
    print(f"SciPy quad result: {quad_result}")
    print(f"Absolute error: {abs(mc_result - quad_result)}")
    print(f"Relative error: {abs(mc_result - quad_result) / quad_result * 100:.4f}%")
