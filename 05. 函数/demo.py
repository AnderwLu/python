def calculate_bmi(weight, height):
    """
    计算 BMI 指数。

    参数:
        weight: 体重，单位千克
        height: 身高，单位米

    返回:
        BMI 值
    """
    return weight / (height**2)


print(calculate_bmi.__doc__)
