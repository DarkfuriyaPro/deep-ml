import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # Your code here
    g = np.poly1d(g_coeffs)
    h = np.poly1d(h_coeffs)

    g_der = np.polyder(g)
    h_der = np.polyder(h)
    return (g_der(x) * h(x) - g(x) * h_der(x)) / (h(x)**2)