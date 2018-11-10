from math import e


def weibull(gamma, beta, delta):
    def distribution_function(x):
        component = ((x-gamma)/delta)**beta
        return 1 - e**(-component)
    return distribution_function
